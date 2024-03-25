import products


class Store:

    def __init__(self, products_list):
        self.my_products = products_list

    def add_product(self, product):
        self.my_products.append(product)

    def remove_product(self, product):
        for item in self.my_products:
            if item.name == product.name:
                del item

    def get_total_quantity(self):
        total = 0
        for item in self.my_products:
            total += item.quantity
        return total

    def get_all_products(self):
        active_products = []
        for item in self.my_products:
            if item.is_active():
                active_products.append(item)
        return active_products

    def order(self, shopping_list):
        total_price = 0
        for item in shopping_list:
            total_price += item[0].buy(item[1])
        return total_price


product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250),
                ]


