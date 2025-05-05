import pygetwindow as gw
import time
import sys
import psutil
from desktop_notifier import DesktopNotifier
import math
import asyncio
import tracemalloc
import json
import os
import random
from datetime import datetime, date, timedelta
import platform

from collections import deque
import concurrent.futures
import traceback
import sqlite3

# --- ANSI Color Codes & Emojis ---
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_BLUE = "\033[94m"
COLOR_MAGENTA = "\033[95m"  # For hyperfocus alerts
COLOR_CYAN = "\033[96m"     # For positive reinforcement
COLOR_RESET = "\033[0m"
BOLD = "\033[1m"

# ADHD-friendly emojis for different states
EMOJI_PRODUCTIVE = "⚡ "     # Energy/focus
EMOJI_BREAK_TIME = "🌱 "    # Refresh/growth
EMOJI_DISTRACTED = "🦋 "    # Butterfly mind - gentler than a warning symbol
EMOJI_HYPERFOCUS = "🔍 "    # Deep focus
EMOJI_ACHIEVEMENT = "🎯 "   # Achievement
EMOJI_SWITCH = "↻ "         # Task switching

# --- Configuration ---

# ** Data Storage **
DATA_DIR_NAME = "adhd_activity_tracker_data"
CONFIG_FILE_NAME = "activity_log.json"
STREAK_FILE_NAME = "achievement_data.json"
CURRENT_WORKING_DIR = os.getcwd()
DATA_DIR_PATH = os.path.join(CURRENT_WORKING_DIR, DATA_DIR_NAME)
LOG_FILE_PATH = os.path.join(DATA_DIR_PATH, CONFIG_FILE_NAME)
STREAK_FILE_PATH = os.path.join(DATA_DIR_PATH, STREAK_FILE_NAME)

# ** Global Log Data (Loaded at start) **
log_data = {}
achievement_data = {
    "streaks": {"current": 0, "best": 0},
    "achievements": [],
    "daily_goals": {"productive_minutes": 120, "completed_dates": []}
}

# Same productivity categories as original
PRODUCTIVITY_CATEGORIES = {
    "Productive": {
        "Office Suites & Docs": ['microsoft word', 'winword', 'excel', 'powerpoint', 'outlook', 'onenote', 'google docs', 'google sheets', 'google slides', 'google forms', 'google calendar', 'gmail', 'libreoffice', 'openoffice', 'writer', 'calc', 'impress', 'zoho work', 'document editor', 'spreadsheet editor', 'wordperfect', 'latex', 'texmaker', 'overleaf'],
        "Programming & Dev": ['visual studio code', 'vscode', 'code.exe', 'code', 'pycharm', 'intellij', 'android studio', 'webstorm', 'clion', 'sublime text', 'atom', 'vim', 'neovim', 'emacs', 'terminal', 'command prompt', 'powershell', 'bash', 'zsh', 'iterm', 'konsole', 'github', 'gitlab', 'bitbucket', 'gitkraken', 'sourcetree', 'docker', 'kubernetes', 'localhost', '127.0.0.1', 'debug', 'compile', 'developer tools', 'postman', 'stackoverflow', 'stack exchange', 'mdn web docs', 'w3schools', 'python.org/docs', 'dev.java', 'cplusplus.com', 'php.net/docs'],
        "Creative & Design": ['photoshop', 'illustrator', 'indesign', 'premiere pro', 'after effects', 'adobe xd', 'figma', 'sketch', 'invision', 'zeplin', 'canva', 'blender', 'maya', '3ds max', 'autocad', 'davinci resolve', 'final cut pro', 'logic pro', 'ableton live', 'pro tools', 'audacity'],
        "Communication (Work/Study)": ['slack', 'microsoft teams', 'zoom', 'google meet', 'webex'],
        "Task & Project Management": ['jira', 'trello', 'asana', 'monday.com', 'clickup', 'basecamp', 'notion', 'obsidian', 'evernote', 'microsoft to do', 'todoist', 'any.do', 'calendar', 'scheduling', 'planner'],
        "Research & Learning": ['Security-Plus-Guide-skillweed', 'wikipedia', 'google scholar', 'pubmed', 'jstor', 'arxiv', 'researchgate', 'coursera', 'edx', 'udemy', 'khan academy', 'linkedin learning', 'documentation', 'research paper', 'study', 'learning', 'tutorial', 'reference'],
        "Focus & Productivity Tools": ['freedom.to', 'cold turkey', 'forest', 'focus keeper', 'rescuetime', 'rize.io', 'lifeat', 'stayfocusd', 'pomodoro', 'session', 'flown', 'brain.fm', 'noisli'],
        "Business Specific": ['quickbooks', 'xero', 'sage', 'netsuite', 'salesforce', 'hubspot', 'zoho crm' ]
    },
    "Non-Productive": {
        "Social Media": ['facebook', 'fb.com', 'instagram', 'twitter', 'x.com', 'tiktok', 'reddit', 'pinterest', 'snapchat', 'tumblr', 'linkedin'],
        "Video Streaming": ['youtube', 'netflix', 'hulu', 'amazon prime video', 'prime video', 'disney+', 'disneyplus', 'hbo max', 'max', 'peacock', 'apple tv', 'twitch', 'vimeo'],
        "Music Streaming (Active Focus)": ['spotify', 'apple music', 'youtube music', 'pandora', 'soundcloud', 'tidal'],
        "Messaging (Casual/Social)": ['whatsapp', 'web.whatsapp.com', 'facebook messenger', 'messenger.com', 'discord', 'telegram', 'signal', 'wechat', 'kik', 'skype'],
        "Shopping": ['amazon', 'ebay', 'etsy', 'walmart', 'target', 'best buy', 'aliexpress', 'shein', 'temu', 'newegg'],
        "News & General Browse": [ 'cnn', 'bbc', 'fox news', 'nytimes', 'washington post', 'guardian', 'npr', 'reuters', 'associated press', 'wsj', 'google news', 'apple news', 'yahoo', 'buzzfeed', 'huffpost', 'the onion', 'cracked', 'vice', 'daily mail', 'reddit', 'imgur', '9gag', 'boredpanda', 'wikipedia'],
        "Gaming": ['steam', 'epic games', 'gog galaxy', 'battle.net', 'origin', 'ea app', 'ubisoft connect', 'minecraft', 'fortnite', 'valorant', 'league of legends', 'dota', 'csgo', 'overwatch', 'apex legends', 'roblox', 'genshin impact', 'miniclip', 'addicting games', 'pogo', 'kongregate', 'twitch'],
        "Miscellaneous Distractions": ['imdb', 'rottentomatoes', 'tmz', 'sports', 'espn', 'bleacher report', 'nfl', 'nba', 'mlb', 'coinbase', 'binance', 'coinmarketcap', 'coingecko', 'dating', 'tinder', 'bumble', 'hinge', 'match.com', 'okcupid', 'personal email']
    }
}

