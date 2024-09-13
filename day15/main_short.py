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
def money(sel):

    quarters = (int(input("How many quarters?")))*0.25
    dimes = (int(input("How many dimes?")))*0.10
    nickels = (int(input("How many nickles?")))*0.05
    pennie = (int(input("How many pennies?")))*0.01

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
def resource_check(sel, order_ingredient):

    if sel == "espresso" or sel == "latte" or sel == "cappuccino":
        menu_ing = MENU[sel]["ingredients"]
        for item in order_ingredient:
            if order_ingredient[item] > resources[item]:
                print(f"Not enough {item}")
        if resources["water"] >= menu_ing["water"] and resources["coffee"] >= menu_ing["coffee"] and resources['milk'] >= menu_ing["milk"]:
            if money(sel) == "good":
                resources["water"] = resources["water"] - MENU[sel]["ingredients"]["water"]
                resources["coffee"] = resources["coffee"] - MENU[sel]["ingredients"]["coffee"]
                resources['milk'] = resources['milk'] - MENU[sel]["ingredients"]["milk"]
                print(f"Here is your {sel}")

while ON:

    selection = input("What would you like? (espresso/latte/cappuccino)\n").lower()
    try:
        if selection == "off":
            on = False
            exit()
        if selection == "report":
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}")
        if selection != "report":
            order_ingredients = MENU[selection]["ingredients"]
            resource_check(selection, order_ingredients)
    except Exception as err:
        print(f"Selection not allow : {err}")


