#!/usr/bin/env python3

# Created by: ????
# Created on: ???? 2019
# This file is the "????" game
#   for CircuitPython

import ugame
import stage
import board
import neopixel
import time
import random

import constants

sprites = []

def blank_white_reset_scene():
    # this function is the splash scene game loop

    # do house keeping to ensure everythng is setup

    # set up the NeoPixels
    pixels = neopixel.NeoPixel(board.NEOPIXEL, 5, auto_write=False)
    pixels.deinit() # and turn them all off

    # reset sound to be off
    sound = ugame.audio
    sound.stop()
    sound.mute(False)

    # an image bank for CircuitPython
    image_bank_1 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_1, 160, 120)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 1/2 seconds
        time.sleep(0.5)
        mt_splash_scene()

        # redraw sprite list

def mt_splash_scene():
    # this function is the MT splash scene

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("mt_game_studio.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    # used this program to split the iamge into tile: https://ezgif.com/sprite-cutter/ezgif-5-818cdbcc3f66.png
    background.tile(2, 2, 0)  # blank white
    background.tile(3, 2, 1)
    background.tile(4, 2, 2)
    background.tile(5, 2, 3)
    background.tile(6, 2, 4)
    background.tile(7, 2, 0)  # blank white

    background.tile(2, 3, 0)  # blank white
    background.tile(3, 3, 5)
    background.tile(4, 3, 6)
    background.tile(5, 3, 7)
    background.tile(6, 3, 8)
    background.tile(7, 3, 0)  # blank white

    background.tile(2, 4, 0)  # blank white
    background.tile(3, 4, 9)
    background.tile(4, 4, 10)
    background.tile(5, 4, 11)
    background.tile(6, 4, 12)
    background.tile(7, 4, 0)  # blank white

    background.tile(2, 5, 0)  # blank white
    background.tile(3, 5, 0)
    background.tile(4, 5, 13)
    background.tile(5, 5, 14)
    background.tile(6, 5, 0)
    background.tile(7, 5, 0)  # blank white

    text = []

    text1 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(20, 10)
    text1.text("MT Game Studios")
    text.append(text1)

    # get sound ready
    # follow this guide to convert your other sounds to something that will work
    #    https://learn.adafruit.com/microcontroller-compatible-audio-file-conversion
    coin_sound = open("coin.wav", 'rb')
    sound = ugame.audio
    sound.stop()
    sound.mute(False)
    sound.play(coin_sound)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 1 seconds
        time.sleep(3.0)
        game_splash_scene()

        # redraw sprite list

def game_splash_scene():
    # this function is the MT splash scene

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("break_out.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    text = []

    text1 = stage.Text(width=29, height=15, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(50, 60)
    text1.text("Ferda Games")
    text.append(text1)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 3 seconds
        time.sleep(3.0)
        main_menu_scene()

        # redraw sprite list

def main_menu_scene():
# this function is the MT splash scene

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("break_out.bmp")

    # sets the background to image 0 in the bank
    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    text = []

    text1 = stage.Text(width=29, height=15, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text1.move(40, 10)
    text1.text("Breakout")
    text.append(text1)

    text2 = stage.Text(width=29, height=14, font=None, palette=constants.MT_GAME_STUDIO_PALETTE, buffer=None)
    text2.move(35, 110)
    text2.text("PRESS START")
    text.append(text2)

    # create a stage for the background to show up on
    #   and set the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # set the layers, items show up in order
    game.layers = sprites + text + [background]
    # render the background and inital location of sprite list
    # most likely you will only render background once per scene
    game.render_block()

    # repeat forever, game loop
    while True:
        # get user input

        # update game logic

        # Wait for 3 seconds
        keys = ugame.buttons.get_pressed()

        if keys & ugame.K_START != 0:  # Start button
            game_scene()

        # redraw sprite list

def game_scene():
    # this function is the game scene
    score = 0

    text = []

    # an image bank for CircuitPython
    image_bank_2 = stage.Bank.from_bmp16("break_out.bmp")

    background = stage.Grid(image_bank_2, constants.SCREEN_GRID_X, constants.SCREEN_GRID_Y)

    ball = stage.Sprite(image_bank_2, 1, 74, 56)
    sprites.insert(0, ball)  # insert at the top of sprite list

    paddle1 = stage.Sprite(image_bank_2, 2, 74, 100)
    sprites.insert(0, paddle1)  # insert at the top of sprite list

    paddle2 = stage.Sprite(image_bank_2, 2, 90, 100)
    sprites.insert(0, paddle2)  # insert at the top of sprite list

    brick1 = stage.Sprite(image_bank_2, 5, 90, 40)
    sprites.insert(0, brick1)  # insert at the top of sprite list

    brick2 = stage.Sprite(image_bank_2, 6, 74, 40)
    sprites.insert(0, brick2)  # insert at the top of sprite list

    brick3 = stage.Sprite(image_bank_2, 5, 58, 40)
    sprites.insert(0, brick3)  # insert at the top of sprite list

    brick4 = stage.Sprite(image_bank_2, 6, 42, 40)
    sprites.insert(0, brick4)  # insert at the top of sprite list

    brick5 = stage.Sprite(image_bank_2, 5, 26, 40)
    sprites.insert(0, brick5)  # insert at the top of sprite list

    brick6 = stage.Sprite(image_bank_2, 6, 10, 40)
    sprites.insert(0, brick6)  # insert at the top of sprite list

    brick7 = stage.Sprite(image_bank_2, 5, -6, 40)
    sprites.insert(0, brick7)  # insert at the top of sprite list

    brick8 = stage.Sprite(image_bank_2, 6, 106, 40)
    sprites.insert(0, brick8)  # insert at the top of sprite list

    brick9 = stage.Sprite(image_bank_2, 5, 122, 40)
    sprites.insert(0, brick9)  # insert at the top of sprite list

    brick10 = stage.Sprite(image_bank_2, 6, 138, 40)
    sprites.insert(0, brick10)  # insert at the top of sprite list

    # create a stage for the background to show up
    # setting the frame rate to 60fps
    game = stage.Stage(ugame.display, 60)
    # setting the layers to show them in order
    game.layers = text + sprites + [background]
    # rendering the background and the locations of the sprites
    game.render_block()

    # repeat forever game loop
    while True:
        # get user input
        keys = ugame.buttons.get_pressed()
        #print(keys)

        # update game logic
        # move ship right
        if keys & ugame.K_RIGHT != 0:
            if paddle1.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                paddle1.move(constants.SCREEN_X - constants.SPRITE_SIZE, paddle1.y)
            else:
                paddle1.move(paddle1.x + 1, paddle1.y)

        # move ship right
        if keys & ugame.K_LEFT != 0:
            if paddle1.x < 0:
                paddle1.move(0, paddle1.y)
            else:
                paddle1.move(paddle1.x - 1, paddle1.y)

        if keys & ugame.K_RIGHT != 0:
            if paddle2.x > constants.SCREEN_X - constants.SPRITE_SIZE:
                paddle2.move(constants.SCREEN_X - constants.SPRITE_SIZE, paddle2.y)
            else:
                paddle2.move(paddle2.x + 1, paddle2.y)

        # move ship right
        if keys & ugame.K_LEFT != 0:
            if paddle2.x < 0:
                paddle2.move(0, paddle2.y)
            else:
                paddle2.move(paddle2.x - 1, paddle2.y)

        # redraw sprite list
        game.render_sprites(sprites)
        game.tick() # wait until refresh rate finishes


if __name__ == '__main__':
    blank_white_reset_scene()
