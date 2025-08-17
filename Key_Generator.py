import secrets

passwords = {}

while True:
    print("Welcome to the Password Generator")
    print("1 - Generate Password")
    print("2 - Delete Password")
    print("3 - List Passwords")
    print("4 - Quit")

    option = int(input("Choose an option: "))

    # Generate Password
    if option == 1:
        lenght = int(input("Number of characters: "))
        name = input("Name: ").strip()
        password = (secrets.token_urlsafe(lenght)).strip()

        if lenght == 0 or name == "":
            print("⚠️ Empty field! Name is required and password cannot be 0 characters long.")
        elif name in passwords:
            print("⚠️ A password with that name already exists.")
        else:
            passwords[name] = password
            print("Passaword and Name Saved")
            print(passwords)

    # Delete Password
    elif option == 2:
        name = input("Enter the name of the password you want to delete: ").strip()
        if name in passwords:
            del passwords[name]
            print("✅ Password deleted successfully!")
            print(passwords)
        else:
            print("⚠️ Password name does not exist.")
    
    # List Passwords
    elif option == 3:
        if len(passwords) == 0:
            print("⚠️ Empty password list")
        else:
            print("\n📒 Saved Passwords:")
            for name, password in passwords.items():
                print(f"Name: {name} | Password: {password}")

    # Quit
    elif option == 4:
        print("👋Exiting the Password Generator...")
        break

    else:
        print("❌Invalid Option")