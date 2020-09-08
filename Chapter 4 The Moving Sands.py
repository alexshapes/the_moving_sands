# -*- coding: UTF-8 -*-
import re
shutdown = False
AreaExplore = False
shutdown2 = False
inventory = False
zombie_fight = False
intromenu = ("yes")
health = 5
hit = 1
zombies = 100
bullets = 1
bullets2 = 2
pick = input
format (health,)

def Boss1movingsands ():
    health = 5
    hit = 1
    shutdown2 = False
    print ("")
    print ("𝔜𝔬𝔲'𝔳𝔢 𝔢𝔫𝔤𝔞𝔤𝔢𝔡 𝔦𝔫𝔱𝔬 𝔞 𝔣𝔦𝔤𝔥𝔱 𝔴𝔦𝔱𝔥 ℭ𝔭𝔱. 𝔅𝔩𝔞𝔠𝔨𝔢𝔶𝔢!")
    print ("")
    print ("Cpt. Blackeye : Aʀɢʜ! I ᴅɪᴅɴ'ᴛ ᴇxᴘᴇᴄᴛ ᴀɴʏ ᴠɪsɪᴛᴏʀs Aɢᴀɪɴ! Yᴏᴜ ᴡɪʟʟ ᴍᴇᴇᴛ ʏᴏᴜʀ ᴅᴏᴏᴍ ᴛᴏᴏ!")
    print ("Cpt. Blackeye : Jᴜsᴛ ʟɪᴋᴇ ᴛʜᴀᴛ ғᴏᴏʟ Pʀᴏғᴇssᴏʀ!")
    while (shutdown2 == False): 
                print ("1 = Cpt. Blackeye's Head", "Shoot 🔫")
                print ("2 = Cpt. Blackeye's Shoulders", "Shoot 🔫")
                print ("3 = Cpt. Blackeye's Hands", "Shoot 🔫")
                print ("4 = Cpt. Blackeye's Feet", "Shoot 🔫")
                print ("5 = Above Tree", "Shoot 🔫")
                print ("6 = Water", "Shoot 🔫")
                print ("7 = Sand", "Shoot 🔫")
                print ("8 = Rum Barrel", "Shoot 🔫")
                print ("9 = Aim for a Zombie, Shoot🔫")

                userchoice1 = int(input ("Action!"))
                if (userchoice1 == 4):
                    print ("Cpt. Blackeye : Oh! No! I am hurt. Here. You can have the map. But you will never get out of here and find the artefact!. This map is your tombstone! Please kill me now! I don't want to live forever in this deadly paradise! ")
                    print ("Your Health is {}".format (health))
                    quit
                    shutdown2 = True
                    

                elif (userchoice1 ==2):
                    print ("Cpt. Blackeye : Yᴏᴜ ᴛʜɪɴᴋ ʏᴏᴜ ᴄᴀɴ sᴛᴇᴀʟ ᴍʏ ᴍᴀᴘ sᴏ ᴇᴀsɪʟʏ?! Yᴏᴜ ᴍᴀɢɢᴏᴛ, Hᴀᴠᴇ sᴏᴍᴇ ᴍᴏʀᴇ!")
                    health -= hit
                    if health < hit:
                        print ("Game Over - Going Back to the beach")
                        quit
                        shutdown2 = True
                    print ("Ouch, that hurt.")
                    print ("Your remaining health is {} ".format (health))
                elif (userchoice1 ==3):
                    print ("Cpt. Blackeye : Nɪᴄᴇ ᴛʀʏ! Hᴀᴠᴇ sᴏᴍᴇ ᴍᴏʀᴇ!")
                    health -= hit
                    if health < hit:
                        print ("Game Over - Going Back to the beach")
                        quit
                        shutdown2 = True
                    print ("Ouch, that hurt. I better make sure my aim is better this time")
                    print ("Your remaining health is {} ".format (health))
                elif (userchoice1 ==1):
                    print ("Cpt. Blackeye : Yᴏᴜ ᴀʀᴇ ɴᴏᴛ ɢᴇᴛᴛɪɴɢ ᴛʜɪs ᴍᴀᴘ!")
                    health -= hit
                    if health < hit:
                        print ("Game Over - Going Back to the beach")
                        quit
                        shutdown2 = True
                    print ("Ouch, that hurt. It looks like we could lose if I don't get my aim straight")
                    print ("Your remaining health is {} ".format (health))
                elif (userchoice1 ==5):
                    print ("Arghh! I will get you before the tide does! Trees won't hurt me")
                    health -= hit
                    if health < hit:
                        print ("Game Over - (Going Back to the beach)")
                        quit
                        shutdown2 = True
                    print ("Ouch, that hurt.")
                    print ("Your remaining health is {} ".format (health))
                elif (userchoice1 ==6):
                    print ("You can't even aim at me! The water is on my side!")
                    health -= hit
                    if health < hit:
                        print ("Game Over - Going Back to the beach")
                        quit
                        shutdown2 = True
                    print ("Ouch, that hurt.")
                    print ("Your remaining health is {} ".format (health))
                elif (userchoice1 ==7):
                    print ("Struck a nerve did I? You must be tired of shooting already!")
                    health -= hit
                    if health < hit:
                        print ("Game Over - Going Back to the beach")
                        quit
                        shutdown2 = True
                    print ("Ouch, that hurt.")
                    print ("Your remaining health is {} ".format (health))
                elif (userchoice1 ==8):
                    print ("")
                    print ("")
                    print ("Argh! Not my Rum stash! You will pay for this!")
                    print ("✨✨✨✨✨𝕊𝕦𝕕𝕕𝕖𝕟 𝕖𝕩𝕡𝕝𝕠𝕤𝕚𝕠𝕟✨✨✨✨✨")
                elif (userchoice1 ==9):
                    print ("")
                    print ("𝔾ℝ𝔸𝕎ℝ 🧟‍♀️ 𝔾ℝ𝔸𝕎ℝ 🇴​​​​​🇭​​​​​ 🇳​​​​​🇴​​​​​, 🇿🇴​​​​​🇲​​​​​🇧​​​​​🇮​​​​​🇪​​​​​🇸​​​​​! 𝔾ℝ𝔸𝕎ℝ 🧟‍♀️ 𝔾ℝ𝔸𝕎ℝ.")
                    print (" Better aim for Cpt. Blackeye instead, there are too many of them!")
                else:
                    print ("Please aim at the target, don't let him get you!")       

