import unittest
from ecommerceutils.product import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.product = Product(":memory:")  # Use in-memory database for testing

    def test_add_and_list_product(self):
        self.product.add_product("Laptop", 1000, "LAP123")
        products = self.product.list_products()
        self.assertEqual(len(products), 1)
        self.assertEqual(products[0][1], "Laptop")