# --- ADHD-Optimized Time Settings ---
CHECK_INTERVAL_SECONDS = 2  # More frequent checks for ADHD users
# Shorter focus alert timeframe - alerts for non-productive time
DISTRACTION_ALERT_SECONDS = 3 * 60  # Alert after 3 min of distraction (shorter for ADHD)
# ADHD-friendly pattern: 25 min work followed by 5 min break (Pomodoro-inspired)
MICRO_BREAK_SUGGESTION = 25 * 60  # Suggest micro-break every 25 minutes
BREAK_DURATION_SECONDS = 5 * 60   # Recommended 5 min break duration
# Hyperfocus detection (long period without switching windows)
HYPERFOCUS_DETECTION_SECONDS = 45 * 60  # 45+ minutes on same task may be hyperfocus
# Task switching metrics (too many switches in short time may indicate attention issues)
TASK_SWITCH_WINDOW = 5 * 60  # Look at switches in 5-minute window
EXCESSIVE_SWITCHES_THRESHOLD = 8  # More than 8 switches in 5 min might be problematic

# --- ADHD-specific Notification Text ---
NOTIFICATION_TITLE_DISTRACTION = "Attention Redirect"  # Less judgmental than "Focus Check"
NOTIFICATION_TITLE_BREAK = "Micro-Break Time"
NOTIFICATION_TITLE_HYPERFOCUS = "Hyperfocus Check-In"
NOTIFICATION_TITLE_ACHIEVEMENT = "Achievement Unlocked!"
NOTIFICATION_TITLE_SWITCH = "Task Switching Check"

# --- Positive Reinforcement Messages (ADHD-friendly) ---
ACHIEVEMENT_MESSAGES = [
    "You've been productive for {time} today! That's awesome!",
    "Look at you go! {time} of productivity today!",
    "You're on fire! {time} of focused work today!",
    "Great job staying on task for {time}!",
    "Amazing focus power! {time} of productivity!",
    "You're crushing it with {time} of productive work!",
    "Productivity superhero! {time} of focused work today!"
]

BREAK_MESSAGES = [
    "You've earned a {duration}-minute break! Stand up, stretch, or grab some water.",
    "Time for a quick {duration}-minute breather! Your brain deserves it.",
    "Let's take {duration} minutes to recharge. Your focus has been great!",
    "Quick {duration}-minute break time! Move your body a bit to refresh your mind.",
    "{duration}-minute break opportunity - your brain works better with small resets!"
]

TASK_SWITCH_MESSAGES = [
    "Notice: You've switched tasks frequently in the last few minutes. Need to settle on one thing?",
    "Lots of task switching detected. Would setting a timer for one focused task help?",
    "Task hopping can drain your energy. Try picking one thing for the next 10 minutes.",
    "Quick check-in: Many switches detected. Is this intentional or feeling scattered?"
]

HYPERFOCUS_MESSAGES = [
    "You've been focused on {activity} for {time}. Just checking you're aware of the time!",
    "Still working on {activity}? You've been at it for {time}. Quick stretch break?",
    "Deep focus detected on {activity} ({time}). Remember to check in with yourself!",
    "You're in the zone with {activity}! {time} of continuous focus. All good?"
]

REDIRECT_MESSAGES = [
    "Noticed you've spent {time} on {activity}. Ready to redirect to something productive?",
    "Quick check-in: {time} on {activity}. What were you planning to work on today?",
    "{time} on {activity}. Would a 2-minute stretch break help reset your focus?",
    "You've used {time} on {activity}. Small reminder of your goals for today."
]

# --- Progress Visualization Settings ---
PROGRESS_BAR_LENGTH = 30  # Characters for progress bar
DAILY_GOAL_MINUTES = 120  # 2 hours of productive time is a reasonable daily goal for ADHD


# --- DB Connection Handler ---
def initialize_database():
    """Create SQLite database for activity tracking"""
    try:
        os.makedirs(DATA_DIR_PATH, exist_ok=True)
        db_path = os.path.join(DATA_DIR_PATH, 'activity_data.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        # Create tables for activities, categories, etc.
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS activities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            title TEXT,
            pid INTEGER,
            main_category TEXT,
            sub_category TEXT,
            start_time REAL,
            end_time REAL,
            duration REAL
        )
        ''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_totals (
            date TEXT PRIMARY KEY,
            productive_seconds REAL,
            non_productive_seconds REAL,
            neutral_seconds REAL,
            idle_seconds REAL
        )
        ''')
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS achievements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            achievement_type TEXT,
            achievement_value TEXT,
            description TEXT
        )
        ''')
        
        conn.commit()
        conn.close()
        print(f"{COLOR_GREEN}Database initialized at {db_path}{COLOR_RESET}")
        return True
    except Exception as e:
        print(f"{COLOR_RED}Error initializing database: {e}{COLOR_RESET}")
        return False


