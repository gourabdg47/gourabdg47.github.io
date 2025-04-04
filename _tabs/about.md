---
# the default layout is 'page'
icon: fas fa-info-circle
order: 4
---
<style>
/* Retro Hacker Theme - Transparent */
.terminal-link {
  font-family: 'Courier New', monospace;
  color: #2ecc71 !important;
  text-decoration: none;
  padding: 8px 12px;
  position: relative;
  overflow: hidden;
  text-shadow: 0 0 4px rgba(46, 204, 113, 0.5);
  transition: all 0.3s;
  background: transparent !important;
  box-shadow: inset 0 0 10px rgba(46, 204, 113, 0.1);
}



/* Blinking Cursor */
.terminal-link::after {
  content: "▋";
  animation: blink 1s step-end infinite;
  color: #2ecc71;
  margin-left: 2px;
  text-shadow: 0 0 8px #2ecc71;
}

@keyframes blink {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}

/* Hover Effects */
.terminal-link:hover {
  box-shadow: 0 0 15px rgba(46, 204, 113, 0.4),
              inset 0 0 20px rgba(46, 204, 113, 0.2);
  animation: glitch 0.2s infinite;
}

/* TV Static Effect on Hover */
.terminal-link:hover::before {
  background: 
    linear-gradient(0deg, rgba(0, 0, 0, 0.1) 25%, 
    transparent 25%, transparent 50%, 
    rgba(0, 0, 0, 0.1) 50%, 
    rgba(0, 0, 0, 0.1) 75%, 
    transparent 75%),
    url('data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAQAAAAECAYAAACp8Z5+AAAAIklEQVQIW2NkQAKrVq36zwjjgzhhYWGMYAEYB8RmROaABADeOQ8CXl/xfgAAAABJRU5ErkJggg==');
  background-size: 100% 4px, auto;
}

@keyframes glitch {
  0% { text-shadow: 1px 0 red, -1px 0 blue; }
  25% { text-shadow: -2px 0 blue, 2px 0 red; }
  50% { transform: translateX(2px); }
  75% { transform: translateX(-2px); }
  100% { text-shadow: none; }
}

/* Command Syntax Coloring */
.terminal-link span.path { color: #3498db; }
.terminal-link span.operator { color: #e74c3c; }
.terminal-link span.command { color: #2ecc71; }
.terminal-link span.coffee { color: #f1c40f; }
</style>

<a href="https://www.buymeacoffee.com/gourabdg" class="terminal-link">
  <span class="command">root@h4x0r:~#</span> 
  <span class="path">cd ~/wallet</span>
  <span class="operator">&& ./</span>
  <span class="command">buy_me_coffee.sh - -fuel 🍵</span>
</a>