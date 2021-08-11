class CoffeeMachine:

    water = 400
    milk = 540
    coffee = 120
    cups = 9
    money = 550

    def remaining(self):

        print(f"""The coffee machine has:
            {self.water} of water
            {self.milk} of milk
            {self.coffee} of coffee beans
            {self.cups} of disposable cups
            {self.money} of money""")
        print()

    def buy(self):

        coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino: ")

        if coffee_type == "back":
            return
        else:
            coffee_type = int(coffee_type)

            if coffee_type == 1:
                if self.water < 250:
                    print("Sorry, not enough water!")
                elif self.coffee < 16:
                    print("Sorry, not enough coffee!")
                elif self.cups < 1:
                    print("Sorry, not enough cups!")
                else:
                    self.water -= 250
                    self.coffee -= 16
                    self.money += 4
                    self.cups -= 1

            elif coffee_type == 2:
                if self.water < 350:
                    print("Sorry, not enough water!")
                elif self.coffee < 20:
                    print("Sorry, not enough coffee!")
                elif self.milk < 75:
                    print("Sorry, not enough milk!")
                elif self.cups < 1:
                    print("Sorry, not enough cups!")
                else:
                    self.water -= 350
                    self.milk -= 75
                    self.coffee -= 20
                    self.money += 7
                    self.cups -= 1

            else:
                if self.water < 200:
                    print("Sorry, not enough water!")
                elif self.coffee < 12:
                    print("Sorry, not enough coffee!")
                elif self.milk < 100:
                    print("Sorry, not enough milk!")
                elif self.cups < 1:
                    print("Sorry, not enough cups!")
                else:
                    self.water -= 200
                    self.milk -= 100
                    self.coffee -= 12
                    self.money += 6
                    self.cups -= 1
                    print("I have enough resources, making you a coffee!")

    def fill(self):

        self.water += int(input("Write how many ml of water you want to add: "))
        self.milk += int(input("Write how many ml of milk you want to add: "))
        self.coffee += int(input("Write how many grams of coffee beans you want to add: "))
        self.cups += int(input("Write how many disposable coffee cups you want to add: "))

    def take(self):

        print(f"I gave you ${self.money}")
        self.money = 0

    def __init__(self):

        action = ""

        while action != "exit":
            action = input("Write action (buy, fill, take, remaining, exit): ")

            if action == "buy":
                self.buy()
                print()
            elif action == "fill":
                self.fill()
                print()
            elif action == "take":
                self.take()
                print()
            elif action == "remaining":
                self.remaining()
                print()
            elif action == "exit":
                return


coffee = CoffeeMachine()