def save_activity_to_db(title, pid, main_category, sub_category, start_time, end_time, duration):
    """Save a single activity segment to the SQLite database"""
    try:
        db_path = os.path.join(DATA_DIR_PATH, 'activity_data.db')
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        today_date = date.today().isoformat()
        
        # Insert the activity
        cursor.execute('''
        INSERT INTO activities (date, title, pid, main_category, sub_category, start_time, end_time, duration)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (today_date, title, pid, main_category, sub_category, start_time, end_time, duration))
        
        # Update daily totals
        cursor.execute('''
        INSERT INTO daily_totals (date, productive_seconds, non_productive_seconds, neutral_seconds, idle_seconds)
        VALUES (?, ?, ?, ?, ?)
        ON CONFLICT(date) DO UPDATE SET
            productive_seconds = productive_seconds + CASE WHEN ? = 'Productive' THEN ? ELSE 0 END,
            non_productive_seconds = non_productive_seconds + CASE WHEN ? = 'Non-Productive' THEN ? ELSE 0 END,
            neutral_seconds = neutral_seconds + CASE WHEN ? = 'Neutral' THEN ? ELSE 0 END,
            idle_seconds = idle_seconds + CASE WHEN ? = 'Idle' THEN ? ELSE 0 END
        ''', (
            today_date, 0, 0, 0, 0,  # Initial values for INSERT
            main_category, duration,  # For Productive
            main_category, duration,  # For Non-Productive
            main_category, duration,  # For Neutral
            main_category, duration   # For Idle
        ))
        
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"{COLOR_RED}Error saving activity to database: {e}{COLOR_RESET}")
        return False

# --- 

# --- Logging Functions ---

def load_log_data():
    """Loads existing log data from the JSON file."""
    try:
        os.makedirs(DATA_DIR_PATH, exist_ok=True)
    except OSError as e:
        print(f"{COLOR_RED}Error creating directory {DATA_DIR_PATH}: {e}{COLOR_RESET}")
        return {}
    try:
        if os.path.exists(LOG_FILE_PATH):
            with open(LOG_FILE_PATH, 'r') as f:
                try:
                    data = json.load(f)
                    print(f"Loaded activity log from {LOG_FILE_PATH}")
                    return data
                except json.JSONDecodeError:
                    print(f"{COLOR_YELLOW}Warning: Log file {LOG_FILE_PATH} is corrupted or empty. Starting fresh.{COLOR_RESET}")
                    return {}
        else:
            print(f"Log file {LOG_FILE_PATH} not found. Starting fresh.")
            return {}
    except IOError as e:
        print(f"{COLOR_RED}Error loading log file {LOG_FILE_PATH}: {e}{COLOR_RESET}")
        return {}

def load_achievement_data():
    """Loads achievement data from file."""
    try:
        if os.path.exists(STREAK_FILE_PATH):
            with open(STREAK_FILE_PATH, 'r') as f:
                try:
                    data = json.load(f)
                    print(f"Loaded achievement data from {STREAK_FILE_PATH}")
                    return data
                except json.JSONDecodeError:
                    return achievement_data  # Return default
        else:
            return achievement_data  # Return default
    except IOError:
        return achievement_data  # Return default

def save_log_data(data):
    """Saves the current log data to the JSON file, calculating final category totals."""
    try:
        os.makedirs(DATA_DIR_PATH, exist_ok=True)

        # --- Calculate final category totals before saving ---
        today_date_str = date.today().isoformat()
        if today_date_str in data:
            category_totals = {
                "Productive": {"total_seconds": 0},
                "Non-Productive": {"total_seconds": 0},
                "Neutral": {"total_seconds": 0},
                "Idle": {"total_seconds": 0}
            }
            for main_cat, sub_cats in data[today_date_str].items():
                if main_cat == "CategoryTotals": continue
                if main_cat not in category_totals: continue

                for sub_cat, activities in sub_cats.items():
                    for activity_title, activity_data in activities.items():
                        category_totals[main_cat]["total_seconds"] += activity_data.get("total_seconds", 0)

            # Add formatted time to category totals
            for cat in category_totals:
                category_totals[cat]["formatted"] = format_duration(category_totals[cat]["total_seconds"])

            # ADHD Addition: Add productivity ratio and visualizations
            total_tracked = max(1, sum(cat["total_seconds"] for cat in category_totals.values()))
            productive_ratio = category_totals["Productive"]["total_seconds"] / total_tracked
            
            # Create visual progress bar (ADHD-friendly)
            progress_chars = math.floor(productive_ratio * PROGRESS_BAR_LENGTH)
            progress_bar = "▓" * progress_chars + "░" * (PROGRESS_BAR_LENGTH - progress_chars)
            
            # Add visualization data
            category_totals["Visualization"] = {
                "productive_ratio": productive_ratio,
                "progress_bar": progress_bar,
                "productive_minutes": math.floor(category_totals["Productive"]["total_seconds"] / 60),
                "daily_goal_minutes": DAILY_GOAL_MINUTES,
                "goal_progress": min(1.0, category_totals["Productive"]["total_seconds"] / (DAILY_GOAL_MINUTES * 60))
            }

            # Ensure CategoryTotals key exists and update it
            data[today_date_str].setdefault("CategoryTotals", {}).update(category_totals)
        
        with open(LOG_FILE_PATH, 'w') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"{COLOR_RED}Error saving log file {LOG_FILE_PATH}: {e}{COLOR_RESET}")
    except Exception as e:
        print(f"{COLOR_RED}Error calculating totals or saving log: {e}{COLOR_RESET}")

def save_achievement_data(data):
    """Saves achievement data to file."""
    try:
        os.makedirs(DATA_DIR_PATH, exist_ok=True)
        with open(STREAK_FILE_PATH, 'w') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        print(f"{COLOR_RED}Error saving achievement data: {e}{COLOR_RESET}")

# --- Helper Functions ---
def get_active_window_info():
    try:
        active_window = gw.getActiveWindow()
        if active_window and active_window.title:
            pid = None
            if sys.platform == 'win32' and hasattr(active_window, '_hWnd'):
                try:
                    pid = gw.getWindowPID(active_window._hWnd)
                except Exception:
                    pid = None
            return active_window.title.strip(), pid
        else:
            return None, None
    except gw.PyGetWindowException:
        return None, None
    except Exception as e:
        print(f"\r\033[K{COLOR_RED}Error getting active window: {e}{COLOR_RESET}", file=sys.stderr)
        return None, None

def get_enhanced_window_info():
    """Get more detailed window and process information"""
    active_window_title, pid = get_active_window_info()
    
    # Default values
    cpu_usage = 0
    is_actually_active = True
    memory_usage = 0
    
    if pid:
        try:
            # Get process details
            process = psutil.Process(pid)
            
            # Get CPU usage (per core)
            cpu_usage = process.cpu_percent(interval=0.1)
            
            # Get memory usage (MB)
            memory_info = process.memory_info()
            memory_usage = memory_info.rss / (1024 * 1024)
            
            # Additional activity checks could be added here
            # For example, checking if the window has keyboard focus
            
        except (psutil.NoSuchProcess, psutil.AccessDenied, Exception) as e:
            if isinstance(e, (psutil.NoSuchProcess, psutil.AccessDenied)):
                # Common errors, no need to print
                pass
            else:
                print(f"{COLOR_RED}Error getting process details: {e}{COLOR_RESET}")
            
    return active_window_title, pid, cpu_usage, memory_usage, is_actually_active

def categorize_activity(title):
    if not title:
        return "Idle", "No Active Window", None
    title_lower = title.lower()
    for sub_category, keywords in PRODUCTIVITY_CATEGORIES["Non-Productive"].items():
        for keyword in keywords:
            if keyword in title_lower:
                return "Non-Productive", sub_category, title
    for sub_category, keywords in PRODUCTIVITY_CATEGORIES["Productive"].items():
        for keyword in keywords:
            if keyword in title_lower:
                return "Productive", sub_category, title
    return "Neutral", "Uncategorized", title


def suggest_category_improvements():
    """Analyze time spent and suggest categorization improvements"""
    # Get all uncategorized applications with significant time
    uncategorized = []
    try:
        for date_str, date_data in log_data.items():
            if "Neutral" in date_data:
                for sub_cat, activities in date_data["Neutral"].items():
                    if sub_cat != "Uncategorized": continue
                    for title, data in activities.items():
                        if data["total_seconds"] > 300:  # More than 5 minutes
                            uncategorized.append({
                                "title": title,
                                "time": data["total_seconds"],
                                "suggestion": predict_category(title)
                            })
        return uncategorized
    except Exception as e:
        print(f"{COLOR_RED}Error analyzing categories: {e}{COLOR_RESET}")
        return []

def predict_category(title):
    """Use basic heuristics to suggest category for uncategorized apps"""
    if not title:
        return "Unknown"
        
    title_lower = title.lower()
    
    # Development-related keywords
    dev_keywords = ['code', 'develop', 'program', 'debug', 'git', 'compiler', 'python', 'java', 'javascript']
    creative_keywords = ['design', 'draw', 'paint', 'photo', 'edit', 'creative', 'photoshop', 'illustrator']
    productivity_keywords = ['document', 'spreadsheet', 'presentation', 'meeting', 'project', 'task', 'note']
    social_keywords = ['chat', 'message', 'social', 'facebook', 'twitter', 'instagram', 'tiktok']
    
    # Check keyword matches
    for keyword in dev_keywords:
        if keyword in title_lower:
            return "Programming & Dev"
    
    for keyword in creative_keywords:
        if keyword in title_lower:
            return "Creative & Design"
            
    for keyword in productivity_keywords:
        if keyword in title_lower:
            return "Office Suites & Docs"
            
    for keyword in social_keywords:
        if keyword in title_lower:
            return "Social Media"
            
    # Could be expanded with more sophisticated ML techniques
    return "Unknown"


def format_duration(seconds):
    if seconds < 0: seconds = 0
    seconds = math.floor(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    secs = seconds % 60
    
    # ADHD-friendly format - show only meaningful units
    if hours > 0:
        return f"{hours}h {minutes}m"
    elif minutes > 0:
        return f"{minutes}m {secs}s"
    else:
        return f"{secs}s"

def check_for_achievements(productive_seconds):
    """Check for and return achievement notifications."""
    achievements = []
    productive_minutes = productive_seconds / 60
    
    # Check daily goal achievement
    today_str = date.today().isoformat()
    if (productive_minutes >= DAILY_GOAL_MINUTES and 
            today_str not in achievement_data["daily_goals"]["completed_dates"]):
        achievement_data["daily_goals"]["completed_dates"].append(today_str)
        achievements.append(f"Daily Goal Reached! {DAILY_GOAL_MINUTES} minutes of productivity!")
        
        # Update streak
        yesterday = (date.today() - timedelta(days=1)).isoformat()
        if yesterday in achievement_data["daily_goals"]["completed_dates"]:
            achievement_data["streaks"]["current"] += 1
            if achievement_data["streaks"]["current"] > achievement_data["streaks"]["best"]:
                achievement_data["streaks"]["best"] = achievement_data["streaks"]["current"]
                
                # Milestone streaks
                if achievement_data["streaks"]["best"] in [3, 5, 7, 14, 30]:
                    achievements.append(f"New Streak Record: {achievement_data['streaks']['best']} days!")
        else:
            achievement_data["streaks"]["current"] = 1
    
    # Milestone achievements
    milestones = [30, 60, 90, 120, 180, 240]
    for milestone in milestones:
        milestone_key = f"productive_{milestone}min"
        if productive_minutes >= milestone and milestone_key not in achievement_data["achievements"]:
            achievement_data["achievements"].append(milestone_key)
            achievements.append(f"Milestone: {milestone} minutes of productivity!")
    
    # Save updated achievement data
    if achievements:
        save_achievement_data(achievement_data)
    
    return achievements

def create_visual_progress(productive_seconds, goal_seconds):
    """Create a visual progress indicator for ADHD users."""
    progress_ratio = min(1.0, productive_seconds / goal_seconds)
    progress_chars = math.floor(progress_ratio * PROGRESS_BAR_LENGTH)
    
    bar = "▓" * progress_chars + "░" * (PROGRESS_BAR_LENGTH - progress_chars)
    percent = math.floor(progress_ratio * 100)
    
    return f"{bar} {percent}% of daily goal"

# --- Task Switching Analysis ---
def analyze_task_switches(switch_times, window_seconds):
    """Analyze if task switching is excessive in the time window."""
    now = time.time()
    recent_switches = [t for t in switch_times if now - t <= window_seconds]
    return len(recent_switches) > EXCESSIVE_SWITCHES_THRESHOLD

# --- Main Tracking Logic (Async) ---
async def main():
    global log_data, achievement_data
    print(f"{COLOR_CYAN}{BOLD}Starting ADHD-Optimized Activity Tracker...{COLOR_RESET}")
    print("Press Ctrl+C to stop.")
    print("\n" + "="*110)

    log_data = load_log_data()
    achievement_data = load_achievement_data()
    notifier = DesktopNotifier()


    initialize_database()
    
    # Create a thread pool for CPU-intensive operations
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=2)

    # --- Runtime State ---
    current_title = None
    current_pid = None
    current_main_category = "Initializing"
    current_sub_category = "Please wait..."
    current_session_start_time = time.time()
    last_break_prompt_time = time.time()
    last_achievement_check_time = time.time()
    
    # ADHD tracking metrics
    task_switch_times = deque(maxlen=100)  # List of timestamps when tasks were switched
    daily_activity_totals_runtime = {}
    last_notification_times = {}  # Track last notification time by type and activity
    is_on_break = False
    break_start_time = 0
    
    # Achievement tracking
    today_productive_seconds = 0
    achievement_thresholds = [15*60, 30*60, 60*60, 90*60, 120*60]  # 15min, 30min, etc.
    achievements_triggered = set()

    # --- Initial Welcome Notification ---
    try:
        today_str = date.today().strftime("%A, %B %d")
        welcome_message = f"Activity tracker started for {today_str}!\n\nYour daily goal: {DAILY_GOAL_MINUTES} minutes of productive time."
        
        # Add streak info if applicable
        if achievement_data["streaks"]["current"] > 0:
            welcome_message += f"\nCurrent streak: {achievement_data['streaks']['current']} days"
        
        await notifier.send(title=f"{EMOJI_ACHIEVEMENT} ADHD Activity Tracker", message=welcome_message)
    except Exception as e:
        print(f"{COLOR_RED}Error sending initial notification: {e}{COLOR_RESET}")

    try:
        while True:
            # --- Get Current Activity ---

            loop = asyncio.get_event_loop()
            window_info = await loop.run_in_executor(executor, get_enhanced_window_info)
            active_title_raw, active_pid_raw, cpu_usage, memory_usage, is_active = window_info

            activity_identifier = active_title_raw if active_title_raw else "No Active Window"
            log_key_identifier = activity_identifier
            if active_pid_raw:
                log_key_identifier = f"{activity_identifier} (PID: {active_pid_raw})"

            # Detect the activity state for smarter tracking
            # activity_state = detect_activity_state(
            #     activity_identifier, 
            #     current_main_category, 
            #     current_sub_category, 
            #     current_segment_duration if 'current_segment_duration' in locals() else 0, 
            #     cpu_usage
            # )

            # --- Activity Change Detection & LOGGING ---
            # Log when the TITLE changes
            if activity_identifier != current_title:
                # Record task switch timestamp for ADHD switch analysis
                task_switch_times.append(time.time())
                
                # 1. Finalize the PREVIOUS activity segment
                if current_title and current_main_category != "Initializing":
                    end_time = time.time()
                    segment_duration = end_time - current_session_start_time
                    segment_duration_rounded = round(segment_duration)

                    if segment_duration_rounded > 0:
                        # Add segment duration to runtime total for display
                        daily_activity_totals_runtime[current_title] = daily_activity_totals_runtime.get(current_title, 0) + segment_duration

                        # --- Update Persistent Log Data ---
                        today_date_str = date.today().isoformat()
                        date_log = log_data.setdefault(today_date_str, {})
                        cat_totals = date_log.setdefault("CategoryTotals", {
                            "Productive": {"total_seconds": 0},
                            "Non-Productive": {"total_seconds": 0},
                            "Neutral": {"total_seconds": 0},
                            "Idle": {"total_seconds": 0}
                        })

                        previous_log_key = current_title
                        if current_pid:
                            previous_log_key = f"{current_title} (PID: {current_pid})"

                        activity_log_entry = date_log.setdefault(current_main_category, {})\
                                                    .setdefault(current_sub_category, {})\
                                                    .setdefault(previous_log_key, {
                                                        "total_seconds": 0,
                                                        "times_opened": 0,
                                                        "total_focus_alerts": 0,
                                                        "total_break_alerts": 0,
                                                        "pids_seen": []
                                                    })

                        # Aggregate data into the activity entry
                        activity_log_entry["total_seconds"] += segment_duration_rounded
                        activity_log_entry["formatted_total_time"] = format_duration(activity_log_entry["total_seconds"])
                        if current_pid and current_pid not in activity_log_entry["pids_seen"]:
                            activity_log_entry["pids_seen"].append(current_pid)

                        # Update Category Totals
                        if current_main_category in cat_totals:
                            cat_totals[current_main_category]["total_seconds"] += segment_duration_rounded
                        else:
                            cat_totals[current_main_category] = {"total_seconds": segment_duration_rounded}
                        
                        # ADHD Feature: Update today's productive time for achievements/streaks
                        if current_main_category == "Productive":
                            today_productive_seconds += segment_duration_rounded

                # 2. Setup the NEW activity segment
                current_title = activity_identifier
                current_pid = active_pid_raw
                main_cat, sub_cat, _ = categorize_activity(current_title)
                current_main_category = main_cat
                current_sub_category = sub_cat
                current_session_start_time = time.time()
                last_break_prompt_time = time.time()

                # --- Increment 'times_opened' in log for the NEW activity ---
                if current_title and current_main_category != "Initializing" and current_main_category != "Idle":
                    today_date_str = date.today().isoformat()
                    date_log = log_data.setdefault(today_date_str, {})
                    date_log.setdefault("CategoryTotals", {
                            "Productive": {"total_seconds": 0}, "Non-Productive": {"total_seconds": 0},
                            "Neutral": {"total_seconds": 0}, "Idle": {"total_seconds": 0}
                        })

                    activity_log_entry = date_log.setdefault(current_main_category, {})\
                                                .setdefault(current_sub_category, {})\
                                                .setdefault(log_key_identifier, {
                                                    "total_seconds": 0,
                                                    "times_opened": 0,
                                                    "total_focus_alerts": 0,
                                                    "total_break_alerts": 0,
                                                    "pids_seen": []
                                                })
                    activity_log_entry["times_opened"] += 1
                    if current_pid and current_pid not in activity_log_entry["pids_seen"]:
                        activity_log_entry["pids_seen"].append(current_pid)

                # ADHD Feature: Task Switching Analysis
                if len(task_switch_times) > 2:  # Need at least a few switches to analyze
                    excessive_switching = analyze_task_switches(task_switch_times, TASK_SWITCH_WINDOW)
                    if excessive_switching:
                        switch_notification_key = "task_switching"
                        if (switch_notification_key not in last_notification_times or 
                                time.time() - last_notification_times[switch_notification_key] > TASK_SWITCH_WINDOW):
                            
                            switch_message = random.choice(TASK_SWITCH_MESSAGES)
                            try:
                                print(f"\r\033[K{COLOR_YELLOW}{EMOJI_SWITCH} Excessive task switching detected.{COLOR_RESET}")
                                await notifier.send(title=f"{EMOJI_SWITCH} {NOTIFICATION_TITLE_SWITCH}", 
                                                   message=switch_message)
                                last_notification_times[switch_notification_key] = time.time()
                            except Exception as e:
                                print(f"\r\033[K{COLOR_RED}Error sending task switching notification: {e}{COLOR_RESET}")

                # Clean old task switch times
                now = time.time()
                task_switch_times = [t for t in task_switch_times if now - t <= TASK_SWITCH_WINDOW*2]

            # --- Calculate Current Times ---
            current_segment_duration = time.time() - current_session_start_time
            total_time_today_for_display = daily_activity_totals_runtime.get(current_title, 0) + current_segment_duration
            formatted_total_time_display = format_duration(total_time_today_for_display)
            formatted_segment_time = format_duration(current_segment_duration)

            # --- Get today's productive seconds for achievements ---
            today_date_str = date.today().isoformat()
            if today_date_str in log_data and "CategoryTotals" in log_data[today_date_str]:
                cat_totals = log_data[today_date_str]["CategoryTotals"]
                if "Productive" in cat_totals:
                    today_productive_seconds = cat_totals["Productive"].get("total_seconds", 0)
                    # Add current segment if we're in a productive app
                    if current_main_category == "Productive":
                        today_productive_seconds += current_segment_duration

            # --- Determine Color & Prepare Status Line (ADHD Enhanced) ---
            if current_main_category == "Productive": 
                color = COLOR_GREEN
                emoji = EMOJI_PRODUCTIVE
            elif current_main_category == "Non-Productive": 
                color = COLOR_RED
                emoji = EMOJI_DISTRACTED
            else: 
                color = COLOR_YELLOW
                emoji = ""
                
            # Create ADHD-friendly progress visualization for productive time
            goal_seconds = DAILY_GOAL_MINUTES * 60
            progress_ratio = min(1.0, today_productive_seconds / goal_seconds)
            progress_chars = math.floor(progress_ratio * PROGRESS_BAR_LENGTH)
            progress_bar = "▓" * progress_chars + "░" * (PROGRESS_BAR_LENGTH - progress_chars)
            progress_percent = int(progress_ratio * 100)
            
            # Create a more visually engaging status line
            max_title_len = 30  # Shorter for cleaner display
            display_title = current_title if current_title != "No Active Window" else "N/A"
            if len(display_title) > max_title_len: 
                display_title = display_title[:max_title_len-3] + "..."
                
            # ADHD-friendly formatting with clear visual separators
            status_line = (
                f"{color}{emoji}{current_main_category:<12}{COLOR_RESET} | "
                f"{color}{current_sub_category:<18}{COLOR_RESET} | "
                f"App: {color}{display_title:<{max_title_len}}{COLOR_RESET} | "
                f"Time: {color}{formatted_segment_time:>8}{COLOR_RESET}"
            )
            
            # Add goal progress on a second line (ADHD visual reward)
            goal_line = (
                f"Daily Goal: {COLOR_CYAN}[{progress_bar}] {progress_percent}%{COLOR_RESET} "
                f"({format_duration(today_productive_seconds)}/{DAILY_GOAL_MINUTES}m)"
            )
            
            # Clear line and print status
            sys.stdout.write(f"\r\033[K{status_line}\n\r\033[K{goal_line}")
            sys.stdout.flush()
            # Move cursor back up one line for next update
            sys.stdout.write("\033[1A")
            sys.stdout.flush()

            # --- ADHD-specific Achievement Notifications ---
            # Check achievements less frequently to reduce processing overhead
            if time.time() - last_achievement_check_time > 60:  # Check once per minute
                achievements = check_for_achievements(today_productive_seconds)
                
                for achievement in achievements:
                    try:
                        achievement_message = f"{achievement}\n\nKeep up the great work! 🎉"
                        if "Streak" in achievement:
                            achievement_message += f"\n\nCurrent streak: {achievement_data['streaks']['current']} days"
                            
                        print(f"\r\033[K{COLOR_CYAN}{EMOJI_ACHIEVEMENT} {achievement}{COLOR_RESET}")
                        await notifier.send(
                            title=f"{EMOJI_ACHIEVEMENT} {NOTIFICATION_TITLE_ACHIEVEMENT}", 
                            message=achievement_message
                        )
                    except Exception as e:
                        print(f"\r\033[K{COLOR_RED}Error sending achievement notification: {e}{COLOR_RESET}")
                        
                # For ADHD: Occasional positive reinforcement even without formal achievements
                productive_minutes = math.floor(today_productive_seconds / 60)
                for threshold in achievement_thresholds:
                    threshold_minutes = threshold // 60
                    threshold_key = f"motivation_{threshold_minutes}"
                    
                    if (today_productive_seconds >= threshold and 
                            threshold_key not in achievements_triggered and
                            time.time() - last_achievement_check_time > 60*5):  # At least 5 min between encouragements
                            
                        achievements_triggered.add(threshold_key)
                        try:
                            encouragement = random.choice(ACHIEVEMENT_MESSAGES).format(
                                time=format_duration(today_productive_seconds)
                            )
                            
                            print(f"\r\033[K{COLOR_CYAN}Encouragement: {encouragement}{COLOR_RESET}")
                            await notifier.send(
                                title=f"{EMOJI_PRODUCTIVE} Productivity Update", 
                                message=encouragement
                            )
                        except Exception as e:
                            print(f"\r\033[K{COLOR_RED}Error sending encouragement: {e}{COLOR_RESET}")
                            
                last_achievement_check_time = time.time()

            # --- ADHD-optimized Notification Logic ---
            
            # 1. Non-Productive Activity Alert (Gentle redirection)
            if current_main_category == "Non-Productive":
                # Categorized as distraction, but use gentler approach for ADHD
                if (total_time_today_for_display > DISTRACTION_ALERT_SECONDS and 
                        (current_title not in last_notification_times or 
                         time.time() - last_notification_times.get(current_title, 0) > DISTRACTION_ALERT_SECONDS)):
                    
                    # Gentle redirection message
                    redirect_message = random.choice(REDIRECT_MESSAGES).format(
                        time=format_duration(total_time_today_for_display),
                        activity=current_sub_category
                    )
                    
                    try:
                        print(f"\r\033[K{COLOR_YELLOW}{EMOJI_DISTRACTED} Sending redirection reminder for {current_sub_category}{COLOR_RESET}")
                        await notifier.send(
                            title=f"{EMOJI_DISTRACTED} {NOTIFICATION_TITLE_DISTRACTION}", 
                            message=redirect_message
                        )
                        last_notification_times[current_title] = time.time()
                    except Exception as e:
                        print(f"\r\033[K{COLOR_RED}Error sending redirection notification: {e}{COLOR_RESET}")

            # 2. Micro-Break Reminder for Productive Work
            if (current_main_category == "Productive" and 
                    current_segment_duration > MICRO_BREAK_SUGGESTION and
                    time.time() - last_break_prompt_time > MICRO_BREAK_SUGGESTION):
                
                # For ADHD: Suggest break *during* productive work to prevent burnout
                break_message = random.choice(BREAK_MESSAGES).format(
                    duration=BREAK_DURATION_SECONDS // 60
                )
                
                try:
                    print(f"\r\033[K{COLOR_BLUE}{EMOJI_BREAK_TIME} Suggesting micro-break after {formatted_segment_time} of {current_sub_category}{COLOR_RESET}")
                    await notifier.send(
                        title=f"{EMOJI_BREAK_TIME} {NOTIFICATION_TITLE_BREAK}", 
                        message=break_message
                    )
                    last_break_prompt_time = time.time()
                except Exception as e:
                    print(f"\r\033[K{COLOR_RED}Error sending break notification: {e}{COLOR_RESET}")

            # 3. Hyperfocus Check (for both productive and non-productive activities)
            if current_segment_duration > HYPERFOCUS_DETECTION_SECONDS:
                hyperfocus_key = f"hyperfocus_{current_title}"
                if (hyperfocus_key not in last_notification_times or 
                        time.time() - last_notification_times.get(hyperfocus_key, 0) > HYPERFOCUS_DETECTION_SECONDS):
                    
                    # Different tone based on if it's productive hyperfocus
                    if current_main_category == "Productive":
                        hyperfocus_message = random.choice(HYPERFOCUS_MESSAGES).format(
                            activity=current_sub_category,
                            time=formatted_segment_time
                        )
                    else:
                        # For non-productive hyperfocus, be more direct about redirection
                        hyperfocus_message = f"You've been on {current_sub_category} for {formatted_segment_time}. This might be hyperfocus on a non-productive activity. Time to redirect?"
                    
                    try:
                        alert_color = COLOR_GREEN if current_main_category == "Productive" else COLOR_RED
                        print(f"\r\033[K{alert_color}{EMOJI_HYPERFOCUS} Hyperfocus detected on {current_sub_category}{COLOR_RESET}")
                        await notifier.send(
                            title=f"{EMOJI_HYPERFOCUS} {NOTIFICATION_TITLE_HYPERFOCUS}", 
                            message=hyperfocus_message
                        )
                        last_notification_times[hyperfocus_key] = time.time()
                    except Exception as e:
                        print(f"\r\033[K{COLOR_RED}Error sending hyperfocus notification: {e}{COLOR_RESET}")

            # --- Wait ---
            await asyncio.sleep(CHECK_INTERVAL_SECONDS)

    except KeyboardInterrupt:
        print(f"\r\033[K\n{COLOR_CYAN}Stopping ADHD Activity Tracker...{COLOR_RESET}")
    except asyncio.CancelledError:
        print(f"\r\033[K\n{COLOR_YELLOW}Activity tracker task cancelled.{COLOR_RESET}")
    except Exception as e:
        print(f"\r\033[K\n{COLOR_RED}An unexpected error occurred: {e}{COLOR_RESET}", file=sys.stderr)
        traceback.print_exc()
    finally:
        # --- Save Log Data on Exit ---
        print(f"{COLOR_YELLOW}Saving final activity log...{COLOR_RESET}")
        # Log the very last activity segment before exiting
        today_date_str = date.today().isoformat()

        if current_title and current_main_category != "Initializing":
            end_time = time.time()
            segment_duration = end_time - current_session_start_time
            segment_duration_rounded = round(segment_duration)
    

            if segment_duration_rounded > 0:
                # --- Update Persistent Log Data for final segment ---
                
                date_log = log_data.setdefault(today_date_str, {})
                cat_totals = date_log.setdefault("CategoryTotals", {
                    "Productive": {"total_seconds": 0}, "Non-Productive": {"total_seconds": 0},
                    "Neutral": {"total_seconds": 0}, "Idle": {"total_seconds": 0}
                })

                final_log_key = f"{current_title}"
                if current_pid:
                    final_log_key = f"{current_title} (PID: {current_pid})"

                activity_log_entry = date_log.setdefault(current_main_category, {})\
                                            .setdefault(current_sub_category, {})\
                                            .setdefault(final_log_key, {
                                                "total_seconds": 0, "times_opened": 0,
                                                "total_focus_alerts": 0, "total_break_alerts": 0,
                                                "pids_seen": []
                                            })

                activity_log_entry["total_seconds"] += segment_duration_rounded
                activity_log_entry["formatted_total_time"] = format_duration(activity_log_entry["total_seconds"])
                activity_log_entry["last_seen_iso"] = datetime.fromtimestamp(end_time).isoformat()
                if current_pid and current_pid not in activity_log_entry["pids_seen"]:
                    activity_log_entry["pids_seen"].append(current_pid)

                # Update Category Totals
                if current_main_category in cat_totals:
                    cat_totals[current_main_category]["total_seconds"] += segment_duration_rounded
                else:
                    cat_totals[current_main_category] = {"total_seconds": segment_duration_rounded}

                save_activity_to_db(
                    current_title, 
                    current_pid, 
                    current_main_category, 
                    current_sub_category,
                    current_session_start_time,  # Start time
                    time.time(),                 # End time
                    segment_duration_rounded     # Duration
                )

        # --- Generate Exit Summary for ADHD Users ---
        if today_date_str in log_data and "CategoryTotals" in log_data[today_date_str]:
            cat_totals = log_data[today_date_str]["CategoryTotals"]
            
            # Calculate today's stats
            productive_seconds = cat_totals.get("Productive", {}).get("total_seconds", 0)
            non_productive_seconds = cat_totals.get("Non-Productive", {}).get("total_seconds", 0)
            neutral_seconds = cat_totals.get("Neutral", {}).get("total_seconds", 0)
            
            total_tracked = productive_seconds + non_productive_seconds + neutral_seconds
            if total_tracked > 0:
                productive_ratio = productive_seconds / total_tracked
                
                # For ADHD: Create visual summary
                print("\n" + "="*50)
                print(f"{COLOR_CYAN}{BOLD}TODAY'S ACTIVITY SUMMARY{COLOR_RESET}")
                print("="*50)
                
                # Productive time
                print(f"{COLOR_GREEN}Productive Time:    {format_duration(productive_seconds)}{COLOR_RESET}")
                print(f"{COLOR_RED}Non-Productive:     {format_duration(non_productive_seconds)}{COLOR_RESET}")
                print(f"{COLOR_YELLOW}Neutral/Other:      {format_duration(neutral_seconds)}{COLOR_RESET}")
                print("-"*50)
                
                # Goal progress 
                goal_seconds = DAILY_GOAL_MINUTES * 60
                progress_ratio = min(1.0, productive_seconds / goal_seconds)
                progress_chars = math.floor(progress_ratio * PROGRESS_BAR_LENGTH)
                progress_bar = "▓" * progress_chars + "░" * (PROGRESS_BAR_LENGTH - progress_chars)
                progress_percent = int(progress_ratio * 100)
                
                print(f"Daily Goal Progress: {COLOR_CYAN}[{progress_bar}] {progress_percent}%{COLOR_RESET}")
                print(f"                     {COLOR_CYAN}{format_duration(productive_seconds)}/{DAILY_GOAL_MINUTES}m{COLOR_RESET}")
                
                # Streak info
                if achievement_data["streaks"]["current"] > 0:
                    print(f"\n{COLOR_CYAN}Current streak: {achievement_data['streaks']['current']} days{COLOR_RESET}")
                    print(f"{COLOR_CYAN}Best streak: {achievement_data['streaks']['best']} days{COLOR_RESET}")
                
                # Final encouragement - always positive for ADHD users
                print("\n" + "-"*50)
                if productive_seconds > 30*60:  # If they did at least 30 minutes productive work
                    print(f"{COLOR_GREEN}{BOLD}Great job today! You made progress!{COLOR_RESET}")
                else:
                    print(f"{COLOR_CYAN}{BOLD}Tomorrow is a new opportunity!{COLOR_RESET}")
                print("="*50)
                
                # Try to send exit summary notification
                try:
                    summary_message = (f"Today's productivity: {format_duration(productive_seconds)}\n"
                                      f"Daily goal progress: {progress_percent}%\n\n")
                    
                    if productive_seconds > goal_seconds:
                        summary_message += "Goal achieved! 🎉"
                    elif productive_seconds > goal_seconds * 0.7:
                        summary_message += "Solid progress toward your goal!"
                    else:
                        summary_message += "More opportunities tomorrow!"
                        
                    await notifier.send(
                        title="Activity Tracker Summary", 
                        message=summary_message
                    )
                except Exception:
                    # Don't worry if exit notification fails
                    pass
        
        # Save both data files
        save_log_data(log_data) # Comment 
        save_achievement_data(achievement_data) # Comment
        # Before ending main(), ensure final save happens:
        await loop.run_in_executor(executor, save_log_data, log_data)
        executor.shutdown()  # Clean shutdown of the executor
        print(f"{COLOR_GREEN}Tracker stopped. Data saved successfully.{COLOR_RESET}") # Comment

        # Use a periodic save approach instead of saving on every change
        last_save_time = time.time()
        if time.time() - last_save_time > 60:  # Save every minute
            await loop.run_in_executor(executor, save_log_data, log_data.copy())
            last_save_time = time.time()

# --- Add Daily Report Function ---
async def generate_daily_report():
    """Generate a comprehensive daily report."""
    # Implementation for detailed reports could go here
    # For ADHD users, visual reports with charts would be ideal
    pass

if __name__ == "__main__":
    os.system('cls' if platform.system() == 'Windows' else 'clear')  # Clear screen for clean start
    print(f"{COLOR_CYAN}{BOLD}╔══════════════════════════════════════════════╗{COLOR_RESET}")
    print(f"{COLOR_CYAN}{BOLD}║   ADHD-OPTIMIZED ACTIVITY TRACKER v1.0       ║{COLOR_RESET}")
    print(f"{COLOR_CYAN}{BOLD}╚══════════════════════════════════════════════╝{COLOR_RESET}")
    
    # Opening message
    print(f"\n{COLOR_GREEN}This version includes:{COLOR_RESET}")
    print(f"• Frequent gentle reminders instead of harsh alerts")
    print(f"• Visual progress tracking with immediate feedback")
    print(f"• Positive reinforcement for productivity")
    print(f"• Hyperfocus detection to help maintain awareness")
    print(f"• Task-switching analysis to reduce context switching")
    print(f"• Achievement system to build momentum")
    
    # Pre-run checks
    print(f"\n{COLOR_YELLOW}--- Pre-run Checks & Config ---{COLOR_RESET}")
    print("1. Dependencies: Ensure 'pygetwindow', 'desktop-notifier', 'psutil' installed.")
    print("2. macOS Permissions: Terminal/IDE might need 'Accessibility' permissions.")
    print("3. Linux Permissions: Ensure a notification daemon is running.")
    print("4. ** Review & Customize PRODUCTIVITY_CATEGORIES in the script! **")
    
    # ADHD-specific settings
    print(f"\n{COLOR_YELLOW}--- ADHD-Optimized Settings ---{COLOR_RESET}")
    print(f"• Micro-break suggestion: Every {MICRO_BREAK_SUGGESTION // 60} minutes")
    print(f"• Distraction alert: After {DISTRACTION_ALERT_SECONDS // 60} minutes")
    print(f"• Hyperfocus check: After {HYPERFOCUS_DETECTION_SECONDS // 60} minutes")
    print(f"• Daily productivity goal: {DAILY_GOAL_MINUTES} minutes")
    print(f"• Data directory: {DATA_DIR_PATH}")
    
    print("\n" + "="*50)
    print(f"{COLOR_CYAN}Starting in 3 seconds... Press Ctrl+C at any time to exit.{COLOR_RESET}")
    print("="*50)
    
    try:
        # Small delay to read instructions
        time.sleep(3)
        os.makedirs(DATA_DIR_PATH, exist_ok=True)
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nExiting due to user interruption (Ctrl+C).")