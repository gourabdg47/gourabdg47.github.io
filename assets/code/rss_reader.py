import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
import sqlite3
import feedparser
import html2text
import markdown
from queue import Queue
import threading
from datetime import datetime, timedelta
import textwrap
import json
import webbrowser
from tkinterweb import HtmlFrame
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

class RSSDatabase:
    """Handles database operations with connection pooling and batch processing"""
    def __init__(self, db_path='feeds.db'):
        self.db_path = db_path
        self.lock = threading.Lock()
        self.connection = None
        self.connect()
        self.create_tables()
        
    def connect(self):
        if self.connection is None:
            logging.info("Connecting to database at %s", self.db_path)
            self.connection = sqlite3.connect(self.db_path, check_same_thread=False)
            self.connection.execute('PRAGMA foreign_keys = ON')
            self.connection.commit()
            
    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
            
    def __del__(self):
        self.close()
        
    def create_tables(self):
        with self.lock, self.connection:
            logging.info("Creating tables if they do not exist")
            self.connection.execute('''CREATE TABLE IF NOT EXISTS feeds
                               (url TEXT PRIMARY KEY,
                                title TEXT,
                                tag TEXT,
                                category TEXT,
                                last_updated TEXT)''')
            self.connection.execute('''CREATE TABLE IF NOT EXISTS cache
                                (url TEXT PRIMARY KEY,
                                    content TEXT,
                                    expires TEXT,
                                    etag TEXT,
                                    last_modified TEXT)''')
            self.connection.execute('CREATE INDEX IF NOT EXISTS idx_tag ON feeds(tag)')
            self.connection.execute('CREATE INDEX IF NOT EXISTS idx_category ON feeds(category)')

    def get_feeds(self, filters=None):
        """Fetch feeds with optional filters"""
        with self.lock:
            query = 'SELECT url, title, tag, category FROM feeds'
            params = []
            if filters:
                clauses = []
                for key, value in filters.items():
                    if value:
                        clauses.append(f"{key} = ?")
                        params.append(value)
                if clauses:
                    query += ' WHERE ' + ' AND '.join(clauses)
            return self.connection.execute(query, params).fetchall()

    def add_feed(self, url, title, tag='', category=''):
        with self.lock, self.connection:
            logging.info("Adding feed: %s", url)
            self.connection.execute('''INSERT OR REPLACE INTO feeds 
                               (url, title, tag, category, last_updated)
                               VALUES (?, ?, ?, ?, ?)''',
                            (url, title, tag, category, datetime.now().isoformat()))
            self.connection.commit()
            
    def get_cache(self, url):
        with self.lock:
            result = self.connection.execute(
                'SELECT content, expires, etag, last_modified FROM cache WHERE url = ?',
                (url,)
            ).fetchone()
        if result:
            return (
                result[0],  # content (raw JSON string)
                result[1],  # expires timestamp
                result[2],  # etag
                result[3]   # last_modified
            )
        return None
            
    def set_cache(self, url, content, expires, etag=None, last_modified=None):
        try:
            with self.lock, self.connection:
                self.connection.execute(
                    '''INSERT OR REPLACE INTO cache 
                    (url, content, expires, etag, last_modified)
                    VALUES (?, ?, ?, ?, ?)''',
                    (url, content, expires, etag, last_modified)
                )
                self.connection.commit()
        except Exception as e:
            logging.error(f"Failed to cache {url}: {str(e)}")
            
    def purge_expired_cache(self):
        """Remove expired cache entries"""
        with self.lock, self.connection:
            logging.info("Purging expired cache entries")
            self.connection.execute(
                "DELETE FROM cache WHERE expires < ?", 
                (datetime.now().isoformat(),)
            )
            self.connection.commit()
            
    def get_unique_values(self, column):
        """Get unique values from a column for filters"""
        with self.lock:
            rows = self.connection.execute(
                f'SELECT DISTINCT {column} FROM feeds WHERE {column} != ""'
            ).fetchall()
            return [row[0] for row in rows]

    def update_feed_title(self, url, new_title):
        with self.lock, self.connection:
            logging.info("Updating feed title for %s to %s", url, new_title)
            self.connection.execute("UPDATE feeds SET title=? WHERE url=?", (new_title, url))
            self.connection.commit()

    def delete_feed(self, url):
        with self.lock, self.connection:
            logging.info("Deleting feed: %s", url)
            self.connection.execute("DELETE FROM feeds WHERE url=?", (url,))
            self.connection.commit()

