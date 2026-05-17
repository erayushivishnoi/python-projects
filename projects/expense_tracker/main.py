# I am demonstrating my learning so far in the form of this expense tracker project
# expense tracker - phase 1
# for now everything stays in memory, no file saving yet
# I have planned this in 2 more phases
# phase 2:
#   - will store data to csv files
#   - will add date to store the data in csv
#   - predefined categories to select from
# phase 3: will add exceptional handling to this code

# In memory list to store the expenses
expenses = []


def add_expense():
    """ask the user for expense details and add it to the list"""
    category = input("Category: ")
    description = input("Description: ")
    amount = float(input("Amount: "))

    expense = {
        "category": category,
        "description": description,
        "amount": amount,
    }
    expenses.append(expense)
    print(f"Added {description} : {amount} in {category}")


def list_expenses():
    """print all expenses and show the total"""
    if len(expenses) == 0:
        print("No expenses yet")
        return

    for expense in expenses:
        print(f"{expense['category']} | {expense['description']} | {expense['amount']}")

    total = 0
    for expense in expenses:
        total = total + expense["amount"]
    print(f"Total: {total}")


def expenses_by_category():
    """group expenses by category and show total for each plus overall total"""
    if len(expenses) == 0:
        print("No expenses yet")
        return

    category_totals = {}
    for expense in expenses:
        category = expense["category"]
        if category in category_totals:
            category_totals[category] = category_totals[category] + expense["amount"]
        else:
            category_totals[category] = expense["amount"]

    total = 0
    for category in category_totals:
        print(f"{category}: {category_totals[category]}")
        total = total + category_totals[category]
    print(f"Total: {total}")


def main():
    print("Expense Tracker")

    while True:
        print()
        print("1. Add expense")
        print("2. List expenses")
        print("3. Expenses by category")
        print("4. Quit")

        choice = input("Choose: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            list_expenses()
        elif choice == "3":
            expenses_by_category()
        elif choice == "4":
            print("Bye")
            break
        else:
            print("Invalid choice, try again")


main()
