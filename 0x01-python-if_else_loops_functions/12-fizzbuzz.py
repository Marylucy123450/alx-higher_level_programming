#!/usr/bin/python3

def fizzbuzz():
    # Loop from 1 to 100 (inclusive)
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            # For multiples of both 3 and 5, print "FizzBuzz"
            print("FizzBuzz", end=" ")
        elif i % 3 == 0:
            # For multiples of 3, print "Fizz"
            print("Fizz", end=" ")
        elif i % 5 == 0:
            # For multiples of 5, print "Buzz"
            print("Buzz", end=" ")
        else:
            # For other numbers, print the number
            print(i, end=" ")
