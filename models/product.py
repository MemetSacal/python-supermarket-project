class Product:
    def __init__(self, name, price, stock, category, product_id):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
        self.product_id = product_id

    def __str__(self):
        return (
            f"Product Name : {self.name}\n"
            f"Price        : {self.price} TL\n"
            f"Stock        : {self.stock}\n"
            f"Category     : {self.category.name}\n"
            f"Product ID   : {self.product_id}"
        )
