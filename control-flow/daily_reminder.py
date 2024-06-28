task = input("Enter your task: ")
priority = input("Enter the task's priority (high, medium, low): ").strip().lower()
time_bound = input("Is the task time_bound? (yes/no): ").strip().lower()
match priority:
    case "high":
        reminder = f"Your high-priority task is: {task}."
    case "medium":
        reminder = f"Your medium-priority task is: {task}."
    case "low":
        reminder = f"Your low-priority task is: {task}."
    case _:
        reminder = f"Your task is: {task}."
if time_bound == "yes":
    reminder += " This task requires immediate attention today!"
print(reminder)
