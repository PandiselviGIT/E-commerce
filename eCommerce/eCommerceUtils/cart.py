from .database import Database

class Cart:
    def __init__(self, db_name="ecommerce.db"):
        self.db = Database(db_name)

    def add_to_cart(self, product_id, quantity):
        """Add a product to the cart."""
        self.db.execute_query(
            "INSERT INTO cart (product_id, quantity) VALUES (?, ?)",
            (product_id, quantity)
        )

    def remove_from_cart(self, product_id):
        """Remove a product from the cart."""
        self.db.execute_query("DELETE FROM cart WHERE product_id = ?", (product_id,))

    def calculate_total(self, tax_rate=0.1, discount=0):
        """Calculate total cost with tax and discount."""
        cart_items = self.db.fetch_all(
            "SELECT p.price, c.quantity FROM cart c JOIN products p ON c.product_id = p.id"
        )
        subtotal = sum(item[0] * item[1] for item in cart_items)
        tax = subtotal * tax_rate
        total = subtotal + tax - discount
        return max(total, 0)

    def cart_summary(self):
        """Generate a summary of the cart."""
        cart_items = self.db.fetch_all(
            "SELECT p.name, p.price, c.quantity FROM cart c JOIN products p ON c.product_id = p.id"
        )
        return [
            {"name": item[0], "price": item[1], "quantity": item[2]}
            for item in cart_items
        ]
