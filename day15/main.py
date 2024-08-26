MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
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
import math
ON = True
# esp_ing = MENU["espresso"]["ingredients"]TODO change all to this later
def money(sel):

    quarter_amount = 0.25
    dimes_amount = 0.10
    nickles_amount = 0.05
    pennie_amount = 0.01

    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickles?"))
    pennie = int(input("How many pennies?"))

    total_quarters = quarter_amount * quarters
    total_dimes = dimes_amount * dimes
    total_nickels = nickles_amount * nickels
    total_pennie = pennie_amount * pennie
    total_payment = total_quarters + total_dimes + total_nickels + total_pennie

    if sel == "espresso":
        if total_payment >= MENU["espresso"]["cost"]:
            change = round((total_payment - MENU["espresso"]["cost"]),2)
            resources["money"] += MENU["espresso"]["cost"]
            print(f"Here is ${change} in change.")
            payment = "good"
            return payment
        else:
            print("Sorry that's not enough money. Money refunded.")
            payment = "bad"
            return payment

    if sel == "latte":
        if total_payment >= MENU["latte"]["cost"]:
            change = round((total_payment - MENU["latte"]["cost"]),2)
            resources["money"] += MENU["latte"]["cost"]
            print(f"Here is ${change} in change.")
            payment = "good"
            return payment
        else:
            print("Sorry that's not enough money. Money refunded.")
            payment = "bad"
            return payment

    if sel == "cappuccino":
        if total_payment >= MENU["cappuccino"]["cost"]:
            change = round((total_payment - MENU["cappuccino"]["cost"]),2)
            resources["cappuccino"] += MENU["cappuccino"]["cost"]
            print(f"Here is ${change} in change.")
            payment = "good"
            return payment
        else:
            print("Sorry that's not enough money. Money refunded.")
            payment = "bad"
            return payment

def resource_check(sel):

    if sel == "espresso":
        target_water = 50
        target_coffee = 18
        if resources["water"] >= target_water and resources["coffee"] >= target_coffee:
            if money(sel) == "good":
                resources["water"] = resources["water"] - target_water
                resources["coffee"] = resources["coffee"] - target_coffee
                print("Here is your espresso")
        else:
            print("Not enough resources")

    if sel == "latte":
        target_water = 200
        target_coffee = 24
        target_milk = 150
        if resources["water"] >= target_water and resources["coffee"] >= target_coffee and resources['milk'] >= target_milk:
            if money(sel) == "good":
                resources["water"] = resources["water"] - target_water
                resources["coffee"] = resources["coffee"] - target_coffee
                resources['milk'] = resources['milk'] - target_milk
                print("Here is your latte")
        else:
            print("Not enough resources")

    if sel == "cappuccino":
        target_water = 250
        target_coffee = 24
        target_milk = 100
        if resources["water"] >= target_water and resources["coffee"] >= target_coffee and resources['milk'] >= target_milk:
            if money(sel) == "good":
                resources["water"] = resources["water"] - target_water
                resources["coffee"] = resources["coffee"] - target_coffee
                resources['milk'] = resources['milk'] - target_milk
                print("Here is your cappuccino, enjoy")
        else:
            print("Not enough resources")

    if sel == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${resources['money']}")

while ON:

    selection = input("What would you like? (espresso/latte/cappuccino)\n")
    if selection == "off":
        on = False
        exit()
    resource_check(selection)


