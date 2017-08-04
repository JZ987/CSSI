import random
import sys

responses = {"JACK": "HI JACKKKKKKKKKKK!!!!", "CHOCOLATE": "I LOVE CHOCOLATE TOO!!!!",
            "CSSI": "CSSI IS REALLY FUN!!!!", "HELLO": "NICE TO MEET YOUUUUU!!!!",
            "GOOGLE": "I WANT TO GET AN UPGRADE THERE!!!"}

# def walle_talk(string):
#     random_number = random.randint(1, 100)
#     output = ""
#     for response in responses:
#         if response == string.upper():
#             output = responses[response]
#
#     if output == "":
#         if string.isupper():
#             print str(random_number) + " EEEEEEEEEEEVAAAAAAAAAA!"
#         else:
#             print str(random_number) + " Dirrrrr-ect-tivvve?"
#     else:
#         print output
#     speak_to_walle(0)

def walle_talk(string):
    random_number = random.randint(1, 100)
    if string.upper() in responses:
        print responses[string.upper()]
    else:
        if string.isupper():
            print str(random_number) + " EEEEEEEEEEEVAAAAAAAAAA!"
        else:
            print str(random_number) + " Dirrrrr-ect-tivvve?"
    speak_to_walle(0)

def speak_to_walle(counter):
    usr_input = raw_input("\nSpeak to Wall E!!\n")
    if usr_input == "BYE":
        if counter == 2:
            print "NOOOOOOOOO DON'T LEAVE MEEEEEEEE\n"
            sys.exit(0)
        else:
            counter += 1
            speak_to_walle(counter)
    else:
        walle_talk(usr_input)

speak_to_walle(0)
