import sqlite3
class DBManager:
    def __init__(self, db_name="supermarket.db"):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()
    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        """)

        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price REAL,
                stock INTEGER,
                category_id INTEGER,
                FOREIGN KEY (category_id) REFERENCES categories(id)
            )
        """)

        self.connection.commit()
    def add_category(self, category):
        self.cursor.execute(
            "INSERT INTO categories VALUES (?, ?)",
            (category.category_id, category.name)
        )
        self.connection.commit()
    def get_categories(self):
        self.cursor.execute("SELECT * FROM categories")
        return self.cursor.fetchall()
    def add_product(self, product):
        self.cursor.execute(
            "INSERT INTO products VALUES (?, ?, ?, ?, ?)",
            (
                product.product_id,
                product.name,
                product.price,
                product.stock,
                product.category.category_id
            )
        )
        self.connection.commit()
    def get_products(self):
        self.cursor.execute("""
            SELECT p.id, p.name, p.price, p.stock, c.id, c.name
            FROM products p
            JOIN categories c ON p.category_id = c.id
        """)
        return self.cursor.fetchall()
