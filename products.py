class Product:
    active = True

    def __init__(self, name, price, quantity):
        if name != "" and price > 0 and quantity > 0:
            self.name = name
            self.price = price
            self.set_quantity(quantity)
        else:
            raise Exception("invalid input!!")

    def show(self):
        print(f"{self.name} ,price:{self.price}, Quantity:{self.quantity}")

    def set_quantity(self, quantity):
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def get_quantity(self):
        return self.quantity

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def is_active(self):
        return self.active

    def buy(self, quantity):
        if self.quantity - quantity >= 0 and self.is_active():
            self.set_quantity(self.quantity - quantity)
            return quantity * self.price

        else:
            raise Exception("order more than quantity")



