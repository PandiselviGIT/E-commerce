import unittest
from ecommerceutils.product import Product
from ecommerceutils.cart import Cart

class TestCart(unittest.TestCase):
    def setUp(self):
        self.product = Product(":memory:")
        self.cart = Cart(":memory:")
        self.product.add_product("Laptop", 1000, "LAP123")

    def test_add_to_cart_and_calculate_total(self):
        products = self.product.list_products()
        self.cart.add_to_cart(products[0][0], 2)
        total = self.cart.calculate_total(tax_rate=0.1)
        self.assertAlmostEqual(total, 2200)  # 2 laptops with 10% tax
