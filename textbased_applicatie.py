# Antwoorden
from os import P_OVERLAY
import time
A = ["A", "a"]
B = ["B", "b"]

def intro():
    print("You are Arne. your mom told you to go the supermarket,  because they ran out of bread. You are at the supermarket. Do you want cornbread or white bread.")
    print("")
    een()


def een():
    print("You are at the supermarket. Do you want cornbread or white bread?")
    print("A: cornbread")
    print("B: whitebread")
    vraag = input(">>> ")
    if vraag in A:
        twee()
    if vraag in B:
        twee()
    else:
        print("ik begrijp je niet")
        een()

def twee():
    print("you got the bread you wanted and after paying you go outside. You are outside it’s dark there’s a faint light in the distance. ")
    time.sleep(3)
    print("You are crossing the street, your looking forward. The light in the distance is growing closer to you but you’re not noticing")
    time.sleep(3)
    print("Its coming closer and closer. It’s not stopping. Closer and closer. Brighter and brighter.")
    time.sleep(3)
    print("")
    time.sleep(3)
    print("And then its complete dark, there’s nothing. Suddenly its cold. Your eyes are closed.")
    time.sleep(3)
    print("When you open them you’re in a cave. Next to you is your bread.")
    time.sleep(3)
    print("You look at the bread for a second. But then you see a light coming from a distance. What do you do?")
    time.sleep(1)
    print("A: eat your bread.")
    print("B: go to the light.")
    vraag = input(">>> ")
    if vraag in A:
        drie()
    if vraag in B:
        vier()


def drie():
    print("you’re eating the bread. It doesn’t have a taste, you eat more still nothing")
    time.sleep(3)
    print("You don’t even feel the bread in your mouth. Something’s wrong.")
    time.sleep(3)
    print("You start to question were you are. Than that light in the distance changes.")
    time.sleep(3)
    print("You see a silhouette. It looks human but smaller and with a big head. The silhouette leaves.")
    time.sleep(3)
    print("You decide to follow it. You leave the cave. When you’re outside you the creature whose silhouette you just saw.")
    time.sleep(3)
    print("It looks aggressive. It comes at you ready to attack. What do you do?")
    time.sleep(3)
    print("A: run away from the creature. ")
    print("B: attack the creature ")
    vraag = input(">>> ")
    if vraag in A:
        vijf()
    if vraag in B: 
        zes()



    

def vier():
    print("you follow the light. It directs you to the outside. You see a small humanoid creature.")
    time.sleep(3)
    print(". It emits a mean aura. Suddenly it starts sprinting at you. With his fists balled. What do you do?")
    time.sleep(3)
    print("A: run away from the creature.")
    print("B: attack the creature.")
    vraag = input(">>> ")
    if vraag in A:
        vijf()
    if vraag in B:
        zes()
    

def vijf():
    print("you start to run away . into the woods.")
    time.sleep(3)
    print("he creature is slow and can’t keep up. You go deeper into the woods.")
    time.sleep(3)
    print("You run till your legs if out. Now very dead into the forest you rest agents a tree.")
    time.sleep(3)
    print("You fall asleep.")
    time.sleep(4)
    print("When you wake up there’s a women Infront of you with a bow pointed at your face. When you wake more up you see that she’s an elf.")
    time.sleep(3)
    print("You stand but up your hands and your arms are tight with a rope.")
    time.sleep(3)
    print("You look behind you and there’s another elf. They start dragging you somewhere.")
    time.sleep(3)
    print("what do you do?")
    time.sleep(3)
    print("A. resist your capturing.")
    print("B. do nothing and let them take you.")
    vraag = input(">>> ")
    if vraag in A:
        zeven()
    if vraag in B:
        ending1()

        
    

    

def zes():
    print("you start to charge back at the creature. You and the creature fight.")
    time.sleep(3)
    print("He’s strong his fist feel like sandpaper. But you’re not that weak either.")
    time.sleep(3)
    print("After a while of fighting, you and the creature stop. Both of you collapse on the ground.")
    time.sleep(3)
    print("The creature starts talking, it says that it sorry. And just didn’t understand what you wanted.")
    time.sleep(3)
    print("You say that it’s alright. You ask where you are? He says that you’re in in the great forest of Madlo.")
    time.sleep(3)
    print("He says excuse me for I did not say who I am: my names is sir Leopold the third")
    time.sleep(3)
    print("You say that your name is Arne. Leopold than tells you that if you want you can come to their village.")
    time.sleep(3)
    print("And heal there until  from the fight. What do you do?")
    time.sleep(3)
    print("A. go with him to the village ")
    print("B. attack him again")
    vraag = input(">>> ")
    if vraag in A:
        acht()
    if vraag in B:
        ending2()



def zeven():
    print("after walking for a bit you and the elf’s stop. One of them blindfolds you.")
    time.sleep(3)
    print("You continue walking. After a while, you stop again.")
    time.sleep(3)
    print("They remove the blindfold. Infront of you is a prison cell.")
    time.sleep(3)
    print("You get thrown in. the elves leave and you’re alone.")
    time.sleep(3)
    print("Alone this is the first time you’re alone since the cave. You can finely think.")
    time.sleep(3)
    print("You start to question where you are. Why the elves captured you? ")
    time.sleep(3)
    print("What that light was at the store. Before you can think of answers a new elf walks Infront of your cell.")
    time.sleep(3)
    print("This elf looks older than the elves that captured you. He’s older than the elves that captured you.")
    time.sleep(3)
    print("He starts talking to you. he sounds mad, you can’t understand him, he speaks a different langue")
    time.sleep(3)
    print("What will you do?")
    print("A. remain silent")
    print("B. try to comminate")


def acht():
    print("a")

def ending1():
    print("tijdelijk")

def ending2():
    print("tijdelijk")




intro()