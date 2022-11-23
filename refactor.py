# TODO add recipe suggestions?


class Customer:
    def __init__(self, name):
        self.name = name
        self.cart = {}
        self.options = ["a", "add", "u", "update",
                        "r", "remove", "v", "view", "q", "quit", ]
        self.yes_no = ['y', 'yes', 'n', 'no']
        self.add_remove = ['a', 'add', 'r', 'remove']

    @classmethod
    def create(cls):
        user_name = input(
            "Welcome to Coding Temple Grocery Planner!\nWhat is your name?\n")
        print(f"Hey there, {user_name.title()}! Let's get to shopping!\n")
        new_customer = Customer(user_name.title())
        return new_customer

    # TODO I THINK THIS WORKS?
    def query(self):
        asking = True
        while asking:
            user_choice = input(
                "What would you like to do?\n(A)dd a new item\n(U)pdate an existing item\n(R)emove an existing item\n(V)iew your cart or\n(Q)uit\n").lower()
            if user_choice not in self.options:
                print(f"{user_choice.title()} is not a valid input.")
            else:
                asking = False
        return user_choice

    # TODO TEST THIS
    def add_item(self):
        user_name = input("What item would you like to add?\n").lower()
        if user_name.endswith('s'):
            user_name = user_name.rstrip('s')
        if user_name in self.cart:
            updating = True
            while updating:
                user_update = input(
                    f"It looks like you already have {self.cart[user_name].quantity} {self.cart[user_name].formatted_name} in your cart.\nWould you like to update that item? (Y)es | (N)o\n").lower()
                if user_update not in self.yes_no:
                    print("Please select (y)es or (n)o.")
                if user_update == 'n' or user_update == 'no':
                    print('No changes were made to your cart.')
                    updating = False
                if user_update == 'y' or user_update == 'yes':
                    self.update_item(user_name)
                    updating = False

        else:
            quantifying = True
            while quantifying:
                user_quantity = input(
                    f"How many {user_name}s would you like to purchase?\n")
                try:
                    user_quantity = int(user_quantity)
                    quantifying = False
                except ValueError:
                    print('\nEnter the quantity as a number.\n')
                except:
                    print("\nUnknown error occurred.\n")
            costing = True
            while costing:
                user_cost = input(f"What do {user_name}s cost per item?\n$")
                try:
                    user_cost = float(user_cost)
                    costing = False
                except ValueError:
                    print("\nEnter the cost as a number.\n")
                except:
                    print('\nUnknown error occurred.\n')
            self.cart[user_name] = Item(user_name, user_quantity, user_cost)
            print(
                f"{self.cart[user_name].quantity} {self.cart[user_name].formatted_name} added to your cart for ${self.cart[user_name].subtotal:.2f}")

    # TODO GIVE USER OPTION TO ADJUST AMOUNT INSTEAD OF DELETE OR ADD
    def update_item(self, user_name=""):
        if not user_name:
            user_name = input("Which item do you want to update?\n").lower()
            if user_name.endswith('s'):
                user_name = user_name.rstrip('s')

        user_choice = input("")

    # TODO TEST THIS MORE
    def remove_item(self, user_name=""):
        if not user_name:
            user_name = input("Which item do you want to remove?\n").lower()
            if user_name.endswith('s'):
                user_name = user_name.rstrip('s')
        if user_name not in self.cart:
            print(f"There are no {user_name}s in your cart.")
        else:
            print(
                f"{self.cart[user_name].quantity} {self.cart[user_name].formatted_name} removed from your shopping list.")
            del self.cart[user_name]

    def view_cart(self):
        if self.cart:
            for item in self.cart.values():
                print(item)
                print(f"Total ~~ ${self.cart_total:.2f}")
        else:
            print("Your cart is empty.")

    @property
    def cart_total(self):
        return sum([item.subtotal for item in self.cart.values()])


class Item:
    def __init__(self, name, quantity, cost):
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def __str__(self):
        return f"{self.quantity} {self.formatted_name} -- ${self.subtotal}"

    @property
    def subtotal(self):
        return self.quantity * self.cost

    @property
    def formatted_name(self):
        if self.quantity > 1:
            return f"{self.name}s"
        else:
            return f"{self.name}"


class App:
    def __init__(self):
        self.customer = Customer.create()
        self.choice = None

    def main(self):
        shopping = True
        while shopping:

            self.choice = self.customer.query()

            if self.choice == "a" or self.choice == "add":
                self.customer.add_item()

            if self.choice == "u" or self.choice == "update":
                self.customer.update_item()

            if self.choice == "r" or self.choice == "remove":
                self.customer.remove_item()

            if self.choice == "v" or self.choice == "view":
                self.customer.view_cart()

            if self.choice == "q" or self.choice == "quit":
                self.customer.view_cart()
                shopping = False


if __name__ == "__main__":
    app = App()
    app.main()
# apples = Item('apple', 1, .5)
# bananas = Item.create()
# print(customer.cart)
# customer.add_item(apples)
# customer.add_item(bananas)
# print(customer.cart)
# customer.remove_item(bananas)
# add driver code

# GENERAL DATA STRUCTURE
# Customer object with cart dict of items with key item.name and value of item object
# Item object contains name, quantity, cost
