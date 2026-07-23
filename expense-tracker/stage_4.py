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

def main() -> None:
    expenses_list = load_expense(filename=FILENAME)
    while True:
        user_choice = input("Select an option: \n1. Add Expense\n2.List all expenses\n3.Exit\nSelect a number from above: ")
        if user_choice == '1':
            amount = float(input("Enter the expense amount: ").strip())
            category = input("Enter the expense category: ").strip()
            description = input("Enter the expense description: ").strip()
            expenses_list.append({'amount': amount, 'category': category, 'description': description})
            save_expense(filename=FILENAME, expenses=expenses_list)
        elif user_choice == '2':
            for expense in expenses_list:
                print(expense)
        else:
            break

if __name__ == "__main__":
    main()
            
            
