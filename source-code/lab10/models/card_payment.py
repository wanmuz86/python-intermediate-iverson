from .payment import Payment
from mixins.logging_mixin import LoggingMixin
from mixins.display_mixin import DisplayMixin
class CardPayment(LoggingMixin, DisplayMixin, Payment):
    def pay(self, amount):
        # This is to prove that Mixin is sharable between classes
        self.log(f"Paid by card, amount: {amount}")
        print(f"[CARD] Paid {amount}")
