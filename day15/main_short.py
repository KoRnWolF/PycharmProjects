MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk" : 0
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

ON = True
QUARTER_AMOUNT = 0.25
DIMES_AMOUNT = 0.10
NICKLES_AMOUNT = 0.05
PENNIE_AMOUNT = 0.01
def money(sel):

    quarters = (int(input("How many quarters?")))*QUARTER_AMOUNT
    dimes = (int(input("How many dimes?")))*DIMES_AMOUNT
    nickels = (int(input("How many nickles?")))*NICKLES_AMOUNT
    pennie = (int(input("How many pennies?")))*PENNIE_AMOUNT

    total_payment = quarters + dimes + nickels + pennie

    if total_payment >= MENU[sel]["cost"]:
        change = round((total_payment - MENU[sel]["cost"]),2)
        resources["money"] += MENU[sel]["cost"]
        print(f"Here is ${change} in change.")
        payment = "good"
        return payment
    else:
        print("Sorry that's not enough money. Money refunded.")
        payment = "bad"
        return payment
def resource_check(sel):

    if sel == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")

    if sel == "espresso" or sel == "latte" or sel == "cappuccino":
        menu_ing = MENU[sel]["ingredients"]
        if resources["water"] >= menu_ing["water"] and resources["coffee"] >= menu_ing["coffee"] and resources['milk'] >= menu_ing["milk"]:
            if money(sel) == "good":
                resources["water"] = resources["water"] - MENU[sel]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU[sel]["ingredients"]["coffee"]
                resources['milk'] = resources['milk'] - MENU[sel]["ingredients"]["milk"]
                print(f"Here is your {sel}")
        else:
            print("Not enough resources")

while ON:

    selection = input("What would you like? (espresso/latte/cappuccino)\n").lower()
    try:
        if selection == "off":
            on = False
            exit()
        resource_check(selection)
    except Exception as err:
        print(f"Selection not allow : {err}")


