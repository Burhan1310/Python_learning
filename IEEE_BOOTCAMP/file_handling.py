# Write Mode
with open("example2.txt", 'w') as file:
    file.write("Hello guys whats up")
    # content = file.read()
    # print(content)

with open("example3.txt", 'w+') as newfile:
    newfile.write("Burhan\nJubaer\nJulfi")
    newtxt = newfile.read()
    print(newtxt)

with open('example3.txt', 'a') as newfile2:
    newfile2.write('Islamic University')

with open('example.txt', 'r+') as newfile3:
    newfile3.seek(10)
    newtxt2 = newfile3.read()
    print(newtxt2)

# Read mode 'r'
file = open('example.txt', 'r')
content1 = file.readline()
content2 = file.readline()
print(content1)
print(content2)
# content = file.read()
# print(content)
content3 = file.readlines()
print(content3)
file.close()

# Append mode
with open('example.txt', 'a+') as file2:
    file2.write('\nAppending something')
    content4 = file2.read()
    print(content4)
    file2.seek(0)

# Exclusive Creation mode

