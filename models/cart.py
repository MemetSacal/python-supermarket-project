from itertools import product


class Cart:
    def __init__(self):
        self.items = {}

    def add_product(self, name, price, quantity = 1):
        if product in self.items:
            self.items[product] += [quantity]
        else:
            self.items[product] = [quantity]

    def remove_product(self,product, quantity = 1):
        if product not in self.items:
            return

        if self.items[product] > [quantity]:
            self.items[product] -= [quantity]

        else:
            del self.items[product]

    def calculate_total_price(self):
        total = 0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total

    def show_cart(self):
        if not self.items:
            print("Cart is empty.")
            return

        print("----- CART -----")
        for product, quantity in self.items.items():
            print(f"{product.name} | {quantity} x {product.price} TL = {product.price * quantity} TL")

        print("----------------")
        print(f"Total Price: {self.calculate_total_price()} TL")

    def clear_cart(self):
        self.items.clear()