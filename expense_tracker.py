expenses = []

while True:
    print("\n========= EXPENSE TRACKER =========")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Search Expense")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        category = input("Enter category: ")
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))

        new_expense = {
            "category": category,
            "description": description,
            "amount": amount
        }

        expenses.append(new_expense)

        print("Expense added successfully!")
        print("Category:", category)
        print("Description:", description)
        print("Amount:", amount)

    elif choice == "2":
        print("\n----- ALL EXPENSES -----")

        if len(expenses) == 0:
            print("No expenses found.")
        else:
            for expense in expenses:
                print("Category:", expense["category"])
                print("Description:", expense["description"])
                print("Amount:", expense["amount"])
                print("------------------------")

    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense["amount"]

        print("Total Expense:", total)

    elif choice == "4":
        search = input("Enter category to search: ")

        found = False

        for expense in expenses:
            if expense["category"].lower() == search.lower():
                print("Category:", expense["category"])
                print("Description:", expense["description"])
                print("Amount:", expense["amount"])
                print("------------------------")
                found = True

        if found == False:
            print("No expense found.")

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice. Please try again.")
