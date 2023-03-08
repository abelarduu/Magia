import pyxel

class Button:
    def __init__(self) -> None:
        #declarando variaveis
        self.button = False
        self.pos_x = 0
        self.pos_y = -16
        self.img_x, self.img_y = 0, 0

    def DrawButton(self):
        pyxel.blt(self.pos_x, self.pos_y,0, self.img_x, self.img_y, 16, 16)

    def PressButton(self):
        if pyxel.mouse_x > self.pos_x+1 and pyxel.mouse_x < self.pos_x +14:
            if pyxel.mouse_y > self.pos_y-1 and pyxel.mouse_y < self.pos_y +13:
                if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                    return True

#instaciando
ButtonPlay= Button()
ButtonPause= Button()
ButtonMusic= Button()
ButtonHome = Button()
ButtonCredits= Button()

#Reconfigurando determinados itens
ButtonPlay.pos_x,ButtonPlay.pos_y= 41, 43
ButtonMusic.pos_x,ButtonMusic.pos_y = 84, 0
ButtonMusic.img_x,ButtonMusic.img_y = 32, 0
ButtonPause.img_x,ButtonPause.img_y = 0, 16
ButtonHome.pos_x,ButtonHome.pos_y= 41, -16
ButtonHome.img_x,ButtonHome.img_y= 0, 32
ButtonCredits.pos_x, ButtonCredits.pos_y = 41, 58
ButtonCredits.img_x, ButtonCredits.img_y = 0, 48
ButtonCredits.credits = ["Credits\n\nV.1.0 Created in 07/10/21\nV.2.0 Created in 14/10/21\nV.3.0 Created in 14/11/21\n\nCreated by:\n  ABEL LUCAS DE A. SOUZA\n\n   thanks for playing"]
ButtonCredits.textX, ButtonCredits.textY= 0,120 