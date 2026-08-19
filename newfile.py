while True:
    print("\n====================")
    print("   Welcome to 3m    ")
    print("====================")
    print("1. Kevin")
    print("2. Irene")
    print("3. Exit")

    child = input("Choose 1, 2, or 3: ")

    if child == "3":
        print("Goodbye!")
        break

    if child == "1":
        print("\nHello Kevin! Choose a game:")
        print("1. Math: 2 + 3 = ?")
        print("2. Bible: Who built the Ark?")
        choice = input("Enter 1 or 2: ")
        
        if choice == "1":
            ans = input("Your answer: ")
            if ans == "5":
                print("Bravo Kevin! Correct! 🎉")
            else:
                print("Try again next time! 👍")
        elif choice == "2":
            ans = input("Your answer: ")
            if ans.lower() == "noah":
                print("Bravo Kevin! Correct! 🎉")
            else:
                print("The correct answer is Noah! ⛵")

    elif child == "2":
        print("\nHello Irene! Choose a game:")
        print("1. Math: 5 - 2 = ?")
        print("2. Bible: Who built the Ark?")
        choice = input("Enter 1 or 2: ")
        
        if choice == "1":
            ans = input("Your answer: ")
            if ans == "3":
                print("Bravo Irene! Correct! 🎉")
            else:
                print("Try again next time! 👍")
        elif choice == "2":
            ans = input("Your answer: ")
            if ans.lower() == "noah":
                print("Bravo Irene! Correct! 🎉")
            else:
                print("The correct answer is Noah! ⛵")