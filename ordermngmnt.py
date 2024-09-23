class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: ${self.price:.2f}"


class Menu:
    def __init__(self):
        self.items = []
        self.predefined_menu()

    def predefined_menu(self):
        predefined_items = [
            ("Steak", 15.99),
            ("Hamburger", 8.99),
            ("Cheeseburger", 9.99),
            ("Hotdogs", 5.99),
            ("Chili Fries", 4.99),
            ("Soft Drink", 1.99)
        ]
        for name, price in predefined_items:
            self.add_item(name, price)

    def add_item(self, name, price):
        item = MenuItem(name, price)
        self.items.append(item)
        print(f"Added {item}")

    def remove_item(self, name):
        self.items = [item for item in self.items if item.name != name]
        print(f"Removed {name}")

    def view_menu(self):
        if not self.items:
            print("Menu is empty.")
        else:
            for item in self.items:
                print(item)


class Order:
    def __init__(self):
        self.items = []

    def add_to_order(self, menu_item):
        self.items.append(menu_item)
        print(f"Added {menu_item} to order")

    def view_order(self):
        if not self.items:
            print("Order is empty.")
        else:
            total = 0
            for item in self.items:
                print(item)
                total += item.price
            print(f"Total: ${total:.2f}")


def main():
    menu = Menu()
    order = Order()

    while True:
        print("\n1. Add Menu Item")
        print("\n2. Remove Menu Item")
        print("\n3. View Menu")
        print("\n4. Add to Order")
        print("\n5. View Order")
        print("\n6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter item name: ")
            price = float(input("Enter item price: "))
            menu.add_item(name, price)
        elif choice == '2':
            name = input("Enter item name to remove: ")
            menu.remove_item(name)
        elif choice == '3':
            menu.view_menu()
        elif choice == '4':
            name = input("Enter item name to add to order: ")
            item = next((item for item in menu.items if item.name == name), None)
            if item:
                order.add_to_order(item)
            else:
                print("Item not found in menu.")
        elif choice == '5':
            order.view_order()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
