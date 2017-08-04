songs = ["uptown funk", "thinking out loud", "blank space", "take me to church", "shake it off", "shape of you", "sorry"]

def ListSongs(list_of_songs):
    print "Your list consists of:"
    for song in list_of_songs:
        print song.title()
    ChooseOption()

def Helper(list_of_songs):
    print "Your list consists of:"
    for song in list_of_songs:
        print song.title()

def PlaySongs(list_of_songs):
    Helper(list_of_songs)
    choose_song = raw_input("\nWhich song do you want?\n")
    if choose_song.lower() in list_of_songs:
        print "\nPlaying {} currently\n".format(choose_song.title())
    else:
        print "\nUnknown song!!\n"
    ChooseOption()

def SearchSongs(list_of_songs):
    choose_word = raw_input("Which song do you want to search for? (You can enter keywords): ")
    print "List consisting of the keyword: \n"
    for song in list_of_songs:
        if choose_word in song:
            print song + "\n"
    ChooseOption()

def ChooseOption():
    choice = raw_input("\nPick an option:\n1). List\n2). Play\n3). Search\n4). Quit\n\n").lower()
    if choice == "1" or choice == "list":
        ListSongs(songs)
    elif choice == "2" or choice == "play":
        PlaySongs(songs)
    elif choice == "3" or choice == "search":
        SearchSongs(songs)
    elif choice == "4" or choice == "quit":
        print "Goodbye"
    else:
        print "Invalid option!!! \n"
        ChooseOption()

ChooseOption()
