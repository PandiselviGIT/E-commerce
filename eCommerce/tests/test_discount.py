import unittest
from ecommerceutils.discount import Discount

class TestDiscount(unittest.TestCase):
    def setUp(self):
        """Set up test variables."""
        self.total_price = 1000  # Example total price

    def test_flat_discount(self):
        """Test applying a flat discount."""
        discounted_price = Discount.apply_flat_discount(self.total_price, 200)
        self.assertEqual(discounted_price, 800, "Flat discount not applied correctly")

    def test_flat_discount_exceeds_total(self):
        """Test flat discount that exceeds the total price."""
        discounted_price = Discount.apply_flat_discount(self.total_price, 1200)
        self.assertEqual(discounted_price, 0, "Flat discount exceeding total should result in 0")

    def test_percentage_discount(self):
        """Test applying a percentage discount."""
        discounted_price = Discount.apply_percentage_discount(self.total_price, 20)
        self.assertEqual(discounted_price, 800, "Percentage discount not applied correctly")

    def test_percentage_discount_full(self):
        """Test applying a 100% discount."""
        discounted_price = Discount.apply_percentage_discount(self.total_price, 100)
        self.assertEqual(discounted_price, 0, "100% discount should result in 0")

    def test_percentage_discount_exceeds_100(self):
        """Test percentage discount over 100% (should cap at 0)."""
        discounted_price = Discount.apply_percentage_discount(self.total_price, 150)
        self.assertEqual(discounted_price, 0, "Percentage discount over 100% should result in 0")

if __name__ == "__main__":
    unittest.main()
