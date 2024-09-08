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

    if (format === 'html') {
        const htmlTemplate = `
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>${title}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }
        header {
            background-color: #f4f4f4;
            padding: 20px;
            text-align: center;
        }
        h1 {
            color: #2c3e50;
        }
        .meta {
            font-style: italic;
            color: #7f8c8d;
        }
        .content {
            margin-top: 20px;
        }
    </style>
</head>
<body>
    <header>
        <h1>${title}</h1>
        <p class="meta">Published on ${date} at ${time}</p>
    </header>
    <div class="content">
        ${content}
    </div>
</body>
</html>`;

        const blob = new Blob([htmlTemplate], { type: 'text/html' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `${title.replace(/\s+/g, '-').toLowerCase()}.html`;
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

updateDateTime();
setInterval(updateDateTime, 60000); // Update every minute

document.getElementById('title').addEventListener('input', updatePreview);
document.getElementById('content').addEventListener('input', updatePreview);