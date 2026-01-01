def cart_not_empty(func):
    def wrapper(self, *args, **kwargs):
        if not self.cart.items:
            print("Cart is empty. Operation cannot be performed.")
            return
        return func(self, *args, **kwargs)
    return wrapper
def stock_available(func):
    def wrapper(self, product_id, quantity=1):
        for product in self.products:
            if product.product_id == product_id:
                if product.stock < quantity:
                    print("Not enough stock.")
                    return
        return func(self, product_id, quantity)
    return wrapper
@stock_available
def add_product_to_cart(self, product_id, quantity=1):
    for product in self.products:
        if product.product_id == product_id:
            self.cart.add_product(product, quantity)
            print("Product added to cart.")
            return
    print("Product not found.")
@cart_not_empty
def checkout(self):
    total = self.cart.calculate_total_price()
    print(f"Total amount to pay: {total} TL")

    for product, quantity in self.cart.items.items():
        product.stock -= quantity

    self.cart.clear_cart()
    print("Payment successful. Thank you for shopping!")
