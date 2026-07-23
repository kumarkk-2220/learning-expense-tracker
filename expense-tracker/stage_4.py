import json
FILENAME = "expenses.json"

def load_expense(filename: str) -> list:
    try:
        with open(filename, 'r') as f:
            current_list = json.load(f)
        return current_list
    except FileNotFoundError:
        return []

def save_expense(filename: str, expenses: list) -> None:
    with open(filename, 'w') as f:
        json.dump(expenses, f)

def expense_summary(expenses: list) -> dict:
    expense_totals = {}
    for expense in expenses:
        if expense['category'] not in expense_totals:
            expense_totals[expense['category']] = expense['amount']
        else:
            expense_totals[expense['category']] += expense['amount']
    return expense_totals

def main() -> None:
    expenses_list = load_expense(filename=FILENAME)
    while True:
        user_choice = input("Select an option: \n1. Add Expense\n2.List all expenses\n3.Summary\n4.Exit\nSelect a number from above: ")
        if user_choice == '1':
            amount = float(input("Enter the expense amount: ").strip())
            category = input("Enter the expense category: ").strip()
            description = input("Enter the expense description: ").strip()
            expenses_list.append({'amount': amount, 'category': category, 'description': description})
            save_expense(filename=FILENAME, expenses=expenses_list)
        elif user_choice == '2':
            for index, expense in enumerate(expenses_list):
                print(f"{index+1}. Rs.{expense['amount']:.2f} | {expense['category']} | {expense['description']}")
        elif user_choice == '3':
            expense_report = expense_summary(expenses=expenses_list)
            for index, (cat, amount) in enumerate(expense_report.items()):
                print(f"{index+1}. {cat}: {amount:.2f}")
        else:
            break

if __name__ == "__main__":
    main()
            
            
