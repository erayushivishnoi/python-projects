# Expense Tracker

A command-line tool to track expenses and see where my money goes.

## What it does (Phase 2)

- Add an expense by picking from predefined categories
- Each expense is saved with today's date automatically
- All data is saved to a CSV file so expenses persist between runs
- List all expenses with date, category, description, and total
- Group expenses by category with totals

## Planned for later

- Phase 3: add error handling

## How to run

```
python main.py
```

## Built with

- Python standard library only (csv, datetime)
- Lists and dictionaries for storing data in memory
- CSV file for persistent storage
- Functions, loops, conditionals, f-strings

## What I learned building this

### Phase 1
- Storing data using lists of dictionaries
- Using dictionaries to group and summarize data
- Taking user input and converting types with float()
- Structuring a program into functions
- Building a menu loop that keeps running until the user quits

### Phase 2
- Importing and using Python standard library modules (csv, datetime)
- Reading from and writing to CSV files using csv.DictReader and csv.DictWriter
- Working with dates using date.today() and isoformat()
- Using a constant list for predefined choices
- Displaying numbered options and converting user input to pick from a list
