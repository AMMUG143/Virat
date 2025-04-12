def login_page():
    print("Welcome to the login page!")
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if authenticate(username, password):
        print("Login successful!")
        # Proceed to the next step
    else:
        print("Invalid credentials. Please try again.")