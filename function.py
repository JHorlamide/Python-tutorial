# Define a function with def keyword
def greet_user():
    print(f"Hi there")
    print('Welcome aboard')


greet_user()


# Function parameters
def greet_customer(parameter='JHorlamide'):
    print(f'Hi {parameter}')


greet_customer('Horlamide')


# Keyword Arguments
def greet(first_name, last_name):
    print(f'Hello {first_name} {last_name}')


# NOTE: positional argument should always come first before keyword argument.
greet('Olamide', last_name='Jubril', )


# RETURN STATEMENT
def square(number):
    return number * number


result = square(3)
print(result)

# NOTE: The default return value of a function is None
