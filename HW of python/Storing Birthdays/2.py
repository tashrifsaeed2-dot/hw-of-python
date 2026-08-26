import keyword
 
person_name = input("Enter your name: ")
goal_name = input("Enter your personal goal: ")
target_month = input("Enter the target month: ")
daily_minutes = 30
 
print("\nName:", person_name)
print("Goal:", goal_name)
print("Target Month:", target_month)
print("Daily Practice:", daily_minutes, "minutes")
 
print("\nMy Personal Goal Plan\n")
 
print("Goal Status:", end=" ")
print("Not Started")
 
print("Progress Reminder:", end=" - ")
print("Practice every day!")
 
print(
    "\n",
    person_name,
    "plans to work on",
    goal_name,
    "for",
    daily_minutes,
    "minutes every day."
)
 
print("\nPython keywords are...\n")
print(keyword.kwlist)