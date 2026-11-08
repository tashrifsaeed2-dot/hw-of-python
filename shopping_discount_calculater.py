print("=== Welcome to the Smart Expense Splitter ===")

valid_input =  not True
while not valid_input:
    try:
        total_amount = float(input("Enter bill amount: "))
        discount_rate = float(input("Enter discount percent: "))
        num_friends = int(input("Enter number of people: "))
        
        saved_amount = total_amount * discount_rate / 100
        net_bill = total_amount - saved_amount
        share_per_person = net_bill / num_friends

    except ValueError:
        print("Oops! Please enter valid numbers only.")
    except ZeroDivisionError:
        print("Error: The number of people cannot be zero.")

    else:
        print("Discounted Total Bill:", net_bill)
        print("Amount each person needs to pay:", share_per_person)
        valid_input = True
    finally:
        print("Calculation attempt finished.")