print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
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

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload
print("You're starting your journey. As a true pirate you sailed to the distanced island navigating by map left to you by notorious old pirate The Bearded Dutchman. Map leads you until you reach the crossroad with left and right turn. Any other marks are gone. To find the treasure you need to risk it. What would you do? \n")
question1=input("Do you want to go right or left?\n").lower()
#print(question1)
if question1!="left":
  print("\nYou are unlucky... You didn't choose left turn and went right in trap set by canibals living on the island. I hope you are a nice meal!\n")
elif question1=="left":
  print("\nYou came back to the shore. You can start swimming or wait for a boat to pick you up. What will you do? Swimm or wait?\n")
  question2=input("\nDo you want to go swim or wait?\n").lower()
  if question2!="wait":
    print("\nToo bad. You are attacked by sharks! GAME OVER!\n")
  else:
    question3=input("\nSo you decided to wait and there comes a boat that is carrying you in front of a hidden cave. You enter, but there are three doors inside. One of them hides treasure, but other two are death traps. Doors are colored in blue, yellow and red color. Which door will you choose? Red, blue or yellow? BE WARE!\n").lower()
    if question3=="red":
      print("\nYou open the red door but inside is a red dragon. He fires a huge fireball on you. You are burned and badly damaged. You can't continue your search. GAME OVER!\n")
    elif question3=="blue":
      print("\nBehind the doors are dozens of hungry beasts. They've been waiting for a next snack. Sorry! GAME OVER!\n")
    else:
      print("\nYou win! Behind the closed doors is a huge treasure that lights the room. You never ever have to work anything again! It is all yours! What are you waiting for! CONGRATS!\n")
