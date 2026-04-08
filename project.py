# Simple Expense Tracker

expenses = []

def add_expense():
    amount = float(input("Enter amount: ₹"))
    category = input("Enter category (Food, Travel, etc.): ")
    description = input("Enter description: ")

    expense = {
        "amount": amount,
        "category": category,
        "description": description
    }

    expenses.append(expense)
    print("✅ Expense added successfully!\n")


def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return

    print("\n--- All Expenses ---")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. ₹{exp['amount']} | {exp['category']} | {exp['description']}")
    print()


def total_expense():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Expense: ₹{total}\n")


def category_wise():
    summary = {}

    for exp in expenses:
        cat = exp["category"]
        summary[cat] = summary.get(cat, 0) + exp["amount"]

    print("\n--- Category-wise Spending ---")
    for cat, amount in summary.items():
        print(f"{cat}: ₹{amount}")
    print()


def main():
    while True:
        print("===== Expense Tracker =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category-wise Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expense()
        elif choice == "4":
            category_wise()
        elif choice == "5":
            print("Exiting... Bye 👋")
            break
        else:
            print("Invalid choice, try again.\n")


if __name__ == "__main__":
    main()