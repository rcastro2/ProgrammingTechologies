from gamelib import *

game = Game(800,600,"Delta Fighter")
bk = Animation("images/field_5.png",5,game,1000,1000)
game.setBackground(bk)

hero = Animation("images/hero2.png",3,game,288 / 3, 96, 2)
    
while not game.over:
    game.processInput()
    game.scrollBackground("down",2)


    game.update(30)
game.quit()
