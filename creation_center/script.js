function updateDateTime() {
    const now = new Date();
    const dateOptions = { day: '2-digit', month: 'short', year: 'numeric' };
    const timeOptions = { hour: '2-digit', minute: '2-digit', hour12: true };
    
    document.getElementById('date').value = now.toLocaleDateString('en-US', dateOptions);
    document.getElementById('time').value = now.toLocaleTimeString('en-US', timeOptions);
}

function updatePreview() {
    const title = document.getElementById('title').value;
    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;
    const content = document.getElementById('content').innerHTML;
    
    const preview = document.getElementById('preview');
    preview.innerHTML = `
        <h2>${title}</h2>
        <p><strong>Date:</strong> ${date}</p>
        <p><strong>Time:</strong> ${time}</p>
        ${content}
    `;
}

function applyStyle(style) {
    document.execCommand(style, false, null);
    document.getElementById('content').focus();
}

function applyHeading(level) {
    const selection = window.getSelection();
    const range = selection.getRangeAt(0);
    const container = range.commonAncestorContainer;

    // Check if we're already inside a heading
    let currentHeading = container.nodeType === Node.TEXT_NODE ? container.parentNode : container;
    while (currentHeading && !['H1', 'H2', 'H3'].includes(currentHeading.tagName)) {
        currentHeading = currentHeading.parentNode;
    }

    if (currentHeading && currentHeading.tagName === level.toUpperCase()) {
        // If we're in the same heading level, remove it
        document.execCommand('formatBlock', false, 'p');
    } else {
        // Apply the new heading
        document.execCommand('formatBlock', false, level);
    }

    document.getElementById('content').focus();
}

function get_file_name(str){
    return str.replace(/ /g, "_");
}

