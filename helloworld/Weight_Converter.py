weight = int(input('Enter your weight : '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == "L":
    converted = weight * 0.454
    print(f'You are {converted} kilos')
elif unit.upper() == "K":
    converted = weight / 0.454
    print(f'You are {converted} pounds')
else:
    print("Please Enter 'L' or 'K' ")