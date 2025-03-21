print("\033[33mBot: Welcome User! To Python Calculator!")
print("Bot: Would you like to pick a name instead of 'User'?")

# var check momento
username_input = []
ans = []

# what de fuk is your name
while True:
    answer_1 = input("You: ").lower()
    if answer_1 in ("of course", "yes", "okay", "sure", "ok"):
        username = input("Username: ")
        username_input.append(username)
        break
    elif answer_1 in ("no", "nah"):
        username_input.append("User") 
        break
    else:
        print("I can't understand it!")

# loop code
while True:
    print("\033[33mBot: What type of math do you need?")
    print("1. Plus (+)")
    print("2. Minus (-)")
    print("3. Multiply (x)")
    print("4. Division (/)")
    print("5. Setting (setting)")
    print("6. Exit (exit)")

    answer_2 = input(f"{username_input[0]}: ").strip().lower()

    # choose pls
    if answer_2 in ("+", "-", "x", "/"):
        print("Bot: Okay! Let's calculate.")

        while True:
            try:
                first_number = float(input("First Number: "))
                second_number = float(input("Second Number: "))

                if answer_2 == "+":
                    result = first_number + second_number
                elif answer_2 == "-":
                    result = first_number - second_number
                elif answer_2 == "x":
                    result = first_number * second_number
                elif answer_2 == "/":
                    if second_number == 0:
                        print("Bot: Cannot divide by zero!")
                        continue 
                    result = first_number / second_number

                print(f"Bot: The answer is {result}")
                ans.append(result) 
                break
            except ValueError:
                print("Bot: Please enter a valid number!")

    elif answer_2 == "setting":
        while True:
            print("\nBot: Settings")
            print("1. See the previous answer ('back')")
            print("2. Return to menu ('menu')")

            answer_setting = input(f"{username_input[0]}: ").strip().lower()

            if answer_setting == "back":
                if ans:
                    print(f"Bot: Previous answer is {ans[-1]}")
                else:
                    print("Bot: No previous answer found!")
            elif answer_setting == "menu":
                break
            else:
                print("Bot: I can't understand!")

    elif answer_2 == "exit":
        print("Bot: Goodbye!")
        break

    else:
        print("Bot: I can't understand! Please enter a valid option.")
