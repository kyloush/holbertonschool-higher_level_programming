#!/usr/bin/python3
lower_case = "".join(chr(i) for i in range(97, 123))
upper_case = "".join(chr(i) for i in range(65, 91))
digits = "".join(chr(i) for i in range(48, 57))
space = "".join(chr(i) for i in range(33))
while True:
    usernumber = input("Enter an ASCII number(exit to quit): ")
    if usernumber == "exit":
        break
    for letters in usernumber:
        if letters in lower_case:
            print(f"{letters} is lower case")
        elif letters in upper_case:
            print(f"{letters} is upper case")
        elif letters in digits:
            print(f"{letters} is a digit")
        elif letters in space:
            print(f"{letters} is a space")
        else:
            print(f"{letters}  ...SEROIUSLY, wtf is that. do you think i'm french")