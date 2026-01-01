from models.product import Product
from models.category import Category
from models.cart import Cart
from services.supermarket_service import SuperMarketService
from database.db_manager import DBManager


def main():
    db = DBManager()

    # CATEGORY ve PRODUCT objelerini DB'den çekip oluşturma
    categories = {}
    for cat_id, cat_name in db.get_categories():
        categories[cat_id] = Category(cat_name, cat_id)

    products = []
    for p_id, name, price, stock, c_id, c_name in db.get_products():
        category = categories[c_id]
        products.append(Product(name, price, stock, category, p_id))

    cart = Cart()

    service = SuperMarketService(products, cart)

    while True:
        print("\n===== SUPERMARKET MENU =====")
        print("1 - List Products")
        print("2 - List Products by Category")
        print("3 - Add Product to Cart")
        print("4 - Remove Product from Cart")
        print("5 - Show Cart")
        print("6 - Checkout")
        print("q - Exit")

        choice = input("Select an option: ")

        if choice == "1":
            service.list_products()

        elif choice == "2":
            category_name = input("Enter category name: ")
            service.list_products_by_category(category_name)

        elif choice == "3":
            try:
                product_id = int(input("Product ID: "))
                quantity = int(input("Quantity: "))
                service.add_product_to_cart(product_id, quantity)
            except ValueError:
                print("Invalid input.")

        elif choice == "4":
            try:
                product_id = int(input("Product ID: "))
                quantity = int(input("Quantity: "))
                service.remove_product_from_cart(product_id, quantity)
            except ValueError:
                print("Invalid input.")

        elif choice == "5":
            service.show_cart()

        elif choice == "6":
            service.checkout()

        elif choice == "q":
            print("Goodbye 👋")
            break

        else:
            print("Invalid selection.")


if __name__ == "__main__":
    main()
