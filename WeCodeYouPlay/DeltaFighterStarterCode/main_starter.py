from gamelib import *

#Game Program
game = Game(800,600,"Delta Fighter")

#Game Loop
while not game.over:
    game.processInput()
       
    game.update(30)
game.quit()
