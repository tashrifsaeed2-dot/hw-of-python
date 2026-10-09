# ================================
# DAILY ACTIVITY PLANNER
# ================================15
homework_minutes = int(input("Enter homework time in minutes: "))

if homework_minutes > 60:
    plan = "start homework now"
    print("That is a long homework session.")
else:
    plan = "finish homework quickly"
    print("That is a short homework session.")

free_time = input("Is there free time after homework? (yes/no): ").strip().lower()
if free_time == "yes":
    print("Don't forget to pick a hobby!")

print("===== DAILY PLAN =====")
print(f"Homework time: {homework_minutes} minutes")
print(f"Plan: {plan}")
print(f"Free time available: {free_time}")