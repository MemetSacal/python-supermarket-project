class Category:
    def __init__(self, name, category_id):
        self.name = name
        self.category_id = category_id

    def __str__(self):
        return f"Category: {self.name} (ID: {self.category_id})"
