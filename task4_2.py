"""
    Task 2

    The valid phone number program.

    Make a program that checks if a string is in the right format for a
    phone
    number. The program should check that the string contains only
    numerical characters and is only 10 characters long. Print a suitable
    message depending on the outcome of the string evaluation."""

phone_number = " "
while phone_number != 'q':

    phone_number = input(
        "Please enter your phone number.\n(Enter 'q' "
        "when you are finished.): ")
    print()
    if phone_number.isdigit():
        if len(phone_number) == 10:
            print(f"Your phone number {phone_number} is saved")
        elif len(phone_number) <= 10:
            print(
                "Your phone number is short. Please enter 10 "
                "digits.")
        else:
            print("Your phone number is  very long. Please "
                  "enter 10 digits.")

    elif phone_number == 'q':
        print("Have a nice day!")
    else:
        print("You must input integer.")
