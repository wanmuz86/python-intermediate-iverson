from models.order import Order
from models.cash_payment import CashPayment
from models.card_payment import CardPayment

def test_composition_version():
    order1 = Order("O200", 80, CardPayment())
    order2 = Order("O201", 30, CashPayment())

    order1.checkout()
    order2.checkout()

test_composition_version()

def test_mixins():
    order = Order("O300", 120, CardPayment())
    # Calling a mixin function from DisplayMixin
    print(order.display())
    order.checkout()

test_mixins()

