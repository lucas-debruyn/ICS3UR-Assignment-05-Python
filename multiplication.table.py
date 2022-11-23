#!/usr/bin/env python3

# Created by: Lucas DeBruyn
# Created on: Nov 2022
# This program uses nested loops to print all multiplication equations from 0 - 9


def main():
    # This program uses nested loops to print multiplication equations

    product = 0
    counter_one = -1
    counter_two = 0

    # input,process,output
    while counter_one < 9:
        counter_one = counter_one + 1
        counter_two = -1
        print("")
        while counter_two < 9:
            counter_two = counter_two + 1
            product = counter_one * counter_two
            print("{0} x {1} = {2}".format(counter_one, counter_two, product))

    print("\nDone.")


if __name__ == "__main__":
    main()
