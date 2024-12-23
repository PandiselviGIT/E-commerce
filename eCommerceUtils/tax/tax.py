# ecommerceutils/tax.py

class Tax:
    @staticmethod
    def calculate_tax(subtotal, tax_rate=0.1):
        """Calculate tax for a given subtotal."""
        return subtotal * tax_rate

    @staticmethod
    def calculate_with_tax(subtotal, tax_rate=0.1):
        """Calculate the total amount including tax."""
        tax = Tax.calculate_tax(subtotal, tax_rate)
        return subtotal + tax
