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
  
