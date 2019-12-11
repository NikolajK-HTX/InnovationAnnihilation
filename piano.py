import arcade
import random

width, height = 800, 600

class Innovation(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.octave = getOctave()
        self.points = 0
        self.randomTone()
        self.mode = "challenge"

    def update(self, delta_time):
        pass

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(str(self.points) + " pts", width / 2, height / 3, arcade.color.WHITE, 15)
        if self.mode == "challenge":
            arcade.draw_text("Press {}".format(self.toneChoice.key), width / 2, height / 2, arcade.color.WHITE, 20)
        arcade.draw_text("Press 'X' to go out of {}".format(self.mode), width / 2, height / 3.5, arcade.color.WHITE, 20)

    def on_key_press(self, key, modifiers):
        if self.mode == "challenge":
            if self.toneChoice.isButtonPressed(key):
                arcade.play_sound(self.toneChoice.sound)
                self.points += 1
                self.randomTone()

        if self.mode == "free mode":
            for tone in self.octave:
                if tone.isButtonPressed(key):
                    arcade.play_sound(tone.sound)

        if (key == arcade.key.X):
            if self.mode == "challenge":
                self.mode = "free mode"
            elif self.mode == "free mode":
                self.mode = "challenge"


    def randomTone(self):
        self.toneChoice = random.choice(self.octave)


class Tone:
    def __init__(self, key, button, sound):
        self.key = key
        self.button = button
        self.sound = arcade.load_sound(sound)

    def isButtonPressed(self, button):
        return self.button == button


def getOctave():
    return [
        Tone("C",  arcade.key.UP,    "sounds/s1.wav"), 
        Tone("C#", arcade.key.RIGHT, "sounds/s2.wav"),
        Tone("D",  arcade.key.DOWN,  "sounds/s3.wav"),
        Tone("D#", arcade.key.LEFT,  "sounds/s4.wav"),
        Tone("E",  arcade.key.SPACE, "sounds/s5.wav"),
        Tone("F",  arcade.key.W,     "sounds/s6.wav"),
        Tone("F#", arcade.key.A,     "sounds/s7.wav"),
        Tone("G",  arcade.key.S,     "sounds/s8.wav"),
        Tone("G#", arcade.key.D,     "sounds/s9.wav"),
        Tone("A",  arcade.key.F,     "sounds/s10.wav"),
        Tone("A#", arcade.key.G,     "sounds/s11.wav"),
        Tone("B",  arcade.key.R,     "sounds/s12.wav"),
    ]


mitSpil = Innovation(width, height)
arcade.run()
