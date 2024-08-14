first = 123
second = 456
third = 789
print(first)
print(second)
print(third)
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)

first_ = 42
second_ = 69
third_ = 42
print(first_)
print(second_)
print(third_)
if first_ == second_ == third_:
    print(3)
elif first_ == second_ or first_ == third_ or second_ == third_:
    print(2)
else:
    print(0)
