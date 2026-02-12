from models.payment import Payment
from mixins.logging_mixin import LoggingMixin
from mixins.display_mixin import DisplayMixin

# Does arrangement matters?
class CashPayment(LoggingMixin, DisplayMixin,Payment):
    def pay(self, amount):
        self.log(f"Paid by cash amount {amount}")
        print(f"[CASH] Paid {amount}")
