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
        ending1()
    if vraag in B:
        zeven()

        
    

    

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
    vraag = input(">>> ")
    if vraag in A:
        elf()
    if vraag in B:
        twaalf()


def acht():
    print("you and Leopold start walking to his village. He said that it’s not far away.")
    time.sleep(3)
    print("After walking for a bit. You arrive at a wooden gate.")
    time.sleep(3)
    print("There a two guards at the gate Leopold ask if they can open the gate for us. One of them nots and pulls a lever.")
    time.sleep(3)
    print("The gate opens and you’re let inside. The village looks like something from the middle ages.")
    time.sleep(3)
    print("This makes you question even more were you are. There are people walking in the main street, they look at you in disbelief.")
    time.sleep(3)
    print("You ask Leopold why they are looking at you. He says that you almost never see humans in this town.")
    time.sleep(3)
    print("And that they look like that because some have never seen a human. If you are a not a human, what are you.")
    time.sleep(3)
    print("you ask. Leopold says that this is a goblin village and mainly goblin’s live here. You now start to understand where you are.")
    time.sleep(3)
    print("You’re in a fantasy world. Than Leopold says that he can sleep at his house till your better.")
    time.sleep(3)
    print(". You thank him for the hospitality. And start walking to his house.")
    time.sleep(3)
    print("When you arrive at his house. You see that it’s a beautiful mansion. What do you do?")
    print("A. now knowing that he’s rich you attack him with al you force to try and steal his money.")
    print("B. go into the mansion with him.")
    vraag = input(">>> ")
    if vraag in A:
        negen()
    if vraag in B:
        tien()

    
def negen():
    print("you attack him again. This time Leopold doesn’t fight. He stands still takes your blows.")
    time.sleep(3)
    print("After a short time he tells you to please stop and that he will give you money.")
    time.sleep(3)
    print("So you stop and take his money and run away. You run into an alley in the distance.")
    time.sleep(3)
    print("You have a fair bit of money to use. What will you buy?")
    print("A. food")
    print("B. weapons")
    vraag = input(">>> ")
    if vraag in A:
        ending3()
    if vraag in B:
        ending3()

def tien():
    print("you start walking inside, the house is grand and luxurious.")
    time.sleep(3)
    print("You ask Leopold how he got this house. He tells you that he’s the mayor and that if you’re the mayor you get to live in this house.")
    time.sleep(3)
    print("You think for yourself that goblins are very different in this world than how goblin’s get depicted in the media.")
    time.sleep(3)
    print("Leopold takes you to his guest room. It’s getting late so Leopold tells you that he will show the town tomorrow. You go to bed.")
    time.sleep(3)
    print("While asleep you get a dream there is a woman telling you that she’s a god and send you to this world to stop a war.")
    time.sleep(3)
    print(". A war between elf’s and goblin’s. she gifts you a choice. Which will you pick?")
    print("A. Power")
    print("B. knowledge")
    vraag = input(">>> ")
    if vraag in A:
        dertien()
    if vraag in B:
        viertien()
    


def elf():
    print("you stay silent. The elf gets very mad and leaves. You are alone again.")
    time.sleep(3)
    print("Alone in the dark for very long. What will you do?")
    print("A. do nothing")
    print("B. try to escape")
    vraag = input(">>> ")
    if vraag in A:
        ending4()
    if vraag in B:
        ending5()
 
def twaalf():
    print("you start to talk you say that you can’t understand him. He notices this, and starts talking in English.")
    time.sleep(3)
    print("He ask you why you went into their forest and that its forbidden to enter their forest.")
    time.sleep(3)
    print("You say that you woke up in a cave and didn’t nowhere you were. The elf ask if you’re telling the truth and you say yes and just want answers.")
    time.sleep(3)
    print("He says sorry and tells you that his name is Cronus. And he will let you out of the cell and get you a place to stay.")
    time.sleep(3)
    print("You agree and he lest you out of the cell, and start walking thru the elf town. You stop and a small house.")
    time.sleep(3)
    print("He tells you that this is a guest house for travellers.")
    time.sleep(3)
    print("You go inside Cronus gifts you some food and tells you to settle down and that he will be back later. You eat and go straight to bed.")
    time.sleep(3)
    print("While asleep you get a dream there is a woman telling you that she’s a god and send you to this world to stop a war.")
    time.sleep(3)
    print("A war between elf’s and goblin’s. she gifts you a choice. Which will you pick?")
    print("A. Power")
    print("B. knowledge")
    vraag = input(">>> ")
    if vraag in A:
        vijftien()
    if vraag in B:
        zestien()


