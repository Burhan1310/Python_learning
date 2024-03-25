#  if the temperature is greater than 30
#     it's a hot day
# otherwise if it's less than 10
#     it's a cold day
# otherwise
#     it's neither hot nor cold

temperature = 35

if temperature != 30:
    print("it's a hot day")
else:
    print("It's not a hot day")

name = input("Enter your name: ")

if len(name) < 3:
    print("Name must be at least 3 characters ")
elif len(name) > 50:
    print("Name must be less than 50 characters")

else:
    print("Great")

