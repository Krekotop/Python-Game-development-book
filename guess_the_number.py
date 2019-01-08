# -*- coding: utf-8 -*-
"""
Created on Wed Jan  2 19:05:33 2019

@author: User
"""
import random


def ask_number(question,low, high):
    response = None
    while response not in range(low, high):
        response = int(input(question))
        
    return response
def main():
    rand_num = random.randint(0,100)
    while True:
        number = ask_number("Hey man what's ur number?\n",0,100)
        if number == rand_num:
            print("you're right")
            break
        elif number > rand_num:
            print("your number is higher than guessed one")
        elif number < rand_num:
            print("your number is lower than guessed one")
main()
input("\n\n Press Enter to exit")