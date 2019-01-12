# -*- coding: utf-8 -*-
"""
Created on Sat Jan 12 13:12:54 2019

@author: User
"""

class TV:
    
    def __init__(self, channel = 0, volume = 0):
        self.channel = channel
        self.volume = volume
    def change_channel(self):
        while True:
            try:
                channel = int(input("Channel number: "))
                break
            except ValueError:
                print("Please enter a number (1-4)")
        if channel == 1:
            print("BBC One.")
        elif channel == 2:
            print("BBC Two.")
        elif channel == 3:
            print("ITV.")
        elif channel == 4:
            print("Channel 4.")
        else:
            print("Out of Range.")
    def adjust(self):
        amount = int(input("By how much should I adjust the volume?"))
        self.volume += amount
        if self.volume < 0:
            self.volume = 0
        print("The volume now is:", self.volume)
def main():
    lg = TV()
    choice = None  
    while choice != "0":
        print \
        ("""
        Television
    
        0 - Quit
        1 - Turn the channel
        2 - Adjust the volume 

        """)
    
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")


        elif choice == "1":
            lg.change_channel()       
        elif choice == "2":
            lg.adjust()
        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.") 
