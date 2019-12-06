import arcade
import random

width, height = 800, 600

class Innovation(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.points = 0
        self.key = 0
        self.randomKey()
        self.mode = "challenge"

    def update(self, delta_time):
        pass

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(str(self.points) + " pts", width / 2, height / 3, arcade.color.WHITE, 15)
        if self.mode == "challenge":
            arcade.draw_text("Press " + str(self.keychoice), width / 2, height / 2, arcade.color.WHITE, 20)
        arcade.draw_text("Press 'X' to go out of {}".format(self.mode), width / 2, height / 3.5, arcade.color.WHITE, 20)

    def on_key_press(self, key, modifiers):
        if self.mode == "challenge":
            for x in range(0, len(self.keysButton)):
                if (key == self.keysButton[x]):
                    if self.keychoice == self.keys[x]:
                        sound = arcade.load_sound(self.sounds[x])
                        arcade.play_sound(sound)
                        self.points += 1
                        self.randomKey()
        if (key == arcade.key.X):
            if self.mode == "challenge":
                self.mode = "free mode"
            elif self.mode == "free mode":
                self.mode = "challenge"

        if self.mode == "free mode":
            for x in range(0, len(self.keysButton)):
                if (key == self.keysButton[x]):
                    sound = arcade.load_sound(self.sounds[x])
                    arcade.play_sound(sound)

    def randomKey(self):
        self.keys = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
        self.keysButton = [arcade.key.UP, arcade.key.RIGHT, arcade.key.DOWN, arcade.key.LEFT, arcade.key.SPACE, arcade.key.W, arcade.key.A, arcade.key.S, arcade.key.D, arcade.key.F, arcade.key.G, arcade.key.R]
        self.sounds = ["sounds/s1.wav", "sounds/s2.wav", "sounds/s3.wav", "sounds/s4.wav", "sounds/s5.wav", "sounds/s6.wav", "sounds/s7.wav", "sounds/s8.wav", "sounds/s9.wav", "sounds/s10.wav", "sounds/s11.wav", "sounds/s12.wav", ]
        self.keychoice = random.choice(self.keys)


mitSpil = Innovation(width, height)
arcade.run()
