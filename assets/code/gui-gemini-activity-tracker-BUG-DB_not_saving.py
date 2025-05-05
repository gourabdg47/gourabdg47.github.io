import tkinter as tk
from tkinter import ttk, messagebox
import pygetwindow as gw
import time
import sys
import psutil
from desktop_notifier import DesktopNotifier
import math
import threading
import tracemalloc # Keep for potential debugging, though not actively used now
import json
import os
import random
from datetime import datetime, date, timedelta
import platform
from collections import deque
import queue # For thread-safe communication
import traceback
import sqlite3

# --- Constants ---

# ** Data Storage **
DATA_DIR_NAME = "adhd_activity_tracker_data"
DB_FILE_NAME = 'activity_data.db'
CURRENT_WORKING_DIR = os.getcwd()
DATA_DIR_PATH = os.path.join(CURRENT_WORKING_DIR, DATA_DIR_NAME)
DB_PATH = os.path.join(DATA_DIR_PATH, DB_FILE_NAME)

# ** GUI Colors & Emojis **
COLOR_PRODUCTIVE = "#2E7D32" # Dark Green
COLOR_NON_PRODUCTIVE = "#C62828" # Dark Red
COLOR_NEUTRAL = "#FF8F00" # Darker Amber/Orange for better contrast
COLOR_IDLE = "#546E7A" # Blue Grey
COLOR_BACKGROUND = "#F5F5F5" # Lighter Grey
COLOR_TEXT = "#212121" # Dark Grey / Black
COLOR_ACCENT = "#1E88E5" # Brighter Blue
COLOR_PROGRESS_BAR = "#43A047" # Slightly brighter Green
COLOR_PROGRESS_BG = "#E0E0E0" # Background for progress bar trough
COLOR_STATUS_BG = "#FFFFFF" # White background for status text
COLOR_SEPARATOR = "#BDBDBD" # Grey for separators

EMOJI_PRODUCTIVE = "⚡"
EMOJI_BREAK_TIME = "🌱"
EMOJI_DISTRACTED = "🦋"
EMOJI_HYPERFOCUS = "🔍"
EMOJI_ACHIEVEMENT = "🎯"
EMOJI_SWITCH = "↻"
EMOJI_NEUTRAL = "⚫"
EMOJI_IDLE = "⚪"
EMOJI_STREAK = "🔥" # Changed streak emoji

# ** Configuration (Keywords - Consider externalizing to JSON/config file later) **
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
        "Social Media": ['facebook', 'fb.com', 'instagram', 'twitter', 'x.com', 'tiktok', 'reddit', 'pinterest', 'snapchat', 'tumblr', 'linkedin'], # LinkedIn can be productive, but often distracting
        "Video Streaming": ['youtube', 'netflix', 'hulu', 'amazon prime video', 'prime video', 'disney+', 'disneyplus', 'hbo max', 'max', 'peacock', 'apple tv', 'twitch', 'vimeo'],
        "Music Streaming (Active Focus)": ['spotify', 'apple music', 'youtube music', 'pandora', 'soundcloud', 'tidal'], # Note: Can be productive for some, categorized as non-prod by default
        "Messaging (Casual/Social)": ['whatsapp', 'web.whatsapp.com', 'facebook messenger', 'messenger.com', 'discord', 'telegram', 'signal', 'wechat', 'kik', 'skype'],
        "Shopping": ['amazon', 'ebay', 'etsy', 'walmart', 'target', 'best buy', 'aliexpress', 'shein', 'temu', 'newegg'],
        "News & General Browse": [ 'cnn', 'bbc', 'fox news', 'nytimes', 'washington post', 'guardian', 'npr', 'reuters', 'associated press', 'wsj', 'google news', 'apple news', 'yahoo', 'buzzfeed', 'huffpost', 'the onion', 'cracked', 'vice', 'daily mail', 'reddit', 'imgur', '9gag', 'boredpanda'], # Removed Wikipedia, moved to Learning
        "Gaming": ['steam', 'epic games', 'gog galaxy', 'battle.net', 'origin', 'ea app', 'ubisoft connect', 'minecraft', 'fortnite', 'valorant', 'league of legends', 'dota', 'csgo', 'overwatch', 'apex legends', 'roblox', 'genshin impact', 'miniclip', 'addicting games', 'pogo', 'kongregate', 'twitch'],
        "Miscellaneous Distractions": ['imdb', 'rottentomatoes', 'tmz', 'sports', 'espn', 'bleacher report', 'nfl', 'nba', 'mlb', 'coinbase', 'binance', 'coinmarketcap', 'coingecko', 'dating', 'tinder', 'bumble', 'hinge', 'match.com', 'okcupid', 'personal email']
    }
}

# ** ADHD-Optimized Time Settings **
CHECK_INTERVAL_SECONDS = 2
DISTRACTION_ALERT_SECONDS = 3 * 60
MICRO_BREAK_SUGGESTION = 25 * 60
BREAK_DURATION_SECONDS = 5 * 60
HYPERFOCUS_DETECTION_SECONDS = 45 * 60
TASK_SWITCH_WINDOW = 5 * 60
EXCESSIVE_SWITCHES_THRESHOLD = 8
SAVE_INTERVAL_SECONDS = 60 # How often to save streaks (activity saved per segment)

# ** Notification Titles & Messages **
NOTIFICATION_TITLE_DISTRACTION = "Attention Redirect"
NOTIFICATION_TITLE_BREAK = "Micro-Break Time"
NOTIFICATION_TITLE_HYPERFOCUS = "Hyperfocus Check-In"
NOTIFICATION_TITLE_ACHIEVEMENT = "Achievement Unlocked!"
NOTIFICATION_TITLE_SWITCH = "Task Switching Check"

# Using f-strings directly in messages for simplicity
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

# ** Progress Visualization Settings **
DAILY_GOAL_MINUTES = 120 # Default daily goal

# --- Global Data (Loaded at start) ---
achievement_data = {
    "streaks": {"current": 0, "best": 0},
    "daily_goals": {"productive_minutes": DAILY_GOAL_MINUTES, "completed_dates": []}
}
daily_totals_runtime = {} # Runtime calculation: {date_str: {'Productive': secs, 'Non-Productive': secs, ...}}

# --- Helper Functions ---

def _add_column_if_not_exists(cursor, table_name, column_name, column_type):
    """
    Helper function to add a column to a table if it doesn't exist.
    Returns True if column was added, False otherwise.
    """
    try:
        cursor.execute(f"PRAGMA table_info({table_name})")
        columns = [info[1] for info in cursor.fetchall()]
        if column_name not in columns:
            cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}")
            print(f"Migration: Added column '{column_name}' to table '{table_name}'.")
            return True # Indicate column was added
        return False # Indicate column already existed
    except sqlite3.Error as e: # Catch specific SQLite errors
        print(f"Warning: Could not check/add column '{column_name}' to '{table_name}'. Error: {e}")
        return False # Indicate potential issue

