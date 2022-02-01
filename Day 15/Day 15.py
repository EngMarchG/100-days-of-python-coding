import math

total_bill = 0
price = 0
Materials = {
    "Water": 300,
    "Milk": 200,
    "Coffee": 100,
    "Money": 0
}

def money(price):
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    bill = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01
    change = abs(bill - price)
    return change, bill

def order(drink_type):
    if drink_type == "espresso":
        money = 1.5
    elif drink_type == "latte":
        money = 2.5
    elif drink_type == "cappuccino":
        money = 3.0
    return money



#print(Materials)


choice = input(print("What would you like? (espresso/latte/cappuccino): ")).lower()
if choice == "report":
    print(Materials)
elif choice == "dimes":
    print("Please insert coins")
elif choice == "nickles":
    pass
elif choice == "pennies":
    pass