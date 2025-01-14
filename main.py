import time
import json
from datetime import datetime
import os
from plyer import notification  # You'll need to install this with: pip install plyer

class ReminderApp:
    def __init__(self):
        self.reminders = []
        self.filename = "reminders.json"
        self.load_reminders()
    
    def load_reminders(self):
        """Load reminders from JSON file if it exists."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                self.reminders = json.load(f)
    
    def save_reminders(self):
        """Save reminders to JSON file."""
        with open(self.filename, 'w') as f:
            json.dump(self.reminders, f)
    
    def add_reminder(self, title, message, reminder_time):
        """Add a new reminder."""
        reminder = {
            'title': title,
            'message': message,
            'time': reminder_time,
            'completed': False
        }
        self.reminders.append(reminder)
        self.save_reminders()
        print(f"Reminder set for {reminder_time}")
    
    def check_reminders(self):
        """Check for due reminders and send notifications."""
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        for reminder in self.reminders:
            if not reminder['completed'] and reminder['time'] <= current_time:
                self.show_notification(reminder['title'], reminder['message'])
                reminder['completed'] = True
                self.save_reminders()
    
    def show_notification(self, title, message):
        """Show desktop notification."""
        notification.notify(
            title=title,
            message=message,
            app_icon=None,
            timeout=10,
        )
    
    def list_reminders(self):
        """Display all reminders."""
        if not self.reminders:
            print("No reminders set!")
            return
        
        print("\nCurrent Reminders:")
        print("-----------------")
        for i, reminder in enumerate(self.reminders, 1):
            status = "Completed" if reminder['completed'] else "Pending"
            print(f"{i}. Title: {reminder['title']}")
            print(f"   Message: {reminder['message']}")
            print(f"   Time: {reminder['time']}")
            print(f"   Status: {status}\n")

def main():
    app = ReminderApp()
    
    while True:
        print("\n=== Reminder App ===")
        print("1. Add Reminder")
        print("2. List Reminders")
        print("3. Check Reminders")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == '1':
            title = input("Enter reminder title: ")
            message = input("Enter reminder message: ")
            print("Enter reminder time (format: YYYY-MM-DD HH:MM)")
            reminder_time = input("Time: ")
            app.add_reminder(title, message, reminder_time)
            
        elif choice == '2':
            app.list_reminders()
            
        elif choice == '3':
            app.check_reminders()
            
        elif choice == '4':
            print("Goodbye!")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()