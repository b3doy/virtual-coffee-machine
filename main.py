from resources import MENU, resources, income

# check if resources is sufficient
def check_resources(order_menu):
    """ Return True When Resources is Sufficient, Return False If Resources is Insufficient"""
    for item in order_menu:
        if order_menu[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        else:
            return True

# Process coins.
## If there are sufficient resources to make the drink selected, then the program should
## prompt the user to insert coins.
## quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
def process_coins():
    print("Please insert coin.")
    """ Return Total Coins Inserted """
    coins = int(input("How many quarters?: ")) * 0.25
    coins += int(input("How many dimes?: ")) * 0.1
    coins += int(input("How many nickels?: ")) * 0.05
    coins += int(input("How many penny?: ")) * 0.01
    return coins

# Check transaction successful?
## Check that the user has inserted enough money to purchase the drink they selected.
## E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
## program should say “​Sorry that's not enough money. Money refunded."​
# ----------------------------------------------------------------------------------
## But if the user has inserted enough money, then the cost of the drink gets added to the
## machine as the profit and this will be reflected the next time “report” is triggered. E.g.
## Water: 100ml, Milk: 50ml, Coffee: 76g, Money: $2.5
# -----------------------------------------------------------------------------------
## If the user has inserted too much money, the machine should offer change.
## The change should be rounded to 2 decimal places.
def check_transaction(payment, cost):
    if payment >= cost:
        change = round(payment - cost, 2)
        print(f"Here is your change: ${change}")
        global income
        income += cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.") 
        return False

# Make Coffee.
## If the transaction is successful and there are enough resources to make the drink the user selected, 
## then the ingredients to make the drink should be deducted from the coffee machine resources.
## Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink.
def make_coffee(order_menu, drink_name):
    """ Deduct Ingredients From Resources """
    for item in order_menu:
        resources[item] -= order_menu[item]
    print(f"Here is your {drink_name}. Enjoy!")

machine_on = True
# Prompt user by asking the menu
while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # Turn off the Coffee Machine by entering “​off​” to the prompt
    if user_choice == "off":
        machine_on = False
    # When the user enters “report” to the prompt, a report should be generated that shows the current resource values.
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gr")
        print(f"Money: ${income}")
    # Make a Coffee when user enter the valid menu
    elif user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        drink = MENU[user_choice]
        if check_resources(drink['ingredients']):
            pay = process_coins()
            if check_transaction(pay, drink['cost']):
                make_coffee(drink['ingredients'], user_choice)
    # user enter invalid menu
    else:
        print("Sorry, There's not in the menu!")