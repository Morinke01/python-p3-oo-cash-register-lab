class CashRegister:
    total = 0  # Class attribute to store the total across all instances

    def __init__(self, discount=0):
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0

    def add_item(self, title, price, quantity=1):
        for _ in range(quantity):
            self.total += price
            self.last_transaction_amount = price  # Update last_transaction_amount for each item
            self.items.append(title)

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.discount / 100) * self.total
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.items:
            self.total -= self.last_transaction_amount
            self.items.pop()

        if not self.items:  # Check if all items have been removed
            self.total = 0.0
        else:
            self.total = round(self.total, 2) if round(self.total, 2) != 0.0 else 0.0

    def _get_total_without_last_item(self):
        if self.items:
            return self.total - self.items.count(self.items[-1]) * self.total / len(self.items)
        return 0
