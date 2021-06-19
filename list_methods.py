numbers = [2, 5, 6, 9, 10, 30, 2]

# Add and item to the of a list
numbers.append(50)

# Insert an item to any index of the list
numbers.insert(3, 50)

# Remove an item from a list
numbers.remove(30)

# Remove the last item from a list
numbers.pop()

# Check if an item exist in a list
print(50 in numbers)
print(numbers[5])

# check the number of occurrences of an item in a list
print(numbers.count(2))


# Sort a list
numbers.sort()
print(numbers)

# Reverse the order of a list
numbers.reverse()
print(numbers)

# Copy a list
copied_list = numbers.copy()
print(copied_list)
