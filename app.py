print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

turn = input("Where will you like to go, left 'L' or right 'R'? ")
if turn == "L":
    print("You are at  a cross road, you need to do something fast")
    act = input("what quick step will you take, 'swim' or 'wait'? ")
    if act == "wait":
        print("You did the right thing! up next ")
        door = input("What is your choice door color: 'Red', 'Blue', 'Yellow'? ")
        if door == "Yellow":
            print("You are at the right door")
            print("You Won!")
        elif door == "Blue":
            print("You are eaten by bests. Game Over")
        elif door == "Red":
            print("You are burned by a fire. Game Over")
        else:
            print("You door color is wrong! game over")
    else:
        print("You got attacked by an angry tout. Game Over")
else:
    print("Game Over!")