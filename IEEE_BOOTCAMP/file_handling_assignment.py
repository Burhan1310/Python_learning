# Exercise 1: 'w+' ModeTasks:
with open('exercise_w.txt', 'w+') as file:
    file.write('Hey, this is Burhan!\nI am a passionate individual eager to learn and explore new '
               'technologies.\nThank You!')
    file.seek(0)
    content = file.read()
    print(content)

with open('exercise_w.txt', 'a+') as file2:
    file2.write('\nMy aim is to contribute positively to the field of technology.')
    file2.seek(0)
    content2 = file2.read()
    print(content2)

# Exercise 2: 'r+' ModeTasks:
with open('exercise_r.txt', 'w') as file3:
    file3.write('Hello there this is a new txt file!'
                'here we do some operations!')

with open('exercise_r.txt', 'r+') as file4:
    content3 = file4.read(10)
    print(content3)
    file4.seek(0)
    file4.write("Task 4: Overwrite the existing content with this line.")
    file4.seek(0)
    content4 = file4.read()
    print(content4)

# Exercise 3: 'a+' ModeTasks:
with open('exercise_a.txt', 'w') as file5:
    file5.write('Hello python learners!'
                '\nWhats up to you guys!')

with open('exercise_a.txt', 'a+') as file6:
    file6.seek(0)
    content5 = file6.read()
    print(content5)
    content6 = file6.write("\nTask 3: Append this line to the end of the file.")
    file6.seek(0, 2)
    file6.seek(file6.tell() // 2)  # Move to the middle
    file6.write(" Task 5: Overwrite the existing content with this line.")
    file6.seek(0)
    content7 = file6.read()
    print(content7)

