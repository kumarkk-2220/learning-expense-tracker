expenses = []

def add_expenses():
    amount = float(input("Enter the expense amount: "))
    category = input("Enter the expense Category: ")
    description = input("Enter the expense Description: ")
    expense_dict = {"amount": amount, "category": category, "description": description}
    expenses.append(expense_dict)
    print(expenses)

def list_expenses():
    for index, expense in enumerate(expenses):
        print(f"{index+1}. Rs.{expense['amount']:.2f} | {expense['category']} | {expense['description']}")

def category_totals():
    expense_summary = {}
    for expense in expenses:
        if expense['category'] not in expense_summary.keys():
            print(f"{expense['category']} not found. hence added")
            expense_summary[expense['category']] = expense['amount']
        else:
            if expense['category'] in expense_summary.keys():
                expense_summary[expense['category']] += expense['amount']
    print(expense_summary)

    
def main():
    while True:
        user_choice = input("Select an option: \n1. Add Expense\n2.List all expenses\n3.Exit\n4.Summary\nSelect a number from above: ")
        if user_choice == '1':
            add_expenses()
        elif user_choice == '2':
            print(list_expenses())
        elif user_choice == '3':
            break
        elif user_choice == '4':
            category_totals()
        else:
            continue

if __name__ == "__main__":
    main()