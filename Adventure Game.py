from random import random
from random import randrange

#Gathering player information
def openingMsg ():
    print ("Welcome to the Temple of Lost Time!")
    print ()
    username = input("Enter a username: ")
    trinket = input("Enter a collectable item (plural) that you like to collect: ")
    print ()
    username = username.capitalize()
    return username, trinket

#Introduction to the game after player information is collected
def mainMsg (stepsTook):
    stepsLeft = 10 - stepsTook
    mainStr = "You are in a dark hallway and see a treasure chest just " + str(stepsLeft) + " steps in front of you."
    print (mainStr)

#Taking the action of the character and outputing the action
def takeStep (stepsTook):
    stepsLeft = 10 - stepsTook
    msgStr = "Only " + str(stepsLeft) + " steps left.  Advance or look around (Y,N)? "
    response = input(msgStr)
    response = response.upper()

    while response != 'Y' and response != 'N':
        print()
        print("Enter a valid response! ")
        response = input(msgStr)
        response = response.upper()

    return response

#Generating a random True or False
def randEvent ():
    eventRand = random()
    event = True
    
    if eventRand < 0.5:
        event = True
    else:
        event = False
    
    return event

#Finding a trinket or item
def trinketEvent (currPiece, pieceRange, item):
    randFound = randrange(pieceRange)
    totalBag = currPiece + randFound
    print()
    if randFound == 0:
        print ("You found an empty crate!  That's too bad!" )
    else:
        print ("You found {} {}!  Now you have {} {}.".format(randFound, item, totalBag, item))
    return totalBag

#Randomly generates the event encounters
def eventGenerate (trinkProb, battleProb, itemProb, currPiece, pieceRange, item, playerName, playerHP, playerStrength):
    randomInt = random()
    if randomInt < trinkProb:
        currPiece = trinketEvent(currPiece, pieceRange, item)
    elif randomInt >= trinkProb and randomInt < (trinkProb + battleProb):
        playerHP = enemyEncounter(playerName, playerHP, playerStrength)
    else:
        playerStrength = findItem(playerStrength)
    return currPiece, playerHP, playerStrength

#Event definition for finding an item to increase strength
def findItem (playerStrength):
    randomInt = randrange(1,10)
    print()
    print("You found a stone to sharpen you sword!")
    print("You increased your attack strength by {}.".format(randomInt))
    playerStrength = playerStrength + randomInt
    return playerStrength

#Outputs the messages of the attacks during a battle
def battleScene (playerName, playerHP, playerStrength, enemyName, enemyHP, enemyStrength, turn):
    if turn == True:
        strMsg = playerName + " attacks " + enemyName + "!!!"
        print (strMsg)
        randDmg = randrange(playerStrength)
        enemyHP = enemyHP - randDmg
        strDmg = enemyName + " loses " + str(randDmg) + " health points. " + str(enemyHP) + " health points left."
        print (strDmg)
        return enemyHP
    elif turn == False:
        strMsg = enemyName + " is attacking " + playerName + "!!!"
        print (strMsg)
        randDmg = randrange(enemyStrength)
        playerHP = playerHP - randDmg
        strDmg = "You lost " + str(randDmg) + " health points. " + str(playerHP) + " health points left."
        print (strDmg)
        return playerHP
    else:
        print ("Something went wrong!")
     
#Plays out the battle of the enemy encounter
def battleEnd(playerName, playerHP, playerStrength, enemyName, enemyHP, enemyStrength):
    firstAtk = randEvent()
    print()
    if firstAtk == True:
        firstMsg = playerName + " surprised " + enemyName + " !!!  " + enemyName + " has " + str(enemyStrength) + " strength and " + str(enemyHP) + " health points."
        print (firstMsg)
        enemyHP = battleScene (playerName, playerHP, playerStrength, enemyName, enemyHP, enemyStrength, firstAtk)
        firstAtk = False
    elif firstAtk == False:
        firstMsg = "The " + enemyName + " appeared suddenly and made a surprise attack!!  " + enemyName + " has " + str(enemyStrength) + " strength and " + str(enemyHP) + " health points."
        print (firstMsg)
        playerHP = battleScene (playerName, playerHP, playerStrength, enemyName, enemyHP, enemyStrength, firstAtk)
        firstAtk = True

    while playerHP > 0 and enemyHP > 0:
        if firstAtk == True:
            enemyHP = battleScene (playerName, playerHP, playerStrength, enemyName, enemyHP, enemyStrength, firstAtk)
            firstAtk = False
        elif firstAtk == False:
            playerHP = battleScene (playerName, playerHP, playerStrength, enemyName, enemyHP, enemyStrength, firstAtk)
            firstAtk = True
    
    print()
    if playerHP <= 0:
        print ("You fainted!")
        return playerHP
    elif enemyHP <= 0:
        beatEnemy = "You beat the " + enemyName + ". You have " + str(playerHP) + " HP left."
        print (beatEnemy)
        return playerHP
    else:
        print ("Battle scene crashed!")

