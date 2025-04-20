import os
import json
import datetime
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

class ADHDDopamineTracker:
    def __init__(self):
        self.activities_file = "adhd_activities.json"
        self.user_data_file = "user_data.json"
        self.activities_categories = {
            "high_boost": [
                "Exercise (30+ min)",
                "Playing music",
                "Creative work",
                "Challenging game",
                "New exciting experience",
                "Successfully completing difficult task"
            ],
            "medium_boost": [
                "Short exercise (<30 min)",
                "Learning something interesting",
                "Social interaction (positive)",
                "Completing routine task",
                "Cooking",
                "Short gaming session",
                "Nature walk"
            ],
            "neutral": [
                "Routine work",
                "Eating regular meal",
                "Short break",
                "Watching educational content"
            ],
            "potential_drain": [
                "Passive scrolling",
                "Waiting",
                "Repetitive tasks",
                "Boring meeting",
                "Administrative paperwork",
                "Interrupted focus",
                "Overstimulation"
            ]
        }
        self.load_data()
    
    def load_data(self):
        """Load user data and activities from files"""
        if os.path.exists(self.user_data_file):
            with open(self.user_data_file, 'r') as f:
                self.user_data = json.load(f)
        else:
            self.user_data = {
                "name": "",
                "baseline": 5,  # Default baseline on a scale of 1-10
                "logs": []
            }
        
        if os.path.exists(self.activities_file):
            with open(self.activities_file, 'r') as f:
                self.activities = json.load(f)
        else:
            # Default activity effects
            self.activities = {}
            # Set default values for each activity
            for category, activities in self.activities_categories.items():
                effect = 2 if category == "high_boost" else \
                         1 if category == "medium_boost" else \
                         0 if category == "neutral" else -1
                
                for activity in activities:
                    self.activities[activity] = {
                        "default_effect": effect,
                        "duration": 30,  # Default duration in minutes
                        "category": category,
                        "personal_effect": None  # To be personalized over time
                    }
            self.save_activities()
    
    def save_activities(self):
        """Save activities to file"""
        with open(self.activities_file, 'w') as f:
            json.dump(self.activities, f, indent=4)
    
    def save_user_data(self):
        """Save user data to file"""
        with open(self.user_data_file, 'w') as f:
            json.dump(self.user_data, f, indent=4)
    
    def setup_user(self):
        """Initial user setup"""
        print(Fore.CYAN + "\n===== ADHD DOPAMINE TRACKER SETUP =====")
        name = input("Enter your name: ")
        self.user_data["name"] = name
        
        while True:
            try:
                baseline = int(input("Rate your typical baseline focus/energy (1-10): "))
                if 1 <= baseline <= 10:
                    self.user_data["baseline"] = baseline
                    break
                else:
                    print("Please enter a number between 1 and 10.")
            except ValueError:
                print("Please enter a valid number.")
        
        self.save_user_data()
        print(Fore.GREEN + f"\nSetup complete! Welcome {name}!")
    
    def log_activity(self):
        """Log a new activity and its effects"""
        print(Fore.CYAN + "\n===== LOG NEW ACTIVITY =====")
        
        # Show activity categories
        self.display_activity_categories()
        
        # Get activity
        activity = self.select_activity()
        
        # Get duration
        duration = input(f"Duration in minutes (default {self.activities[activity]['duration']}): ")
        duration = int(duration) if duration.isdigit() else self.activities[activity]['duration']
        
        # Get pre-activity state
        pre_state = int(input("Rate your focus/energy BEFORE this activity (1-10): "))
        
        # Get post-activity state
        post_state = int(input("Rate your focus/energy AFTER this activity (1-10): "))
        
        # Calculate effect
        effect = post_state - pre_state
        
        # Update personal effect
        if self.activities[activity]['personal_effect'] is None:
            self.activities[activity]['personal_effect'] = effect
        else:
            # Moving average
            self.activities[activity]['personal_effect'] = round(
                (self.activities[activity]['personal_effect'] * 0.7) + (effect * 0.3), 1
            )
        
        # Save log
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        log_entry = {
            "timestamp": timestamp,
            "activity": activity,
            "duration": duration,
            "pre_state": pre_state,
            "post_state": post_state,
            "effect": effect,
            "notes": input("Any notes about this activity? (optional): ")
        }
        
        self.user_data["logs"].append(log_entry)
        self.save_user_data()
        self.save_activities()
        
        print(Fore.GREEN + f"\nActivity logged! Effect: {self.format_effect(effect)}")
    
    def display_activity_categories(self):
        """Display activities by category"""
        for category, activities in self.activities_categories.items():
            category_name = category.replace("_", " ").title()
            
            if category == "high_boost":
                color = Fore.GREEN
            elif category == "medium_boost":
                color = Fore.CYAN
            elif category == "neutral":
                color = Fore.YELLOW
            else:
                color = Fore.RED
                
            print(f"\n{color}{category_name}:")
            
            for i, activity in enumerate(activities, 1):
                effect = self.activities[activity]['personal_effect']
                effect_str = f" (Your effect: {self.format_effect(effect)})" if effect is not None else ""
                print(f"  {i}. {activity}{effect_str}")
    
    def select_activity(self):
        """Allow user to select or enter an activity"""
        print("\nSelect an activity:")
        all_activities = []
        for category, activities in self.activities_categories.items():
            all_activities.extend(activities)
        
        for i, activity in enumerate(all_activities, 1):
            print(f"{i}. {activity}")
        
        print(f"{len(all_activities) + 1}. Enter custom activity")
        
        while True:
            choice = input("\nEnter number or activity name: ")
            
            if choice.isdigit():
                choice = int(choice)
                if 1 <= choice <= len(all_activities):
                    return all_activities[choice-1]
                elif choice == len(all_activities) + 1:
                    custom = input("Enter custom activity name: ")
                    category = self.select_category()
                    effect = 2 if category == "high_boost" else \
                             1 if category == "medium_boost" else \
                             0 if category == "neutral" else -1
                    
                    self.activities[custom] = {
                        "default_effect": effect,
                        "duration": 30,
                        "category": category,
                        "personal_effect": None
                    }
                    self.activities_categories[category].append(custom)
                    self.save_activities()
                    return custom
                else:
                    print("Invalid selection.")
            else:
                # Check if entered text matches an activity
                for activity in all_activities:
                    if choice.lower() == activity.lower():
                        return activity
                
                # If no match, add as custom
                category = self.select_category()
                effect = 2 if category == "high_boost" else \
                         1 if category == "medium_boost" else \
                         0 if category == "neutral" else -1
                
                self.activities[choice] = {
                    "default_effect": effect,
                    "duration": 30,
                    "category": category,
                    "personal_effect": None
                }
                self.activities_categories[category].append(choice)
                self.save_activities()
                return choice
    
    def select_category(self):
        """Select a category for a new activity"""
        print("\nSelect category:")
        categories = list(self.activities_categories.keys())
        for i, category in enumerate(categories, 1):
            print(f"{i}. {category.replace('_', ' ').title()}")
        
        while True:
            choice = input("Enter number: ")
            if choice.isdigit() and 1 <= int(choice) <= len(categories):
                return categories[int(choice) - 1]
            print("Invalid selection.")
    
    def view_stats(self):
        """View statistics and patterns"""
        if not self.user_data["logs"]:
            print(Fore.YELLOW + "\nNo activities logged yet. Start logging to see stats!")
            return
        
        print(Fore.CYAN + "\n===== YOUR DOPAMINE PATTERNS =====")
        
        # Most effective activities
        activities_effect = {}
        for activity in self.activities:
            if self.activities[activity]['personal_effect'] is not None:
                activities_effect[activity] = self.activities[activity]['personal_effect']
        
        if activities_effect:
            print("\nYour Top Dopamine Boosters:")
            sorted_activities = sorted(activities_effect.items(), key=lambda x: x[1], reverse=True)
            for activity, effect in sorted_activities[:5]:
                print(f"  • {activity}: {self.format_effect(effect)}")
            
            print("\nActivities to Be Cautious With:")
            for activity, effect in sorted(activities_effect.items(), key=lambda x: x[1])[:3]:
                if effect < 0:
                    print(f"  • {activity}: {self.format_effect(effect)}")
        
        # Show recent trend
        if len(self.user_data["logs"]) >= 3:
            print("\nRecent Energy/Focus Trend:")
            recent_logs = self.user_data["logs"][-10:]
            timestamps = [log["timestamp"].split()[0] for log in recent_logs]
            pre_states = [log["pre_state"] for log in recent_logs]
            post_states = [log["post_state"] for log in recent_logs]
            
            plt.figure(figsize=(10, 5))
            plt.plot(timestamps, pre_states, 'o-', label='Pre-Activity')
            plt.plot(timestamps, post_states, 'o-', label='Post-Activity')
            plt.axhline(y=self.user_data["baseline"], color='r', linestyle='--', label='Your Baseline')
            plt.title('Energy/Focus Trend')
            plt.xlabel('Date')
            plt.ylabel('Level (1-10)')
            plt.ylim(0, 11)
            plt.legend()
            plt.xticks(rotation=45)
            plt.tight_layout()
            plt.savefig('trend.png')
            plt.close()
            
            print(Fore.YELLOW + "  → Trend chart saved as 'trend.png'")
    
    def get_recommendations(self):
        """Get personalized recommendations"""
        print(Fore.CYAN + "\n===== DOPAMINE BALANCE RECOMMENDATIONS =====")
        
        if not self.user_data["logs"]:
            print(Fore.YELLOW + "No activities logged yet. Start logging to get personalized recommendations!")
            return
        
        # Get current state
        current_state = int(input("Rate your current focus/energy level (1-10): "))
        
        # Check if below baseline
        if current_state < self.user_data["baseline"]:
            print(Fore.YELLOW + f"\nYour current level ({current_state}) is below your baseline ({self.user_data['baseline']}).")
            print("Recommended dopamine-boosting activities:")
            
            # Find personalized effective activities
            effective_activities = []
            for activity, data in self.activities.items():
                if data['personal_effect'] is not None and data['personal_effect'] > 0:
                    effective_activities.append((activity, data['personal_effect'], data['duration']))
            
            # If we have personalized data, use it
            if effective_activities:
                # Sort by effect per minute (efficiency)
                effective_activities.sort(key=lambda x: x[1]/x[2], reverse=True)
                
                # Recommend based on available time
                available_time = input("How many minutes do you have available? ")
                try:
                    available_time = int(available_time)
                    print(f"\nTop recommendations for {available_time} minutes:")
                    
                    recommendations = []
                    for activity, effect, duration in effective_activities:
                        if duration <= available_time:
                            recommendations.append((activity, effect, duration))
                    
                    if recommendations:
                        for i, (activity, effect, duration) in enumerate(recommendations[:3], 1):
                            print(f"{i}. {activity} ({duration} min) - Expected boost: {self.format_effect(effect)}")
                    else:
                        print("No activities match your available time. Consider breaking down a larger activity.")
                except ValueError:
                    # Just show top activities if time not specified correctly
                    print("\nYour most effective dopamine boosters:")
                    for i, (activity, effect, duration) in enumerate(effective_activities[:5], 1):
                        print(f"{i}. {activity} ({duration} min) - Expected boost: {self.format_effect(effect)}")
            else:
                # No personalized data, use defaults
                print("\nBased on general patterns (you haven't logged these activities yet):")
                for activity in self.activities_categories["high_boost"][:3]:
                    print(f"  • {activity}")
        else:
            print(Fore.GREEN + f"\nYour current level ({current_state}) is at or above your baseline ({self.user_data['baseline']}).")
            print("This is a good time for:")
            print("  1. Tackling challenging tasks that need focus")
            print("  2. Learning something new")
            print("  3. Completing important work")
    
    def view_logs(self):
        """View activity logs"""
        if not self.user_data["logs"]:
            print(Fore.YELLOW + "\nNo activities logged yet.")
            return
        
        print(Fore.CYAN + "\n===== ACTIVITY LOGS =====")
        
        # Get number of logs to show
        num_logs = len(self.user_data["logs"])
        show_num = min(10, num_logs)  # Default to last 10
        
        user_input = input(f"Show how many recent logs? (1-{num_logs}, default: 10): ")
        if user_input.isdigit() and 1 <= int(user_input) <= num_logs:
            show_num = int(user_input)
        
        # Get logs to display
        logs_to_show = self.user_data["logs"][-show_num:]
        
        # Prepare table data
        table_data = []
        for log in logs_to_show:
            table_data.append([
                log["timestamp"],
                log["activity"],
                log["duration"],
                log["pre_state"],
                log["post_state"],
                self.format_effect(log["effect"]),
                log["notes"][:20] + ("..." if len(log["notes"]) > 20 else "")
            ])
        
        # Display table
        headers = ["Time", "Activity", "Duration", "Before", "After", "Effect", "Notes"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
    
    def format_effect(self, effect):
        """Format effect value with color"""
        if effect is None:
            return "N/A"
        
        effect_str = f"{effect:+.1f}" if isinstance(effect, float) else f"{effect:+d}"
        
        if effect > 1:
            return Fore.GREEN + effect_str
        elif effect > 0:
            return Fore.CYAN + effect_str
        elif effect == 0:
            return Fore.YELLOW + effect_str
        else:
            return Fore.RED + effect_str
    
    def educational_info(self):
        """Display educational information about ADHD and dopamine"""
        print(Fore.CYAN + "\n===== ADHD & DOPAMINE: THE BASICS =====")
        
        print("""
ADHD and Dopamine
----------------
Dopamine is a neurotransmitter that plays a crucial role in motivation, focus, and reward. 
People with ADHD typically have lower baseline dopamine levels or differences in dopamine 
processing, which contributes to many ADHD symptoms.

How Activities Affect Your Dopamine:
----------------------------------
• HIGH BOOST activities provide significant dopamine release through novelty, challenge, 
  or physical activity
• MEDIUM BOOST activities provide moderate dopamine through engagement and completion
• NEUTRAL activities maintain current levels
• POTENTIAL DRAIN activities can deplete dopamine through boredom or frustration

Managing Your Dopamine:
---------------------
1. Build "dopamine bridges" - schedule high-boost activities before challenging tasks
2. Take regular "dopamine breaks" with quick booster activities
3. Avoid multiple drain activities in sequence
4. Monitor personal patterns - what works for you specifically
5. Create a balanced daily schedule with varied activity types

When You're in a Dopamine Crash:
------------------------------
• Try a quick exercise (jumping jacks, quick walk)
• Change your environment
• Listen to upbeat music
• Engage in a small, achievable task for a quick win
• Use sensory stimulation (cold water, strong mint)
""")
        input("\nPress Enter to return to menu...")

    def run(self):
        """Main program loop"""
        if not self.user_data["name"]:
            self.setup_user()
        
        while True:
            print(Fore.CYAN + f"\n===== ADHD DOPAMINE TRACKER - Hi {self.user_data['name']}! =====")
            print("1. Log a new activity")
            print("2. View your patterns and stats")
            print("3. Get recommendations")
            print("4. View activity logs")
            print("5. Learn about ADHD and Dopamine")
            print("6. Exit")
            
            choice = input("\nChoose an option (1-6): ")
            
            if choice == "1":
                self.log_activity()
            elif choice == "2":
                self.view_stats()
            elif choice == "3":
                self.get_recommendations()
            elif choice == "4":
                self.view_logs()
            elif choice == "5":
                self.educational_info()
            elif choice == "6":
                print(Fore.GREEN + "\nThank you for using the ADHD Dopamine Tracker! Goodbye!")
                break
            else:
                print(Fore.RED + "Invalid choice. Please try again.")


if __name__ == "__main__":
    tracker = ADHDDopamineTracker()
    tracker.run()