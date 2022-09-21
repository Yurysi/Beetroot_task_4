"""The name check.

            Write a program that has a variable with your name stored
            (in lowercase) and then asks for your name as input. The program
            should check if your input is equal to the stored name even if the
            given name has another case, e.g., if your input is “Anton” and the
            stored name is “anton”, it should return True."""
users_name = None
name = ''
while name != 'q':
    name = input(" Enter your name\n(Enter 'q' "
                 "when you are finished.): ")
    if name == users_name:
        print(True)

    elif name.lower() == users_name:
        print(True)
    else:
        if users_name == None:
            if name != name.lower():
                users_name = name.lower()
                print(f"I saved your name, {users_name}")
            elif name == 'q':
                print(f"Bye, {users_name}")
            else:
                users_name = name
                print(f"I saved name, {users_name}")
        else:
            print(False)

    print()