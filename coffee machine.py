class CoffeeMachine:
    def __init__(self):
        self.water = 1000
        self.milk = 500
        self.coffee = 250
        self.money = 0

    def report(self):
        print(f"Water: {self.water}ml")
        print(f"Milk: {self.milk}ml")
        print(f"Coffee: {self.coffee}g")
        print(f"Money: ${self.money}")

    def check_resources(self, choice):
        if choice == 1:  # Espresso
            return self.water >= 50 and self.coffee >= 20
        elif choice == 2:  # Latte
            return self.water >= 200 and self.milk >= 150 and self.coffee >= 20
        elif choice == 3:  # Cappuccino
            return self.water >= 250 and self.milk >= 100 and self.coffee >= 20

    def process_coins(self, price):
        print(f"The price is ${price}.")
        print("Please insert coins.")
        try:
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
            total_money = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
            return total_money
        except ValueError:
            print("Invalid input. Please enter a valid number of coins.")
            return 0

    def make_coffee(self, choice, total_money, price):
        if total_money < price:
            print("Sorry that's not enough money. Money refunded.")
        else:
            change = round(total_money - price, 2)
            if change > 0:
                print(f"Here is ${change} in change.")
            if choice == 1:  # Espresso
                self.water -= 50
                self.coffee -= 20
            elif choice == 2:  # Latte
                self.water -= 200
                self.milk -= 150
                self.coffee -= 20
            elif choice == 3:  # Cappuccino
                self.water -= 250
                self.milk -= 100
                self.coffee -= 20
            self.money += price
            print("Here is your coffee. Enjoy!")

    def serve_customer(self):
        while True:
            print("What would you like?")
            print("1. Espresso ($1.50)")
            print("2. Latte ($2.50)")
            print("3. Cappuccino ($3.00)")
            print("Type 'off' to turn off the machine.")
            print("Type 'report' to get a report of resources.")
            choice = input("Please enter the number: ")
            if choice == 'off':
                break
            elif choice == 'report':
                self.report()
            else:
                try:
                    choice = int(choice)
                    if choice in [1, 2, 3]:
                        if self.check_resources(choice):
                            if choice == 1:
                                price = 1.50
                            elif choice == 2:
                                price = 2.50
                            elif choice == 3:
                                price = 3.00
                            total_money = self.process_coins(price)
                            self.make_coffee(choice, total_money, price)
                        else:
                            print("Sorry, there is not enough resources to make this drink.")
                    else:
                        print("Invalid choice. Please enter a valid number.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

coffee_machine = CoffeeMachine()
coffee_machine.serve_customer()
