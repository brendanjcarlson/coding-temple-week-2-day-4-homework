

class ShoppingList:

    def __init__(self):
        self.list = {}

    def add_item(self):
        name = input("What item would you like to add?\n").lower()
        quantity = int(
            input(f"How many {name.lower()} would you like to add?\n"))
        cost = int(
            float(input(f"What does {name.lower()} cost per item?\n")) * 1000)

        if name in self.list:
            choice = input(
                f"{name} is already on your shopping list. Would you like to update it?\n(Y)es to update | Any other key to go back").lower()
            if choice == "y" or choice == "yes":
                self.update_item()
        else:
            self.list[name] = {"quantity": quantity, "cost": cost}
            print(
                f"Successfully added {quantity} {name.lower()} to your shopping list.")

    def update_item(self):
        name = input("Which item do you want to update?\n").lower()
        print(
            f"You currently have {self.list[name]['quantity']} {name} on your shopping list.")
        choice = input(
            "Would you like to add or remove items?\n(A)dd | (R)emove")
        asking = True
        while asking:

            if choice == 'a' or choice == 'add':
                change = int(
                    input(f"How many {name} would you like to add?\n"))
                self.list[name]["quantity"] += change
                print(f"{change} {name} added to your shopping list.")
                asking = False

            elif choice == 'r' or choice == 'remove':
                change = int(
                    input(f"How many {name} would you like to remove?\n"))

                while change >= self.list[name]["quantity"]:
                    sub_choice = input(
                        f"You only have {self.list[name]['quantity']} {name} on your list.\nDo you want to remove them all? (Y)es | (N)o\n").lower()

                    if sub_choice == 'y' or sub_choice == 'yes':
                        del self.list[name]
                        return

                    elif sub_choice == 'n' or sub_choice == 'no':
                        change = int(
                            input(f"You have {self.list[name]['quantity']} {name} on your list. How many {name} would you like to remove?\n"))

                self.list[name]["quantity"] -= change
                print(f"{change} {name} removed from your shopping list.")
                asking = False

            else:
                print('Please select (A)dd or (R)emove')

    def remove_item(self):
        if not self.list:
            print('Your shopping list is empty.')
        else:
            name = input("Which item do you want to remove?\n").lower()
            if name not in self.list:
                # clear_output()
                print(f"There are no {name.lower()} on your shopping list.")
            else:
                # clear_output()
                print(f"{name.title()} removed from your shopping list.")
                del self.list[name]

    def view_list(self):
        if not self.list:
            print('Your shopping list is empty.')
        else:
            total = 0
            for key in self.list.keys():
                subtotal = self.list[key]["quantity"] * \
                    (self.list[key]["cost"])
                total += subtotal
                print(
                    f"{self.list[key]['quantity']} {key}: ${subtotal / 1000}")
            print(f"Total: ${total / 1000}")


def main():
    options = {
        "a": True, "add": True,
        "u": True, "update": True,
        "r": True, "remove": True,
        "v": True, "view": True,
        "q": True, "quit": True, }

    user_list = ShoppingList()

    browsing = True
    while browsing:

        asking = True
        while asking:
            choice = input(
                "What would you like to do?\n(A)dd a new item\n(U)pdate an existing item\n(R)emove an existing item\n(V)iew your list or\n(Q)uit\n").lower()
            if choice not in options:
                # clear_output()
                print(f"{choice.title()} is not a valid input.")
            else:
                asking = False

        if choice == "a" or choice == "add":
            user_list.add_item()

        if choice == "u" or choice == "update":
            user_list.update_item()

        if choice == "r" or choice == "remove":
            user_list.remove_item()

        if choice == "v" or choice == "view":
            user_list.view_list()

        if choice == "q" or choice == "quit":
            user_list.view_list()
            browsing = False


main()
