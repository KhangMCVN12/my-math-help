print("Hello user, how are you today?")
print("Welcome to my login section! Let's start by choosing a username.")

# Lists to store usernames and passwords
user_name = []
password = []

# Get user input for name
name = input("Your name you would like to pick: ")
user_name.append(name)
print(f"Your name '{name}' is cool!")

# Get user input for password
print("Next is password. What password do you want to add?")
password_input = input("Your password is: ")
password.append(password_input)

# Asking if user wants to check the password
print("Do you want to check the password?")
answer = input(f"{name}: ").lower()

if answer in ("yes", "of course", "sure", "ok", "okay"):
    print("Okay, let's check it out!")

    # Keep asking for the correct username
    while True:
        name_1 = input("Username: ")
        if name_1 in user_name:
            print("Correct! Now let's verify your password.")
            break  # Exit loop when username is correct
        else:
            print("Incorrect username! Try again.")

    # Keep asking for the correct password
    while True:
        pass_1 = input("Password: ")
        if pass_1 in password:
            print("Login successful! Welcome back!")
            break  # Exit loop when password is correct
        else:
            print("Incorrect password! Try again.")