def zombie_fight_menu ():
    zombies = 100
    bullets = 1
    bullets2 = 2
    zombie_fight = False
    while (zombie_fight == False):
                    print ("1 = Fire!")
                    print ("")
                    print ("2 = Double Barrel ")
                    print ("")
                    print ("3 = Enough zombie kills for now, I'd better save some bullets for later")
                    print ("")
                    pick = int(input("𝑪𝒉𝒐𝒐𝒔𝒆"))
                    if (pick ==1):
                        zombies -= bullets
                        print (" 𝕱𝖎𝖗𝖊 🔫 ")
                        print ("Wretched Pirate Zombies Remaining : {} ".format (zombies))
                    elif (pick ==2):
                        zombies -= bullets2
                        print (" 🔫 𝔽𝕚𝕣𝕖 🔫 ")
                        print ("Wretched Pirate Zombies Remaining : {} ".format (zombies))
                    elif (pick ==3):
                        print ("Enough zombie kills for now, I'd better save some bullets for later")
                        print ("")
                        quit
                        zombie_fight = True
                    else:
                        print ("I'd better do something in this dreadful situation")
                        
                
                        

def inventory ():
        inventory = False
        while (inventory == False):
                    print ("1 = Compass (Check where you are)")
                    print ("2 = Notebook (Hints)")
                    print ("3 = Close Inventory ")
                    print ("4 = Collect Item")
                    pick = int(input("Please select your item"))
                    if (pick == 1):
                        print ("")
                        print ("It looks like i am finally at the moving sands beach, I'd better be careful. I've been told this beach lives up to its name!")
                    elif (pick == 2):
                        print ("")
                        print ("Maybe if i aim for the legs and not for the head I can question victims as i go along.")
                        
                    elif (pick == 4):
                        print ("")
                        print ("Oh look! A ship in a bottle! This would make a great souvenir!")
                        print ("")   
                    elif (pick == 3):
                        print ("Let's explore and see if we can find the map, We know it's guarded so it'd better be prepared")
                        quit
                        inventory = True
                    else:
                        print ("----------Please pick an item from your inventory---------")
