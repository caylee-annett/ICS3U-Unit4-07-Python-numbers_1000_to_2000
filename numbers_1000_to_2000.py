#!/usr/bin/env python3

# Created by: Caylee Annett
# Created on: May 2021
# This program prints the numbers 1000 to 2000 with five integers per line


def main():
    # This function prints the numbers

    # Process & Output
    print("This program prints the integers from 1000 to 2000.")
    print("")
    for loop_counter in range(1000, 2000 + 1):
        if loop_counter % 5 == 4:
            print("{} ".format(loop_counter))
        else:
            print("{} ".format(loop_counter), end="")
    print("")
    print("\nDone.")


if __name__ == "__main__":
    main()
