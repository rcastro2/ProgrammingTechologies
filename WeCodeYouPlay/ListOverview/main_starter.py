from gamelib import *

game = Game(600,600,"Super Novas")

sun1 = Animation("images/nova.png",5,game,240/3,160/2)
sun2 = Animation("images/nova.png",5,game,240/3,160/2)
sun3 = Animation("images/nova.png",5,game,240/3,160/2)
sun4 = Animation("images/nova.png",5,game,240/3,160/2)
sun5 = Animation("images/nova.png",5,game,240/3,160/2)



while not game.over:
    game.processInput()


    game.update(30)
game.quit()
