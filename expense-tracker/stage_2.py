expenses = []

while True:
    menu = input("Select an option: \n1. Add Expense\n2.List all expenses\n3.Exit\nSelect a number from above: ")
    if menu == '1':
        amount = float(input("Enter the expense amount: "))
        category = input("Enter expense the category: ")
        description = input("Enter the expense description: ")
        expenses.append({"amount": f"{amount:.2f}", "category": f"{category}", "description": f"{description}"})
        print("Added the expense: ", expenses)
    elif menu == '2':
        for index, expense in enumerate(expenses):
            print(f"{index+1}. Rs.{expense["amount"]} | {expense["category"]} | {expense["description"]}")
    else:
        break