def dertien():
    print("so you pick power. The power to destroy, the power to kill, strength. Well strong you will be.")
    time.sleep(3)
    print("You wake up feeling different. You start to think that, that wasn’t a dream.")
    time.sleep(3)
    print("You now need to stop a war, or in the least save the goblin’s. you hear Leopold talking, in the distance with some people outside your room.")
    time.sleep(3)
    print("There talking about elves and war you can’t understand anymore, so you open your door and sneak to them.")
    time.sleep(3)
    print("Leopold see´s you and ask you to come to him and the other goblin’s.")
    time.sleep(3)
    print("so you walk towards them, when you get there Leopold starts telling you about a war against the elves and that he´s sorry that they can´t show you the town.")
    time.sleep(3)
    print("Then Leopold notices that your different from before. He says that you seem stronger than before.")
    time.sleep(3)
    print("He ask you if you can help against the elf´s and that you will be rewarded handsomely.")
    time.sleep(3)
    print("What will you do?")
    print("A. don’t help")
    print("B. help with the war")
    vraag = input(">>> ")
    if vraag in A:
        ending6()
    if vraag in B:
        zeventien()

def viertien():
    print("so you pick knowledge, skill. Strategy, wisdom will be given to you. you wake up.")
    time.sleep(3)
    print(" Feeling your brain flood with knowledge. You get a headache that gets worse and worse till you collapse.")
    time.sleep(3)
    print("Leopold hears this and comes straight to you. he puts you in the bed.")
    time.sleep(3)
    print("When you wake up Leopold and you hear some other goblin’s are talking about a war with the elf’s")
    time.sleep(3)
    print("when your fully awake you feel better than before like the locks in your brain have been lifted and you can freely think.")
    time.sleep(3)
    print("A wave of curiosity comes over you and you start asking questions to Leopold. About the war, strategies were the fight will happen.")
    time.sleep(3)
    print("Best formations for war and a lot more. Leopold shuts you up. And starts talking, he says that you’ve changed when you woke up.")
    time.sleep(3)
    print("That you feel smarter and wiser than before. He than ask for your help in the war.")
    time.sleep(3)
    print("What do you do?")
    print("A. don’t help")
    print("B. help with the war")
    vraag = input(">>> ")
    if vraag in A:
        ending6()
    if vraag in B:
        achttien()


def vijftien():
    print("so you pick power. The power to destroy, the power to kill, strength.")
    time.sleep(3)
    print("Well strong you will be. You wake up feeling different. You start to think that, that wasn’t a dream.")
    time.sleep(3)
    print("You now need to stop a war, or in the least save the goblin’s. you hear Cronus talking, in the distance with some people outside you’re house.")
    time.sleep(3)
    print("There talking about elves and war you can’t understand anymore, so you open your door and sneak to them.")
    time.sleep(3)
    print("see´s you and ask you to come to him and the other elf’s.")
    time.sleep(3)
    print("so you walk towards them, when you get there Cronus starts telling you about a war against the goblins and that he´s sorry that they can´t show you the town.")
    time.sleep(3)
    print("Then Cronus notices that your different from before. He says that you seem stronger than before.")
    time.sleep(3)
    print(". He ask you if you can help against the elf´s and that you will be rewarded handsomely.")
    time.sleep(3)
    print("What do you do?")
    print("A. don’t help")
    print("B. help with the war")
    vraag = input(">>> ")
    if vraag in A:
        ending6()
    if vraag in B:
        negentien()


