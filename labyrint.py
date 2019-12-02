import arcade


SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.text = ""

    
    def update(self, delta_time):
        pass

    def on_draw(self):
        arcade.start_render()
        if (self.text != ""):
            arcade.draw_text(self.text, SCREEN_WIDTH/2 - 100, SCREEN_HEIGHT/2, arcade.color.WHITE, 40)

    def on_key_press(self, key, modifiers):
        if (key == arcade.key.RIGHT):
            print("You won!")
            self.text = "You won!"
        elif (key == arcade.key.LEFT):
            print("You lost :(")
            self.text = "You lost!"
        elif (key == arcade.key.R):
            self.text = ""

MyGame(600, 600, "Hejsa")

arcade.run()