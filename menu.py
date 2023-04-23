def menu():
    while True:
        print("Options:")
        print("1. Road with miles")
        print("2. See road without miles")
        print("3. Enter path")
        print("4. Quit")
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            print("You chose Road with miles")
            # Do something related to Road with miles
        elif choice == "2":
            print("You chose See road without miles")
            # Do something related to See road without miles
        elif choice == "3":
            print("You chose Enter path")
            # Do something related to Enter path
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