def zestien():
    print("so you pick knowledge, skill. Strategy, wisdom will be given to you. you wake up.")
    time.sleep(3)
    print("Feeling your brain flood with knowledge. You get a headache that gets worse and worse till you collapse.")
    time.sleep(3)
    print("Cronus hears this and comes straight to you. he puts you in the bed.")
    time.sleep(3)
    print(". When you wake up Leopold and some other elf’s are talking about a war with the goblin’s.")
    time.sleep(3)
    print("when your fully awake you feel better than before like the locks in your brain have been lifted and you can freely think.")
    time.sleep(3)
    print("A wave of curiosity comes over you and you start asking questions to Cronus. About the war, strategies were the fight will happen.")
    time.sleep(3)
    print(". Best formations for war and a lot more. Cronus shuts you up. And starts talking, he says that you’ve changed when you woke up.")
    time.sleep(3)
    print("That you feel smarter and wiser than before. He then ask for your help in the war.")
    time.sleep(3)
    print("What do you do?")
    print("A. don’t help ")
    print("B. help with the war ")
    vraag = input(">>> ")
    if vraag in A:
        ending6()
    if vraag in B:
        twintig()

def zeventien():
    print("you decide to help with the war with your strength, the goblin’s are sure to win.")
    time.sleep(3)
    print("The goblin’s and the elf’s are fighting on a plain just outside the forest.")
    time.sleep(3)
    print("You’re on the side of the goblin’s.")
    time.sleep(3)
    print("how will you fight?")
    print("A. charge in ")
    print("B. wait for orders and help your comrades")
    vraag = input(">>> ")
    if vraag in A:
        ending7()
    if vraag in B:
        ending8()


def achttien():
    print("with your skill and strategies the goblin’s are sure to win.")
    time.sleep(3)
    print("Your fighting in a plain outside the forest. Everything is flat there is no high ground.")
    time.sleep(3)
    print("What will you do?")
    print("A. make the army charge in with al their might ")
    print("B. set up archers in the back and solders on the front and make the elves come to you ")
    vraag = input(">>> ")
    if vraag in A:
        ending9()
    if vraag in B:
        ending10()

def negentien():
    print(". you decide to help with the war with your strength, the elf’s are sure to win.")
    time.sleep(3)
    print("The goblin’s and the elf’s are fighting on a plain just outside the forest. You’re on the side of the elf’s.")
    time.sleep(3)
    print("how will you fight?")
    print("A. charge in")
    print("B. wait for orders and help your comrades")
    vraag = input(">>> ")
    if vraag in A:
        ending11()
    if vraag in B:
        ending12()


def twintig():
    print("you are smart but do you really want to do this you have only seen a goblin once jet you are now fighting them.")
    time.sleep(3)
    print("With you smarts you can easily win, but you are also smart enough to stop a war.")
    time.sleep(3)
    print("What will you do?")
    print("A. stop the war")
    print("B. win")
    vraag = input(">>> ")
    if vraag in A:
        eenentwintig()
    if vraag in B:
        ending13()

def eenentwintig():
    print("you talk to the elf’s and tell them to stop the war.")
    time.sleep(3)
    print("And that you will try to set up a meeting with the goblin’s.")
    time.sleep(3)
    print("how will you do this?")
    print("A. sneak to the goblin village and force the leader to talk with the elf’s")
    print("B. ask Cronus to go with you to the goblin village to negotiate ")
    vraag = input(">>> ")
    if vraag in A:
        ending14()
    if vraag in B:
        ending15()



    



def ending1():
    print("Ending 1. You start resisting and one of the elf’s shoots you in the head with a bow")
    time.sleep(2)
    print("do you want to restart?")
    print("A: jes")
    print("B: no")
    vraag = input(">>> ")
    if vraag in A:
        intro()
    if vraag in B:
        end()


