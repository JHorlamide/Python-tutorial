from typing import Coroutine


list_numbers = [1, 2, 3]
tuples_numbers = (1, 2, 3)

print(type(list_numbers))
print(type(tuples_numbers))

# Index of an item in a tuple
print(tuples_numbers[0])

# Unpacking
coordinates = (1, 2, 3)
x, y, z = coordinates

print('Tuple')
print(x)
print(y)
print(z)

print('List')
coordinates2 = [10, 20, 30]
m, l, o = coordinates2
print(m)
print(l)
print(o)
