tuple_ = ("Python", "Tuple", "Ordered", "Immutable")
print(tuple_ + (4, 5, 6))  # Adding a tuple to the tuple_
tuple_[1] = "gopal"  # TypeError: 'tuple' object does not support item assignment
print(tuple_)