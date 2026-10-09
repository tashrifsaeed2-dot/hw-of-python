print("=== Swimming Pool Entry Checker ===")
print("Answer 3 questions and I will tell you which pool you can use.\n")

try:
    age = int(input("Enter your age: "))
except ValueError:
    age = None

can_swim_input = input("Can you swim? (yes/no): ").lower()
adult_here_input = input("Is an adult present with you? (yes/no): ").lower()

if can_swim_input in ["yes", "no"]:
    swim_known = True
    can_swim = (can_swim_input == "yes")
else:
    swim_known = False
    can_swim = False
    print("Error: Invalid response for swimming ability. Please enter 'yes' or 'no'.")

if adult_here_input in ["yes", "no"]:
    adult_known = True
    adult_here = (adult_here_input == "yes")
else:
    adult_known = False
    adult_here = False
    print("Error: Invalid response for adult presence. Please enter 'yes' or 'no'.")

print()
print("=== Entry Decision ===")
print("-" * 32)

if age is not None and age < 12 and not adult_here:
    print("Notice: Visitors under 12 require adult supervision.")

if swim_known and not can_swim:
    print("Notice: Non-swimmers are restricted to designated shallow areas.")

if adult_known and not adult_here:
    print("Reminder: No adult is present with you.")

if age is None or not swim_known or not adult_known:
    print("Refusal: One or more inputs were invalid. Cannot determine pool access.")

elif age < 4:
    if adult_here:
        print("Verdict: Access allowed to the Splash Pool only (adult supervision required).")
    else:
        print("Verdict: Access denied. Toddlers must be accompanied by an adult.")

elif age < 13:
    if adult_here:
        print("Verdict: Access allowed to the Main Pool with an adult present.")
    else:
        print("Verdict: Access denied to the Main Pool. Children under 13 require adult supervision.")

elif age < 18:
    if can_swim:
        print("Verdict: Access allowed to the Main Pool alone.")
    elif adult_here:
        print("Verdict: Access allowed to the Main Pool only with an adult present (cannot swim).")
    else:
        print("Verdict: Access denied. Teens who cannot swim require adult supervision.")

else:
    if can_swim:
        print("Verdict: All pools are open to you!")
    else:
        print("Verdict: Access allowed to shallow areas and main pool (exercise caution as non-swimmer).")

print()
print("Have a safe swim!")