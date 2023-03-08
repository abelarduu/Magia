#Importações
import pyxel
from random import randint

class Items():
    def __init__(self) -> None:
        #declarando variaveis
        self.item = False
        self.pos_x = randint(10,50)
        self.pos_y = -16
        self.img_x, self.img_y = 0, 144
    
    def Collision(self):
        #gravidade no item
        if self.item == False:
            if self.pos_y < 68:
                self.pos_y +=1

        #ao colidir com o item
        if self.item == True:
            self.pos_y= -16

    def DrawItem(self):
        pyxel.blt(self.pos_x, self.pos_y, 1 , self.img_x, self.img_y, 16, 16)

#instaciando
Mushroom = Items()
Coin = Items()
staff = Items()

#Reconfigurando determinados itens
Mushroom.item=True
Coin.img_x, Coin.img_y= 16, 144
staff.pos_x, staff.pos_y= 75,68
staff.img_x, staff.img_y= 96,0