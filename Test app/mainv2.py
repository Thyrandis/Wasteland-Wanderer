import time
import os
from slowprint.slowprint import *
import random


pHealthPoints = 100
pAttack = 10
pLuck = 5
pMedPack = 1

eHealthPoints = 100
eAttack = 15

bHealthPoints = 250
bAttack = 25
bSpecial = 35
bEnergy = 0


class Player():
      
    def __init__(self, sName, sLuck, sAttack, sHp):
        self.name = sName
        self.luck = sLuck
        self.attack = sAttack
        self.health = sHp

    def getLuck(self):
        return self.luck
    
    def getHealth(self):
        return self.health
    
    def getAttack(self):
        return self.attack
    
    def setAttack(self, newAttack):
        self.attack = newAttack
    
    def setLuck(self, newLuck):
        self.luck = newLuck
    
    def setHp(self, newHp):
        self.health = newHp

         
    

class Loot():
    def loot(luck):
        global pLuck, pAttack, pMedPack
        lootChance = random.randint(0,4)
        if luck < lootChance:
            slowprint(f"You found nothing of value.", 0.5)

        else:
            tableNum = random.randint(0, 2 )
            lootTableList = ["attack", "luck", "items"]
            itemType = lootTableList[tableNum]
            file = open(itemType+".txt", "r")
            lines = file.readlines()

            slowprint(f"You have found....", 0.5)

            item = random.randint(0,len(lines)-1)

            itemLine = lines[item]
            splitItemLine = itemLine.split(",")

            name = splitItemLine[0]
            value = int(splitItemLine[1])
        
            slowprint(name, 0.5)

            if itemType == "attack":
                pAttack = pAttack + value
                slowprint(f"Your new attack is {pAttack}", 0.5)
            
            if itemType == "items":
                pMedPack = pMedPack + value
                slowprint(f"You now have {pMedPack} medpacks", 0.5)

            if itemType == "luck":
                pLuck = value + pLuck
                slowprint(f"Your new luck skill is {pLuck}", 0.5)

class Enemies():
    def __init__(self, name, ehealth, eattack):
        self.health = ehealth
        self.attack = eattack
        self.name = name

    def gethealth(self):
        return self.health
    
    def getattack(self):
        return self.attack

    def sethealth(self, newHealth):
        self.health = newHealth
        
    def setattack(self, newAttack):
        self.attack = newAttack

class Combat():
    def playerAttack(self):
        pDmg = random.randint(0, pAttack)
        eHealthPoints = eHealthPoints - pDmg
        
    def playerHeal(self):
        pHeal = random.randint(5, 20)
        pHealthPoints = pHealthPoints + pHeal

    def enemyAttack(self):
        eDmg = random.randint(0, eAttack)
        pHealthPoints = pHealthPoints - eDmg
    
    def bossAttack(self):
        global bEnergy
        bDmg = random.randint(0, bAttack)
        pHealthPoints = pHealthPoints - bDmg
        bEnergy += 10
    def bossSpecial(self):
        bSpec = random.randint(10, bSpecial)
        pHealthPoints = pHealthPoints - bSpec



        


print(" ________________________________")
print("|                                |")
print("|<<< The Wasteland Wanderer >>>  |") 
print("|           <<< By >>>           |")
print("|________________________________|") 

time.sleep(4)
slowprint(f"\n\nWelcome to 'The Wasteland Wanderer'", 0.5)
time.sleep(1)
slowprint(f"Would you like to begin?: ", 0.5)
begin = input(f"Y/N: ")

