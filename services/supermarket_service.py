class SuperMarketService:
    def __init__(self, products, cart):
        self.products = products
        self.cart = cart

    def list_products(self):
        for product in self.products:
            print(product)
            print("-" * 30)

    def list_products_by_category(self, category_name):
        found = False
        for product in self.products:
            if product.category.name.lower() == category_name.lower():
                print(product)
                print("-" * 30)
                found = True

        if not found:
            print("No products found for this category.")

    def add_product_to_cart(self, product_id, quantity=1):
        for product in self.products:
            if product.product_id == product_id:
                if product.stock >= quantity:
                    self.cart.add_product(product, quantity)
                    print("Product added to cart.")
                else:
                    print("Not enough stock.")
                return

        print("Product not found.")

    def remove_product_from_cart(self, product_id, quantity=1):
        for product in self.products:
            if product.product_id == product_id:
                self.cart.remove_product(product, quantity)
                print("Product removed from cart.")
                return

        print("Product not found.")

    def show_cart(self):
        self.cart.show_cart()

    def checkout(self):
        if not self.cart.items:
            print("Cart is empty. Cannot proceed to checkout.")
            return

        total = self.cart.calculate_total_price()
        print(f"Total amount to pay: {total} TL")

        for product, quantity in self.cart.items.items():
            product.stock -= quantity

        self.cart.clear_cart()
        print("Payment successful. Thank you for shopping!")
