# -*- coding: utf-8 -*-
"""
Created on Thu Jan 10 23:54:48 2019

@author: User
"""
import sys
def open_file(file_name,mode):
    try:
        the_file = open(file_name, mode, encoding = 'utf-8')
    except IOError as e:
        print("Can't open the file")
        input("\nPress enter to exit")
        sys.exit()
    else:
        return the_file
def next_line(the_file):
    line = the_file.readline()
    return line
def next_block(the_file):
    category = next_line(the_file)
    question = next_line(the_file)
    answers= []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    nominal = int(next_line(the_file))
    return category, question, answers, correct, explanation, nominal
def welcome(title):
    print("\t\twelcome to the game 'Quiz'!")
    print("\t\t",title,"\n")
def main():
    trivia_file = open_file("questions.txt","r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    
    category, question, answers, correct, explanation, nominal = next_block(trivia_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print("\t", i+1, "-", answers[i])
        answer = input("Your answer:\n")
        if answer == correct:
            print("\nYou are right!", end = " ")
            score = score + nominal
        else:
            print("no", end = " ")
        print(explanation)
        print("Score:", score, "\n\n")
        category, question, answers, correct, explanation, nominal = next_block(trivia_file)
    trivia_file.close()
    print("it was the last question! Your score is:", score)
main()
input("press enter to exit")
