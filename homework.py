


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
                print(f"There are no {name.lower()} on your shopping list.")
            else:
                del self.list[name]
