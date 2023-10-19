while True:
    try:
        user_input = int(input("Enter a number (or '0' to exit): "))

        if user_input == 0:
            print("Exiting the program. Goodbye!")
            break  # Exit the loop if the user inputs 0.

        if user_input % 2 == 0:
            print(f"{user_input} is even.")
        else:
            print(f"{user_input} is odd.")

    except ValueError:
        print("Invalid input. Please enter a valid number.")
