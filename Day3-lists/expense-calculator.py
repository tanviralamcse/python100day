def add_expense(expenses):
    try:
        amount = float(input("Enter the expense amount: "))
        category = input("Enter the category (e.g., Food, Rent, Utilities): ").capitalize()
        description = input("Enter a short description of the expense: ")
        expenses.append({"amount": amount, "category": category, "description": description})
        print(f"Expense added: {description} ({category}) - ${amount:.2f}")
    except ValueError:
        print("Invalid input! Please enter a valid amount.")


def view_expenses(expenses):
    if not expenses:
        print("No expenses recorded yet!")
        return

    print("\n--- All Expenses ---")
    for idx, expense in enumerate(expenses, 1):
        print(f"{idx}. {expense['description']} | {expense['category']} | ${expense['amount']:.2f}")
    print("--------------------")


def total_expenses(expenses):
    total = sum(expense['amount'] for expense in expenses)
    print(f"\nTotal expenses so far: ${total:.2f}")


def expenses_by_category(expenses):
    if not expenses:
        print("No expenses recorded yet!")
        return

    categories = {}
    for expense in expenses:
        category = expense['category']
        categories.setdefault(category, []).append(expense)

    print("\n--- Expenses by Category ---")
    for category, category_expenses in categories.items():
        print(f"\n{category}:")
        for expense in category_expenses:
            print(f"  - {expense['description']}: ${expense['amount']:.2f}")
    print("-----------------------------")


def main():
    expenses = []
    while True:
        print("\n--- Personal Expense Tracker ---")
        print("1. Add Expense")
        print("2. View All Expenses")
        print("3. View Total Expenses")
        print("4. View Expenses by Category")
        print("5. Exit")

        try:
            choice = int(input("Choose an option: "))
            if choice == 1:
                add_expense(expenses)
            elif choice == 2:
                view_expenses(expenses)
            elif choice == 3:
                total_expenses(expenses)
            elif choice == 4:
                expenses_by_category(expenses)
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Invalid choice! Please select a valid option.")
        except ValueError:
            print("Invalid input! Please enter a number.")

if __name__ == "__main__":
    main()
