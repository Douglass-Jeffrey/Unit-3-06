#!/usr/bin/env python3

# Created by: Douglass Jeffrey
# Created on: Oct 2019
# This program plays a number generation game


import random


def main():
    # this function checks user inputted number is the same as the computers
    # secret number

    random_number = random.randint(1, 3)

    # process
    try:
        # input
        user_number = int(input("Enter your number: "))
        print("")

    # Output
        if user_number == random_number:
            print("You got the answer right!!!")
        else:
            print("You got the answer wrong, try again.")
    except Exception:
        print("Please input an integer number")


if __name__ == "__main__":
    main()
