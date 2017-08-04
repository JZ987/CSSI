# Happy Parrot - This parrot is so happy. It accepts a 'thing' as its argument
# and then returns a string where it says how happy it is about the thing!
def HappyParrot(thing):
    print "I am so happy about %s" %(thing)

HappyParrot('carrots')
# Boring Parrot - Write a method for a boring parrot that just returns whatever
# string you give him as an argument.
def BoringParrot(string):
    print string

BoringParrot("I'm boring!")
# Math Parrot - Create a method that accepts two numbers as arguments and adds
# them together!
def MathParrot(first, second):
    print "The sum of {} and {} is {}".format(first, second, first + second)

MathParrot(1, 3)
# Friendly Parrot - This parrot greets people by returning their name and age
# (don't forget to pass that information in as arguments).
def FriendlyParrot(name, age):
    print "Hi! Nice to meet you {}! So you are {} years old eh?".format(name, age)

FriendlyParrot("Jack", 18)
# Favorites Parrot - Tell this parrot about your three favorite things and he
# will return "I love <that thing> too!" for each of them.
def FavoritesParrot(thing1, thing2, thing3):
    print "I love {}, {}, and {} too!!".format(thing1, thing2, thing3)

FavoritesParrot("Chocolate", "Chocolate", "Chocolate")
# Now try calling your methods below with any arguments of your choice and
# print them to the screen. Like this:
HappyParrot("waffles")
# call your methods here


# Now let's pretend you are a wizard and you want to place a spell on each of
# the parrots so that they speak backwards. How would you do that?




# The spell has been broken and everyone is speaking normally again. The
# parrots are really excited about it though - make them shout in all caps.
