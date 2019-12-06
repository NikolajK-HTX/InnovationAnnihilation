import arcade
import random
from playsound import playsound

width, height = 800, 600

class Innovation(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.points = 0
        self.key = 0
        self.randomKey()

    def update(self, delta_time):
        pass

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(str(self.points) + " pts", width / 2, height / 3, arcade.color.WHITE, 15)
        arcade.draw_text("Press " + str(self.keychoice), width / 2, height / 2, arcade.color.WHITE, 20)

    def on_key_press(self, key, modifiers):
        for x in range(0, len(self.keysButton)):
            if (key == self.keysButton[x]):
                if self.keychoice == self.keys[x]:
                    playsound(self.sounds[x])
                    self.points += 1
                    self.randomKey()

    def randomKey(self):
        self.keys = ["C", "D", "E", "F", "G", "A", "B", "C#", "D#", "F#", "G#", "A#"]
        self.keysButton = [arcade.key.UP, arcade.key.DOWN, arcade.key.LEFT, arcade.key.RIGHT, arcade.key.SPACE, arcade.key.W, arcade.key.A, arcade.key.S, arcade.key.D, arcade.key.F, arcade.key.G]
        self.sounds = ["sounds/s1.mp3", "sounds/s2.wav", "sounds/s3.mp3", "sounds/s4.mp3", "sounds/s5.mp3", "sounds/s6.wav", "sounds/s7.wav", "sounds/s8.mp3", "sounds/s9.wav", "sounds/s10.mp3", "sounds/s11.mp3", "sounds/s12.ogg", ]
        self.keychoice = random.choice(self.keys)


mitSpil = Innovation(width, height)

arcade.run()