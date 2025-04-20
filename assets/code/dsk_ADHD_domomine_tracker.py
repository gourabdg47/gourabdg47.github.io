import tkinter as tk
from tkinter import ttk, messagebox
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import json
import datetime
import webbrowser
import os
from pathlib import Path

class ADHDTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("NeuroFocus Balance Tracker")
        self.root.geometry("1200x800")
        self.style = ttk.Style()
        self.current_theme = "light"  # Options: "light", "dark", "paper"
        
        # Initialize data
        self.data_file = Path("neurofocus_data.json")
        self.load_data()
        
        # Check if username exists and prompt if needed
        if not self.user_data.get("username"):
            self.prompt_for_username()
        
        # Apply theme
        self.setup_style()
        
        # Create main container
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Setup navigation
        self.create_navigation()
        self.create_main_content()
        
        # Initialize first view
        self.current_view = None
        self.show_view('dashboard')

    def setup_style(self):
        """Set up theme styles for the application"""
        self.style.theme_use('clam')
        
        # Define color schemes for different themes
        if self.current_theme == "light":
            # Light theme - calm, zen-focused
            bg_color = '#f5f7fa'        # Light background
            accent_color = '#78a1bb'    # Calm blue accent
            text_color = '#3a4454'      # Dark gray text
            highlight = '#a8d0db'       # Light blue highlight
            emergency = '#e74c3c'       # Emergency red
        elif self.current_theme == "dark":
            # Dark theme
            bg_color = '#1e2430'        # Dark blue-gray
            accent_color = '#4d6b8a'    # Muted blue
            text_color = '#dfe6e9'      # Light gray text
            highlight = '#546e7a'       # Muted teal
            emergency = '#c0392b'       # Dark red
        else:  # paper theme
            # Paper theme (black & white)
            bg_color = '#ffffff'        # White
            accent_color = '#2c3e50'    # Dark blue-gray
            text_color = '#000000'      # Black
            highlight = '#95a5a6'       # Gray
            emergency = '#7f0000'       # Dark red
        
        # Configure base styles
        self.style.configure('.', 
                        background=bg_color, 
                        foreground=text_color,
                        font=('Segoe UI', 10))
        
        self.style.configure('TFrame', background=bg_color)
        self.style.configure('TLabel', background=bg_color)
        self.style.configure('TButton', 
                        padding=8, 
                        relief='flat',
                        background=bg_color,
                        foreground=text_color)
        
        self.style.map('TButton',
                    background=[('active', highlight), ('pressed', accent_color)],
                    foreground=[('active', text_color), ('pressed', 'white')])
        
        # Navigation buttons
        self.style.configure('Nav.TButton', 
                        padding=12, 
                        font=('Segoe UI', 10),
                        background=bg_color)
        
        self.style.map('Nav.TButton',
                    background=[('active', highlight), ('pressed', accent_color)],
                    foreground=[('active', text_color), ('pressed', 'white')])
        
        # Headers
        self.style.configure('Header.TLabel', 
                        font=('Segoe UI', 14, 'bold'),
                        background=bg_color)
        
        # Emergency button
        self.style.configure('Emergency.TButton', 
                        foreground='white', 
                        background=emergency,
                        padding=10)
        
        self.style.map('Emergency.TButton', 
                    background=[('active', '#c0392b')])
        
        # Action buttons
        self.style.configure('Action.TButton', 
                        padding=10, 
                        background=accent_color,
                        foreground='white')
        
        self.style.map('Action.TButton',
                    background=[('active', highlight), ('pressed', accent_color)],
                    foreground=[('active', text_color), ('pressed', 'white')])
        
        # Treeview
        self.style.configure('Treeview', 
                        background='white' if self.current_theme != 'dark' else '#2d3436',
                        fieldbackground='white' if self.current_theme != 'dark' else '#2d3436',
                        rowheight=25)
        
        self.style.map('Treeview',
                    background=[('selected', highlight)],
                    foreground=[('selected', text_color)])

    def load_data(self):
        """Load user data from file or initialize with defaults"""
        if self.data_file.exists():
            try:
                with open(self.data_file, 'r') as f:
                    self.user_data = json.load(f)
            except json.JSONDecodeError:
                self.initialize_default_data()
        else:
            self.initialize_default_data()
    
    def initialize_default_data(self):
        """Set up default user data"""
        self.user_data = {
            "logs": [],
            "baseline": 5,
            "username": "",
            "activities": [
                "Deep Work", "Physical Exercise", "Mindful Break", 
                "Creative Activity", "Social Interaction", "Passive Consumption"
            ],
            "strategies": [
                {"name": "Pomodoro Technique", "description": "Work for 25 minutes, then take a 5-minute break"},
                {"name": "Body Doubling", "description": "Work alongside someone else to maintain focus"},
                {"name": "Task Chunking", "description": "Break large tasks into smaller, manageable pieces"},
                {"name": "Dopamine Fasting", "description": "Take breaks from high-stimulation activities to reset dopamine sensitivity"},
                {"name": "Reward Bundling", "description": "Pair less engaging tasks with small rewards to boost dopamine release"},
                {"name": "Exercise Microdosing", "description": "Short 2-5 minute movement breaks promote healthy dopamine regulation"}
            ]
        }

    def prompt_for_username(self):
        """Prompt the user for their name on first launch"""
        name_dialog = tk.Toplevel(self.root)
        name_dialog.title("Welcome to NeuroFocus Balance")
        name_dialog.geometry("400x250")
        name_dialog.transient(self.root)
        name_dialog.grab_set()
        
        frame = ttk.Frame(name_dialog, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Welcome to NeuroFocus!", 
            font=('Segoe UI', 14, 'bold')).pack(pady=(0, 10))
        
        ttk.Label(frame, text="Please enter your name:", 
            font=('Segoe UI', 11)).pack(pady=5)
        
        name_var = tk.StringVar()
        name_entry = ttk.Entry(frame, textvariable=name_var, width=30, font=('Segoe UI', 11))
        name_entry.pack(pady=10)
        name_entry.focus()
        
        def save_name():
            name = name_var.get().strip()
            if name:
                self.user_data["username"] = name
                self.save_data()
                name_dialog.destroy()
            else:
                ttk.Label(frame, text="Please enter your name to continue", 
                    foreground="red").pack(pady=5)
        
        ttk.Button(frame, text="Let's Begin!", 
                command=save_name,
                style='Action.TButton',
                padding=10).pack(pady=20)
        
        # Center the dialog
        name_dialog.update_idletasks()
        x = (self.root.winfo_width() - name_dialog.winfo_width()) // 2 + self.root.winfo_x()
        y = (self.root.winfo_height() - name_dialog.winfo_height()) // 2 + self.root.winfo_y()
        name_dialog.geometry(f"+{x}+{y}")
    
    def save_data(self):
        """Save user data to file"""
        with open(self.data_file, 'w') as f:
            json.dump(self.user_data, f)

    def change_theme(self):
        """Switch between themes"""
        new_theme = self.theme_var.get()
        if new_theme != self.current_theme:
            self.current_theme = new_theme
            self.setup_style()
            # Refresh UI
            if self.current_view:
                self.show_view(self.current_view)

    def create_navigation(self):
        """Create the side navigation panel"""
        nav_frame = ttk.Frame(self.main_frame, padding=(10, 20))
        nav_frame.pack(side=tk.LEFT, fill=tk.Y)
        
        # App title
        ttk.Label(nav_frame, text="NeuroFocus", style='Header.TLabel').pack(pady=(0, 20))
        
        nav_buttons = [
            ("🏠 Dashboard", 'dashboard'),
            ("➕ Log Activity", 'log_activity'),
            ("📈 Focus Trends", 'insights'),
            ("🛠 Strategies", 'recommendations'),
            ("ℹ️ Resources", 'resources'),
        ]
        
        # Create a reference to track which button is active
        self.nav_buttons = {}
        
        for text, view_name in nav_buttons:
            btn = ttk.Button(nav_frame, text=text, 
                        command=lambda v=view_name: self.show_view(v),
                        style='Nav.TButton',
                        width=20)
            btn.pack(fill=tk.X, pady=4)
            self.nav_buttons[view_name] = btn
        
        # Add theme switcher
        theme_frame = ttk.LabelFrame(nav_frame, text="Appearance", padding=10)
        theme_frame.pack(fill=tk.X, pady=15)
        
        themes = [("Light", "light"), ("Dark", "dark"), ("Paper", "paper")]
        self.theme_var = tk.StringVar(value=self.current_theme.capitalize())
        
        for text, theme_value in themes:
            rb = ttk.Radiobutton(theme_frame, text=text, value=theme_value,
                            variable=self.theme_var, command=self.change_theme)
            rb.pack(anchor=tk.W, pady=3)
        
        # Emergency help button
        ttk.Separator(nav_frame).pack(fill=tk.X, pady=15)
        ttk.Button(nav_frame, text="🚨 Crisis Help", 
                command=self.show_emergency_resources,
                style='Emergency.TButton').pack(side=tk.BOTTOM, fill=tk.X, pady=20)

    def create_main_content(self):
        """Create the main content area and initialize all view frames"""
        self.content_frame = ttk.Frame(self.main_frame, padding=20)
        self.content_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
        
        # Initialize view frames
        self.views = {
            'dashboard': self.create_dashboard(),
            'log_activity': self.create_log_activity(),
            'insights': self.create_insights(),
            'recommendations': self.create_recommendations(),
            'resources': self.create_resources(),
        }
        
        # Hide all views initially
        for view in self.views.values():
            view.pack_forget()

    def show_view(self, view_name):
        """Switch between different views in the application"""
        if view_name not in self.views:
            return
        
        # Hide current view if any
        if self.current_view and self.current_view in self.views:
            self.views[self.current_view].pack_forget()
            
            # Reset the previously active nav button style if any
            if self.current_view in self.nav_buttons:
                self.nav_buttons[self.current_view].configure(style='Nav.TButton')
        
        # Show new view
        self.views[view_name].pack(fill=tk.BOTH, expand=True)
        self.current_view = view_name
        
        # Highlight the active nav button
        if view_name in self.nav_buttons:
            self.nav_buttons[view_name].configure(style='Action.TButton')
        
        # Refresh data for the view
        if view_name == 'dashboard':
            self.update_dashboard()
        elif view_name == 'insights':
            self.update_insights()

    def create_dashboard(self):
        """Create the dashboard view"""
        frame = ttk.Frame(self.content_frame)
        
        # Welcome and time
        header_frame = ttk.Frame(frame)
        self.time_label = ttk.Label(header_frame, text=self.get_time_greeting(), style='Header.TLabel')
        self.time_label.pack(side=tk.LEFT)
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Current status panel
        status_frame = ttk.LabelFrame(frame, text="Current Status", padding=15)
        
        focus_frame = ttk.Frame(status_frame)
        ttk.Label(focus_frame, text="Focus Level:").pack(side=tk.LEFT)
        self.current_focus = ttk.Label(focus_frame, text="Loading...", font=('Segoe UI', 16))
        self.current_focus.pack(side=tk.LEFT, padx=10)
        focus_frame.pack(fill=tk.X, pady=10)
        
        # Quick action buttons
        action_frame = ttk.Frame(status_frame)
        ttk.Button(action_frame, text="5-Minute Focus Reset", 
                 command=self.focus_reset, 
                 style='Action.TButton').pack(side=tk.LEFT, padx=5)
        ttk.Button(action_frame, text="Sensory Break", 
                 command=self.sensory_break, 
                 style='Action.TButton').pack(side=tk.LEFT, padx=5)
        action_frame.pack(fill=tk.X, pady=10)
        
        status_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Recent activities section
        activities_frame = ttk.LabelFrame(frame, text="Recent Activities", padding=15)
        
        # Recent activities table
        self.recent_activities_table = ttk.Treeview(activities_frame, 
                                                   columns=('Time', 'Activity', 'Effect'), 
                                                   show='headings',
                                                   height=8)
        self.recent_activities_table.heading('Time', text='Time')
        self.recent_activities_table.heading('Activity', text='Activity')
        self.recent_activities_table.heading('Effect', text='Effect')
        
        # Configure column widths
        self.recent_activities_table.column('Time', width=150)
        self.recent_activities_table.column('Activity', width=200)
        self.recent_activities_table.column('Effect', width=150)
        
        # Add scrollbar
        scrollbar = ttk.Scrollbar(activities_frame, orient="vertical", 
                                command=self.recent_activities_table.yview)
        self.recent_activities_table.configure(yscrollcommand=scrollbar.set)
        
        self.recent_activities_table.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        activities_frame.pack(fill=tk.BOTH, expand=True)
        
        return frame

    def create_log_activity(self):
        """Create the log activity view"""
        frame = ttk.Frame(self.content_frame)
        
        ttk.Label(frame, text="Log New Activity", style='Header.TLabel').pack(pady=(0, 20))
        
        form_frame = ttk.LabelFrame(frame, text="Activity Details", padding=20)
        
        # Two-column layout
        form_grid = ttk.Frame(form_frame)
        
        # Activity type
        ttk.Label(form_grid, text="Activity Type:").grid(row=0, column=0, sticky=tk.W, pady=10)
        self.activity_combo = ttk.Combobox(form_grid, values=self.user_data['activities'], width=30)
        self.activity_combo.grid(row=0, column=1, sticky=tk.W, pady=10, padx=10)
        
        # Duration
        ttk.Label(form_grid, text="Duration (minutes):").grid(row=1, column=0, sticky=tk.W, pady=10)
        self.duration_spin = ttk.Spinbox(form_grid, from_=5, to=180, width=10)
        self.duration_spin.set(30)
        self.duration_spin.grid(row=1, column=1, sticky=tk.W, pady=10, padx=10)
        
        # Focus before
        ttk.Label(form_grid, text="Focus Level Before:").grid(row=2, column=0, sticky=tk.W, pady=10)
        self.focus_before_frame = ttk.Frame(form_grid)
        self.focus_before_var = tk.IntVar(value=5)
        self.focus_before_scale = ttk.Scale(self.focus_before_frame, 
                                         from_=1, to=10, 
                                         variable=self.focus_before_var,
                                         length=200,
                                         command=lambda v: self.focus_before_label.config(text=f"{int(float(v))}/10"))
        self.focus_before_scale.pack(side=tk.LEFT)
        self.focus_before_label = ttk.Label(self.focus_before_frame, text="5/10")
        self.focus_before_label.pack(side=tk.LEFT, padx=10)
        self.focus_before_frame.grid(row=2, column=1, sticky=tk.W, pady=10, padx=10)
        
        # Focus after
        ttk.Label(form_grid, text="Focus Level After:").grid(row=3, column=0, sticky=tk.W, pady=10)
        self.focus_after_frame = ttk.Frame(form_grid)
        self.focus_after_var = tk.IntVar(value=5)
        self.focus_after_scale = ttk.Scale(self.focus_after_frame, 
                                        from_=1, to=10, 
                                        variable=self.focus_after_var,
                                        length=200,
                                        command=lambda v: self.focus_after_label.config(text=f"{int(float(v))}/10"))
        self.focus_after_scale.pack(side=tk.LEFT)
        self.focus_after_label = ttk.Label(self.focus_after_frame, text="5/10")
        self.focus_after_label.pack(side=tk.LEFT, padx=10)
        self.focus_after_frame.grid(row=3, column=1, sticky=tk.W, pady=10, padx=10)
        
        # Notes
        ttk.Label(form_grid, text="Notes:").grid(row=4, column=0, sticky=tk.NW, pady=10)
        self.notes_text = tk.Text(form_grid, height=4, width=40)
        self.notes_text.grid(row=4, column=1, sticky=tk.W, pady=10, padx=10)
        
        form_grid.pack(fill=tk.BOTH, expand=True)
        
        # Submit button
        ttk.Button(form_frame, text="Log Activity", 
                 command=self.log_activity,
                 style='Action.TButton',
                 padding=10).pack(pady=15)
        
        form_frame.pack(fill=tk.BOTH, expand=True, padx=50, pady=20)
        
        return frame

    def create_insights(self):
        """Create the focus trends & insights view"""
        frame = ttk.Frame(self.content_frame)
        
        ttk.Label(frame, text="Focus Trends", style='Header.TLabel').pack(pady=(0, 20))
        
        # Create chart frame
        chart_frame = ttk.LabelFrame(frame, text="Focus Level Over Time", padding=15)
        self.chart_container = ttk.Frame(chart_frame)
        self.chart_container.pack(fill=tk.BOTH, expand=True)
        chart_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Create pattern insights frame
        insights_frame = ttk.LabelFrame(frame, text="Activity Insights", padding=15)
        self.insights_text = tk.Text(insights_frame, height=8, wrap=tk.WORD)
        self.insights_text.pack(fill=tk.BOTH, expand=True)
        insights_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        return frame

    def create_recommendations(self):
        """Create the recommendations & strategies view"""
        frame = ttk.Frame(self.content_frame)
        
        ttk.Label(frame, text="Focus Strategies", style='Header.TLabel').pack(pady=(0, 20))
        
        # Strategies container with scrollbar
        strategies_frame = ttk.Frame(frame)
        self.strategies_canvas = tk.Canvas(strategies_frame, highlightthickness=0)
        scrollbar = ttk.Scrollbar(strategies_frame, orient="vertical", command=self.strategies_canvas.yview)
        
        self.strategy_container = ttk.Frame(self.strategies_canvas)
        self.strategy_container.bind(
            "<Configure>",
            lambda e: self.strategies_canvas.configure(scrollregion=self.strategies_canvas.bbox("all"))
        )
        
        self.strategies_canvas.create_window((0, 0), window=self.strategy_container, anchor="nw")
        self.strategies_canvas.configure(yscrollcommand=scrollbar.set)
        
        strategies_frame.pack(fill=tk.BOTH, expand=True)
        self.strategies_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Add strategies
        self.display_strategies()
        
        # Add new strategy section
        add_strategy_frame = ttk.LabelFrame(frame, text="Add New Strategy", padding=15)
        
        strategy_form = ttk.Frame(add_strategy_frame)
        ttk.Label(strategy_form, text="Name:").grid(row=0, column=0, sticky=tk.W, pady=5)
        self.new_strategy_name = ttk.Entry(strategy_form, width=40)
        self.new_strategy_name.grid(row=0, column=1, sticky=tk.W, pady=5, padx=5)
        
        ttk.Label(strategy_form, text="Description:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.new_strategy_desc = ttk.Entry(strategy_form, width=40)
        self.new_strategy_desc.grid(row=1, column=1, sticky=tk.W, pady=5, padx=5)
        
        strategy_form.pack(fill=tk.X)
        
        ttk.Button(add_strategy_frame, text="Add Strategy", 
                 command=self.add_strategy,
                 style='Action.TButton').pack(pady=10)
        
        add_strategy_frame.pack(fill=tk.X, pady=10)
        
        return frame

    def display_strategies(self):
        """Display strategies in the recommendations view"""
        # Clear any existing strategies
        for widget in self.strategy_container.winfo_children():
            widget.destroy()
        
        # Add each strategy as a card
        for i, strategy in enumerate(self.user_data['strategies']):
            strategy_card = ttk.LabelFrame(self.strategy_container, padding=10)
            
            ttk.Label(strategy_card, text=strategy['name'], 
                    style='Header.TLabel').pack(anchor=tk.W)
            
            ttk.Label(strategy_card, text=strategy['description'], 
                    wraplength=500).pack(anchor=tk.W, pady=5)
            
            # Add delete button
            ttk.Button(strategy_card, text="Delete", 
                     command=lambda idx=i: self.delete_strategy(idx)).pack(anchor=tk.E)
            
            strategy_card.pack(fill=tk.X, expand=True, pady=5)

    def create_resources(self):
        """Create the resources view"""
        frame = ttk.Frame(self.content_frame)
        
        ttk.Label(frame, text="ADHD & Focus Resources", style='Header.TLabel').pack(pady=(0, 20))
        
        resources_container = ttk.Frame(frame)
        resources_container.pack(fill=tk.BOTH, expand=True)
        
        # Create resource categories
        resource_groups = {
            "Immediate Help": [
                ("Crisis Hotline", "tel:1-800-273-8255"),
                ("ADHD Coaching Directory", "https://www.adhdcoaches.org"),
                ("Talk to a Therapist", "https://www.psychologytoday.com/us/therapists"),
            ],
            "Learning Resources": [
                ("CHADD - National Resource on ADHD", "https://chadd.org"),
                ("ADDitude Magazine", "https://additudemag.com"),
                ("How to ADHD (YouTube)", "https://www.youtube.com/c/HowtoADHD"),
            ],
            "Focus Tools": [
                ("Focus Timer", self.open_focus_timer),
                ("Sensory Toolkit", self.open_sensory_tools),
                ("Task Manager", "https://todoist.com"),
            ]
        }
        
        row, col = 0, 0
        for group, resources in resource_groups.items():
            group_frame = ttk.LabelFrame(resources_container, text=group, padding=15)
            
            for text, action in resources:
                btn = ttk.Button(group_frame, text=text, 
                               command=lambda a=action: self.open_resource(a))
                btn.pack(fill=tk.X, pady=4, ipady=4)
            
            group_frame.grid(row=row, column=col, padx=10, pady=10, sticky=tk.NSEW)
            col += 1
            if col > 1:
                col = 0
                row += 1
        
        # Configure grid weights
        resources_container.grid_columnconfigure(0, weight=1)
        resources_container.grid_columnconfigure(1, weight=1)
        
        return frame

    def log_activity(self):
        """Save a new activity log entry"""
        activity_type = self.activity_combo.get()
        if not activity_type:
            messagebox.showwarning("Input Required", "Please select an activity type")
            return
        
        try:
            duration = int(self.duration_spin.get())
            focus_before = int(self.focus_before_var.get())
            focus_after = int(self.focus_after_var.get())
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter valid numbers")
            return
            
        notes = self.notes_text.get("1.0", tk.END).strip()
        
        # Create new log entry
        timestamp = datetime.datetime.now().isoformat()
        new_entry = {
            "timestamp": timestamp,
            "activity": activity_type,
            "duration": duration,
            "focus_before": focus_before,
            "focus_after": focus_after,
            "notes": notes,
            "impact": focus_after - focus_before
        }
        
        # Add to user data
        self.user_data["logs"].append(new_entry)
        self.save_data()
        
        # Clear form
        self.activity_combo.set("")
        self.duration_spin.set(30)
        self.focus_before_var.set(5)
        self.focus_after_var.set(5)
        self.notes_text.delete("1.0", tk.END)
        
        messagebox.showinfo("Success", "Activity logged successfully")
        self.show_view('dashboard')  # Return to dashboard

    def update_dashboard(self):
        """Update the dashboard with current data"""
        # Update greeting
        self.time_label.config(text=self.get_time_greeting())
        
        # Update focus level
        current_focus = self.calculate_current_focus()
        self.current_focus.config(text=f"{current_focus}/10")
        
        # Update activities table
        for item in self.recent_activities_table.get_children():
            self.recent_activities_table.delete(item)
            
        # Get recent logs (up to 10)
        recent_logs = sorted(
            self.user_data["logs"], 
            key=lambda x: x["timestamp"], 
            reverse=True
        )[:10]
        
        for log in recent_logs:
            timestamp = datetime.datetime.fromisoformat(log["timestamp"])
            formatted_time = timestamp.strftime("%b %d, %I:%M %p")
            impact = log["focus_after"] - log["focus_before"]
            
            if impact > 0:
                effect = f"↑ +{impact}"
            elif impact < 0:
                effect = f"↓ {impact}"
            else:
                effect = "→ 0"
                
            self.recent_activities_table.insert("", "end", values=(
                formatted_time,
                f"{log['activity']} ({log['duration']} min)",
                effect
            ))

    def calculate_current_focus(self):
        """Calculate current focus level based on recent logs"""
        if not self.user_data["logs"]:
            return self.user_data["baseline"]
            
        # Sort logs by timestamp
        sorted_logs = sorted(
            self.user_data["logs"], 
            key=lambda x: x["timestamp"], 
            reverse=True
        )
        
        # Get most recent focus reading
        most_recent = sorted_logs[0]["focus_after"]
        
        # Apply time decay (focus regresses toward baseline over time)
        timestamp = datetime.datetime.fromisoformat(sorted_logs[0]["timestamp"])
        now = datetime.datetime.now()
        hours_passed = (now - timestamp).total_seconds() / 3600
        
        baseline = self.user_data["baseline"]
        decay_factor = min(1.0, max(0.0, hours_passed / 24))  # Full decay after 24 hours
        
        focus = most_recent * (1 - decay_factor) + baseline * decay_factor
        return round(focus)

    def update_insights(self):
        """Update the insights view with charts and analysis"""
        # Clear existing chart
        for widget in self.chart_container.winfo_children():
            widget.destroy()
            
        if not self.user_data["logs"]:
            ttk.Label(self.chart_container, 
                    text="No activity data available yet. Start logging activities to see trends.").pack()
            return
            
        # Create figure for matplotlib
        fig, ax = plt.subplots(figsize=(8, 4))
        fig.patch.set_facecolor('#f5f7fa')
        ax.set_facecolor('#f5f7fa')
        
        # Get data for chart - last 10 activities
        logs = sorted(
            self.user_data["logs"], 
            key=lambda x: x["timestamp"]
        )[-15:]
        
        timestamps = [datetime.datetime.fromisoformat(log["timestamp"]) for log in logs]
        focus_before = [log["focus_before"] for log in logs]
        focus_after = [log["focus_after"] for log in logs]
        
        # Plot data
        ax.plot(timestamps, focus_before, 'o-', label='Before', color='#78a1bb')
        ax.plot(timestamps, focus_after, 'o-', label='After', color='#a8d0db')
        
        # Format chart
        ax.set_ylim(0, 11)
        ax.set_ylabel('Focus Level')
        ax.grid(True, linestyle='--', alpha=0.7)
        ax.legend()
        
        # Format x-axis dates
        fig.autofmt_xdate()
        
        # Add chart to UI
        canvas = FigureCanvasTkAgg(fig, master=self.chart_container)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        
        # Generate insights
        self.generate_insights()

    def generate_insights(self):
        """Generate insights based on activity logs"""
        if not self.user_data["logs"] or len(self.user_data["logs"]) < 3:
            self.insights_text.delete("1.0", tk.END)
            self.insights_text.insert(tk.END, "Log at least 3 activities to generate insights.")
            return
            
        # Clear existing insights
        self.insights_text.delete("1.0", tk.END)
        
        # Calculate activity impacts
        activity_impacts = {}
        for log in self.user_data["logs"]:
            activity = log["activity"]
            impact = log["focus_after"] - log["focus_before"]
            
            if activity not in activity_impacts:
                activity_impacts[activity] = []
                
            activity_impacts[activity].append(impact)
            
        # Generate text insights
        insights = []
        
        # Most positive activity
        best_activity = max(activity_impacts.items(), 
                        key=lambda x: sum(x[1])/len(x[1]) if x[1] else 0)
        if best_activity[1]:
            avg_impact = sum(best_activity[1])/len(best_activity[1])
            if avg_impact > 0:
                insights.append(f"• '{best_activity[0]}' seems to improve your focus the most " +
                            f"(average +{avg_impact:.1f} points).")
                insights.append(f"• Activities like '{best_activity[0]}' help release dopamine, which improves focus and motivation.")
        
        # Most negative activity
        worst_activity = min(activity_impacts.items(), 
                        key=lambda x: sum(x[1])/len(x[1]) if x[1] else 0)
        if worst_activity[1]:
            avg_impact = sum(worst_activity[1])/len(worst_activity[1])
            if avg_impact < 0:
                insights.append(f"• '{worst_activity[0]}' tends to decrease your focus " +
                            f"(average {avg_impact:.1f} points).")
                insights.append("• High-dopamine passive activities can deplete your dopamine reserves for focused work.")
        
        # Duration insights
        short_activities = [log for log in self.user_data["logs"] if log["duration"] <= 30]
        long_activities = [log for log in self.user_data["logs"] if log["duration"] > 30]
        
        if short_activities and long_activities:
            short_impact = sum(log["focus_after"] - log["focus_before"] for log in short_activities) / len(short_activities)
            long_impact = sum(log["focus_after"] - log["focus_before"] for log in long_activities) / len(long_activities)
            
            if abs(short_impact - long_impact) > 1:
                if short_impact > long_impact:
                    insights.append(f"• Shorter activities (≤30 min) tend to be more beneficial for your focus " +
                                f"than longer ones (+{short_impact:.1f} vs. {long_impact:.1f}).")
                    insights.append("• Short, focused sessions may optimize dopamine cycling for ADHD brains.")
                else:
                    insights.append(f"• Longer activities (>30 min) tend to be more beneficial for your focus " +
                                f"than shorter ones (+{long_impact:.1f} vs. {short_impact:.1f}).")
                    insights.append("• Your dopamine system may benefit from sustained engagement.")
        
        # Time of day insights
        morning_logs = [log for log in self.user_data["logs"] 
                    if datetime.datetime.fromisoformat(log["timestamp"]).hour < 12]
        afternoon_logs = [log for log in self.user_data["logs"] 
                    if 12 <= datetime.datetime.fromisoformat(log["timestamp"]).hour < 18]
        evening_logs = [log for log in self.user_data["logs"] 
                    if datetime.datetime.fromisoformat(log["timestamp"]).hour >= 18]
        
        times = []
        if morning_logs:
            morning_impact = sum(log["focus_after"] - log["focus_before"] for log in morning_logs) / len(morning_logs)
            times.append(("Morning", morning_impact))
        
        if afternoon_logs:
            afternoon_impact = sum(log["focus_after"] - log["focus_before"] for log in afternoon_logs) / len(afternoon_logs)
            times.append(("Afternoon", afternoon_impact))
            
        if evening_logs:
            evening_impact = sum(log["focus_after"] - log["focus_before"] for log in evening_logs) / len(evening_logs)
            times.append(("Evening", evening_impact))
        
        if times:
            best_time = max(times, key=lambda x: x[1])
            insights.append(f"• {best_time[0]} appears to be your most productive time of day " +
                        f"(average focus impact: +{best_time[1]:.1f}).")
            insights.append("• Your natural dopamine rhythm may peak during this time. Consider scheduling important tasks then.")
        
        # Pattern recommendations
        if best_activity[1]:
            insights.append(f"• Try incorporating more '{best_activity[0]}' activities into your schedule.")
            
        # Dopamine-specific insights
        insights.append("• Regular physical movement helps regulate dopamine levels throughout the day.")
        insights.append("• Alternating between focus and rest helps maintain optimal dopamine balance.")
        
        # Add insights to text widget
        if insights:
            self.insights_text.insert(tk.END, "Based on your activity patterns:\n\n" + "\n\n".join(insights))
        else:
            self.insights_text.insert(tk.END, "Continue logging activities to generate meaningful insights.")

    def add_strategy(self):
        """Add a new strategy to the recommendations"""
        name = self.new_strategy_name.get().strip()
        description = self.new_strategy_desc.get().strip()
        
        if not name or not description:
            messagebox.showwarning("Input Required", "Please enter both name and description")
            return
            
        # Add to user data
        self.user_data["strategies"].append({
            "name": name,
            "description": description
        })
        self.save_data()
        
        # Clear inputs
        self.new_strategy_name.delete(0, tk.END)
        self.new_strategy_desc.delete(0, tk.END)
        
        # Refresh display
        self.display_strategies()

    def delete_strategy(self, index):
        """Delete a strategy from recommendations"""
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this strategy?"):
            del self.user_data["strategies"][index]
            self.save_data()
            self.display_strategies()

    def focus_reset(self):
        """Show focus reset guidance"""
        reset_window = tk.Toplevel(self.root)
        reset_window.title("5-Minute Focus Reset")
        reset_window.geometry("500x400")
        
        main_frame = ttk.Frame(reset_window)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create canvas with scrollbar
        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        frame = ttk.Frame(scrollable_frame, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="5-Minute Focus Reset", 
            font=('Segoe UI', 14, 'bold')).pack(pady=(0, 20))
        
        steps = [
            ("1. Deep Breathing (1 min)", 
            "Take 5 deep breaths, inhaling for 4 counts and exhaling for 6 counts."),
            ("2. Physical Reset (1 min)", 
            "Stand up, stretch your arms overhead, and gently twist side to side."),
            ("3. Mental Reset (1 min)", 
            "Close your eyes and visualize a calming scene."),
            ("4. Environment Reset (1 min)", 
            "Clear immediate workspace of distractions, adjust lighting if needed."),
            ("5. Intention Setting (1 min)", 
            "Write down what you want to focus on for the next work period.")
        ]
        
        for title, desc in steps:
            step_frame = ttk.Frame(frame, padding=5)
            ttk.Label(step_frame, text=title, 
                    font=('Segoe UI', 10, 'bold')).pack(anchor=tk.W)
            ttk.Label(step_frame, text=desc, 
                    wraplength=450).pack(anchor=tk.W, padx=20)
            step_frame.pack(fill=tk.X, pady=5)
            
        # Dopamine note
        dopamine_frame = ttk.LabelFrame(frame, text="Dopamine Effect", padding=10)
        ttk.Label(dopamine_frame, text="This reset activates your brain's reward system by providing " +
                "a refreshing change of stimulation. The physical movement and deep breathing " +
                "help regulate dopamine levels that support sustained attention.",
                wraplength=450).pack(anchor=tk.W)
        dopamine_frame.pack(fill=tk.X, pady=10)
        
        ttk.Button(frame, text="Start Timer", 
                command=lambda: self.start_countdown(reset_window, 300, "Focus Reset"),
                style='Action.TButton').pack(pady=20)

    def sensory_break(self):
        """Show sensory break options"""
        sensory_window = tk.Toplevel(self.root)
        sensory_window.title("Sensory Break Options")
        sensory_window.geometry("500x400")
        
        main_frame = ttk.Frame(sensory_window)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create canvas with scrollbar
        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        frame = ttk.Frame(scrollable_frame, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Sensory Break Options", 
            font=('Segoe UI', 14, 'bold')).pack(pady=(0, 20))
        
        # Dopamine explanation
        dopamine_frame = ttk.LabelFrame(frame, text="Dopamine & Sensory Input", padding=10)
        ttk.Label(dopamine_frame, text="ADHD brains are often seeking optimal dopamine levels. " +
                "Strategic sensory input can help regulate your dopamine system and improve focus. " +
                "Different sensory channels affect your brain's reward system in unique ways.",
                wraplength=450).pack(anchor=tk.W)
        dopamine_frame.pack(fill=tk.X, pady=10)
        
        options = [
            ("Visual", [
                "Look out the window at nature for 30 seconds",
                "Close your eyes and rest them for 1 minute",
                "Adjust lighting (dimmer or brighter)"
            ]),
            ("Auditory", [
                "Listen to white noise or nature sounds",
                "Put on noise-cancelling headphones",
                "Listen to a favorite energizing song"
            ]),
            ("Tactile", [
                "Use a fidget toy or stress ball",
                "Run hands under warm or cool water",
                "Wrap yourself in a weighted or soft blanket"
            ]),
            ("Proprioceptive", [
                "Do 10 wall push-ups",
                "Stretch arms, neck, and back",
                "Rock gently in a chair"
            ])
        ]
        
        for category, items in options:
            cat_frame = ttk.LabelFrame(frame, text=category, padding=10)
            for item in items:
                ttk.Label(cat_frame, text="• " + item).pack(anchor=tk.W, pady=2)
            cat_frame.pack(fill=tk.X, pady=5)
            
        ttk.Button(frame, text="Start 2-Minute Timer", 
                command=lambda: self.start_countdown(sensory_window, 120, "Sensory Break"),
                style='Action.TButton').pack(pady=10)

    def start_countdown(self, parent_window, seconds, activity_name):
        """Start a countdown timer for an activity"""
        timer_window = tk.Toplevel(parent_window)
        timer_window.title(f"{activity_name} Timer")
        timer_window.geometry("300x200")
        
        frame = ttk.Frame(timer_window, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text=activity_name, 
               font=('Segoe UI', 14, 'bold')).pack(pady=(0, 20))
        
        time_label = ttk.Label(frame, 
                             text=self.format_time(seconds), 
                             font=('Segoe UI', 24))
        time_label.pack(pady=10)
        
        def update_timer():
            nonlocal seconds
            if seconds > 0:
                seconds -= 1
                time_label.config(text=self.format_time(seconds))
                timer_window.after(1000, update_timer)
            else:
                time_label.config(text="Complete!")
                ttk.Label(frame, text="Break completed. You can return to your tasks.",
                        font=('Segoe UI', 10)).pack(pady=10)
                ttk.Button(frame, text="Close", 
                         command=timer_window.destroy).pack()
        
        # Start the countdown
        update_timer()

    def format_time(self, seconds):
        """Format seconds as MM:SS"""
        minutes, seconds = divmod(seconds, 60)
        return f"{minutes:02d}:{seconds:02d}"

    def open_focus_timer(self):
        """Open a Pomodoro-style focus timer"""
        timer_window = tk.Toplevel(self.root)
        timer_window.title("Focus Timer")
        timer_window.geometry("400x300")
        
        frame = ttk.Frame(timer_window, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Focus Timer", 
               font=('Segoe UI', 14, 'bold')).pack(pady=(0, 20))
        
        # Timer settings
        settings_frame = ttk.Frame(frame)
        
        ttk.Label(settings_frame, text="Work:").grid(row=0, column=0, padx=5, pady=5)
        work_time = ttk.Spinbox(settings_frame, from_=1, to=60, width=5)
        work_time.set(25)
        work_time.grid(row=0, column=1, padx=5, pady=5)
        ttk.Label(settings_frame, text="min").grid(row=0, column=2, padx=5, pady=5)
        
        ttk.Label(settings_frame, text="Break:").grid(row=1, column=0, padx=5, pady=5)
        break_time = ttk.Spinbox(settings_frame, from_=1, to=30, width=5)
        break_time.set(5)
        break_time.grid(row=1, column=1, padx=5, pady=5)
        ttk.Label(settings_frame, text="min").grid(row=1, column=2, padx=5, pady=5)
        
        settings_frame.pack(pady=10)
        
        # Timer display
        time_display = ttk.Label(frame, text="25:00", font=('Segoe UI', 32))
        time_display.pack(pady=10)
        
        status_label = ttk.Label(frame, text="Ready to start")
        status_label.pack(pady=5)
        
        # Timer variables
        timer_running = False
        timer_paused = False
        remaining_seconds = 0
        timer_job = None
        current_mode = "work"  # "work" or "break"
        
        def start_timer():
            nonlocal timer_running, timer_paused, remaining_seconds, timer_job, current_mode
            
            if timer_running and not timer_paused:
                # Pause timer
                timer_paused = True
                start_btn.config(text="Resume")
                status_label.config(text="Paused")
                if timer_job:
                    frame.after_cancel(timer_job)
                    
            elif timer_paused:
                # Resume timer
                timer_paused = False
                start_btn.config(text="Pause")
                status_label.config(text=f"{current_mode.capitalize()} time" if current_mode == "work" 
                                else "Break time")
                update_timer()
                
            else:
                # Start new timer
                try:
                    if current_mode == "work":
                        remaining_seconds = int(work_time.get()) * 60
                    else:
                        remaining_seconds = int(break_time.get()) * 60
                except ValueError:
                    messagebox.showwarning("Invalid Input", "Please enter valid times")
                    return
                    
                timer_running = True
                timer_paused = False
                start_btn.config(text="Pause")
                status_label.config(text=f"{current_mode.capitalize()} time")
                reset_btn.config(state="normal")
                update_timer()
                
        def update_timer():
            nonlocal remaining_seconds, timer_job, current_mode
            
            if remaining_seconds > 0:
                minutes, seconds = divmod(remaining_seconds, 60)
                time_display.config(text=f"{minutes:02d}:{seconds:02d}")
                remaining_seconds -= 1
                timer_job = frame.after(1000, update_timer)
            else:
                # Timer finished
                time_display.config(text="00:00")
                
                if current_mode == "work":
                    messagebox.showinfo("Timer", "Work session complete! Time for a break.")
                    current_mode = "break"
                    remaining_seconds = int(break_time.get()) * 60
                    status_label.config(text="Break time")
                    update_timer()
                else:
                    messagebox.showinfo("Timer", "Break complete! Ready for next work session?")
                    current_mode = "work"
                    time_display.config(text=f"{work_time.get()}:00")
                    status_label.config(text="Ready to start")
                    start_btn.config(text="Start")
                    timer_running = False
                
        def reset_timer():
            nonlocal timer_running, timer_paused, timer_job, current_mode
            
            if timer_job:
                frame.after_cancel(timer_job)
                
            timer_running = False
            timer_paused = False
            current_mode = "work"
            
            try:
                minutes = int(work_time.get())
                time_display.config(text=f"{minutes:02d}:00")
            except ValueError:
                time_display.config(text="25:00")
                
            status_label.config(text="Ready to start")
            start_btn.config(text="Start")
            reset_btn.config(state="disabled")
        
        # Control buttons
        buttons_frame = ttk.Frame(frame)
        start_btn = ttk.Button(buttons_frame, text="Start", command=start_timer, style='Action.TButton')
        start_btn.pack(side=tk.LEFT, padx=5)
        
        reset_btn = ttk.Button(buttons_frame, text="Reset", command=reset_timer, state="disabled")
        reset_btn.pack(side=tk.LEFT, padx=5)
        
        buttons_frame.pack(pady=15)

    def open_sensory_tools(self):
        """Open sensory tools guide"""
        tools_window = tk.Toplevel(self.root)
        tools_window.title("Sensory Toolkit")
        tools_window.geometry("600x500")
        
        frame = ttk.Frame(tools_window, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="ADHD Sensory Toolkit", 
               font=('Segoe UI', 14, 'bold')).pack(pady=(0, 20))
        
        # Create notebook with tabs
        notebook = ttk.Notebook(frame)
        
        # Visual tab
        visual_tab = ttk.Frame(notebook, padding=10)
        ttk.Label(visual_tab, text="Visual Tools", 
               font=('Segoe UI', 12, 'bold')).pack(anchor=tk.W, pady=5)
        
        visual_items = [
            "Adjust lighting - Use warm lights, reduce fluorescent exposure",
            "Use color coding systems for organization",
            "Create a visually calm workspace with minimal clutter",
            "Try colored overlays for reading (blue or yellow often help)",
            "Consider glasses with tints designed for focus"
        ]
        
        for item in visual_items:
            ttk.Label(visual_tab, text="• " + item, wraplength=500).pack(anchor=tk.W, pady=3)
            
        # Auditory tab
        auditory_tab = ttk.Frame(notebook, padding=10)
        ttk.Label(auditory_tab, text="Auditory Tools", 
               font=('Segoe UI', 12, 'bold')).pack(anchor=tk.W, pady=5)
        
        auditory_items = [
            "Noise-cancelling headphones",
            "White noise, brown noise, or pink noise generators",
            "Lo-fi or instrumental music (avoid lyrics for deep work)",
            "Nature sounds like rainfall or ocean waves",
            "Ear plugs or ear defenders for high-sensitivity moments"
        ]
        
        for item in auditory_items:
            ttk.Label(auditory_tab, text="• " + item, wraplength=500).pack(anchor=tk.W, pady=3)
            
        # Tactile tab
        tactile_tab = ttk.Frame(notebook, padding=10)
        ttk.Label(tactile_tab, text="Tactile & Movement Tools", 
               font=('Segoe UI', 12, 'bold')).pack(anchor=tk.W, pady=5)
        
        tactile_items = [
            "Fidget toys (spinners, cubes, putty, tangles)",
            "Textured items (stress balls, brushes, fabrics)",
            "Weighted items (lap pad, blanket, vest)",
            "Standing desk or wobble stool",
            "Balance board for subtle movement while working",
            "Chewable jewelry or gum for oral sensory needs"
        ]
        
        for item in tactile_items:
            ttk.Label(tactile_tab, text="• " + item, wraplength=500).pack(anchor=tk.W, pady=3)
            
        # Add tabs to notebook
        notebook.add(visual_tab, text="Visual")
        notebook.add(auditory_tab, text="Auditory")
        notebook.add(tactile_tab, text="Tactile & Movement")
        notebook.pack(fill=tk.BOTH, expand=True)
        
        # Resources section
        resources_frame = ttk.LabelFrame(frame, text="Additional Resources", padding=10)
        
        resources = [
            ("Sensory Diet Guide", "https://www.sensorysmarts.com"),
            ("DIY Sensory Tools", "https://www.understood.org")
        ]
        
        for text, link in resources:
            ttk.Button(resources_frame, text=text, 
                     command=lambda l=link: webbrowser.open(l)).pack(side=tk.LEFT, padx=10, pady=5)
            
        resources_frame.pack(fill=tk.X, pady=10)

    def open_resource(self, resource):
        """Open a resource, either a URL or a function"""
        if isinstance(resource, str):
            # Handle different URL types
            if resource.startswith("tel:"):
                messagebox.showinfo("Phone Number", f"Call {resource[4:]}")
            elif resource.startswith("sms:"):
                messagebox.showinfo("Text Number", f"Text {resource[4:]}")
            else:
                webbrowser.open(resource)
        else:
            # It's a function, call it
            resource()

    def show_emergency_resources(self):
        """Show emergency mental health resources"""
        emergency_window = tk.Toplevel(self.root)
        emergency_window.title("Emergency Mental Health Resources")
        emergency_window.geometry("400x400")
        
        main_frame = ttk.Frame(emergency_window)
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Create canvas with scrollbar
        canvas = tk.Canvas(main_frame)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        frame = ttk.Frame(scrollable_frame, padding=20)
        frame.pack(fill=tk.BOTH, expand=True)
        
        ttk.Label(frame, text="Crisis Resources", 
            font=('Segoe UI', 14, 'bold')).pack(pady=(0, 20))
        
        resources = [
            ("National Suicide Prevention Lifeline", "Call 988 or 1-800-273-8255", "tel:988"),
            ("Crisis Text Line", "Text HOME to 741741", "sms:741741"),
            ("SAMHSA Helpline", "1-800-662-4357", "tel:1-800-662-4357"),
            ("Locate Local Crisis Centers", "https://findtreatment.samhsa.gov")
        ]
        
        for title, desc, link in resources:
            resource_frame = ttk.Frame(frame, padding=5)
            ttk.Label(resource_frame, text=title, 
                    font=('Segoe UI', 10, 'bold')).pack(anchor=tk.W)
            ttk.Label(resource_frame, text=desc).pack(anchor=tk.W, padx=10)
            
            btn = ttk.Button(resource_frame, text="Access", 
                        command=lambda l=link: self.open_resource(l),
                        style='Emergency.TButton')
            btn.pack(anchor=tk.W, pady=5)
            
            resource_frame.pack(fill=tk.X, pady=5)
        
        # Add ADHD-specific crisis info
        adhd_frame = ttk.LabelFrame(frame, text="ADHD Crisis Support", padding=10)
        ttk.Label(adhd_frame, text="ADHD can intensify emotional responses. If you're experiencing:" +
                "\n• Extreme overwhelm\n• Intense rejection sensitivity\n• Emotional dysregulation" +
                "\n\nThese are valid concerns that deserve attention. Professional support can help.",
                wraplength=350).pack(pady=5)
        adhd_frame.pack(fill=tk.X, pady=10)
        
        # Safety reminder
        ttk.Separator(frame).pack(fill=tk.X, pady=10)
        ttk.Label(frame, text="If you're in immediate danger, please call 911 or go to your nearest emergency room.",
                wraplength=350).pack(pady=10)

    def get_time_greeting(self):
        """Return a time-appropriate greeting with username"""
        hour = datetime.datetime.now().hour
        username = self.user_data.get("username", "")
        
        greeting = ""
        if 5 <= hour < 12:
            greeting = "Good morning"
        elif 12 <= hour < 18:
            greeting = "Good afternoon"
        else:
            greeting = "Good evening"
            
        if username:
            greeting += f", {username}"
            
        return greeting


if __name__ == "__main__":
    root = tk.Tk()
    app = ADHDTrackerApp(root)
    root.mainloop()