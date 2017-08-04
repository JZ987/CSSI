import random

counter = 0
breaker = False

while not breaker:
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    print "Rolls: {} {}".format(die1, die2)
    counter += 1
    if die1 == 1 and die2 == 1:
        print "Got snake eyes!"
    elif die1 == 6 and die2 == 6:
        print "Got double sixes!"
        breaker = True
print "Rolled the dice {} times".format(counter)
