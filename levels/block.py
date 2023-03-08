#Importações
import pyxel

#Função colocar blocos
def DrawBlock(x, y, posx, posy, quant, space):    
    #Loop para colocar os blocos mais de uma vez
    for _ in range(quant):
        #mostrar o bloco na tela
        pyxel.blt(x, y, 1, posx, posy, 16, 16)
        x +=space