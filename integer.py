#!/usr/bin/env python3

# Created by: Sarah
# Created on: Mar 31, 2022
# This program asks the user to enter an interger. It then
# checks to see if the number entered is positive, negative, or just zero.


def main():
    # get number entered from user
    user_number = int(input("Enter an integer: "))
    print("")

    # check if the number user entered is positive, negative, or zero
    if user_number > 0:
        print(user_number, "is a positive number")
    elif user_number < 0:
        print(user_number, "is a negative number")
    elif user_number == 0:
        print(user_number, "is just zero")


if __name__ == "__main__":
    main()