function saveContent(format) {
    const title = document.getElementById('title').value;
    const date = document.getElementById('date').value;
    const time = document.getElementById('time').value;
    const content = document.getElementById('content').innerHTML;
    const tags = document.getElementById('tags').value.split(',').map(tag => tag.trim()).filter(tag => tag);

    if (format === 'html') {
        const htmlTemplate = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-4428530035708940"
    crossorigin="anonymous"></script>
    <title>${title}</title>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;500;700&family=Roboto+Mono:wght@300;400;500&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --bg-gradient: linear-gradient(135deg, #1f2937 0%, #263445 50%, #1e3a5f 100%);
            --text-color: #e5e7eb;
            --accent-color: #60a5fa;
            --accent-hover: #3b82f6;
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        html, body {
            height: 100%;
            font-size: 16px;
        }

        body {
            background: var(--bg-gradient) fixed;
            color: var(--text-color);
            font-family: 'Roboto Mono', monospace;
            line-height: 1.6;
            padding: 2rem 1rem;
        }

        .container {
            max-width: 800px;
            margin: 0 auto;
            background-color: rgba(255, 255, 255, 0.05);
            border-radius: 10px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
            overflow: hidden;
            backdrop-filter: blur(10px);
            border: 1px solid rgba(255, 255, 255, 0.1);
        }

        header {
            text-align: center;
            padding: 2rem 1rem;
            background-color: rgba(0, 0, 0, 0.2);
        }

        h1, h2, h3, h4, h5, h6 {
            font-family: 'Orbitron', sans-serif;
            letter-spacing: 1px;
            line-height: 1.2;
            margin-bottom: 1rem;
            color: var(--accent-color);
        }

        header h1 {
            font-size: 2.5rem;
            color: #fff;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            margin-bottom: 0.5rem;
        }

        .meta {
            font-style: italic;
            color: #bbb;
            font-size: 0.9rem;
        }

        .content {
            padding: 2rem;
            color: #FFFFFF;
            background-color: rgba(255, 255, 255, 0.03);
        }

        a {
            color: var(--accent-color);
            text-decoration: none;
            transition: color 0.3s ease;
        }

        a:hover {
            color: var(--accent-hover);
            text-decoration: underline;
        }

        p {
            margin-bottom: 1rem;
        }

        img {
            max-width: 100%;
            height: auto;
            border-radius: 5px;
            margin: 1rem 0;
        }
        
        .tags {
            margin-top: 1.5rem;
            padding: 1rem;
            background-color: rgba(0, 0, 0, 0.2);
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        .tag {
            display: inline-block;
            background-color: var(--accent-color);
            color: #000;
            font-size: 0.8rem;
            padding: 0.3rem 0.6rem;
            margin: 0.2rem;
            border-radius: 15px;
            transition: all 0.3s ease;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
        }

        .tag:hover {
            background-color: var(--accent-hover);
            transform: translateY(-2px);
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        }

        footer {
            background-color: rgba(25, 35, 52, 0.8);
            color: var(--text-color);
            padding: 2rem 1rem;
            text-align: center;
            margin-top: 2rem;
            backdrop-filter: blur(10px);
            border-top: 1px solid rgba(255, 255, 255, 0.1);
        }

        .social-icons {
            margin-top: 1rem;
        }

        .social-icons a {
            color: var(--text-color);
            font-size: 1.5rem;
            margin: 0 0.5rem;
            transition: color 0.3s ease;
        }

        .social-icons a:hover {
            color: var(--accent-color);
        }

        .disqus-container {
                margin-top: 2rem;
                padding: 1rem;
                background-color: rgba(0, 0, 0, 0.2);
                border-radius: 10px;
                box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1), 0 1px 3px rgba(0, 0, 0, 0.08);
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.1);
            }

        @media (max-width: 600px) {
            html {
                font-size: 14px;
            }

            body {
                padding: 1rem;
            }

            header, .content {
                padding: 1.5rem 1rem;
            }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>${title}</h1>
            <p class="meta">Published on ${date} at ${time}</p>
        </header>
        <div class="content">
            ${content}
        </div>
        <div class="tags">
            ${tags.map(tag => `<span class="tag">#${tag}</span>`).join(' ')}
        </div>
        <!-- Disqus comments section -->
        <div id="disqus_thread"></div>
            <script>
                var disqus_config = function () {
                    this.page.url = window.location.href;
                    this.page.identifier = window.location.pathname;
                };
                (function() {
                    var d = document, s = d.createElement('script');
                    s.src = 'https://gourabdg47-github-io.disqus.com/embed.js';
                    s.setAttribute('data-timestamp', +new Date());
                    (d.head || d.body).appendChild(s);
                })();
            </script>
            <noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
        </div>
    </div>
    <footer>
        <p>&copy; 2024 Singularity. All rights reserved.</p>
        <div class="social-icons">
            <a href="#" aria-label="GitHub"><i class="fab fa-github"></i></a>
            <a href="mailto:gourab@gmail.com" aria-label="Gmail"><i class="fas fa-envelope"></i></a>
            <a href="https://www.linkedin.com/in/gourabdasgupta/" aria-label="LinkedIn"><i class="fab fa-linkedin"></i></a>
            <a href="https://www.reddit.com/user/kikimora47" aria-label="Reddit"><i class="fab fa-reddit"></i></a>
        </div>
    </footer>
</body>
</html>`;

        const blob = new Blob([htmlTemplate], { type: 'text/html' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `${get_file_name(title)}.html`;
        a.click();
        URL.revokeObjectURL(url);
    } else {
        // ... existing code for other formats ...
    }
}

function insertLink() {
    const selection = window.getSelection();
    const range = selection.getRangeAt(0);
    const selectedText = range.toString();

    const url = prompt("Enter the URL:", "https://");
    if (url) {
        const linkText = selectedText || prompt("Enter the link text:", "");
        if (linkText) {
            const link = document.createElement('a');
            link.href = url;
            link.textContent = linkText;
            range.deleteContents();
            range.insertNode(link);
        }
    }
    updatePreview();
}

function insertImage() {
    const url = prompt('Enter the URL of the image:');
    if (url) {
        document.execCommand('insertImage', false, url);
    }
}

function changeTextColor() {
    const color = prompt('Enter a color name or hex code:');
    if (color) {
        document.execCommand('foreColor', false, color);
    }
}

updateDateTime();
setInterval(updateDateTime, 60000); // Update every minute

document.getElementById('title').addEventListener('input', updatePreview);
document.getElementById('content').addEventListener('input', updatePreview);