class FeedParser:
    """Handles feed parsing with caching and background processing"""
    def __init__(self, db):
        self.db = db
        self.work_queue = Queue()
        self.handler = html2text.HTML2Text()
        self.num_workers = 5
        for _ in range(self.num_workers):
            threading.Thread(target=self._worker_loop, daemon=True).start()
        
    def _worker_loop(self):
        while True:
            task = self.work_queue.get()
            try:
                task()
            except Exception as e:
                logging.error("Worker error: %s", str(e))
            finally:
                self.work_queue.task_done()
        
    def parse_feed(self, url, callback=None):
        cache = self.db.get_cache(url)
        if cache:
            content, expires, etag, last_modified = cache
            parsed = json.loads(content)
            if callback:
                callback(parsed)
            if datetime.fromisoformat(expires) <= datetime.now():
                # Refresh in background
                self.work_queue.put(lambda: self._refresh_feed(url, callback, etag, last_modified))
            return parsed
        else:
            self.work_queue.put(lambda: self._parse_feed(url, callback))
            return None

    def _refresh_feed(self, url, callback, etag, last_modified):
        try:
            feed = feedparser.parse(url, etag=etag, modified=last_modified)
            if feed.status == 304:
                # Update only expiry
                existing = self.db.get_cache(url)
                if existing:
                    content = existing[0]
                    new_expires = (datetime.now() + timedelta(minutes=15)).isoformat()
                    self.db.set_cache(url, content, new_expires, etag, last_modified)
            else:
                self._process_and_cache_feed(url, feed, callback)
        except Exception as e:
            logging.error(f"Error refreshing {url}: {e}")

    def _parse_feed(self, url, callback):
        try:
            feed = feedparser.parse(url)
            self._process_and_cache_feed(url, feed, callback)
        except Exception as e:
            logging.error(f"Error parsing {url}: {e}")

    def _process_and_cache_feed(self, url, feed, callback):
        if not feed.entries:
            return
        parsed = self._process_entries(feed.entries)
        new_etag = feed.get('etag', '')
        new_last_modified = feed.get('modified', '')
        expires = (datetime.now() + timedelta(minutes=15)).isoformat()
        self.db.set_cache(url, json.dumps(parsed), expires, new_etag, new_last_modified)
        if callback:
            callback(parsed)

    def _process_entries(self, entries):
        """Convert HTML content to Markdown"""
        result = []
        for entry in entries:
            title = entry.get('title', 'No Title')
            content = ''
            if 'content' in entry and entry.content:
                content = entry.content[0].get('value', '')
            elif 'description' in entry:
                content = entry.description
            elif 'summary' in entry:
                content = entry.summary
            link = entry.get('link', '')
            markdown_content = self.handler.handle(content)
            if link:
                markdown_content = f"[Original Article]({link})\n\n{markdown_content}"
            result.append((title, markdown_content))
        return result

