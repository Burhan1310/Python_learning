command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started ")
        else:
            started = True
            print("Car Started....")
    elif command == "stop":
        if not started:
            print("Car is already stopped..")
        else:
            started = False
            print("Car Stopped....")
    elif command == "help":
        print('''
    start - To start the car
    stop - To stop the car
    quit - To exit the game
        ''')
    elif command == "quit":
        print("Game ended...")
        break
    else:
        print("Sorry, I don't understand that")