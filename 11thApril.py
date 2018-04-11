# If else statement(Conditional statement)
check = True

if check == False:
    print("It is False")
elif check == "not mentioned":
    print("It is not mentioned")
elif check == "Mentioned":
    print("It is Mentioned")
else:
    print("It is True")

# For/while Loops

#For loop

Numbers = ["first","Second","Third",4,5]
for items in Numbers:
    print(items)

# While Loop
run = True
items = 1

while run:
  if items == 10:
    run =False
  else:
    print(items)
    items += 1



# Import libraries into scripts


import re
string = "I AM HAPPY PERSON,/ if everyone is happy: "
print(string)
new = re.sub('[A-Z]', '', string)
print(new)
new = re.sub('[a-z]', '', string)
print(new)
new = re.sub('[,/:]', '', string)
print(new)
new = re.sub('[A-Za-z,/:]', '', string)
print(new)
new = re.sub('[A-Z,/:+" "]', '', string)
print(new)

string = string + "6 365-98"
print(string)
new = re.sub('[^0-9]', '', string)
print(new)



# Breaking out of while loop
import random


playerhp = 260
enemytkl = 60
enemytkh = 80

while playerhp > 0:
    dmg = random.randrange(enemytkl, enemytkh)
    print("The value", dmg)
    playerhp = playerhp - dmg

    if playerhp <= 30:
       playerhp = 30

    print("Enemy strikes for", dmg, "Current HP is", playerhp)

    if playerhp > 30:
       continue

    print("You have low health")
    break


# Classes & Objects


class Enemy:
       attacklaw = 60
       attackhgh = 80

       def getattack(self):
           print(self.attacklaw)

       def getattack1(self):
           print(self.attackhgh)


enemy1 = Enemy()
enemy1.getattack()

enemy2 = Enemy()
enemy2.getattack1()