class RSSApp(tk.Tk):
    """Main application class with optimized UI and Markdown support"""
    def __init__(self):
        super().__init__()
        self.title("Research RSS Reader")
        self.geometry("1200x800")
        self.settings = {
            "theme": "light",
            "font_family": "Segoe UI",
            "font_size": 10,
            "heading_font_size": 12
        }
        self.db = RSSDatabase()
        self.parser = FeedParser(self.db)
        self.current_content = []
        self.current_feeds = []
        self.pending_feeds = 0
        self.setup_ui()
        self.setup_theme()
        self.update_filters()
        self.load_feeds()
        self.after(3600000, self.purge_cache)
        self.feed_list.bind("<Button-3>", self.show_feed_context_menu)




    def setup_theme(self):
        """Configure theme settings"""
        self.available_themes = {
            "light": {
                "bg": "#f0f0f0",
                "fg": "#000000",
                "textbg": "#ffffff",
                "textfg": "#000000",
                "headingfg": "#0078d7"
            },
            "dark": {
                "bg": "#2d2d30",
                "fg": "#ffffff",
                "textbg": "#1e1e1e",
                "textfg": "#ffffff",
                "headingfg": "#00aeff"
            }
        }
        self.style = ttk.Style()
        self.apply_theme()

    def apply_theme(self):
        """Apply current theme settings"""
        theme = self.settings["theme"]
        colors = self.available_themes[theme]
        
        self.style.configure(".", background=colors["bg"], foreground=colors["fg"])
        self.style.configure("TFrame", background=colors["bg"])
        self.style.configure("TLabel", background=colors["bg"], foreground=colors["fg"])
        self.style.configure("TButton", background=colors["bg"], foreground=colors["fg"])
        self.style.configure("Treeview", 
                           background=colors["textbg"], 
                           foreground=colors["textfg"],
                           fieldbackground=colors["textbg"])
        self.style.map("Treeview", 
                      background=[('selected', colors["headingfg"])],
                      foreground=[('selected', colors["bg"])])
        self.configure(background=colors["bg"])
        
        # Update content display if any
        selection = self.tree.selection()
        if selection:
            self.show_content(None)

    def setup_ui(self):
        """Create UI components with better layout"""
        self.setup_menu()
        
        # Main content pane with sash
        self.paned = ttk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.paned.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)
        
        self.setup_left_panel()
        self.setup_right_panel()
        self.setup_status_bar()

    def setup_menu(self):
        """Create menu system"""
        menubar = tk.Menu(self)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        file_menu.add_command(label="Refresh All", command=self.threaded_refresh)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.quit)
        menubar.add_cascade(label="File", menu=file_menu)
        
        view_menu = tk.Menu(menubar, tearoff=0)
        view_menu.add_command(label="Toggle Theme", command=self.toggle_theme)
        menubar.add_cascade(label="View", menu=view_menu)
        
        self.config(menu=menubar)

    def setup_left_panel(self):
        """Left panel with filters and controls"""
        left_frame = ttk.Frame(self.paned, padding=10)
        self.paned.add(left_frame, weight=1)
        
        # Add Feed Section
        # ttk.Label(left_frame, text="Add New Feed").pack(anchor=tk.W)
        # self.url_entry = ttk.Entry(left_frame, width=30)
        # self.url_entry.pack(fill=tk.X, pady=5)
        
        add_frame = ttk.Frame(left_frame)
        add_frame.pack(fill=tk.X, pady=5)
        
        ttk.Button(add_frame, text="Add Feed", command=self.show_add_dialog).pack(side=tk.LEFT, fill=tk.X, expand=True)
        ttk.Button(add_frame, text="Refresh", command=self.threaded_refresh).pack(side=tk.RIGHT, padx=(5,0))
        
        # Filter Section
        ttk.Label(left_frame, text="Filters").pack(anchor=tk.W, pady=(10,0))
        
        ttk.Label(left_frame, text="Category:").pack(anchor=tk.W, pady=(5,0))
        self.category_filter = ttk.Combobox(left_frame, state="readonly")
        self.category_filter.pack(fill=tk.X, pady=2)
        
        ttk.Label(left_frame, text="Tag:").pack(anchor=tk.W, pady=(5,0))
        self.tag_filter = ttk.Combobox(left_frame, state="readonly")
        self.tag_filter.pack(fill=tk.X, pady=2)
        
        ttk.Button(left_frame, text="Apply Filters", command=self.apply_filters).pack(fill=tk.X, pady=5)
        ttk.Button(left_frame, text="Clear Filters", command=self.clear_filters).pack(fill=tk.X)
        
        # Feed list in left panel
        ttk.Label(left_frame, text="Available Feeds:").pack(anchor=tk.W, pady=(10,0))
        
        feed_frame = ttk.Frame(left_frame)
        feed_frame.pack(fill=tk.BOTH, expand=True, pady=5)
        
        self.feed_list = ttk.Treeview(feed_frame, columns=('title',), show='headings')
        self.feed_list.heading('title', text='Feed Title')
        self.feed_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        feed_scroll = ttk.Scrollbar(feed_frame, orient=tk.VERTICAL, command=self.feed_list.yview)
        feed_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.feed_list.configure(yscrollcommand=feed_scroll.set)
        
        self.feed_list.bind("<ButtonRelease-1>", self.load_selected_feed)

    def setup_right_panel(self):
        """Right panel with feed list and content viewer"""
        right_frame = ttk.Frame(self.paned)
        self.paned.add(right_frame, weight=4)
        
        # Split pane for article list and content
        right_paned = ttk.PanedWindow(right_frame, orient=tk.VERTICAL)
        right_paned.pack(fill=tk.BOTH, expand=True)
        
        # Article List
        tree_frame = ttk.Frame(right_paned)
        right_paned.add(tree_frame, weight=1)
        
        self.tree = ttk.Treeview(tree_frame, columns=('title', 'tag', 'category'), show='headings')
        self.tree.heading('title', text='Title')
        self.tree.heading('tag', text='Tag')
        self.tree.heading('category', text='Category')
        self.tree.column('title', width=400)
        self.tree.column('tag', width=100)
        self.tree.column('category', width=100)
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        tree_scroll = ttk.Scrollbar(tree_frame, orient=tk.VERTICAL, command=self.tree.yview)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        self.tree.configure(yscrollcommand=tree_scroll.set)
        
        self.tree.bind("<ButtonRelease-1>", self.show_content)
        
        # Content Viewer
        content_frame = ttk.Frame(right_paned)
        right_paned.add(content_frame, weight=3)
        
        self.content = HtmlFrame(content_frame, messages_enabled=False)
        self.content.load_html("<html><body><h1>Select an article to view</h1></body></html>")
        # self.content.on_link_click(lambda url: webbrowser.open(url))
        self.content.pack(fill=tk.BOTH, expand=True)

    def setup_status_bar(self):
        """Status bar at bottom"""
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(self, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(fill=tk.X, side=tk.BOTTOM, pady=(5,0))

    def toggle_theme(self):
        """Toggle between light and dark themes"""
        self.settings["theme"] = "dark" if self.settings["theme"] == "light" else "light"
        self.apply_theme()

    def update_filters(self):
        """Update filter dropdown values"""
        # Save current selections
        current_tag = self.tag_filter.get() if hasattr(self, 'tag_filter') else ""
        current_category = self.category_filter.get() if hasattr(self, 'category_filter') else ""
        
        # Update categories
        categories = [""] + self.db.get_unique_values("category")
        self.category_filter['values'] = categories
        if current_category in categories:
            self.category_filter.set(current_category)
        else:
            self.category_filter.set("")
            
        # Update tags
        tags = [""] + self.db.get_unique_values("tag")
        self.tag_filter['values'] = tags
        if current_tag in tags:
            self.tag_filter.set(current_tag)
        else:
            self.tag_filter.set("")


    def show_feed_context_menu(self, event):
        # Identify the row under the cursor
        row_id = self.feed_list.identify_row(event.y)
        if row_id:
            self.feed_list.selection_set(row_id)
            menu = tk.Menu(self.feed_list, tearoff=0)
            menu.add_command(label="Rename", command=lambda: self.rename_feed(row_id))
            menu.add_command(label="Delete", command=lambda: self.delete_feed(row_id))
            menu.tk_popup(event.x_root, event.y_root)

    def rename_feed(self, item_id):
        current_title = self.feed_list.item(item_id, 'values')[0]
        url = self.feed_list.item(item_id, 'tags')[0]
        new_title = simpledialog.askstring("Rename Feed", "Enter new title:", initialvalue=current_title)
        if new_title and new_title != current_title:
            logging.info("Renaming feed %s to %s", url, new_title)
            self.db.update_feed_title(url, new_title)
            self.load_feeds()
            self.status_var.set(f"Feed renamed to {new_title}")

    def delete_feed(self, item_id):
        url = self.feed_list.item(item_id, 'tags')[0]
        if messagebox.askyesno("Delete Feed", "Are you sure you want to delete this feed?"):
            logging.info("Deleting feed with URL: %s", url)
            self.db.delete_feed(url)
            self.load_feeds()
            self.status_var.set("Feed deleted")


    def load_feeds(self, filters=None):
        """Load feed sources into the feed list"""
        logging.info("Loading feeds with filters: %s", filters)
        self.feed_list.delete(*self.feed_list.get_children())
        feeds = self.db.get_feeds(filters)
        self.current_feeds = feeds
        
        for feed in feeds:
            url, title, tag, category = feed
            self.feed_list.insert('', tk.END, values=(title,), tags=(url,))
            
        logging.info("Loaded %d feeds", len(feeds))
        self.status_var.set(f"Loaded {len(feeds)} feeds")

    def load_selected_feed(self, event=None):
        """Load articles from the selected feed"""
        selection = self.feed_list.selection()
        if not selection:
            return
            
        url = self.feed_list.item(selection[0], 'tags')[0]
        feed_title = self.feed_list.item(selection[0], 'values')[0]
        tag = ""
        category = ""
        
        # Find tag and category for this feed
        for feed in self.current_feeds:
            if feed[0] == url:
                tag = feed[2]
                category = feed[3]
                break
                
        self.tree.delete(*self.tree.get_children())
        self.status_var.set(f"Loading articles from {feed_title}...")
        
        def on_feed_parsed(entries):
            self.tree.delete(*self.tree.get_children())
            if not entries:
                self.status_var.set(f"No articles found in {feed_title}")
                return
                
            for title, content in entries:
                self.tree.insert('', tk.END, 
                               values=(textwrap.shorten(title, width=80), tag, category), 
                               tags=(content,))
            self.status_var.set(f"Loaded {len(entries)} articles from {feed_title}")
            
        self.parser.parse_feed(url, callback=on_feed_parsed)

    def show_content(self, event):
        """Display formatted Markdown content"""
        selection = self.tree.selection()
        if not selection:
            return
            
        markdown_content = self.tree.item(selection[0], 'tags')[0]
        theme_colors = self.available_themes[self.settings["theme"]]
        
        html_content = markdown.markdown(markdown_content)
        full_html = f"""
        <html>
        <head>
        <style>
        body {{
            background-color: {theme_colors['textbg']};
            color: {theme_colors['textfg']};
            font-family: {self.settings['font_family']};
            font-size: {self.settings['font_size']}pt;
            padding: 20px;
            line-height: 1.5;
        }}
        a {{ color: {theme_colors['headingfg']}; }}
        h1, h2, h3 {{ color: {theme_colors['headingfg']}; }}
        img {{ max-width: 100%; height: auto; }}
        pre {{ 
            background-color: {theme_colors['bg']}; 
            padding: 10px; 
            border-radius: 5px; 
            overflow: auto;
        }}
        </style>
        </head>
        <body>{html_content}</body>
        </html>
        """
        self.content.load_html(full_html)

    def show_add_dialog(self):
        """Add feed dialog with more fields"""
        dialog = tk.Toplevel(self)
        dialog.title("Add New Feed")
        dialog.geometry("400x200")
        dialog.resizable(False, False)
        dialog.transient(self)
        dialog.grab_set()
        
        fields = {}
        
        ttk.Label(dialog, text="RSS URL:").grid(row=0, column=0, sticky=tk.W, padx=10, pady=5)
        fields['url'] = ttk.Entry(dialog, width=40)
        fields['url'].grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(dialog, text="Title:").grid(row=1, column=0, sticky=tk.W, padx=10, pady=5)
        fields['title'] = ttk.Entry(dialog, width=40)
        fields['title'].grid(row=1, column=1, padx=10, pady=5)

        ttk.Label(dialog, text="Tag (optional):").grid(row=2, column=0, sticky=tk.W, padx=10, pady=5)
        fields['tag'] = ttk.Entry(dialog, width=40)
        fields['tag'].grid(row=2, column=1, padx=10, pady=5)

        ttk.Label(dialog, text="Category (optional):").grid(row=3, column=0, sticky=tk.W, padx=10, pady=5)
        fields['category'] = ttk.Entry(dialog, width=40)
        fields['category'].grid(row=3, column=1, padx=10, pady=5)

        button_frame = ttk.Frame(dialog)
        button_frame.grid(row=4, column=0, columnspan=2, pady=20)

        ttk.Button(
            button_frame, text="Add",
            command=lambda: self.validate_and_add(
                fields['url'].get(),
                fields['title'].get(),
                fields['tag'].get(),
                fields['category'].get(),
                dialog
            )
        ).pack(side=tk.LEFT, padx=10)

        ttk.Button(button_frame, text="Cancel", command=dialog.destroy).pack(side=tk.LEFT, padx=10)


    def validate_and_add(self, url, title, tag, category, dialog):
        """Async feed validation with progress indicator"""
        logging.info("Validating feed for URL: %s", url)
        if not url:
            messagebox.showerror("Error", "URL is required")
            return
            
        self.status_var.set("Validating feed...")
        dialog.withdraw()  # Hide dialog during validation
        
        def validation_task():
            try:

            
                feed = feedparser.parse(url)
                
                if not feed.entries:
                    raise ValueError("Invalid RSS feed or no entries found")
                    
                # Determine the title to use
                determined_title = title.strip()  # Start with user-provided title
                # if not determined_title:  # If empty, get from feed
                #     determined_title = feed.feed.get('title', url)  # Fallback to URL if no feed title

                logging.info("Feed validation successful for %s", url)
                self.after(0, lambda: self.save_feed(url, determined_title, tag, category, dialog))
            except Exception as e:
                logging.error("Validation error for %s: %s", url, str(e))
                dialog.deiconify()  # Show dialog again on error
                self.after(0, lambda: messagebox.showerror("Error", str(e)))
                self.after(0, lambda: self.status_var.set("Ready"))
                
        threading.Thread(target=validation_task, daemon=True).start()

    def save_feed(self, url, title, tag, category, dialog):
        logging.info("Saving feed: %s", url)
        self.db.add_feed(url, title, tag, category)
        self.load_feeds()
        self.update_filters()
        dialog.destroy()
        self.status_var.set(f"Added feed: {title}")

    def apply_filters(self, event=None):
        """Apply selected filters"""
        filters = {}
        if self.tag_filter.get():
            filters['tag'] = self.tag_filter.get()
        if self.category_filter.get():
            filters['category'] = self.category_filter.get()
        self.load_feeds(filters)

    def clear_filters(self):
        """Clear all filters"""
        self.tag_filter.set("")
        self.category_filter.set("")
        self.load_feeds()

    def threaded_refresh(self):
        """Refresh all feeds in background threads"""
        logging.info("Refreshing all feeds")
        self.tree.delete(*self.tree.get_children())
        feeds = self.db.get_feeds()
        self.pending_feeds = len(feeds)
        
        if not feeds:
            self.status_var.set("No feeds to refresh")
            return
            
        self.status_var.set(f"Refreshing {self.pending_feeds} feeds...")
        
        # Clear cache first
        self.db.purge_expired_cache()
        
        # Refresh each feed
        for feed in feeds:
            url = feed[0]
            self.parser.parse_feed(url, callback=lambda x: self.update_refresh_status())
            
    def update_refresh_status(self):
        """Update refresh status as feeds complete"""
        self.pending_feeds -= 1
        if self.pending_feeds <= 0:
            self.status_var.set("All feeds refreshed")
            self.update_filters()
            self.load_feeds()
        else:
            self.status_var.set(f"Refreshing... {self.pending_feeds} feeds remaining")
            
    def purge_cache(self):
        """Periodically purge expired cache entries"""
        self.db.purge_expired_cache()
        self.after(3600000, self.purge_cache)  # Schedule next run
        
    def on_closing(self):
        """Proper cleanup when closing the application"""
        try:
            if self.db:
                self.db.close()
        except:
            logging.exception("Error during closing: %s", str(e))
            pass
        self.quit()
        
    def __del__(self):
        self.on_closing()


if __name__ == "__main__":
    app = RSSApp()
    app.protocol("WM_DELETE_WINDOW", app.on_closing)
    app.mainloop()