import random

DiceNumberOne = random.randint(1, 6)
DiceNumberTwo = random.randint(1, 6)

def RollDice():
    if DiceNumberOne == DiceNumberTwo:
        print "Doubles! Move {} spaces and roll again!\n".format(DiceNumberOne + DiceNumberTwo)
    else:
        print "Move {} spaces. Next player's turn!\n".format(DiceNumberOne + DiceNumberTwo)

def RollDungeonsAndDragonsDice(number_of_side, modifier):
    CurrentRoll = random.randint(1, number_of_side)
    print "Your dice have {} sides and the number you rolled is {}, the modifier is {} so your total roll is {}".format(
            number_of_side, CurrentRoll, modifier, CurrentRoll + modifier)

def RollManyDungeonsAndDragonsDice(list_of_dice):
    TotalNumber = 0
    for dice in list_of_dice:
        TotalNumber += random.randint(1, dice)
    print "Your total number is {}! \n".format(TotalNumber)

cake = [3, 4, 12, 13, 8, 20]

RollManyDungeonsAndDragonsDice(cake)