def ending2():
    print("Ending 2. You attack the creature again but this time it killed you.")
    time.sleep(2)
    print("do you want to restart?")
    print("A: jes")
    print("B: no")
    vraag = input(">>> ")
    if vraag in A:
        intro()
    if vraag in B:
        end()

def ending3():
    print("Ending 3. nobody wanted to sell you anything and after a while you died.")
    time.sleep(2)
    print("do you want to restart?")
    print("A: jes")
    print("B: no")
    vraag = input(">>> ")
    if vraag in A:
        intro()
    if vraag in B:
        end()

def ending4():
    print("Ending 4. You did nothing and after a while you died.")
    time.sleep(2)
    print("do you want to restart?")
    print("A: jes")
    print("B: no")
    vraag = input(">>> ")
    if vraag in A:
        intro()
    if vraag in B:
        end()

def ending5():
    print("Ending 5. While you were trying to escape a elf saw you and shot you dead.")
    time.sleep(2)
    print("do you want to restart?")
    print("A: jes")
    print("B: no")
    vraag = input(">>> ")
    if vraag in A:
        intro()
    if vraag in B:
        end()

def ending6():
    print("Ending 6. You did not help in the war. And when the enemies attacked the village you where swiftly killed.")
    time.sleep(2)
    print("do you want to restart?")
    print("A: jes")
    print("B: no")
    vraag = input(">>> ")
    if vraag in A:
        intro()
    if vraag in B:
        end()

def ending7():
    print("Ending 7. You charged in with all your power. But there were to many elf’s and you got killed.")
    time.sleep(2)
    print("do you want to restart?")
    print("A: jes")
    print("B: no")
    vraag = input(">>> ")
    if vraag in A:
        intro()
    if vraag in B:
        end()

def ending8():
    print("Ending 8.you stood by the goblins and fought to getter and won.")
    time.sleep(2)
    print("do you want to restart?")
    print("A: jes")
    print("B: no")
    vraag = input(">>> ")
    if vraag in A:
        intro()
    if vraag in B:
        end()

def ending9():
    print("Ending 9. The entire army charged in and all swiftly got killed by archers")
    time.sleep(2)
    print("do you want to restart?")
    print("A: jes")
    print("B: no")
    vraag = input(">>> ")
    if vraag in A:
        intro()
    if vraag in B:
        end()

def ending10():
    print("Ending 10. By position smartly you manged to win.")
    time.sleep(2)
    print("do you want to restart?")
    print("A: jes")
    print("B: no")
    vraag = input(">>> ")
    if vraag in A:
        intro()
    if vraag in B:
        end()

def ending11():
    print("Ending 11.  You charged in with all your power. But there were to many goblin’s and you got killed.")
    time.sleep(2)
    print("do you want to restart?")
    print("A: jes")
    print("B: no")
    vraag = input(">>> ")
    if vraag in A:
        intro()
    if vraag in B:
        end()

def ending12():
    print("Ending 12. you stood by the goblins and fought to getter and won.")
    time.sleep(2)
    print("do you want to restart?")
    print("A: jes")
    print("B: no")
    vraag = input(">>> ")
    if vraag in A:
        intro()
    if vraag in B:
        end()

def ending13():
    print("Ending 13. You won, now happy.")
    time.sleep(2)
    print("do you want to restart?")
    print("A: jes")
    print("B: no")
    vraag = input(">>> ")
    if vraag in A:
        intro()
    if vraag in B:
        end()

def ending14():
    print("Ending 14. You sneaked into the goblin village. Got found and killed.")
    time.sleep(2)
    print("do you want to restart?")
    print("A: jes")
    print("B: no")
    vraag = input(">>> ")
    if vraag in A:
        intro()
    if vraag in B:
        end()

def ending15():
    print("Ending 15. You and Cronus want to the goblin village. And made a peace treaty. Good job.")
    time.sleep(2)
    print("do you want to restart?")
    print("A: jes")
    print("B: no")
    vraag = input(">>> ")
    if vraag in A:
        intro()
    if vraag in B:
        end()

def end():
    print("this was it goodbye")








intro()