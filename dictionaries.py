# customers = {
#     "name": "JHorlamide Muiz",
#     "email": "jhorlamide@gmail.com",
#     "phone": "07053517306"
# }

# print(len(customers))

user_input = input('Phone: ')

numbers = {
    '1': "one",
    "2": "Two",
    "3": "Three",
    "4": "Four",
}

output = ''

for number in user_input:
    output += numbers.get(number, '!') + ' '

print(output)
