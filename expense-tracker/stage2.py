expenses = []
    
while True:
    amount = float(input("Enter the expense amount: "))
    category = input("Enter expense the category: ")
    description = input("Enter the expense description: ")
    expenses.append({"amount": f"{amount}", "category": f"{category}", "description": f"{description}"})
    print("Added the expense: ", expenses)
    for index, expense in enumerate(expenses):
        print(f"{index}. Rs.{amount:.2f} | {category} | {description}")
    break

