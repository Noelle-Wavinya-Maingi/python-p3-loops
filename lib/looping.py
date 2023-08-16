#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print("Happy New Year!")
    

def square_integers(int_list):
    # code goes here!
    squared_list = [integer ** 2 for integer in int_list]
    return squared_list

def fizzbuzz():
    # code goes here!
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 != 0:
            print("Fizz")
        elif num % 5 == 0 and num % 3 != 0:
            print("Buzz")
        elif num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        else:
            print(num)

happy_new_year()
square_integers([12, 123, 23, 36])
fizzbuzz()