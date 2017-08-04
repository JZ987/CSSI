class Musician:

    def __init__(self, name, instrument, song, recording):
        self.name = name
        self.instrument = instrument
        self.song = song
        self.recording = recording

    def description(self):
        print "My name is {}, I play {}, and my favorite song is {}".format(self.name, self.instrument, self.song)

    def is_recording(self):
        if self.recording:
            print "WooHoo!"
        else:
            print "Nahhhh"

kanye = Musician("Kanye", "Vocals", "Famous", True)
chance = Musician("Chance", "Rapper", "No Problem", False)

kanye.description()
kanye.is_recording()
