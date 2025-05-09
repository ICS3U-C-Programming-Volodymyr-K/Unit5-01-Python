#!/usr/bin/env python3
# Created By: Volodymyr Kryzhanovskyi
# Date: 05, 5, 2025
# This program calculates fahrenheits.


def fahrenheit_calc():  # Defining function called fahrenheit_calc
    celsius = input("Enter the degrees in celsius.")  # Getting user input for celsius
    try:
        celsius = float(celsius)  # Catching any potential incorrect input
        fahrenheit = (
            9 / 5
        ) * celsius + 32  # Calculating fahrenheit degrees based on user input
        fahrenheit = round(
            fahrenheit, 2
        )  # Rounding the final value in order to make it look better
        print(
            f"Your degrees in fahrenheit are: {fahrenheit}"
        )  # Displaying degrees in fahrenheit
    except Exception:
        print(
            "Need a decimal as a value."
        )  # Prints of this statement when input is incorrect


def main():
    fahrenheit_calc()  # Calling the fahrenheit function


if __name__ == "__main__":
    main()
