import random
import time
import os
from slowprint.slowprint import *


class player_spec:
  strength = 0
  agility = 0
  health_points = 0
  rs = 0
  ms = 0
  charisma = 0
  ah = 0

# -------------- Berserker class ---------------#
bb_s = 8
bb_a = 3
bb_hp = 8
bb_rs = 1
bb_ms = 8
bb_c = 5
bb_ah = 2

#--------------- Sniper Class -----------------#

sn_s = 2
sn_a = 8
sn_hp = 5
sn_rs = 8
sn_ms = 2
sn_c = 7
sn_ah = 3

#-------------- Scientist Class ---------------#

s_s = 4
s_a = 4
s_hp = 8
s_rs = 4
s_ms = 2
s_c = 9
s_ah = 4

#-------------- Animal Handeler ----------------#

ah_s = 4
ah_a = 3
ah_hp = 8
ah_rs = 1
ah_ms = 5
ah_c = 6
ah_ah = 8
class start():

    print(" ________________________________")
    print("|                                |")
    print("|<<< The Wasteland Wanderer >>>  |") 
    print("|           <<< By >>>           |")
    print("|       <<< Adam Senior >>>>     |") 
    print("|                                |") 
    print("|________________________________|") 

    time.sleep(4)
    slowprint(f"\n\nWelcome to 'The Wasteland Wanderer'.", 0.5)
    time.sleep(1)
    slowprint(f"Would you like to begin?: ", 0.5)
    begin = input(f"Y/N: ")

    if begin == 'Y':
        time.sleep(2)
#-------- Insert Back story here --------#
        slowprint("\nYou wake up....", 0.5)
        time.sleep(1)
        slowprint("Cold, hungry and alone.", 0.5)
        time.sleep(2)
        slowprint("You look around, the world is desolate. Scorched with no signs of life.", 0.5)
        time.sleep(2)
        slowprint("'What happened to me? where did everybody go? who am I?....'", 0.5)
        time.sleep(2)
        slowprint("You get up onto your feet, and try to remeber who you are.", 0.5)
        time.sleep(2)
        slowprint("...", 1)
        time.sleep(2)
        slowprint("....", 1)
        time.sleep(2)
        print("!!!")
        time.sleep(2)
        slowprint("Thats right im...", 0.5)
        time.sleep(0.5)
        name = input(f"My name is: ")
        age = input(f"I am how old: ")
        race = input(f"My country of birth: ")
        time.sleep(0.5)
        slowprint(f"Oh i remeber, my name is {name}, I am {age} years old and I come from {race}.", 0.5)
        time.sleep(1)
        slowprint(f"What type of character am I? \n\n1) Berserker \n2) Sniper \n3) Scientist \n4) Animal handler \n5) See stats", 0.5)
    
    choose_class = input(f"Choose: ")

    if choose_class == '1':
        slowprint(f"So you have chosen the Berskerer is that right?: \n", 0.5)
        bb = input(f"Yes/No: ")
    elif choose_class == '2':
        slowprint(f"So you have chosen the Sniper is that right?: \n", 0.5)
        sn = input(f"Yes/No: ")
    elif choose_class == '3':
        slowprint(f"So you have chosen the Scientist is that right?: \n", 0.5)
        s = input(f"Yes/No: ")
    elif choose_class == '4':
        slowprint(f"So you have chosen the Animal handeler is that right?: \n")
        ah = input(f"Yes/No: ")
    elif choose_class == '5':
        slowprint(f"\nThe Berserker: \n\n  Strength:{bb_s}\n  Agility:{bb_a}\n  HP:{bb_hp}\n  Ranged skill:{bb_rs}\n  Melee skill:{bb_ms}\n  Crafting:{bb_c}\n  Animal Handeling:{bb_ah}", 0.5)
        time.sleep(1)
        slowprint(f"\nThe Sniper: \n\n  Strength:{sn_s}\n  Agility:{sn_a}\n  HP:{sn_hp}\n  Ranged skill:{sn_rs}\n  Melee skill:{sn_ms}\n  Crafting:{sn_c}\n  Animal Handeling:{sn_ah}", 0.5)
        time.sleep(1)
        slowprint(f"\nThe Scientist: \n\n  Strength:{s_s}\n  Agility:{s_a}\n  HP:{s_hp}\n  Ranged skill:{s_rs}\n  Melee skill:{s_ms}\n  Crafting:{s_c}\n  Animal Handeling:{s_ah}", 0.5)
        time.sleep(1)
        slowprint(f"\nThe Animal Handler: \n\n  Strength:{ah_s}\n  Agility:{ah_a}\n  HP:{ah_hp}\n  Ranged skill:{ah_rs}\n  Melee skill:{ah_ms}\n  Crafting:{ah_c}\n  Animal Handeling:{ah_ah}\n\n", 0.5)
        time.sleep(3)
    
class choice():
    def start(self):
        slowprint(f"What type of character am I? \n\n1) Berserker \n2) Sniper \n3) Scientist \n4) Animal handler \n", 0.5)

    choose_class2 = input(f"Choose: ")

    
print(f"You have chosen")
        
      





