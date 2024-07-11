import pyxel
from src import *

class Game:
    def __init__(self):
        self.play = False
        self.tutorial = False
        pyxel.init(SCREEN_W, SCREEN_H, title= "Magia")
        pyxel.load('src/assets/magia.pyxres')
        pyxel.playm(0, loop= True)
        pyxel.run(self.update, self.draw)

    def update(self):
        """Verifica interação a cada quadro."""
        if self.tutorial or self.play:
            MOVE_HOLD = 12
            MOVE_REPEAT = 3
            #Movimentação do Player
            player.move(left= pyxel.btnp(pyxel.KEY_A, hold= MOVE_HOLD, repeat= MOVE_REPEAT),
                        right= pyxel.btnp(pyxel.KEY_D, hold= MOVE_HOLD, repeat= MOVE_REPEAT),
                        jump= pyxel.btnp(pyxel.KEY_W, hold= MOVE_HOLD, repeat= MOVE_REPEAT),
                        attack= pyxel.btnp(pyxel.KEY_E))
            
            self.check_player_collisions()

            #Se Player estiver com cajado:
            #Acaba o tutorial
            if player.staff:
                self.play = True
                self.tutorial = False
                
            if self.play:
                #Gravidade nos itens
                if not player.power:
                    mushroom.apply_gravity()
                coin.apply_gravity()
                
                #Movimentação do Goblin Lanceiro
                GOBLIN_POSITION= SCREEN_W - goblin_lancer.w
                goblin_lancer.move(left= goblin_lancer.x >= GOBLIN_POSITION,
                                   attack= (goblin_lancer.x <= GOBLIN_POSITION and
                                   spear.x <= -16))

                #Movimentação dos ataques
                #Lanca do goblin lanceiro
                if spear.x <= -16: 
                    goblin_lancer.attacking = False
                else:
                    spear.x -= 2

                #Movimento da bola de fogo
                if fireball.x >= SCREEN_W:
                    player.attacking = False
                else:  
                   fireball.x += 2

        #Menu Inicial
        else:
            #Verificação de interação para inicialização do Game
            if pyxel.btnr(pyxel.KEY_KP_ENTER):
                self.tutorial = True
                
    def check_player_collisions(self):
        """Código para verificar colisões entre objetos."""
        #Colisão com o goblin
        if (player.check_collision(goblin_lancer) or
            player.check_collision(spear)):
            player.animate_and_apply_damage()

        #Colisão com o cajado
        if player.check_collision(staff):
            staff.move_off_screen()
            player.staff = True
            player.imgy = 16
            
        #Colisão com o cogumelo
        if player.check_collision(mushroom):
            mushroom.move_off_screen()
            mushroom.x = randint(0, SCREEN_W - mushroom.w*3)
            player.power = True
            player.score += 5
            player.imgy = 32

        #Colisão com a moeda
        if player.check_collision(coin):
            coin.move_off_screen()
            coin.x = randint(0, SCREEN_W - coin.w*3)
            player.score += 1
    
    def draw(self):
        """atualiza a interface a cada quadro."""
        pyxel.cls(0)
        self.draw_floor()

        if self.tutorial or self.play:
            #Desenhando Entidades
            for entity in entities_list:
                entity.draw()
                
                #Animando entidades/Mobs
                if not entity == player:
                    if pyxel.frame_count % 4 == 0:
                        entity.update_sprite()
                        
            #Desenhando itens
            for item in items_list:
                item.draw()
                
                #Animando itens
                if not item == spear:
                    if pyxel.frame_count % 4 == 0:
                        item.update_sprite()
                        
            if self.play:
                center_score = len(str(player.score)) / 2 * pyxel.FONT_WIDTH
                pyxel.text(pyxel.width / 2 - center_score, 5, str(player.score), 7)
                
            else:
                TXT= "Mova-se e pegue o cajado..."
                CENTER_TXT = len(TXT) / 2 * pyxel.FONT_WIDTH
                pyxel.text(pyxel.width / 2 - CENTER_TXT, pyxel.height / 2 - 32, TXT, 7)
        
        #Menu Inicial
        else:
            pyxel.blt(0, 0, 0, 0, 0, 140, 100, 0)
            
            TXT = "Enter para continuar"
            CENTER_TXT = len(TXT) / 2 * pyxel.FONT_WIDTH
            pyxel.text(pyxel.width / 2 - CENTER_TXT, SCREEN_H - 16, TXT, 7)

    def draw_floor(self):
        """Desenha o chão usando um tileset, um bloco de cada vez."""
        for x in range(3):
            pyxel.blt(x * 48, pyxel.height - 16, 1, 72, 128, 48, 16)

if __name__ == "__main__":
    Game()