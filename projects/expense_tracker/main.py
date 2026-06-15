# I am demonstrating my learning so far in the form of this expense tracker project
# expense tracker - phase 2
# now saves data to a csv file so expenses persist between runs
# added date tracking and predefined categories
# phase 3: will add error handling to this code

import csv
from datetime import date

CSV_FILE = "expenses.csv"

CATEGORIES = [
    "Food",
    "Transport",
    "Shopping",
    "Bills",
    "Entertainment",
    "Health",
    "Other",
]

# list to store expenses in memory (loaded from csv on startup)
expenses = []


def load_expenses():
    """load expenses from the csv file into the list"""
    file = open(CSV_FILE, "r")
    reader = csv.DictReader(file)
    for row in reader:
        row["amount"] = float(row["amount"])
        expenses.append(row)
    file.close()


def save_all_expenses():
    """save all expenses to the csv file"""
    file = open(CSV_FILE, "w", newline="")
    writer = csv.DictWriter(file, fieldnames=["date", "category", "description", "amount"])
    writer.writeheader()
    for expense in expenses:
        writer.writerow(expense)
    file.close()


def add_expense():
    """ask the user for expense details and add it to the list"""
    print("Categories:")
    for i in range(len(CATEGORIES)):
        print(f"  {i + 1}. {CATEGORIES[i]}")

    cat_choice = int(input("Pick a category number: "))
    category = CATEGORIES[cat_choice - 1]

    description = input("Description: ")
    amount = float(input("Amount: "))
    today = date.today().isoformat()

    expense = {
        "date": today,
        "category": category,
        "description": description,
        "amount": amount,
    }
    expenses.append(expense)
    save_all_expenses()
    print(f"Added {description} : {amount} in {category} on {today}")


def list_expenses():
    """print all expenses and show the total"""
    if len(expenses) == 0:
        print("No expenses yet")
        return

    for expense in expenses:
        print(f"{expense['date']} | {expense['category']} | {expense['description']} | {expense['amount']}")

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
    load_expenses()
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
