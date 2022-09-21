""" Write a program that asks the answer for a mathematical
            expression, checks whether the user is right or wrong, and then
            responds with a message accordingly."""
print(" Hi!\n I have several mathematical expression.")
ready = input('If you ready ask the answer enter "ok":')

while ready == 'ok':

    print("Скільки буде 5х5?")
    res1 = input("Відповідь: ")
    if int(res1) == 25:
        print("Вірно")
    else:
        print("Ні, правильна відповідь 25")

    print("Скільки буде корінь з 36?")
    res2 = input("Відповідь: ")
    if int(res2) == 6:
        print("Вірно")
        break
    else:
        print("Ні, правильна відповідь 6")
        break
