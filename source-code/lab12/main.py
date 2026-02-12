from models.bad_counter import BadCounter
from models.good_counter import GoodCounter

def test_class_attribute_side_effect():
    print("\n--- Class Attribute Side Effect ---")

    a = BadCounter()
    b = BadCounter()

    a.add(1) # a.history supposed to be [1]. b.history supposed to be []
    a.add(2) # a.history supposed to be [1,2]. b.history supposed to be []

    print("a.history:", a.history)
    print("b.history:", b.history)  # ❌ unexpected shared data. BUGGGGGGGG!!!

test_class_attribute_side_effect()

def test_fixed_counter():
    print("\n--- Fixed Counter Test ---")

    a = GoodCounter()
    b = GoodCounter()

    a.add(1)
    a.add(2)

    print("a.history:", a.history)
    print("b.history:", b.history)  # ✅ correct

test_fixed_counter()