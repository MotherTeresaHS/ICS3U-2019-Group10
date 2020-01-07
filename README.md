# ICS3U-2019-Group10
Euel  Yirga and Austin Harty

#!/usr/bin/env python3

# Created by: Euel Yirga
# Created on: Sep 2019
# This program draws sprites on the PyBadge

import ugame
import stage

# an image bank for CircuitPython
image_bank_1 = stage.Bank.from_bmp16("ball.bmp")
# a list of sprites that will be updated every frame
sprites = []

def main():
    # this function is a scene

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 10, 8)

    # create a sprite
    # parameters (image_bank, image # in bank, x, y)
    ball_1 = stage.Sprite(image_bank_1, 2, 64, 56)
    sprites.append(ball_1)
    ball_2 = stage.Sprite(image_bank_1, 3, 75, 56)
    sprites.insert(0, ball_2) # insert at top of sprite list

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the background layer
    game.layers = sprites + [background]
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # redraw sprite list
        game.render_sprites(sprites)
        game.tick() # wait until refresh rate finishes


if __name__ == "__main__":
    main()