if begin == 'Y':
    time.sleep(2)
    #--------- back story here ---------#

    slowprint("\nYou wake up....", 0.5)
    time.sleep(1)
    slowprint("Cold, hungry and alone.", 0.5)
    time.sleep(2)
    slowprint("You look around, the world is desolate. Scorched with no signs of life. You find your backpack next to you on the ground.", 0.5)
    time.sleep(2)
    slowprint("'What happened to me? where did everybody go? who am I?....'", 0.5)
    time.sleep(4)
    slowprint("You clamor up onto your feet, in pain and confused. You stop for a moment and try to remeber who you are.", 0.5)
    time.sleep(2)
    slowprint("...", 1)
    time.sleep(2)
    slowprint("....", 1)
    time.sleep(2)
    print("!!!")
    time.sleep(2)
    slowprint("Thats right I'm...", 0.5)
    time.sleep(0.5)
    name = input(f"My name is: ")
    age = input(f"I am how old: ")
    race = input(f"My country of birth: ")
    time.sleep(0.5)
    slowprint(f"Oh i remeber, my name is {name}, I am {age} years old and I come from {race}.", 0.5)
    time.sleep(1)
    slowprint(f"Confusion hits you harder, how did you end up here? what is this place? You have so many questions and very little answers....", 0.5)
    time.sleep(1)
    slowprint(f"A pain, like no pain you have ever felt before cripples your thoughts in their tracks.", 0.5)
    time.sleep(1)
    slowprint(f"You look down to see your blood stained shirt.", 0.5)
    time.sleep(1)
    slowprint(f"You lift your shirt to see a deep laceration to your body.", 0.5)
    time.sleep(1)
    slowprint(f"From your assessment you see it is not life threatening.", 0.5)
    time.sleep(2)
    slowprint(f"Remebering your backpack on the ground, you winse in pain as you lean over and pick it up.", 0.5)
    time.sleep(1)
    slowprint(f"You open your backpack to find a medkit, a map and a multi-tool.", 0.5)
    time.sleep(1)
    slowprint(f"Faced with a choice, you can use your medkit and tend to your wound(Use 1 medkit 'current medkits {pMedPack}').\nOr you can use your shirt and craft a make shift bandage.(Keep your medkit, and lose 20 hitpoints)", 0.5)
    time.sleep(1)
    slowprint(f"You have no idea what lies ahead, what will you do?", 0.5)
    time.sleep(3)
    slowprint(f"1) Use medkit.\n2) Save the medkit and loose 20hp.", 0.5)
    choice1 = input("Your choice: ")
    time.sleep(1)

if choice1 == '1':
    Player.med_pack -= 1
    slowprint(f"You take out your medkit, disinfecting your wound and applying a dressing. (- 1 medkit 'medkits remaining {pMedPack}')", 0.5)
    time.sleep(1)
if choice1 == '2':
    Player.health_points -= 20
    slowprint(f"You take off your first, using the multi-tool from your backpack you craft a makeshift bandage and apply the dressing. (-20hp 'Hp remaining {pHealthPoints}')", 0.5)
    time.sleep(1)

slowprint(f"Now that you have tended to your wound, and feel more comfortable. You pull out your map.", 0.5)
time.sleep(1)
slowprint(f"You vaugle remeber you was on your way to visit a friend. But what happend?", 0.5)
time.sleep(1)
slowprint(f"The world around you is in ruin, not a soul in sight. You can see you are stood on the outskirts of forest or woodland.", 0.5)
time.sleep(1)
slowprint(f"and can see a road leading towards a town. What should you do?", 0.5)
time.sleep(1)
slowprint(f"Do you prioritize heading towards the town to find out what has happened? and look for supplies?", 0.5)
time.sleep(1)
slowprint(f"Or do you head into the woods, set up a lean-to and wait, assessing the situation and your surounding further.", 0.5)



    # -------------------- LOOK AT CHANGING IF STATEMENTS TO WHILE LOOPS ----------------------#
    #--------------------- LOOK AT LISTS AND DICT's -------------------------------------------#
    # --------------------- REMEMBER THAT PYTHON STARTS AT 0 NOT 1 ----------------------------#
    #-------------------------referece https://www.youtube.com/watch?v=RNsWIS6vGH8 ------------#