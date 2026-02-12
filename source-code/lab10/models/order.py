from .payment import Payment
from mixins.logging_mixin import LoggingMixin
from mixins.display_mixin import DisplayMixin

# ❌ Problem: Order inherits from CardPayment even though Order is not a payment type.
# This should be a composition not inheritance

# class Order(CardPayment):
#     def __init__(self, order_id, total):
#         self.order_id = order_id
#         self.total = total

 # correction - to add reference to Payment inside order, not inherits it       

# Multiple Inheritence
# MRO (What is it?)
# Does arrangement matter?
class Order(LoggingMixin, DisplayMixin):
    # Example of loose coupling. What is it? 
    def __init__(self, order_id, total,payment_method:Payment):
        self.order_id = order_id
        self.total = total
        self.payment_method = payment_method
    
    def checkout(self):
        self.log(f"Checkout started: {self.order_id}")
        self.payment_method.pay(self.total)
        self.log(f"Checkout ended: {self.order_id}")