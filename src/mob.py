#importações
import pyxel
from levels import item

#Função de mobs
class Mobs:
    def __init__(self) -> None:
        #declarando variaveis
            self.pos_x = 320
            self.pos_y = 68
            self.img_x = 0
            self.img_y = 112
            self.spear_x = -16
            self.spear_y = self.pos_y
            self.life = True
            
    #Função para as açoes do mob
    def Move(self):
        #mover
        if item.staff.item == True and self.pos_x > 75 - 10:
            #Mudando Sprites
            for _ in range(3):
                self.img_x +=16
                self.pos_x -=0.5
                
                #zerando o indice de sprites
                if self.img_x >=32:
                    self.img_x = 0

        #permitir ataque na hora certa 
        if self.pos_x <= 75  and self.spear_x == -16:
            self.img_x =  80
            self.spear_x = self.pos_x-16

        #movimento da lanca
        if self.spear_x > -16:
            self.spear_x -= 1
            
        #sprite parado
        if self.spear_x == self.pos_x -20:
            self.img_x = 0

    #Mostrar na tela o mob
    def DrawMobs(self): 
        pyxel.blt(self.pos_x, self.pos_y, 1, self.img_x, self.img_y, 16, 16)
        pyxel.blt(self.spear_x, self.spear_y, 1, 96, 112, 16, 16)

Goblin = Mobs()