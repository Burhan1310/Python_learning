import random

for i in range(3):
    print(random.random())

for a in range(3):
    print(random.randint(0, 100))

for b in range(5):
    print(f'hello {random.randrange(20)}')

members = ['Burhan', 'Ashik', 'Hemayet', 'Showon', 'Miad', 'A.Rouf']
Madafakah = random.choice(members)
print(Madafakah)

dice1 = random.randint(1,6)

dice2 = random.randint(1,6)
print('''
if we ROLE Two Dice
then,''')
print(f'({dice1}, {dice2})')

