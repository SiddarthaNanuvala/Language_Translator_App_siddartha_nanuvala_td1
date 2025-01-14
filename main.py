import time
import datetime
import json
import os

# File to store reminders (absolute path for safety)
REMINDERS_FILE = os.path.join(os.getcwd(), "reminders.json")

# Function to load reminders
def load_reminders():
    try:
        with open(REMINDERS_FILE, "r") as file:
            content = file.read().strip()
            if content:  # If content is not empty
                return json.loads(content)
            else:
                return []  # Return empty list if the file is empty
    except FileNotFoundError:
        print("File not found, returning empty reminders.")
        return []
    except json.JSONDecodeError:
        print("Error decoding JSON, returning empty reminders.")
        return []
    except Exception as e:
        print(f"Error loading reminders: {e}")
        return []

# Function to save reminders
def save_reminders(reminders):
    try:
        with open(REMINDERS_FILE, "w") as file:
            json.dump(reminders, file, indent=4)
        print(f"Reminders saved: {reminders}")  # Debugging line to check what's being saved
    except Exception as e:
        print(f"Error saving reminders: {e}")

# Function to add a new reminder
def add_reminder(task, date_time):
    reminders = load_reminders()
    reminders.append({"task": task, "time": date_time})
    save_reminders(reminders)
    print("Reminder added successfully!")

# Function to view reminders
def view_reminders():
    reminders = load_reminders()
    if reminders:
        for reminder in reminders:
            print(f"Task: {reminder['task']}, Time: {reminder['time']}")
    else:
        print("No reminders found!")

# Function to check and trigger reminders
def check_reminders():
    reminders = load_reminders()
    now = datetime.datetime.now()
    for reminder in reminders:
        reminder_time = datetime.datetime.strptime(reminder["time"], "%Y-%m-%d %H:%M:%S")
        if reminder_time <= now:
            print(f"Reminder: {reminder['task']}")
            reminders.remove(reminder)
    save_reminders(reminders)

# Main function
def main():
    while True:
        print("\nReminder App")
        print("1. Add Reminder")
        print("2. View Reminders")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            date_time = input("Enter date and time (YYYY-MM-DD HH:MM:SS): ")
            add_reminder(task, date_time)
        elif choice == "2":
            view_reminders()
        elif choice == "3":
            break
        else:
            print("Invalid choice! Try again.")

        check_reminders()
        time.sleep(1)  # Avoid high CPU usage

if __name__ == "__main__":
    main()
