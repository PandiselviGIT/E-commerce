from .database import Database

class Product:
    def __init__(self, db_name="ecommerce.db"):
        self.db = Database(db_name)

    def add_product(self, name, price, sku):
        """Add a new product."""
        self.db.execute_query(
            "INSERT INTO products (name, price, sku) VALUES (?, ?, ?)",
            (name, price, sku)
        )

    def update_product(self, sku, name=None, price=None):
        """Update product details."""
        if name:
            self.db.execute_query("UPDATE products SET name = ? WHERE sku = ?", (name, sku))
        if price:
            self.db.execute_query("UPDATE products SET price = ? WHERE sku = ?", (price, sku))

    def delete_product(self, sku):
        """Delete a product."""
        self.db.execute_query("DELETE FROM products WHERE sku = ?", (sku,))

    def list_products(self):
        """List all products."""
        return self.db.fetch_all("SELECT * FROM products")