def zombie ():
        coffin = False
        zombie = input
        while (coffin == False):
                    print ("1 = Open Coffin. (Should i really open it?)")
                    print ("")
                    print ("2 = Forget it. (Nah, I am a bit afraid and have better things to do.)")
                    print ("")
                    print ("3 = Shoot it. (Maybe it's better if i shoot it first, a vampire could be lurking!")
                    print ("")
                    print ("4 = Go Back")
                    pick = int(input(" Select "))
                    if (pick == 1):
                        print ("")
                        print ("🦴 🇴​​​​​🇭​​​​​ 🇳​​​​​🇴​​​​​! 🇦​​​​​ 🇿🇴​​​​​🇲​​​​​🇧​​​​​🇮​​​​​🇪​​​​​! 🦴")
                        print ("Zombies? I can't believe it..4")
                        print ("")
                        print ("I'd better shoot it")
                    elif (pick == 2):
                        print ("Better go back to investigate something else on the beach..")
                        quit
                        coffin = True
                    elif (pick == 3):
                        print ("")
                        print ("🦴 🇴​​​​​🇭​​​​​ 🇳​​​​​🇴​​​​​! 🇦​​​​​ 🇿🇴​​​​​🇲​​​​​🇧​​​​​🇮​​​​​🇪​​​​​! 🦴") 
                        print ("")
                        zombie = input("Should i fight it? Yes/No  ")
                        print ("")
                        if input == "yes":
                            print ("")
                            print ("Now i am trouble")
                            print ("")
                            zombie_fight_menu ()
                        else:
                            print ("")
                            print ("I'm still in trouble, I have no choice but to fight it.")
                            print ("")
                            zombie_fight_menu ()
                    elif (pick == 4):
                        print ("")
                        print ("Don't bother, i am getting carried away from my main objective. ")
                        quit
                        coffin = True


def movingsandsintro ():
    AreaExplore = False
    while (AreaExplore == False):

        print ("")
        print ("1 = Shipwreck ⚓")
        print ("2 = Rum Barrel 🛢️")
        print ("3 = Beach 🌊 ")
        print ("4 = Animals 🦀 ")
        print ("5 = Compass 🧭 ")
        print ("6 = Check Inventory 🎒 ")
        print ("7 = Investigate Coffin ⚰️")
        print ("")
        choice = int(input ("𝑊ℎ𝑎𝑡 𝑤𝑜𝑢𝑙𝑑 𝑦𝑜𝑢 𝑙𝑖𝑘𝑒 𝑡𝑜 𝑑𝑜? : "))
        print ("")

        if (choice == 1):
            Boss1movingsands ()
        elif (choice ==2):
            print ("")
            print ("These look flammable! and delicious, I wonder how aged they are..")
        elif (choice ==3):
            print ("")
            print ("I can see the Shipwreck and perhaps that's where I need to go and investigate")
        elif (choice ==4):
            print ("")
            print ("...the crustaceans look very strange, they act as if they are afraid of something ")
        elif (choice ==5):
            print ("")
            print ("My compass doesn't work here anymore")
        elif (choice ==6):
            inventory ()
            print ("")
            print ("Let me see if what i have in my Inventory can help")
        elif (choice ==7):
            zombie ()
        else:
            print ("----------I'd better do something---------")
            
