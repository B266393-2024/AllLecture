#!/usr/bin/python3

def getinfor():
    infor = {}
    infor['name'] = input("What's your name? ")
    infor['age'] = input("How old are you? ")
    infor['colour'] = input("What is your favourite colour? ")
    infor['python'] = input("Do you like Python? ")
    infor['world'] = input("The world is flat: True or False? ")
    
    print(f"Your name is {infor['name']}. Nice to meet you!")
    print(f"Your age is {infor['age']}. It is the best age!")
    print(f"Your favourite colour is {infor['colour']}. Nice taste!")
    print(f"DO you like python? {infor['python']}. Run!")
    print(f"You think the flat world is {infor['world']}. Exactly!")
    
getinfor()

    