#Randomly generates an enemy encounter
def enemyEncounter (playerName, playerHP, playerStrength):
    randInt = random()
    print ()
    print ("An enemy approaches!")
    if randInt < 0.5:
        print ("Its a Slime!  They are very common.")
        health = battleEnd (playerName, playerHP, playerStrength, "Slime", 50, 10)
        return health
    elif randInt >= 0.5 and randInt < 0.87:
        print ("Its a Skeleton Warrior!  They guard the treasure.")
        health = battleEnd (playerName, playerHP, playerStrength, "Skeleton Warrior", 75, 15)
        return health
    elif randInt >= 0.87 and randInt <= 0.99:
        print ("Its a Ghoul!  They are extremely difficult to kill.")
        health = battleEnd (playerName, playerHP, playerStrength, "Ghoul", 200, 10)
        return health
    else:
        print ("You spotted a rare gold rabbit, but it ran away!")
        return playerHP   

#Taking in input of the class or character role with message description
def charClass (item):
    print("Choose the role you want to play:")
    print()
    thief = "(T)hief: Higher chance to find " + item + " and ability to avoid enemies but lower health."
    adventurer = "(A)dventurer: Balanced all around."
    soldier = "(S)oldier: Loves to pick a fight.  Has high health"
    print (thief)
    print (adventurer)
    print (soldier)
    print()
    choiceMsg = "Type \"T\" for Thief, \"A\" for Adventurer, \"S\" for Soldier: "
    choice = input(choiceMsg)
    choice = choice.upper()
    
    while choice != "T" and choice != "A" and choice != "S":
        print ()
        print ("Invalid choice!")
        choice = input (choiceMsg)
    
    playerHP, playerStrength, trinkProb, battleProb, itemProb, maxHP = choiceClass(choice)
    return playerHP, playerStrength, trinkProb, battleProb, itemProb, maxHP

#Defining the elements of each class or character role
def choiceClass (choice):
    playerHP = 0
    playerStrength = 0
    trinkProb = 0
    battleProb = 0
    if choice == "T":
        print()
        print("You have chosen to be a Thief")
        playerHP = 80
        playerStrength = 30
        trinkProb = .55
        battleProb = .9 - trinkProb
        itemProb = .1
    elif choice == "A":
        print()
        print("You have chosen to be a Adventurer")
        playerHP = 100
        playerStrength = 30
        trinkProb = .45
        battleProb = .9 - trinkProb
        itemProb = .1
    elif choice == "S":
        print()
        print("You have chosen to be a Soldier")
        playerHP = 150
        playerStrength = 35
        trinkProb = 0.35
        battleProb = .9 - trinkProb
        itemProb = .1
    else :
        print("Error occured")
    maxHP = playerHP
    return playerHP, playerStrength, trinkProb, battleProb, itemProb, maxHP

#Winning Message
def winMsg (playerName, playerHP, trinketCollection, item):
    item = item.capitalize()
    print("You reached the heart of the Temple of Lost Time!")
    print("You found the Time Stone!!")
    print()
    print("YOU WON {} !!!".format(playerName.upper()))
    print()
    print("End Health: {}".format(playerHP))
    print("End {}: {}".format(item, trinketCollection))

#Losing message
def loseMsg (playerName, trinketCollection, item):
    item = item.capitalize()
    print("You made some bad choices and lost all your health!!")
    print()
    print("GAME OVER {}".format(playerName.upper()))
    print()
    print("End Health: 0")
    print("End {}: {}".format(item, trinketCollection))

#End on error message if program crashes
def endError ():
    print("You got lost in a time warp!")
    print()
    print("GAME OVER")

#The resting message
def restMsg (restCount, playerHP, maxHP):
    randomInt = random()
    print()
    if restCount < 5 and randomInt < 0.4:
        hpGain = randrange(15,25)
        tempHP = playerHP + hpGain
        if tempHP > maxHP:
            hpGain = maxHP - playerHP
            playerHP = maxHP
            print("You stopped and rested! You gained {} health points!".format(hpGain))
            print("You will not recover any more HP if you rest at full health points.")
        else:
            playerHP = playerHP + hpGain
            print("You stopped and rested! You gained {} health points!".format(hpGain))
            print("You currently have {} health points".format(playerHP))
        restCount += 1
        return restCount, playerHP
    elif restCount >= 5:
        print("You are resting too much!  Get on with the journey!")
    else:
        print("You stopped and nothing happened.")
    return restCount, playerHP

#Main Program
playerName, item = openingMsg()
playerHP, playerStrength, trinkProb, battleProb, itemProb, maxHP = charClass(item)

stepsTook = 0
currPiece = 0
pieceRange = 40
restCount = 0
print()
mainMsg(stepsTook)

while stepsTook < 10 and playerHP > 0:
    stepResponse = takeStep(stepsTook)
    if stepResponse == "Y":
        currPiece, playerHP, playerStrength = eventGenerate (trinkProb, battleProb, itemProb, currPiece, pieceRange, item, playerName, playerHP, playerStrength)
        stepsTook += 1
    elif stepResponse == "N":
        restCount, playerHP = restMsg(restCount, playerHP, maxHP)
        print()
    else:
        print("Error occured")

print()

if stepsTook >= 10 and playerHP > 0:
    winMsg(playerName, playerHP, currPiece, item)
elif playerHP <= 0:
    loseMsg(playerName, currPiece, item)
else:
    endError()
