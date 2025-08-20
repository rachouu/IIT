while True:
    print("Welcome to the Python Coffee Shop!")
    customer_name = input("What is your name?")
    print("Hello, " + customer_name + "! Let's order some coffee.")

    price_coffee = 3.50
    price_latte = 4.00
    price_iced_matcha = 8.00

    print("Coffee: $" + str(price_coffee))
    print("Latte: $" + str(price_latte))
    print("Iced matcha: $" + str(price_iced_matcha))

    choice = input("What would you like to order? (coffee/latte/iced matcha): ")

    if choice == "coffee":
        cost = price_coffee
    elif choice == "latte":
        cost = price_latte
    elif choice == "iced_matcha":
        cost = price_iced_matcha
    else:
        print("Sorry we do not have that.")
        cost = 0

    quantity = int(input("How many cups would you like?"))

    student_discount = input("Are you a student? (yes/no): ").lower()
    if student_discount == "yes":
        cost *= 0.9 # apply a 10% discount for students
        print("You have received a 10% discount for being a student.")

    total_cost = cost * quantity

    if quantity > 1:
        print("You get a discount of $1!")
        total_cost -= 1.00

    print("Your total is: $" + str(total_cost))
    print("Thank you, " + customer_name + "! Enjoy your coffee!")

    ask = input("Would you like to order anything else? (yes/no): ").lower()
    if ask == "no":
        print("Thanks for your order! Please come again.")
        break
