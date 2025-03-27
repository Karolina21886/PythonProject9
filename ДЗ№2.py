#Звдання1
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product, quantity):
        if product.quantity >= quantity:
            self.items.append((product, quantity))
            product.quantity -= quantity
        else:
            print("Not enough stock.")

    def total_price(self):
        return sum(product.price * quantity for product, quantity in self.items)

    def show_cart(self):
        for product, quantity in self.items:
            print(f"{quantity} x {product.name} - ${product.price * quantity}")
        print(f"Total: ${self.total_price()}")

if __name__ == "__main__":
    laptop = Product("Laptop", 1000, 5)
    mouse = Product("Phone", 50, 10)

    cart = Cart()
    cart.add_product(laptop, 1)
    cart.add_product(mouse, 2)
    cart.show_cart()

#Завдання2
class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount


class Bank:
    def transfer(self, acc1, acc2, amount):
        if acc1.balance >= amount:
            acc1.withdraw(amount)
            acc2.deposit(amount)


if __name__ == "__main__":
    acc1 = BankAccount(1000)
    acc2 = BankAccount(500)

    acc1.deposit(200)
    acc1.withdraw(500)
    bank = Bank()
    bank.transfer(acc1, acc2, 300)