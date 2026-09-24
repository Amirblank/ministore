class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    # show product info
    def info(self):
        print(self.name, "- $", self.price, "(Stock:", self.stock, ")")


class Store:
    def __init__(self):
        self.products = []

    # add new product
    def add_product(self, name, price, stock):
        new_product = Product(name, price, stock)
        self.products.append(new_product)

    # show all products
    def list_products(self):
        if len(self.products) == 0:
            print("No products found")
            return
        print("\nProducts:")

        count = 1
        for product in self.products:
            print("[", count, "]", end=" ")
            product.info()
            count += 1

    # search product
    def find_product(self, name):
        for product in self.products:
            if product.name.lower() == name.lower():
                return product
        return None


class CartItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity


class Cart:
    def __init__(self):
        self.items = []

    # add product to cart
    def add_to_cart(self, product, quantity):
        if quantity > product.stock:
            print("Not enough stock")
            return

        found = False

        for item in self.items:
            if item.product.name.lower() == product.name.lower():
                item.quantity += quantity
                found = True

        if not found:
            item = CartItem(product, quantity)
            self.items.append(item)
        product.stock -= quantity

        print("Product added")

    # remove product from cart
    def remove_from_cart(self, name):
        for item in self.items:
            if item.product.name.lower() == name.lower():
                item.product.stock += item.quantity
                self.items.remove(item)
                print("Removed successfully")
                return
        print("Product not in cart")

    # display cart items
    def show_cart(self):
        if len(self.items) == 0:
            print("Cart is empty")
            return

        total = 0

        print("\nYour cart:")

        for item in self.items:
            price = item.product.price * item.quantity
            total += price
            print(
                item.product.name,
                "x",
              item.quantity,
                "- $",
                price
            )

        print("Total = $", total)

    # final checkout
    def checkout(self):
        if len(self.items) == 0:
            print("Cart is empty")
            return

        total = 0

        print("\nFinal Invoice:")

        for item in self.items:
            price = item.product.price * item.quantity
            total += price

            print(
                item.product.name,
                "x",
                item.quantity,
                "- $",
                price
            )

        print("Total Price = $", total)

        self.items.clear()

        print("Thanks for shopping!")


# manager menu
def manager_menu(store):
    username = input("Username: ")
    password = input("Password: ")

    if username != "admin" or password != "1234":
        print("Wrong username or password")
        return

    print("Login successful")

    while True:
        print("\n............ Manager Menu ............")
        print("1. Add product")
        print("2. Show products")
        print("3. Back")

        choice = input("Choice: ")

        if choice == "1":
            name = input("Product name: ")
            try:
                price = float(input("Price: "))
                stock = int(input("Stock: "))
                store.add_product(name, price, stock)
                print("Product added")

            except:
                print("Invalid input")

        elif choice == "2":
            store.list_products()

        elif choice == "3":
            break

        else:
            print("Invalid choice")


# customer menu
def customer_menu(store):
    cart = Cart()
    while True:
        print("\n............ Customer Menu ............")
        store.list_products()
        print("\n1. Add to cart")
        print("2. Remove from cart")
        print("3. Show cart")
        print("4. Checkout")
        print("5. Back")

        choice = input("Choice: ")
        if choice == "1":
            name = input("Enter product name: ")
            product = store.find_product(name)

            if product == None:
                print("Product not found")
                continue
            try:
                quantity = int(input("Quantity: "))
                cart.add_to_cart(product, quantity)
            except:
                print("Invalid quantity")

        elif choice == "2":
            name = input("Enter product name: ")
            cart.remove_from_cart(name)

        elif choice == "3":
            cart.show_cart()

        elif choice == "4":
            cart.checkout()

        elif choice == "5":
            break

        else:
            print("Invalid choice")

# main function
def main():
    store = Store()
    while True:
        print("\n............ MINI STORE ............")
        print("1. Manager")
        print("2. Customer")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            manager_menu(store)

        elif choice == "2":
            customer_menu(store)

        elif choice == "3":
            print("Goodbye")
            break

        else:
            print("Invalid choice")

main()