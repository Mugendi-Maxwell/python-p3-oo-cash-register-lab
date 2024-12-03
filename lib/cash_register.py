#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        
        self.discount = discount  # Discount percentage
        self.total = 0  # Total cost
        self.items = []  # List to store item names
        self.last_transaction = {"total": 0, "items": []}  # Track the last transaction

    def add_item(self, title, price, quantity=1):
        
        if not isinstance(price, (int, float)):
            raise TypeError("Price must be a numeric value (int or float).")
        if not isinstance(quantity, int) or quantity < 1:
            raise ValueError("Quantity must be a positive integer.")
        
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = {"total": price * quantity, "items": [title] * quantity}

    def apply_discount(self):
    
     if self.discount > 0:
        self.total *= (1 - self.discount / 100)
        self.total = round(self.total, 2) 
        
        
        formatted_total = f"{self.total:.0f}" if self.total.is_integer() else f"{self.total:.2f}"
        print(f"After the discount, the total comes to ${formatted_total}.")
     else:
        print("There is no discount to apply.")


    def void_last_transaction(self):
        
        self.total -= self.last_transaction["total"]
        for item in self.last_transaction["items"]:
            self.items.remove(item)
        self.last_transaction = {"total": 0, "items": []}
