import products
import store

product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                products.Product("Google Pixel 7", price=500, quantity=250)
                ]
best_buy = store.Store(product_list)


def list_all_products(all_product):
    for item in all_product:
        item.show()


def make_order(my_store):
    name = input("Which product # do you want?")
    quantity = int(input("What amount do you want?"))
    for item in my_store.get_all_products():
        if name == item.name:
            item.buy(quantity)
            print("item added")
            return True
    print("item not found")
    return False


def menu():
    print("1. List all products in store\n2. Sho w total amount in store\n3. Make an order\n4. Quit")
    user_input = int(input())
    return user_input


def start(my_store):
    user_input = menu()
    while user_input != 4:
        if user_input == 1:
            list_all_products(my_store.get_all_products())
        if user_input == 2:
            print(my_store.get_total_quantity())
        if user_input == 3:
            make_order(my_store)
        user_input = menu()


if __name__ == '__main__':
    start(best_buy)