print ("")
print ("Wᴇʟᴄᴏᴍᴇ ᴛᴏ Cʜᴀᴘᴛᴇʀ 4 🗺️ ")
print ("")
print (" 🏴‍☠️  Tʜᴇ Mᴏᴠɪɴɢ Sᴀɴᴅs 🏴‍☠️")
print ("")
next = (input("Continue? (Yes/No)"))
if next == "yes":
        print ("")
        print ("")
else:
    quit()
print ("")
print ("You feel disorientated 💫, as you walk out of the cave, the sun hurts your eyes, the fresh air coming into your lungs feel like they were never really used.")
print ("")
print ("🌊 𝘈 𝘸𝘢𝘷𝘦 𝘤𝘳𝘶𝘴𝘩𝘦𝘴....")
print ("")
print ("Morgana : But the air is different, its so clean...and so are the animals, it looks like nothing i have ever seen before")
print ("You start to question where did the cave lead you.")
print ("You check your compass, but its on a continuous spin.")
print ("Morgana : Could this be the end of my journey? Is this where Professor Patrick Worthingbury went missing? One thing I know for sure, I don't know where I am and neither does my compass. 🧭")
print ("")
next = (input("Continue? (Yes/No)"))
if next == "yes":
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
else:
    print ("Error")
    next = (input("Continue? (Yes/No)"))
    if next == "yes":
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
print ("You spend some time putting, facts together. You look around, everything looks strange..")
print ("Morgana : I've spent some time recovering..and I noticed that the sun didn't move.")
print ("You look up and you notice that the sky is missing.")
print ("Morgana : This is getting stranger and stranger. I can see an existing fauna thriving, birds are flying and animals are present..yet nothing makes sense")
print ("🦋 𝘈 𝘣𝘶𝘵𝘵𝘦𝘳𝘧𝘭𝘺 𝘱𝘢𝘴𝘴𝘪𝘯𝘨 𝘣𝘺...")
print ("You start questioning your wits")
print ("Morgana : Could I be dead? Am I hallucinating?... Did I ever leave the cave?")
print ("You look in the distance and you notice a big mountain ⛰️ ")
print ("Morgana : Oddly enough, I can see ✨ lots of shimmering lights on the mountain, but I wonder how tall it is.")
print ("")
next = (input("Continue? (Yes/No)"))
if next == "yes":
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
else:
    print ("Error")
    next = (input("Continue? (Yes/No)"))
    if next == "yes":
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
        print ("")
print ("As you walk towards the beach, you see a wood plank with a name carved on it")
print ("Morgana : This looks interesting, it looks like an engraved wood plank. Could it hold some information? 19 Spring Gardens, Manchester M2 1FB")
print ("")
print ("")
print ("Type yes to check the name on the wood plank 🔍")
print ("Type no to Ignore and move towards the beach")
next1 = (input("Continue? (Yes/No)"))
print ("")
print ("")
if next1 == "yes":
    print ("丿闩丫 山闩丂 卄🝗尺🝗")
    print ("Morgana : I wonder who Jay was.., I was expecting to see Professor Worthingbury")
else:
    print ("Ok")

print ("")
print ("You begin to approach the shore and you notice on the beach, a rum barrel, a shipwreck, and a coffin.")
print ("It looks like the end of an expedition, could Professor Worthingbury be part of this? perhaps if you take a closer look, you can discover more")

print ("")
print ("You've reached the beach front")
print ("")

Intromenu = input ("Would you like to start exploring? Yes/No")
if (intromenu == "yes"):
    movingsandsintro ()
elif (intromenu == "no"):
    print ("You have no choice")
    movingsandsintro ()
else:
    print ("Again, you have no choice")  
    movingsandsintro ()  
