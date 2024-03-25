customer = {
    "name": "Burhan joy",
    "age": 23,
    "email": "burhanjoy2014@gmail,com",
    "is_verified": True
}
print(customer["name"],["age"])
# Entry new key
customer["birthdate"] = "Mar 15 2000"
print(customer["birthdate"])
# update
customer["name"] = "Burhan"
print(customer["name"])

customer["name"] = "Noman"
print(customer["name"])


Phone = input("Phone : ")
digit_mapping = {
    '1': 'One',
    '2': 'Two',
    '3': 'Three',
    '4': 'Four',
    '5': 'Five',
    '6': 'Six',
    '7': 'Seven',
    '8': 'Eight',
    '9': 'Nine',
    '0': 'Zero'
}
output = ''
for character in Phone:
    output += digit_mapping.get(character) + " "
print(output)