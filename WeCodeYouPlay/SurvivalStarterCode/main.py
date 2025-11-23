from gamelib import *
game = Game(800,600,"Survival")



while not game.over:
  game.processInput()


    
  game.update(30)
game.quit()