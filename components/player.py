#importações
import pyxel
from levels import item, mob, button

class Player:
    def __init__(self) -> None:
        #declarando variaveis
        self.img = 1
        self.pos_x, self.pos_y = 10,68
        self.img_x, self.img_y = 0,0
        self.width, self.height = 16,16
        self.staff = False
        self.jump = True
        self.power = False
        self.atack = False
        self.defense = False
        self.life = 3
        self.scores = 0

    def Move(self):
        #enquanto nao morrer, e enquanto no jogo nao iniciar
        if self.life >0 and button.ButtonPlay.button:

            #mover pra cima
            if pyxel.btn(pyxel.KEY_W) and self.jump == True:
                self.jump = False
                #Troca de sprites
                for _ in range(4):
                    self.img_x +=16
                    self.pos_y -=5

                    #zerando o indice
                    if self.img_x >=48:
                        self.img_x = 0

            #mover pra esquerda
            elif pyxel.btn(pyxel.KEY_A) and self.pos_x > 0:
                #Troca de sprites
                for _ in range(4):
                    self.img_x +=16
                    self.pos_x -=0.5

                    #zerando o indice            
                    if self.img_x >=48:
                        self.img_x = 0

            #mover pra direita
            elif pyxel.btn(pyxel.KEY_D) and self.pos_x < 100 - 16:
                #Troca de sprites
                for _ in range(4):
                    self.img_x +=16
                    self.pos_x +=0.5

                    #zerando o indice
                    if self.img_x >=48:
                        self.img_x = 0

            #sprite parado
            else:
                self.img_x = 0

            #gravidade
            if self.pos_y < 68:
                self.pos_y +=1
                if self.pos_y == 68:
                    self.jump = True

    def Collision(self):
        from random import randint
        #Colisao com o cajado
        if self.pos_x == item.staff.pos_x-9 and self.pos_y > item.staff.pos_y-16:
            self.img_y =16
            item.staff.item = True
            self.staff = True

            #ao colidir com cajado o cogumelo aparecerá
            item.Mushroom.item = False

            #Troca de sprites
            if self.power == True:
                self.img_y = 64

        #Colisao com o cogumelo
        if self.pos_y == item.Mushroom.pos_y:
            if self.pos_x >= item.Mushroom.pos_x-10 and self.pos_x <= item.Mushroom.pos_x+10:
                item.Mushroom.item = True
                self.power = True
                self.img_y = 48
                self.scores += 10

                #Troca de sprites para sprite do cajado + Power
                if self.staff == True:
                    self.img_y = 64

        #Colisao com moeda
        if self.pos_y == item.Coin.pos_y:
            if self.pos_x >= item.Coin.pos_x-10 and self.pos_x <= item.Coin.pos_x+10:
                self.scores += 5
                
                item.Coin.pos_y= -16
                item.Coin.pos_x =randint(10,50)

        #colisao com o mob 
        if self.pos_y == mob.Goblin.pos_y:
            if  self.pos_x >= mob.Goblin.pos_x-10 and self.pos_x <= mob.Goblin.pos_x+12:
                self.img_x = 64
                #limitando o score a 0
                if self.scores > 0:
                    self.scores -=5

                #perdendo o power
                if item.Mushroom.item == True:
                    item.Mushroom.item = False
                    self.img_y = 16

                #Recuo
                if self.pos_x > 0:  
                    self.pos_x -=10 
                    #perde uma vida
                    self.life -=1

        #colisao com a lanca do goblin
        if self.pos_x == mob.Goblin.spear_x-10 and self.pos_y == mob.Goblin.spear_y: 
            self.img_x = 64

            #perdendo o power
            if item.Mushroom.item == True:
                item.Mushroom.item = False
                self.img_y = 16

            #limitando o score a 0
            if self.scores > 0:
                self.scores -=5

            #recuo
            if self.pos_x > 0:  
                self.pos_x -=1
                #perde uma vida
                self.life -=1

    def DrawPlayer(self):
        #desenhando o player na tela
        pyxel.blt(self.pos_x, self.pos_y, self.img, self.img_x, self.img_y, self.height, self.width)

        if self.staff == True:
            #scores na tela
            pyxel.text(45, 5, f"{self.scores}", 7)

        if not self.life > 0:
            #game over na tela
            pyxel.text(50 -19, 40, "Game Over", pyxel.frame_count % 16)

Player1 = Player()