def initialize_data_dir_and_db():
    """
    Creates the data directory and initializes/updates the SQLite DB schema robustly.
    Ensures commits happen after schema changes.
    """
    conn = None
    try:
        os.makedirs(DATA_DIR_PATH, exist_ok=True)
        conn = sqlite3.connect(DB_PATH, timeout=10)
        cursor = conn.cursor()
        print("Initializing/Checking Database Schema...")

        # --- Create Tables IF NOT EXISTS ---
        # Use the latest correct schema definitions here
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS activities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp REAL NOT NULL,
            date TEXT NOT NULL,
            title TEXT,
            pid INTEGER,
            main_category TEXT,
            sub_category TEXT,
            duration REAL NOT NULL
        )''')
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS daily_totals (
            date TEXT PRIMARY KEY,
            productive_seconds REAL DEFAULT 0,
            non_productive_seconds REAL DEFAULT 0,
            neutral_seconds REAL DEFAULT 0,
            idle_seconds REAL DEFAULT 0,
            goal_minutes INTEGER DEFAULT ?,
            goal_achieved INTEGER DEFAULT 0
        )''', (DAILY_GOAL_MINUTES,))
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS achievements (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp REAL NOT NULL,
            date TEXT NOT NULL,
            achievement_key TEXT NOT NULL UNIQUE,
            description TEXT
        )''')
        cursor.execute("CREATE INDEX IF NOT EXISTS idx_achievement_key ON achievements (achievement_key)")
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS streaks (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            current_streak INTEGER DEFAULT 0,
            best_streak INTEGER DEFAULT 0,
            last_streak_date TEXT
        )''')
        cursor.execute("INSERT OR IGNORE INTO streaks (id, current_streak, best_streak) VALUES (1, 0, 0)")

        # Commit table creations before attempting migrations
        conn.commit()
        print("Schema: Base tables ensured.")

        # --- Schema Migration: Add missing columns safely ---
        # Use the helper function and commit after successful additions
        print("Schema: Checking for necessary column migrations...")
        migration_done = False
        if _add_column_if_not_exists(cursor, "daily_totals", "goal_minutes", "INTEGER"):
             migration_done = True
             # Set default value for existing rows if column was just added
             cursor.execute("UPDATE daily_totals SET goal_minutes = ? WHERE goal_minutes IS NULL", (DAILY_GOAL_MINUTES,))
        if _add_column_if_not_exists(cursor, "daily_totals", "goal_achieved", "INTEGER"):
             migration_done = True
             # Set default value for existing rows
             cursor.execute("UPDATE daily_totals SET goal_achieved = 0 WHERE goal_achieved IS NULL")
        if _add_column_if_not_exists(cursor, "achievements", "achievement_key", "TEXT"): # Add without UNIQUE here for migration
             migration_done = True
             # If adding achievement_key, we might need to handle potential duplicates
             # in existing data if the script ran before with errors.
             # For simplicity now, we rely on INSERT OR IGNORE later.
             # A more complex migration would identify and handle/remove duplicates here.
             print("Warning: Added 'achievement_key'. Existing data might need manual check if errors occurred previously.")
        if _add_column_if_not_exists(cursor, "achievements", "timestamp", "REAL"): migration_done = True
        if _add_column_if_not_exists(cursor, "achievements", "date", "TEXT"): migration_done = True
        # Add checks for activities table columns if needed (though they were likely okay)
        if _add_column_if_not_exists(cursor, "activities", "timestamp", "REAL"): migration_done = True
        if _add_column_if_not_exists(cursor, "activities", "date", "TEXT"): migration_done = True


        # Commit any migrations that occurred
        if migration_done:
            conn.commit()
            print("Schema: Migrations committed.")
        else:
            print("Schema: No column migrations were needed.")

        # --- Final Schema Verification (Optional but helpful for debugging) ---
        print("Schema: Verifying final structure...")
        for table in ["activities", "daily_totals", "achievements", "streaks"]:
            cursor.execute(f"PRAGMA table_info({table})")
            columns = [info[1] for info in cursor.fetchall()]
            print(f"  Table '{table}' columns: {columns}")


        conn.close()
        print(f"Database initialization/update complete: {DB_PATH}")
        return True
    except Exception as e:
        print(f"CRITICAL Error initializing/updating database: {e}")
        traceback.print_exc()
        if conn:
            try: conn.close()
            except: pass
        return False

