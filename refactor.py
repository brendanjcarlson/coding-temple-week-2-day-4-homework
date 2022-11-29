class Customer:

    def __init__(self, name) -> None:
        self.name = name.title()
        self.cart = {}
        self.options = ["a", "add", "r", "remove", "v", "view", "q", "quit", ]
        self.yes_no = ['y', 'yes', 'n', 'no']
        self.add_remove = ['a', 'add', 'r', 'remove']

    def add_to_cart(self, new_item: object) -> None:
        self.cart[new_item.name] = new_item
        print(
            f"{self.cart[new_item.name].quantity} {self.cart[new_item.name].formatted_name} added to your cart for ${self.cart[new_item.name].subtotal:.2f}")

    def remove_from_cart(self, user_item) -> None:
        if user_item not in self.cart:
            print(f"There are no {user_item}s in your cart.")
        else:
            print(
                f"{self.cart[user_item].quantity} {self.cart[user_item].formatted_name} removed from your shopping list.")
            del self.cart[user_item]

    def view_cart(self) -> None:
        if self.cart:
            for item in self.cart.values():
                print(item)
            print(f"Total ~~ ${self.cart_total:.2f}")
        else:
            print("Your cart is empty.")

    @property
    def cart_total(self) -> float:
        return sum([item.subtotal for item in self.cart.values()])


class Item:
    def __init__(self, name: str, quantity: int, cost: float) -> None:
        self.name = name
        self.quantity = quantity
        self.cost = cost

    def __str__(self) -> str:
        return f"{self.quantity} {self.formatted_name} -- ${self.subtotal:.2f}"

    @property
    def subtotal(self) -> float:
        return self.quantity * self.cost

    @property
    def formatted_name(self) -> str:
        if self.quantity > 1:
            return f"{self.name}s"
        else:
            return f"{self.name}"


class App:
    def __init__(self) -> None:
        self.choice = None
        self.name = input(
            "Welcome to Coding Temple Grocery Planner!\nWhat is your name?\n")

    def main(self) -> None:
        self.customer = Customer(self.name)
        print(f"Hey there, {self.customer.name}! Let's get to shopping!\n")
        shopping = True
        while shopping:

            choosing = True
            while choosing:
                self.choice = input(
                    "\nWhat would you like to do?\n(A)dd a new item\n(R)emove an existing item\n(V)iew your cart or\n(Q)uit\n").lower()
                if self.choice not in self.customer.options:
                    print("Invalid option.")
                else:
                    choosing = False

# _ ADD
            if self.choice == "a" or self.choice == "add":
                user_item = input(
                    "What item would you like to add?\n").lower().removesuffix('s')
                if user_item in self.customer.cart:
                    print(
                        f"It looks like you already have {self.customer.cart[user_item].quantity} {self.custoomer.cart[user_item].formatted_name} in your cart.\n")
                else:
                    quantifying = True
                    while quantifying:
                        user_quantity = input(
                            f"How many {user_item}s would you like to purchase?\n")
                        try:
                            user_quantity = int(user_quantity)
                            if user_quantity < 0:
                                print("\nQuantity must be greater than 0")
                            else:
                                quantifying = False
                        except:
                            print("Enter a number")

                    costing = True
                    while costing:
                        user_cost = input(
                            f"What do {user_item}s cost per item?\n$")
                        try:
                            user_cost = float(user_cost)
                            if user_cost < 0:
                                print("Cost must be greater than 0")
                            else:
                                costing = False
                        except:
                            print("Enter a number")

                self.customer.add_to_cart(
                    Item(user_item, user_quantity, user_cost))

# _ REMOVE
            if self.choice == "r" or self.choice == "remove":
                if self.customer.cart:
                    self.customer.view_cart()
                    user_item = input(
                        "Which item do you want to remove?\n").lower().removesuffix('s')
                    self.customer.remove_from_cart(user_item)
                else:
                    self.customer.view_cart()


# _ VIEW
            if self.choice == "v" or self.choice == "view":
                self.customer.view_cart()

# _ QUIT
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
