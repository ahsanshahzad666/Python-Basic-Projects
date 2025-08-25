# Rent Calculator in Python
# This program calculates the rent share for people living in a flat/hostel.

# -------------------------------
# Step 1: Take inputs from the user
rent = int(input("Enter your hostel/flat rent: "))
food = int(input("Enter the total food expense: "))
electricity_units = int(input("Enter the total electricity units consumed: "))
charge_per_unit = int(input("Enter the charge per electricity unit: "))
persons = int(input("Enter the number of persons living in the room/flat: "))


# -------------------------------
# Step 2: Perform calculations
electricity_bill = electricity_units * charge_per_unit
total_expenses = rent + food + electricity_bill
share_per_person = total_expenses / persons


# -------------------------------
# Step 3: Display results
print("\n----- Rent Calculator Result -----")
print(f"Total Rent: {rent}")
print(f"Total Food Expense: {food}")
print(f"Electricity Bill: {electricity_bill}")
print(f"Grand Total: {total_expenses}")
print(f"Each Person Should Pay: {share_per_person}")