def save_activity_segment_db(timestamp, date_str, title, pid, main_cat, sub_cat, duration):
    """Saves a single activity segment and updates daily totals in the DB."""
    if duration <= 0: return
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH, timeout=5.0)
        cursor = conn.cursor()

        # Insert activity segment
        cursor.execute('''
        INSERT INTO activities (timestamp, date, title, pid, main_category, sub_category, duration)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (timestamp, date_str, title, pid, main_cat, sub_cat, duration))

        # Update daily totals
        cursor.execute('''
        UPDATE daily_totals SET
            productive_seconds = CASE WHEN ? = 'Productive' THEN productive_seconds + ? ELSE productive_seconds END,
            non_productive_seconds = CASE WHEN ? = 'Non-Productive' THEN non_productive_seconds + ? ELSE non_productive_seconds END,
            neutral_seconds = CASE WHEN ? = 'Neutral' THEN neutral_seconds + ? ELSE neutral_seconds END,
            idle_seconds = CASE WHEN ? = 'Idle' THEN idle_seconds + ? ELSE idle_seconds END
        WHERE date = ?
        ''', (main_cat, duration, main_cat, duration, main_cat, duration, main_cat, duration, date_str))

        conn.commit()
    except sqlite3.Error as e:
        print(f"DB Error in save_activity_segment_db for '{title}' ({duration}s): {e}")
        # Check if the error is specifically about missing columns, suggesting schema issues persist
        if "no such column" in str(e):
            print("!!! Schema Error Detected: Please check database initialization and migrations. !!!")
        # traceback.print_exc() # Enable for full trace
        raise
    except Exception as e:
        print(f"Unexpected error saving activity: {e}")
        traceback.print_exc()
        raise
    finally:
        if conn:
            try:
                conn.close()
            except Exception as e:
                print(f"Error closing connection: {e}")

def load_initial_data():
    """Loads streaks, achievements, and today's totals from DB."""
    global achievement_data, daily_totals_runtime
    # Ensure DB exists and schema is updated first. Crucial step.
    if not initialize_data_dir_and_db():
        print("CRITICAL: Database initialization failed. Using default values.")
        # Set defaults to allow app to limp along, but data won't save/load
        today_str = date.today().isoformat()
        daily_totals_runtime.setdefault(today_str, {"Productive": 0.0, "Non-Productive": 0.0, "Neutral": 0.0, "Idle": 0.0})
        achievement_data["streaks"] = {"current": 0, "best": 0}
        achievement_data["daily_goals"] = {"productive_minutes": DAILY_GOAL_MINUTES, "completed_dates": []}
        return # Don't proceed with loading if DB init failed

    conn = None
    try:
        print("Loading initial data from database...")
        conn = sqlite3.connect(DB_PATH, timeout=10)
        cursor = conn.cursor()

        # --- Load Streaks ---
        cursor.execute("SELECT current_streak, best_streak, last_streak_date FROM streaks WHERE id = 1")
        streak_row = cursor.fetchone()
        if streak_row:
            achievement_data["streaks"]["current"] = streak_row[0] if streak_row[0] is not None else 0
            achievement_data["streaks"]["best"] = streak_row[1] if streak_row[1] is not None else 0
            last_streak_date_str = streak_row[2]

            # Check if streak is broken
            if last_streak_date_str:
                today_str = date.today().isoformat()
                yesterday_str = (date.today() - timedelta(days=1)).isoformat()
                if last_streak_date_str != today_str and last_streak_date_str != yesterday_str:
                    print(f"Streak broken (Last streak day: {last_streak_date_str}). Resetting current streak.")
                    achievement_data["streaks"]["current"] = 0
                    cursor.execute("UPDATE streaks SET current_streak = 0 WHERE id = 1")
                    conn.commit()
            elif achievement_data["streaks"]["current"] != 0:
                print("Resetting current streak as last_streak_date is missing.")
                achievement_data["streaks"]["current"] = 0
                cursor.execute("UPDATE streaks SET current_streak = 0 WHERE id = 1")
                conn.commit()
        else:
            print("Warning: Streaks row missing from DB. Initializing.")
            cursor.execute("INSERT OR IGNORE INTO streaks (id, current_streak, best_streak) VALUES (1, 0, 0)")
            conn.commit()
            achievement_data["streaks"] = {"current": 0, "best": 0}
        print(f"Loaded streaks: Current={achievement_data['streaks']['current']}, Best={achievement_data['streaks']['best']}")

        # --- Load Today's Totals & Goal ---
        today_str = date.today().isoformat()
        # Ensure all expected columns are selected
        cursor.execute('''
        SELECT productive_seconds, non_productive_seconds, neutral_seconds, idle_seconds, goal_minutes, goal_achieved
        FROM daily_totals WHERE date = ?
        ''', (today_str,))
        totals_row = cursor.fetchone()

        if totals_row:
            daily_totals_runtime[today_str] = {
                "Productive": totals_row[0] or 0.0,
                "Non-Productive": totals_row[1] or 0.0,
                "Neutral": totals_row[2] or 0.0,
                "Idle": totals_row[3] or 0.0
            }
            # Use DB goal if available, otherwise default
            db_goal = totals_row[4]
            achievement_data["daily_goals"]["productive_minutes"] = db_goal if db_goal is not None else DAILY_GOAL_MINUTES
            achievement_data["daily_goals"]["completed_dates"] = [today_str] if totals_row[5] == 1 else []
            print(f"Loaded today's totals: Prod={daily_totals_runtime[today_str]['Productive']:.0f}s, Goal={achievement_data['daily_goals']['productive_minutes']}min, Met={bool(totals_row[5])}")
        else:
            # Initialize today's entry if not found
            daily_totals_runtime[today_str] = {"Productive": 0.0, "Non-Productive": 0.0, "Neutral": 0.0, "Idle": 0.0}
            achievement_data["daily_goals"]["productive_minutes"] = DAILY_GOAL_MINUTES
            achievement_data["daily_goals"]["completed_dates"] = []
            # Insert the new day with the default goal and 0 times
            cursor.execute('''
                INSERT OR IGNORE INTO daily_totals (date, goal_minutes, goal_achieved, productive_seconds, non_productive_seconds, neutral_seconds, idle_seconds)
                VALUES (?, ?, 0, 0, 0, 0, 0)
            ''', (today_str, DAILY_GOAL_MINUTES))
            conn.commit()
            print(f"Initialized today's totals in DB. Goal: {DAILY_GOAL_MINUTES}min")

        # --- Verify Achievements Table Structure ---
        # (Actual loading/checking happens in check_for_achievements)
        try:
            cursor.execute("PRAGMA table_info(achievements)")
            columns = [info[1] for info in cursor.fetchall()]
            if 'achievement_key' in columns:
                print("Achievements table structure verified ('achievement_key' found).")
            else:
                 # This indicates a persistent problem with the migration
                 print("CRITICAL WARNING: 'achievement_key' column is STILL missing from 'achievements' table after initialization.")
        except sqlite3.Error as e:
            print(f"Warning: Could not verify achievements table structure: {e}")


        conn.close()
        print("Initial data loading complete.")

    except sqlite3.Error as e:
        print(f"DB Error loading initial data: {e}")
        traceback.print_exc()
        # Fallback to defaults
        today_str = date.today().isoformat()
        daily_totals_runtime.setdefault(today_str, {"Productive": 0.0, "Non-Productive": 0.0, "Neutral": 0.0, "Idle": 0.0})
        achievement_data["streaks"] = {"current": 0, "best": 0}
        achievement_data["daily_goals"] = {"productive_minutes": DAILY_GOAL_MINUTES, "completed_dates": []}
        print("Using default values due to DB error during loading.")
    except Exception as e:
        print(f"Unexpected error loading initial data: {e}")
        traceback.print_exc()
    finally:
        if conn:
            try: conn.close()
            except: pass

def save_streaks_db():
    """Saves the current streak data to the DB."""
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH, timeout=5.0)
        cursor = conn.cursor()
        last_date_to_save = None
        if achievement_data["streaks"]["current"] > 0:
            cursor.execute("SELECT MAX(date) FROM daily_totals WHERE goal_achieved = 1")
            result = cursor.fetchone()
            if result and result[0]:
                last_date_to_save = result[0]
                if last_date_to_save:
                    try:
                        last_date_obj = date.fromisoformat(last_date_to_save)
                        today_obj = date.today()
                        if (today_obj - last_date_obj).days > 1:
                            print(f"Inconsistency detected during streak save: Current streak > 0 but last goal completion ({last_date_to_save}) is too old. Resetting streak.")
                            achievement_data["streaks"]["current"] = 0
                            last_date_to_save = None
                    except ValueError:
                        print(f"Error parsing last_streak_date '{last_date_to_save}' from DB. Resetting streak.")
                        achievement_data["streaks"]["current"] = 0
                        last_date_to_save = None

        cursor.execute('''
            UPDATE streaks 
            SET current_streak = ?, best_streak = ?, last_streak_date = ? 
            WHERE id = 1
        ''', (
            achievement_data["streaks"]["current"],
            achievement_data["streaks"]["best"],
            last_date_to_save
        ))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error saving streaks: {e}")
        traceback.print_exc()
        raise
    except Exception as e:
        print(f"Unexpected error saving streaks: {e}")
        traceback.print_exc()
        raise
    finally:
        if conn:
            try:
                conn.close()
            except Exception as e:
                print(f"Error closing connection: {e}")

def save_achievement_db(timestamp, date_str, key, description):
    """Saves a specific achievement to the DB, ignoring if key already exists."""
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH, timeout=5.0)
        cursor = conn.cursor()
        cursor.execute('''
            INSERT OR IGNORE INTO achievements (timestamp, date, achievement_key, description)
            VALUES (?, ?, ?, ?)
        ''', (timestamp, date_str, key, description))
        conn.commit()
    except sqlite3.Error as e:
        if "UNIQUE constraint failed" in str(e):
            print(f"Achievement '{key}' already exists (INSERT OR IGNORE handled).")
        else:
            print(f"Database error saving achievement {key}: {e}")
            traceback.print_exc()
            raise
    except Exception as e:
        print(f"Unexpected error saving achievement {key}: {e}")
        traceback.print_exc()
        raise
    finally:
        if conn:
            try:
                conn.close()
            except Exception as e:
                print(f"Error closing connection: {e}")

def mark_daily_goal_achieved_db(date_str):
    """Marks the daily goal as achieved in the DB for the given date."""
    conn = None
    try:
        conn = sqlite3.connect(DB_PATH, timeout=5.0)
        cursor = conn.cursor()
        current_goal = achievement_data["daily_goals"].get("productive_minutes", DAILY_GOAL_MINUTES)
        
        # First ensure the row exists
        cursor.execute('''
            INSERT OR IGNORE INTO daily_totals 
            (date, goal_minutes, goal_achieved, productive_seconds, non_productive_seconds, neutral_seconds, idle_seconds)
            VALUES (?, ?, 0, 0, 0, 0, 0)
        ''', (date_str, current_goal))
        
        # Then update the goal achievement
        cursor.execute('''
            UPDATE daily_totals
            SET goal_achieved = 1, goal_minutes = ?
            WHERE date = ?
        ''', (current_goal, date_str))
        
        if cursor.rowcount == 0:
            print(f"Warning: Failed to mark goal achieved for date '{date_str}' in DB.")
        
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error marking goal achieved for {date_str}: {e}")
        traceback.print_exc()
        raise
    except Exception as e:
        print(f"Unexpected error marking goal achieved for {date_str}: {e}")
        traceback.print_exc()
        raise
    finally:
        if conn:
            try:
                conn.close()
            except Exception as e:
                print(f"Error closing connection: {e}")

def get_active_window_info():
    """Gets active window title and PID (Windows specific)."""
    active_window = None
    try:
        active_window = gw.getActiveWindow()
        if active_window and active_window.title:
            title = active_window.title.strip()
            pid = None
            if platform.system() == "Windows":
                try:
                    import win32process
                    import win32gui
                    hwnd = win32gui.GetForegroundWindow()
                    if hwnd:
                        _, pid = win32process.GetWindowThreadProcessId(hwnd)
                    elif hasattr(active_window, '_hWnd') and active_window._hWnd:
                        tid, pid = win32process.GetWindowThreadProcessId(active_window._hWnd)
                except ImportError:
                    pid = None
                except Exception:
                    pid = None
            return title, pid
        else:
            return "No Active Window", None
    except gw.PyGetWindowException:
        return "No Active Window", None
    except Exception as e:
        print(f"Error getting active window: {e}")
        return "Error Getting Window", None

def categorize_activity(title):
    """Categorizes activity based on title keywords."""
    if not title or title in ["No Active Window", "Error Getting Window", "Desktop", "Task Switching"]:
        return "Idle", "System Idle", title

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

def format_duration(seconds):
    """Formats seconds into Hh Mm Ss or Mm Ss or Ss."""
    if not isinstance(seconds, (int, float)) or seconds < 0:
        seconds = 0
    seconds = math.floor(seconds)
    if seconds < 60:
        return f"{seconds}s"
    elif seconds < 3600:
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes}m {secs:02d}s"
    else:
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        secs = seconds % 60
        return f"{hours}h {minutes:02d}m {secs:02d}s"

def check_for_achievements(today_productive_seconds):
    """
    Checks for achievements based on productive time and updates streaks.
    Returns a list of achievement description strings that were newly triggered.
    Queries DB directly to check if milestones/streaks were already logged today.
    """
    newly_achieved_descs = []
    today_str = date.today().isoformat()
    now_ts = time.time()
    conn_ach = None

    try:
        conn_ach = sqlite3.connect(DB_PATH, timeout=10)
        cursor_ach = conn_ach.cursor()

        # --- Check Daily Goal ---
        daily_goal_seconds = achievement_data["daily_goals"]["productive_minutes"] * 60
        goal_key_today = f"daily_goal_{today_str}"

        # Check runtime state first AND DB state
        goal_already_completed_runtime = today_str in achievement_data["daily_goals"]["completed_dates"]
        cursor_ach.execute("SELECT 1 FROM achievements WHERE achievement_key = ?", (goal_key_today,))
        goal_already_logged_db = cursor_ach.fetchone() is not None

        if not goal_already_completed_runtime and not goal_already_logged_db and today_productive_seconds >= daily_goal_seconds:
            print(f"Daily goal hit! Prod Secs: {today_productive_seconds:.0f}, Goal Secs: {daily_goal_seconds}")
            achievement_data["daily_goals"]["completed_dates"].append(today_str)
            mark_daily_goal_achieved_db(today_str) # Updates daily_totals table

            desc = f"Daily Goal Reached! ({achievement_data['daily_goals']['productive_minutes']} min)"
            newly_achieved_descs.append(desc)
            save_achievement_db(now_ts, today_str, goal_key_today, desc) # Saves to achievements table

            # --- Update Streak ---
            yesterday_str = (date.today() - timedelta(days=1)).isoformat()
            cursor_ach.execute("SELECT last_streak_date FROM streaks WHERE id = 1")
            res = cursor_ach.fetchone()
            last_streak_day_db = res[0] if res else None

            print(f"Streak check: Last streak day from DB = {last_streak_day_db}, Yesterday = {yesterday_str}")

            if last_streak_day_db == yesterday_str:
                achievement_data["streaks"]["current"] += 1
                print(f"Streak continued! New current streak: {achievement_data['streaks']['current']}")
            else:
                 achievement_data["streaks"]["current"] = 1
                 print(f"Streak started/restarted! Current streak: {achievement_data['streaks']['current']}")

            if achievement_data["streaks"]["current"] > achievement_data["streaks"]["best"]:
                achievement_data["streaks"]["best"] = achievement_data["streaks"]["current"]
                print(f"New best streak! Best: {achievement_data['streaks']['best']}")
                best_streak_key = f"best_streak_{achievement_data['streaks']['best']}_{today_str}"
                desc_streak = f"New Best Streak: {achievement_data['streaks']['best']} days!"
                cursor_ach.execute("SELECT 1 FROM achievements WHERE achievement_key = ?", (best_streak_key,))
                if cursor_ach.fetchone() is None:
                    newly_achieved_descs.append(desc_streak)
                    save_achievement_db(now_ts, today_str, best_streak_key, desc_streak)

            # Save updated streak info (important after potential changes)
            save_streaks_db() # This handles its own connection/commit

        # --- Check Time Milestones ---
        milestones_minutes = [15, 30, 60, 90, 120, 180, 240, 300, 360, 420, 480]
        # Verify structure *before* querying
        cursor_ach.execute("PRAGMA table_info(achievements)")
        columns = [info[1] for info in cursor_ach.fetchall()]
        if 'achievement_key' in columns:
            for minutes in milestones_minutes:
                milestone_seconds = minutes * 60
                if today_productive_seconds >= milestone_seconds:
                    milestone_key_today = f"productive_{minutes}min_{today_str}"
                    cursor_ach.execute("SELECT 1 FROM achievements WHERE achievement_key = ?", (milestone_key_today,))
                    if cursor_ach.fetchone() is None:
                        desc = f"Milestone: {minutes} productive minutes today!"
                        newly_achieved_descs.append(desc)
                        save_achievement_db(now_ts, today_str, milestone_key_today, desc)
        else:
            # This is a fallback warning if the initialization somehow failed
            print("Warning: Skipping milestone check - 'achievement_key' column not found in achievements table.")

        conn_ach.close()

    except sqlite3.Error as e: # Catch specific DB errors
        print(f"DB Error checking achievements: {e}")
        # Check if it's the missing column error again
        if "no such column" in str(e) and "achievement_key" in str(e):
             print("!!! Persistent Schema Error: 'achievement_key' column check failed. Database might need manual inspection or reset. !!!")
        traceback.print_exc()
    except Exception as e:
        print(f"Unexpected error checking achievements: {e}")
        traceback.print_exc()
    finally:
        if conn_ach:
            try: conn_ach.close()
            except: pass

    return newly_achieved_descs


# --- Background Tracking Thread ---
class TrackerThread(threading.Thread):
    def __init__(self, gui_queue):
        super().__init__(daemon=True)
        self.gui_queue = gui_queue
        self.running = True
        self.notifier = None
        try:
            self.notifier = DesktopNotifier(app_name="ADHD Activity Tracker")
            print("DesktopNotifier initialized successfully.")
        except Exception as e:
            print(f"Failed to initialize DesktopNotifier: {e}. Notifications disabled.")
            self.notifier = None

        # Runtime State
        self.current_title = "Initializing..."
        self.current_pid = None
        self.current_main_category = "Neutral"
        self.current_sub_category = "Initializing"
        self.current_session_start_time = time.time()
        self.last_save_time = time.time()
        self.last_notification_times = {}
        self.task_switch_times = deque(maxlen=50)

    def stop(self):
        self.running = False
        print("Tracker thread stop requested.")

    def send_to_gui(self, msg_type, data):
        """Safely put data onto the queue for the GUI thread."""
        try:
            self.gui_queue.put_nowait({"type": msg_type, "data": data})
        except queue.Full:
            print("Warning: GUI queue full. Dropping message.")
        except Exception as e:
            print(f"Error sending to GUI queue: {e}")

    def _send_notification(self, title, message):
        """Helper to send notification via GUI queue and desktop notifier."""
        self.send_to_gui("notification", {"title": title, "message": message})
        if self.notifier:
            try:
                self.notifier.send_sync(title=title, message=message)
            except NotImplementedError:
                 try:
                      self.notifier.send(title=title, message=message)
                 except Exception as e_send:
                      print(f"DesktopNotifier error sending '{title}': {e_send}")
            except Exception as e:
                print(f"DesktopNotifier error sending '{title}': {e}")

    def run(self):
        """The main loop of the tracker thread."""
        print("Tracker thread started.")
        global daily_totals_runtime

        # Send initial state loaded by main thread
        self.send_to_gui("init_data", {
            "streaks": achievement_data["streaks"],
            "goal_minutes": achievement_data["daily_goals"]["productive_minutes"]
        })

        while self.running:
            start_loop_time = time.time()
            today_str = date.today().isoformat()

            try:
                # --- Get Current Activity ---
                active_title_raw, active_pid_raw = get_active_window_info()
                activity_identifier = active_title_raw

                # --- Activity Change Detection & Logging ---
                if activity_identifier != self.current_title:
                    now = time.time()
                    segment_duration = now - self.current_session_start_time

                    # 1. Log PREVIOUS segment
                    if self.current_title != "Initializing..." and segment_duration >= 1.0:
                        segment_duration_rounded = round(segment_duration)
                        save_activity_segment_db(
                            self.current_session_start_time, today_str,
                            self.current_title, self.current_pid,
                            self.current_main_category, self.current_sub_category,
                            segment_duration_rounded
                        )

                        # Update runtime totals
                        if today_str not in daily_totals_runtime:
                             daily_totals_runtime[today_str] = {"Productive": 0.0, "Non-Productive": 0.0, "Neutral": 0.0, "Idle": 0.0}
                             achievement_data["daily_goals"]["completed_dates"] = []
                             print(f"New day detected ({today_str}). Initializing runtime totals.")

                        if self.current_main_category in daily_totals_runtime[today_str]:
                            daily_totals_runtime[today_str][self.current_main_category] += segment_duration_rounded
                        else:
                             print(f"Warning: Unknown category '{self.current_main_category}' for runtime totals.")

                        if self.current_main_category != "Idle":
                            self.task_switch_times.append(now)

                    # 2. Setup NEW segment
                    self.current_title = activity_identifier
                    self.current_pid = active_pid_raw
                    main_cat, sub_cat, _ = categorize_activity(self.current_title)
                    self.current_main_category = main_cat
                    self.current_sub_category = sub_cat
                    self.current_session_start_time = now

                    # --- Task Switching Analysis ---
                    if self.current_main_category != "Idle" and len(self.task_switch_times) >= EXCESSIVE_SWITCHES_THRESHOLD:
                        recent_switches = [t for t in self.task_switch_times if now - t <= TASK_SWITCH_WINDOW]
                        if len(recent_switches) >= EXCESSIVE_SWITCHES_THRESHOLD:
                            switch_key = "task_switching"
                            if now - self.last_notification_times.get(switch_key, 0) > 60: # Cooldown 1 min
                                msg = random.choice(TASK_SWITCH_MESSAGES)
                                self._send_notification(f"{EMOJI_SWITCH} {NOTIFICATION_TITLE_SWITCH}", msg)
                                self.last_notification_times[switch_key] = now

                # --- Calculate Current Times & Stats ---
                now = time.time()
                current_segment_duration = now - self.current_session_start_time

                if today_str not in daily_totals_runtime:
                     daily_totals_runtime[today_str] = {"Productive": 0.0, "Non-Productive": 0.0, "Neutral": 0.0, "Idle": 0.0}
                     achievement_data["daily_goals"]["completed_dates"] = []
                     print(f"New day detected ({today_str}) during calculation. Initializing runtime totals.")

                today_totals = daily_totals_runtime[today_str]

                # Calculate display totals including current segment
                display_prod_secs = today_totals.get("Productive", 0.0)
                display_nonprod_secs = today_totals.get("Non-Productive", 0.0)
                display_neutral_secs = today_totals.get("Neutral", 0.0)
                display_idle_secs = today_totals.get("Idle", 0.0)

                if self.current_main_category == "Productive": display_prod_secs += current_segment_duration
                elif self.current_main_category == "Non-Productive": display_nonprod_secs += current_segment_duration
                elif self.current_main_category == "Neutral": display_neutral_secs += current_segment_duration
                elif self.current_main_category == "Idle": display_idle_secs += current_segment_duration

                # --- Update GUI ---
                gui_update_data = {
                    "title": self.current_title if self.current_title else "N/A",
                    "main_category": self.current_main_category,
                    "sub_category": self.current_sub_category,
                    "segment_duration": current_segment_duration,
                    "today_productive_seconds": display_prod_secs,
                    "today_nonprod_seconds": display_nonprod_secs,
                    "today_neutral_seconds": display_neutral_secs,
                    "today_idle_seconds": display_idle_secs,
                    "streaks": achievement_data["streaks"],
                    "goal_minutes": achievement_data["daily_goals"]["productive_minutes"]
                }
                self.send_to_gui("update", gui_update_data)

                # --- Achievement Checks ---
                new_achievements = check_for_achievements(display_prod_secs)
                if new_achievements:
                    for desc in new_achievements:
                        self._send_notification(f"{EMOJI_ACHIEVEMENT} {NOTIFICATION_TITLE_ACHIEVEMENT}", desc)
                    # Resend update if streaks changed
                    gui_update_data["streaks"] = achievement_data["streaks"]
                    self.send_to_gui("update", gui_update_data)


                # --- ADHD Notification Logic ---
                if self.current_main_category != "Idle":
                    now = time.time() # Refresh time

                    # 1. Non-Productive Alert
                    if self.current_main_category == "Non-Productive" and current_segment_duration > DISTRACTION_ALERT_SECONDS:
                            distraction_key = f"distraction_{self.current_title}"
                            if now - self.last_notification_times.get(distraction_key, 0) > DISTRACTION_ALERT_SECONDS * 1.5:
                                msg = random.choice(REDIRECT_MESSAGES).format(time=format_duration(current_segment_duration), activity=self.current_sub_category)
                                self._send_notification(f"{EMOJI_DISTRACTED} {NOTIFICATION_TITLE_DISTRACTION}", msg)
                                self.last_notification_times[distraction_key] = now

                    # 2. Micro-Break Reminder
                    if self.current_main_category == "Productive" and current_segment_duration > MICRO_BREAK_SUGGESTION:
                            break_key = f"break_timer_{self.current_title}"
                            if now - self.last_notification_times.get(break_key, 0) > MICRO_BREAK_SUGGESTION * 0.9:
                                msg = random.choice(BREAK_MESSAGES).format(duration=BREAK_DURATION_SECONDS // 60)
                                self._send_notification(f"{EMOJI_BREAK_TIME} {NOTIFICATION_TITLE_BREAK}", msg)
                                self.last_notification_times[break_key] = now

                    # 3. Hyperfocus Check
                    if current_segment_duration > HYPERFOCUS_DETECTION_SECONDS:
                        hyperfocus_key = f"hyperfocus_{self.current_title}"
                        if now - self.last_notification_times.get(hyperfocus_key, 0) > HYPERFOCUS_DETECTION_SECONDS * 0.8:
                            if self.current_main_category == "Productive":
                                msg = random.choice(HYPERFOCUS_MESSAGES).format(activity=self.current_sub_category, time=format_duration(current_segment_duration))
                            else:
                                msg = f"Deep focus on {self.current_sub_category} for {format_duration(current_segment_duration)}. Time check?"
                            self._send_notification(f"{EMOJI_HYPERFOCUS} {NOTIFICATION_TITLE_HYPERFOCUS}", msg)
                            self.last_notification_times[hyperfocus_key] = now

                # --- Periodic Save (Streaks) ---
                if now - self.last_save_time > SAVE_INTERVAL_SECONDS:
                    save_streaks_db()
                    self.last_save_time = now

            except Exception as e:
                print(f"ERROR in tracker thread loop: {e}")
                traceback.print_exc()
                time.sleep(CHECK_INTERVAL_SECONDS * 2)

            # --- Wait ---
            loop_duration = time.time() - start_loop_time
            sleep_time = max(0.1, CHECK_INTERVAL_SECONDS - loop_duration)
            time.sleep(sleep_time)

        # --- Cleanup on thread stop ---
        print("Tracker thread finishing...")
        now = time.time()
        segment_duration = now - self.current_session_start_time
        if self.current_title != "Initializing..." and segment_duration >= 1.0:
            segment_duration_rounded = round(segment_duration)
            today_str = date.today().isoformat()
            print(f"Saving final segment: {self.current_title}, Duration: {segment_duration_rounded}")
            save_activity_segment_db(
                self.current_session_start_time, today_str,
                self.current_title, self.current_pid,
                self.current_main_category, self.current_sub_category,
                segment_duration_rounded
            )
        save_streaks_db()
        print("Tracker thread finished final save.")


# --- GUI Application Class ---
class ActivityTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ADHD Activity Tracker")
        self.root.geometry("700x500")
        self.root.minsize(600, 450)
        self.root.configure(bg=COLOR_BACKGROUND)
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        # Style Configuration
        self.style = ttk.Style()
        try:
            if platform.system() == "Windows": self.style.theme_use('vista')
            elif platform.system() == "Darwin": self.style.theme_use('aqua')
            else: self.style.theme_use('clam')
        except tk.TclError:
            print("Selected theme not available, using default.")
            self.style.theme_use('default')

        self.style.configure("TFrame", background=COLOR_BACKGROUND)
        self.style.configure("TLabel", background=COLOR_BACKGROUND, foreground=COLOR_TEXT, font=("Segoe UI", 10))
        self.style.configure("TButton", font=("Segoe UI", 10), padding=5)
        self.style.configure("TSeparator", background=COLOR_SEPARATOR)
        self.style.configure("Title.TLabel", font=("Segoe UI", 12, "bold"))
        self.style.configure("Category.TLabel", font=("Segoe UI", 10, "bold"))
        self.style.configure("Time.TLabel", font=("Segoe UI", 9), foreground="#555555")
        self.style.configure("StatsHeader.TLabel", font=("Segoe UI", 11, "bold"), foreground=COLOR_ACCENT)
        self.style.configure("Stats.TLabel", font=("Segoe UI", 10))
        self.style.configure("ProgressText.TLabel", font=("Segoe UI", 8), background=COLOR_BACKGROUND, foreground="#333333")
        self.style.configure("StatusHeader.TLabel", font=("Segoe UI", 11, "bold"), foreground=COLOR_ACCENT)
        self.style.configure("Custom.Horizontal.TProgressbar", thickness=22, troughcolor=COLOR_PROGRESS_BG, background=COLOR_PROGRESS_BAR, bordercolor=COLOR_BACKGROUND, lightcolor=COLOR_PROGRESS_BAR, darkcolor=COLOR_PROGRESS_BAR)

        # Queue
        self.gui_queue = queue.Queue()

        # --- GUI Layout ---
        main_frame = ttk.Frame(root, padding="15 15 15 15", style="TFrame")
        main_frame.pack(expand=True, fill=tk.BOTH)
        main_frame.rowconfigure(2, weight=1)
        main_frame.columnconfigure(0, weight=1)

        # Top Frame: Current Activity
        top_frame = ttk.Frame(main_frame, padding="0 0 0 10", style="TFrame")
        top_frame.grid(row=0, column=0, sticky="ew", pady=(0, 10))
        top_frame.columnconfigure(1, weight=1)
        ttk.Label(top_frame, text="Current:", style="Title.TLabel").grid(row=0, column=0, padx=(0, 10), pady=(0, 5), sticky="w")
        self.current_activity_var = tk.StringVar(value="Initializing...")
        self.current_activity_label = tk.Label(top_frame, textvariable=self.current_activity_var, font=("Segoe UI", 12, "bold"), wraplength=600, justify=tk.LEFT, anchor="w", bg=COLOR_BACKGROUND, fg=COLOR_TEXT)
        self.current_activity_label.grid(row=0, column=1, padx=0, pady=(0, 5), sticky="ew")
        self.category_var = tk.StringVar(value=f"{EMOJI_NEUTRAL} Neutral: Initializing")
        self.category_label = ttk.Label(top_frame, textvariable=self.category_var, style="Category.TLabel")
        self.category_label.grid(row=1, column=0, columnspan=2, padx=0, pady=(2, 2), sticky="w")
        self.segment_time_var = tk.StringVar(value="Segment: 0s")
        ttk.Label(top_frame, textvariable=self.segment_time_var, style="Time.TLabel").grid(row=2, column=0, columnspan=2, padx=0, pady=(2, 0), sticky="w")

        # Middle Frame: Daily Progress
        progress_frame = ttk.Frame(main_frame, padding="0 0 0 5", style="TFrame")
        progress_frame.grid(row=1, column=0, sticky="ew", pady=10)
        progress_frame.columnconfigure(0, weight=1)
        self.progress_var = tk.DoubleVar(value=0.0)
        self.progress_bar = ttk.Progressbar(progress_frame, variable=self.progress_var, maximum=100, mode='determinate', length=500, style="Custom.Horizontal.TProgressbar")
        self.progress_bar.grid(row=1, column=0, padx=(0, 10), pady=2, sticky="ew")
        self.progress_label_var = tk.StringVar(value=f"0s / {DAILY_GOAL_MINUTES} min (0%)")
        ttk.Label(progress_frame, textvariable=self.progress_label_var, style="ProgressText.TLabel").grid(row=1, column=1, padx=0, pady=2, sticky="e")

        # Bottom Frame: Stats & Status
        bottom_frame = ttk.Frame(main_frame, style="TFrame", padding="0 10 0 0")
        bottom_frame.grid(row=2, column=0, sticky="nsew", pady=(10, 0))
        bottom_frame.rowconfigure(0, weight=1)
        bottom_frame.columnconfigure(0, weight=1) # Stats column
        bottom_frame.columnconfigure(1, weight=0) # Separator column
        bottom_frame.columnconfigure(2, weight=2) # Status column

        # Stats Section (Left Column)
        stats_frame = ttk.Frame(bottom_frame, padding=10, style="TFrame")
        stats_frame.grid(row=0, column=0, sticky="nsew", padx=(0, 5))
        ttk.Label(stats_frame, text="Today's Time", style="StatsHeader.TLabel").pack(anchor="w", pady=(0, 8))
        self.productive_time_var = tk.StringVar(value=f"{EMOJI_PRODUCTIVE} Productive: 0s")
        self.productive_label = ttk.Label(stats_frame, textvariable=self.productive_time_var, style="Stats.TLabel")
        self.productive_label.pack(anchor="w", padx=5, pady=3)
        self.nonprod_time_var = tk.StringVar(value=f"{EMOJI_DISTRACTED} Non-Prod: 0s")
        self.nonprod_label = ttk.Label(stats_frame, textvariable=self.nonprod_time_var, style="Stats.TLabel")
        self.nonprod_label.pack(anchor="w", padx=5, pady=3)
        self.neutral_time_var = tk.StringVar(value=f"{EMOJI_NEUTRAL} Neutral: 0s")
        self.neutral_label = ttk.Label(stats_frame, textvariable=self.neutral_time_var, style="Stats.TLabel")
        self.neutral_label.pack(anchor="w", padx=5, pady=3)
        self.idle_time_var = tk.StringVar(value=f"{EMOJI_IDLE} Idle: 0s")
        self.idle_label = ttk.Label(stats_frame, textvariable=self.idle_time_var, style="Stats.TLabel")
        self.idle_label.pack(anchor="w", padx=5, pady=3)
        ttk.Separator(stats_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, pady=15, padx=5)
        ttk.Label(stats_frame, text="Streaks", style="StatsHeader.TLabel").pack(anchor="w", pady=(0, 8))
        self.streak_var = tk.StringVar(value=f"{EMOJI_STREAK} Current: 0 days | Best: 0 days")
        ttk.Label(stats_frame, textvariable=self.streak_var, style="Stats.TLabel").pack(anchor="w", padx=5, pady=3)

        # Vertical Separator
        ttk.Separator(bottom_frame, orient=tk.VERTICAL).grid(row=0, column=1, sticky="ns", padx=5, pady=5)

        # Status Messages Section (Right Column)
        status_frame = ttk.Frame(bottom_frame, padding=10, style="TFrame")
        status_frame.grid(row=0, column=2, sticky="nsew", padx=(5, 0))
        status_frame.rowconfigure(1, weight=1)
        status_frame.columnconfigure(0, weight=1)
        ttk.Label(status_frame, text="Status / Notifications", style="StatusHeader.TLabel").grid(row=0, column=0, sticky="w", pady=(0, 5))
        text_frame = ttk.Frame(status_frame, style="TFrame")
        text_frame.grid(row=1, column=0, sticky="nsew", pady=(5,0))
        text_frame.rowconfigure(0, weight=1)
        text_frame.columnconfigure(0, weight=1)
        self.status_text = tk.Text(text_frame, height=10, width=40, wrap=tk.WORD, state=tk.DISABLED, font=("Segoe UI", 9), bg=COLOR_STATUS_BG, fg=COLOR_TEXT, relief=tk.SOLID, borderwidth=1, padx=5, pady=5, undo=False)
        self.status_text.grid(row=0, column=0, sticky="nsew")
        scrollbar = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=self.status_text.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        self.status_text['yscrollcommand'] = scrollbar.set

        # Start Background Thread & Queue Processing
        self.tracker_thread = None
        self.start_tracker()
        self.process_queue()

    def add_status_message(self, message, level="info"):
        """Adds a timestamped message to the status text box."""
        if not hasattr(self, 'status_text') or not self.status_text.winfo_exists():
            print(f"Debug Status (GUI not ready?): {message}")
            return
        try:
            self.status_text.config(state=tk.NORMAL)
            timestamp = datetime.now().strftime("%H:%M:%S")
            prefix = f"[{timestamp}] "
            full_message = prefix + str(message).strip() + "\n"
            self.status_text.insert(tk.END, full_message)
            self.status_text.see(tk.END)
            self.status_text.config(state=tk.DISABLED)
        except tk.TclError as e:
            print(f"Error adding status message (window likely closed): {e}")
        except Exception as e:
            print(f"Unexpected error adding status message: {e}")
            traceback.print_exc()

    def process_queue(self):
        """Processes messages from the tracker thread queue."""
        try:
            for _ in range(100): # Process multiple messages
                msg = self.gui_queue.get_nowait()
                msg_type = msg.get("type")
                data = msg.get("data")

                if msg_type == "update": self.update_ui(data)
                elif msg_type == "notification": self.add_status_message(f"{data.get('title', 'Note')}: {data.get('message', '')}")
                elif msg_type == "init_data":
                    self.update_streaks(data.get("streaks", {"current": 0, "best": 0}))
                    goal_minutes = data.get("goal_minutes", DAILY_GOAL_MINUTES)
                    self.progress_label_var.set(f"0s / {goal_minutes} min (0%)") # Init progress label
                else: print(f"Unknown message type in queue: {msg_type}")
        except queue.Empty:
            pass
        except Exception as e:
            print(f"Error processing GUI queue: {e}")
            traceback.print_exc()
        finally:
            if hasattr(self, 'root') and self.root.winfo_exists():
                self.root.after(150, self.process_queue) # Schedule next check

    def update_ui(self, data):
        """Updates the GUI elements based on data from the tracker thread."""
        if not data or not hasattr(self, 'root') or not self.root.winfo_exists():
            return

        try:
            # Current Activity
            title = data.get("title", "N/A")
            main_cat = data.get("main_category", "Neutral")
            sub_cat = data.get("sub_category", "Unknown")
            segment_duration = data.get("segment_duration", 0)
            display_title = title if len(title) < 90 else title[:87]+"..."
            self.current_activity_var.set(display_title)
            self.segment_time_var.set(f"Segment: {format_duration(segment_duration)}")

            # Category Color/Emoji
            color, emoji = COLOR_NEUTRAL, EMOJI_NEUTRAL
            if main_cat == "Productive": color, emoji = COLOR_PRODUCTIVE, EMOJI_PRODUCTIVE
            elif main_cat == "Non-Productive": color, emoji = COLOR_NON_PRODUCTIVE, EMOJI_DISTRACTED
            elif main_cat == "Idle": color, emoji = COLOR_IDLE, EMOJI_IDLE
            cat_text = f"{main_cat}: {sub_cat}"
            self.category_label.config(foreground=color)
            self.category_var.set(f"{emoji} {cat_text}")

            # Daily Totals
            prod_secs = data.get("today_productive_seconds", 0)
            nonprod_secs = data.get("today_nonprod_seconds", 0)
            neutral_secs = data.get("today_neutral_seconds", 0)
            idle_secs = data.get("today_idle_seconds", 0)
            self.productive_time_var.set(f"{EMOJI_PRODUCTIVE} Productive: {format_duration(prod_secs)}")
            self.nonprod_time_var.set(f"{EMOJI_DISTRACTED} Non-Prod: {format_duration(nonprod_secs)}")
            self.neutral_time_var.set(f"{EMOJI_NEUTRAL} Neutral: {format_duration(neutral_secs)}")
            self.idle_time_var.set(f"{EMOJI_IDLE} Idle: {format_duration(idle_secs)}")
            self.productive_label.config(foreground=COLOR_PRODUCTIVE)
            self.nonprod_label.config(foreground=COLOR_NON_PRODUCTIVE)
            self.neutral_label.config(foreground=COLOR_NEUTRAL)
            self.idle_label.config(foreground=COLOR_IDLE)

            # Progress Bar
            goal_minutes = data.get("goal_minutes", DAILY_GOAL_MINUTES)
            goal_seconds = goal_minutes * 60
            if goal_seconds > 0:
                progress_percent = min(100.0, (prod_secs / goal_seconds) * 100.0)
                self.progress_var.set(progress_percent)
                self.progress_label_var.set(f"{format_duration(prod_secs)} / {goal_minutes} min ({progress_percent:.0f}%)")
            else:
                self.progress_var.set(0)
                self.progress_label_var.set(f"{format_duration(prod_secs)} / {goal_minutes} min (N/A)")

            # Streaks
            if "streaks" in data: self.update_streaks(data["streaks"])

        except tk.TclError as e:
            print(f"Error updating UI (widgets likely gone): {e}")
        except Exception as e:
            print(f"Unexpected error during UI update: {e}")
            traceback.print_exc()

    def update_streaks(self, streak_data):
        """Updates the streak display label."""
        if not streak_data: return
        current = streak_data.get("current", 0)
        best = streak_data.get("best", 0)
        self.streak_var.set(f"{EMOJI_STREAK} Current: {current} days | Best: {best} days")

    def start_tracker(self):
        """Loads data and starts the background tracker thread."""
        if self.tracker_thread is None or not self.tracker_thread.is_alive():
            self.add_status_message("Loading initial data...")
            load_initial_data() # Load/Migrate DB *before* starting thread
            if not os.path.exists(DB_PATH): # Check if DB file was created successfully
                 messagebox.showerror("Database Error", "Failed to initialize the database.\nPlease check file permissions or delete the data folder and restart.")
                 self.root.destroy()
                 return

            self.add_status_message("Data loaded. Starting tracker...")
            self.tracker_thread = TrackerThread(self.gui_queue)
            self.tracker_thread.start()
            self.add_status_message("Tracker started successfully.")
        else:
            self.add_status_message("Tracker is already running.")

    def stop_tracker(self):
        """Signals the tracker thread to stop."""
        if self.tracker_thread and self.tracker_thread.is_alive():
            self.add_status_message("Stopping tracker thread...")
            self.tracker_thread.stop()
            self.add_status_message("Stop signal sent.")

    def on_closing(self):
        """Handles the window close event."""
        print("Close button clicked.")
        self.root.after(50, self._show_quit_dialog) # Delay dialog slightly

    def _show_quit_dialog(self):
        """Shows the quit confirmation dialog."""
        if messagebox.askokcancel("Quit", "Do you want to quit the ADHD Activity Tracker?\n(Final data will be saved)"):
            print("User confirmed quit.")
            self.add_status_message("Exiting application...")
            self.stop_tracker()
            if self.tracker_thread and self.tracker_thread.is_alive():
                print("Waiting for tracker thread to finish...")
                self.tracker_thread.join(timeout=2.0) # Wait max 2s
                if self.tracker_thread.is_alive():
                    print("Warning: Tracker thread did not exit gracefully.")
            print("Destroying main window.")
            self.root.destroy()
        else:
            print("User cancelled quit.")


# --- Main Execution ---
if __name__ == "__main__":
    # Optional Dependency Check
    if platform.system() == "Windows":
        try:
            import win32process
            print("pywin32 found - PID detection enabled.")
        except ImportError:
            print("--- Optional Dependency Missing: 'pywin32' (Install with: pip install pywin32) ---")
            time.sleep(1)

    # Set up Tkinter
    root = tk.Tk()

    # Icon Loading
    script_dir = os.path.dirname(__file__)
    icon_path_ico = os.path.join(script_dir, 'icon.ico')
    icon_path_png = os.path.join(script_dir, 'icon.png')
    icon_loaded = False
    if os.path.exists(icon_path_ico):
        try:
            root.iconbitmap(icon_path_ico); icon_loaded = True
            print(f"Loaded icon: {icon_path_ico}")
        except tk.TclError: pass # Ignore error if ico invalid
    if not icon_loaded and os.path.exists(icon_path_png):
         try:
             png_icon = tk.PhotoImage(file=icon_path_png)
             root.iconphoto(True, png_icon); icon_loaded = True
             print(f"Loaded icon: {icon_path_png}")
         except tk.TclError as e: print(f"Warning: Could not load PNG icon: {e}")
    if not icon_loaded: print("Info: No 'icon.ico' or 'icon.png' found. Using default icon.")

    # Create and Run App
    app = ActivityTrackerApp(root)
    root.mainloop()

    print("Application main loop finished.")
    if app.tracker_thread and app.tracker_thread.is_alive():
        print("Stopping tracker thread...")
        app.stop_tracker()
        app.tracker_thread.join(timeout=2.0) # Wait max 2s
        if app.tracker_thread.is_alive():
            print("Warning: Tracker thread did not exit gracefully.")
    print("Exiting application.")