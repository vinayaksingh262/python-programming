def expense_tracker():

    income = float(input("Enter total income: "))

    expenses = {}
    total_expenses = 0

    while True:
        category = input("Enter expense and type or 'done': ").strip().lower()
        if category == "done":
            break
        price = float(input("Enter the price: "))

        expenses[category] = expenses.get(category, 0) + price
        total_expenses += price

    savings = income - total_expenses

    print("\nSummary of expenses:")
    print(f"Total income: {income}")
    print(f"Total expenses: {total_expenses}")
    print(f"Total savings: {savings}")

    print("\nAnalysis:")
    print("Expense and amount:")
    for category, amount in expenses.items():
        print(f"- {category}: {amount}")


expense_tracker()
