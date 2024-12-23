class Discount:
    @staticmethod
    def apply_flat_discount(total, discount):
        """Apply a flat discount."""
        return max(total - discount, 0)

    @staticmethod
    def apply_percentage_discount(total, percentage):
        """Apply a percentage discount."""
        discount = total * (percentage / 100)
        return max(total - discount, 0)
