import arcade
import random

width, height = 800, 600

class Innovation(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.octave = getOctave()
        self.chords = getChords(self.octave)
        self.points = 0
        self.randomTone()
        self.randomChord()
        self.modes = ["challenge", "free mode", "chord mode"]
        self.mode = 1
        self.piano = Piano(100, height / 1.4, self.octave)

    def update(self, delta_time):
        self.chordChoice.timer(delta_time)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(str(self.points) + " pts", width / 2, height / 3, arcade.color.WHITE, 15)
        if self.modes[self.mode%len(self.modes)] == "challenge":
            arcade.draw_text("Press {}".format(self.toneChoice.key), width / 2, height / 2, arcade.color.WHITE, 20)
        elif self.modes[self.mode%len(self.modes)] == "chord mode":
            arcade.draw_text("Press {}".format(self.chordChoice.chordName), width / 2, height / 2 - 20, arcade.color.WHITE, 20)
        arcade.draw_text("Press 'X' to go out of {}".format(self.modes[self.mode%len(self.modes)]), width / 2, height / 3.5, arcade.color.WHITE, 20)
        self.piano.display()

    def on_key_press(self, key, modifiers):
        if self.modes[self.mode%len(self.modes)] == "challenge":
            if self.toneChoice.isTonePressed(key):
                arcade.play_sound(self.toneChoice.sound)
                self.points += 1
                self.randomTone()

        if self.modes[self.mode%len(self.modes)] == "free mode":
            for tone in self.octave:
                if not tone.pressed:
                    if tone.isTonePressed(key):
                        arcade.play_sound(tone.sound)

        if self.modes[self.mode%len(self.modes)] == "chord mode":
            self.chordChoice.keyPressedChord(key)
            if self.chordChoice.isChordPressed():
                self.chordChoice.playSounds()
                self.points += 1
                self.randomChord()

        if (key == arcade.key.X):
            self.mode += 1
        
        for tone in self.octave:
            if not tone.pressed:
                tone.isTonePressed(key)


    def on_key_release(self, key, modifier):
        if self.modes[self.mode%len(self.modes)] == "chord mode":
            self.chordChoice.keyReleasedChord(key)
        
        for tone in self.octave:
            if tone.pressed:
                tone.fixStuff(key)


    def randomTone(self):
        self.toneChoice = random.choice(self.octave)
    
    def randomChord(self):
        self.chordChoice = random.choice(self.chords)


class Tone:
    def __init__(self, key, button, sound, type):
        self.key = key
        self.button = button
        self.sound = arcade.load_sound(sound)
        self.type = type
        self.pressed = False

    def isTonePressed(self, button):
        self.pressed = self.button == button
        return self.pressed
    
    def fixStuff(self, button):
        print("shii " + self.key)
        self.pressed = self.button != button


class Chord:
    def __init__(self, keys, buttons, sounds, chordName="fejl"):
        self.keys = keys
        self.buttons = buttons
        self.buttonsState = []
        self.chordName = chordName
        self.sounds = sounds
        self.timerIsDone = False
        self.countTime = 0.4
        self.counter = 0

        for _button in self.buttons:
            self.buttonsState.append(False)
    def timer(self, delta_time):
        self.counter += delta_time
        self.timerIsDone = self.counter > self.countTime

        if True not in self.buttonsState:
            self.counter = 0

    def keyPressedChord(self, button):
        if button in self.buttons:
            self.buttonsState[self.buttons.index(button)] = True

    def keyReleasedChord(self, button):
        if button in self.buttons:
            self.buttonsState[self.buttons.index(button)] = False

    def playSounds(self):
        for sound in self.sounds:
            arcade.play_sound(sound)

    def isChordPressed(self):
        return (not self.timerIsDone and False not in self.buttonsState)


class Piano2:
    def __init__(self, correspondingTone, x, y, width, height):
        self.correspondingTone = correspondingTone
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def display(self):
        if self.correspondingTone.type == 1:
            print()
            if self.correspondingTone.pressed:
                arcade.draw_rectangle_filled(self.x, self.y, self.width, self.height, arcade.color.GRAY)
            else:
                arcade.draw_rectangle_filled(self.x, self.y, self.width/1.03, self.height, arcade.color.WHITE)
        if self.correspondingTone.type == 2:
            if self.correspondingTone.pressed:
                arcade.draw_rectangle_filled(self.x, self.y + 50, self.width/1.2, self.height/2, arcade.color.WHITE)
            else:
                arcade.draw_rectangle_outline(self.x, self.y + 50, self.width/1.2, self.height/2, arcade.color.GRAY)
            

class Piano:
    def __init__(self, x, y, octave):
        self.listPiano2 = []
        self.x = x
        self.y = y
        width = 50
        counter = 0
        for x in octave:
            self.toneX = self.x + width * counter
            self.listPiano2.append(Piano2(x, self.toneX, self.y, width, 200))
            counter += 1
    
    def display(self):
        for pianoTile in self.listPiano2:
            pianoTile.display()
        


def getOctave():
    return [
        Tone("C",  arcade.key.UP,    "sounds/s1.wav",  1), 
        Tone("C#", arcade.key.RIGHT, "sounds/s2.wav",  2),
        Tone("D",  arcade.key.DOWN,  "sounds/s3.wav",  1),
        Tone("D#", arcade.key.LEFT,  "sounds/s4.wav",  2),
        Tone("E",  arcade.key.SPACE, "sounds/s5.wav",  1),
        Tone("F",  arcade.key.W,     "sounds/s6.wav",  1),
        Tone("F#", arcade.key.A,     "sounds/s7.wav",  2),
        Tone("G",  arcade.key.S,     "sounds/s8.wav",  1),
        Tone("G#", arcade.key.D,     "sounds/s9.wav",  2),
        Tone("A",  arcade.key.F,     "sounds/s10.wav", 1),
        Tone("A#", arcade.key.G,     "sounds/s11.wav", 2),
        Tone("B",  arcade.key.R,     "sounds/s12.wav", 1),
    ]


def getChords(octaves):
    chords = []
    steps = [0, 4, 7]
    for i in range(12):
        keys = []
        buttons = []
        sounds = []
        chordName = "{} major".format(octaves[i].key)
        for n in range(3):
            if i + steps[n] >= 12:
                i -= 12
            keys.append(octaves[i + steps[n]].key)
            buttons.append(octaves[i + steps[n]].button)
            sounds.append(octaves[i + steps[n]].sound)
        chord = Chord(keys, buttons, sounds, chordName)
        chords.append(chord)
    return chords



mitSpil = Innovation(width, height)
arcade.run()
