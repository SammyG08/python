coffee_making_resources = {
    "water": 500,
    "milk": 100,
    "sugar": 700,
}
types_of_coffee_served = ["latte", "expresso", "cuppuccino"]
not_enough_resources_printed_count = 0


def particular_coffee_type_requirements(choice):
    if choice == types_of_coffee_served[1]:
        if coffee_making_resources["water"] > 100 and coffee_making_resources["milk"] > 20 and coffee_making_resources["sugar"] > 100:
            can_make_expresso = True
            return can_make_expresso
        elif coffee_making_resources["water"] < 100 or coffee_making_resources["milk"] < 20 and coffee_making_resources["sugar"] < 100:
            can_make_expresso = False
            return can_make_expresso
    elif choice == types_of_coffee_served[0]:
        if coffee_making_resources["water"] > 100 and coffee_making_resources["milk"] > 50 and coffee_making_resources["sugar"] > 200:
            can_make_latte = True
            return can_make_latte
        elif coffee_making_resources["water"] < 100 or coffee_making_resources["milk"] < 50 or coffee_making_resources["sugar"] < 200:
            can_make_latte = False
            return can_make_latte
    elif choice == types_of_coffee_served[2]:
        if coffee_making_resources["water"] > 100 and coffee_making_resources["milk"] > 70 and coffee_making_resources["sugar"] > 250:
            can_make_cappuccino = True
            return can_make_cappuccino
        elif coffee_making_resources["water"] < 100 or coffee_making_resources["milk"] < 70 or coffee_making_resources["sugar"] < 310:
            can_make_cappuccino = False
            return can_make_cappuccino


def accepting_user_coffee_choice():
    user_choice = int(input("\nWhat type of coffee will you be having?\n1. Latte ($15)\n2. Expresso ($20)\n3. Cuppuccino ($27)\nResponse: "))
    return user_choice


def pricing(choice):
    if choice == types_of_coffee_served[0]:
        price = 15
    elif choice == types_of_coffee_served[1]:
        price = 20
    elif choice == types_of_coffee_served[2]:
        price = 27
    return price


def accepting_payment(choice):
    cash = int(input("\nInput cash in the slot: "))
    price_of_item = pricing(choice)
    if cash < price_of_item:
        print("\nAmount provided is insufficient for this type of coffee.\nYou will be refunded thank you.")
        return "false"
    elif cash > price_of_item:
        change = cash - price_of_item
        print(f"\nPayment received.\nWorking on your order now.\nYour change is ${change}")
    elif cash == price_of_item:
        print("\nPayment received.\nWorking on you order now.")


def processing_order():
    global not_enough_resources_printed_count

    choice = accepting_user_coffee_choice()
    if choice == 1:
        latte_can_be_made = particular_coffee_type_requirements("latte")
        if latte_can_be_made:
            if accepting_payment("latte") == "false":
                return not_enough_resources_printed_count
            else:
                coffee_making_resources["water"] = 110
                coffee_making_resources["milk"] = 52
                coffee_making_resources["sugar"] = 420
                print("\nHere is your latte")
        else:
            print("\nNot enough resources to make your latte sorry.")
            not_enough_resources_printed_count += 1
    elif choice == 2:
        expresso_can_be_made = particular_coffee_type_requirements("expresso")
        if expresso_can_be_made:
            if accepting_payment("expresso") == "false":
                return not_enough_resources_printed_count
            else:
                coffee_making_resources["water"] = 110
                coffee_making_resources["milk"] = 52
                coffee_making_resources["sugar"] = 420
                print("\nHere is your expresso")
        else:
            print("\nNot enough resources to make your expresso sorry.")
            not_enough_resources_printed_count += 1
    elif choice == 3:
        cuppuccino_can_be_made = particular_coffee_type_requirements("cuppuccino")
        if cuppuccino_can_be_made:
            if accepting_payment("cuppuccino") == "false":
                return not_enough_resources_printed_count
            else:
                coffee_making_resources["water"] = 110
                coffee_making_resources["milk"] = 52
                coffee_making_resources["sugar"] = 420
                print("\nHere is your cuppuccino")
        else:
            print("\nNot enough resources to make your cuppuccino sorry.")
            not_enough_resources_printed_count += 1
    else:
        print("Choice not recognised by the system.")

    return  not_enough_resources_printed_count