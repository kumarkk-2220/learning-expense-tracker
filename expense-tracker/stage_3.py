def add_expenses(expenses: list, amount: float, category: str, description: str) -> dict:
    expense_dict = {"amount": amount, "category": category, "description": description}
    expenses.append(expense_dict)
    return expense_dict

def list_expenses(expenses: list) -> None:
    for index, expense in enumerate(expenses):
        print(f"{index+1}. Rs.{expense['amount']:.2f} | {expense['category']} | {expense['description']}")

def category_totals(expenses: list) -> None:
    expense_summary = {}
    for expense in expenses:
        if expense['category'] not in expense_summary.keys():
            expense_summary[expense['category']] = expense['amount']
        else:
            if expense['category'] in expense_summary.keys():
                expense_summary[expense['category']] += expense['amount']
    return expense_summary

    
def main() -> None:
    expenses_list = []
    while True:
        user_choice = input("Select an option: \n1. Add Expense\n2.List all expenses\n3.Exit\n4.Summary\nSelect a number from above: ")
        if user_choice == '1':
            amount = float(input("Enter the expense amount: "))
            category = input("Enter the expense category: ").strip()
            description = input("Enter the expense description: ").strip()
            add_expenses(expenses_list, amount, category, description)
        elif user_choice == '2':
            list_expenses(expenses_list)
        elif user_choice == '3':
            break
        elif user_choice == '4':
            print(category_totals(expenses_list))
        else:
            continue

if __name__ == "__main__":
    main()