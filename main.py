import pyxel
from src import *

class Game:
    def __init__(self):
        self.play = False
        self.tutorial = False
        self.mobs_list = [goblin_lancer, goblin_bomber, 
                          goblin_shaman, revived_goblin_shaman, seller]

        pyxel.init(SCREEN_W, SCREEN_H, title= "Magia")
        pyxel.load('src/assets/Magia.pyxres')
        pyxel.playm(0, loop= True)
        pyxel.run(self.update, self.draw)
    
    def reset_game_objects(self):
        """Reseta todos atributos dos objetos e entidades do game."""
        # Resetando tudo
        # Objetos/Itens
        coin.x = randint(0, SCREEN_W - coin.w*3)
        coin.y =  -16

        mushroom.x = randint(0, SCREEN_W -  mushroom.w*3)
        mushroom.y = -16

        staff.x = SCREEN_W / 2 - 2
        staff.y = SCREEN_H - 32

        fireball.x = -16
        fireball.y =  -16

        spear.x = -16
        spear.y = 76

        # Entitades
        player.x = 10
        player.y = 68
        player.imgx = 0
        player.imgy = 0
        player.life = player.MAX_LIFE
        player.staff = False
        player.scores = 0
        
        self.mobs_list = [goblin_lancer, goblin_bomber, 
                          goblin_shaman, revived_goblin_shaman, seller]
                 
        for mob in self.mobs_list:
            mob.life = mob.MAX_LIFE
            mob.x = 160
            mob.y = 68

    def mov_mobs(self):
        """Código para movimentação dos mobs."""
        GOBLIN_POSITION = SCREEN_W - goblin_lancer.w
       
        if goblin_lancer.life >= 0:
            # Movimentação do Goblin Lanceiro
            goblin_lancer.move(left= goblin_lancer.x >= GOBLIN_POSITION,
                               attack= (goblin_lancer.x <= GOBLIN_POSITION and
                                        spear.x <= -16))

        if goblin_lancer.life <= 0:
            # Movimentação do Goblin Bombeiro
            goblin_bomber.move(left= (goblin_bomber.x > -16))
      
        if goblin_bomber.life <= 0:
            # Movimentação do Goblin Shaman Revivido
            goblin_shaman.move(left= (goblin_shaman.x >= GOBLIN_POSITION))
            
        if goblin_shaman.life <= 0:
            # Movimentação do Goblin Shaman Revivido
            revived_goblin_shaman.x = goblin_shaman.x 

    def check_all_collisions(self):
        """Código para verificar colisões entre objetos."""
        # Colisão com o goblin
        for mob in self.mobs_list:
            # Colisão de cada mob com a bola de fogo
            if mob.check_collision(fireball):
                mob.animate_and_apply_damage()
                fireball.move_off_screen()
                
                # Adicionando recuo após o HIT
                if mob.x >= 5:
                    mob.x +=5

            # Colisão do player com cada mob
            if (player.check_collision(mob) or
                player.check_collision(spear)):
                player.animate_and_apply_damage()
                
                # Se colidir com a lança:
                # Remove a lança da tela
                if player.check_collision(spear):
                    spear.move_off_screen()
                    
                # Adicionando recuo após o HIT
                if player.x >= 5:
                    player.x -=5

        # Colisão com o cajado
        if player.check_collision(staff):
            staff.move_off_screen()
            player.staff = True
            player.imgy = 16
            pyxel.play(1, 2)
            
        # Colisão com o cogumelo
        if player.check_collision(mushroom):
            mushroom.move_off_screen()
            mushroom.x = randint(0, SCREEN_W - mushroom.w*3)
            player.power = True
            player.scores += 5
            player.imgy = 32
            pyxel.play(1, 2)

        # Colisão com a moeda
        if player.check_collision(coin):
            coin.move_off_screen()
            coin.x = randint(0, SCREEN_W - coin.w*3)
            player.scores += 1
            pyxel.play(2, 3)
            
    def update(self):
        """Verifica interação a cada quadro."""
        if self.tutorial or self.play:
            MOVE_HOLD = 12
            MOVE_REPEAT = 3
            # Movimentação do Player
            player.move(left= pyxel.btnp(pyxel.KEY_A, hold= MOVE_HOLD, repeat= MOVE_REPEAT),
                        right= pyxel.btnp(pyxel.KEY_D, hold= MOVE_HOLD, repeat= MOVE_REPEAT),
                        jump= pyxel.btnp(pyxel.KEY_W, hold= MOVE_HOLD, repeat= MOVE_REPEAT),
                        attack= pyxel.btnp(pyxel.KEY_E) and player.staff)
            
            self.check_all_collisions()

            # Se Player estiver com cajado:
            # Acaba o tutorial
            if player.staff:
                self.play = True
                self.tutorial = False
                
            if self.play:
                # Gravidade nos itens
                if not player.power:
                    mushroom.apply_gravity()
                coin.apply_gravity()

                self.mov_mobs()

                # ATAQUES
                # Ataque do Player
                # Movimento da bola de fogo
                if player.attacking:
                    if fireball.x >= SCREEN_W:
                        player.attacking = False
                    else:  
                       fireball.x += 2
                       
                # Ataque do Goblin Lanceiro
                # Movimento da Lanca
                if goblin_lancer.attacking:
                    if spear.x <= -16: 
                        goblin_lancer.attacking = False
                    else:
                        spear.x -= 2
                       
                #CICLO DO CIRCUITO DE MOBS
                #se o mob morrer:
                #remova da lista o mob morto
                if self.mobs_list[0].life <= 0:
                    self.mobs_list.remove(self.mobs_list[0])
                
            # Reset Game
            if (player.life <= 0 or 
                revived_goblin_shaman.life <= 0):
                # Verificação de interação para resetar/reniciar o Game
                if (pyxel.btnr(pyxel.KEY_KP_ENTER) or
                    pyxel.btnr(pyxel.KEY_RETURN)):

                    self.reset_game_objects()
                    self.tutorial = False
                    self.play = False

        # Menu Inicial
        else:
            # Verificação de interação para inicialização do Game
            if (pyxel.btnp(pyxel.KEY_KP_ENTER) or
                pyxel.btnp(pyxel.KEY_RETURN)):
                self.tutorial = True
                pyxel.play(2, 3)
                
    def draw_centered_text(self, txt, y, col):
        """Centraliza e desenha o texto na tela"""
        text_center_x = len(txt) / 2 * pyxel.FONT_WIDTH
        pyxel.text(pyxel.width / 2 - text_center_x, y, txt, col)
        
    def draw_floor(self):
        """Desenha o chão usando um tileset, um bloco de cada vez."""
        BLOCK_WIDTH = 48
        for x in range(3):
            pyxel.blt(x * BLOCK_WIDTH, pyxel.height - 16, 1, 72, 128, 48, 16)

    def draw_life_HUD(self):
        """Adiciona na tela os elementos da HUD de vida."""
        #HUD Player
        for x in range(player.MAX_LIFE):
            PADX = x * 8
            pyxel.blt(3 + PADX , 3, 1, 33, 152, 7, 7, 0)
        
        for x in range(player.life):
            PADX = x * 8
            pyxel.blt(3 + PADX , 3, 1, 25, 152, 7, 7, 0)

        #HUD Mobs
        mob = self.mobs_list[0]
        for x in range(mob.MAX_LIFE):
            PADX = x * 8
            POS_INITIAL_X = SCREEN_W -10 - PADX
            pyxel.blt(POS_INITIAL_X, 3, 1, 33, 160, 7, 7, 0)
        
        for x in range(mob.life):
            PADX = x * 8
            POS_INITIAL_X = SCREEN_W -10 - PADX
            pyxel.blt(POS_INITIAL_X, 3, 1, 25, 160, 7, 7, 0)
    
    def draw(self):
        """atualiza a interface a cada quadro."""
        pyxel.cls(0)
        self.draw_floor()

        if self.tutorial or self.play:
            # Desenhando Entidades
            player.draw()
            for mob in self.mobs_list:
                mob.draw()
                # Animando entidades/Mobs
                if pyxel.frame_count % 4 == 0:
                    mob.update_sprite()
                        
            # Desenhando itens
            for item in items_list:
                item.draw()
                # Animando itens
                if not item == spear:
                    if pyxel.frame_count % 4 == 0:
                        item.update_sprite()
            
            if self.play:
                self.draw_life_HUD()
                self.draw_centered_text(str(player.scores), 5, 7)
                
                # Reset Game
                if (player.life <= 0 or 
                    revived_goblin_shaman.life <= 0):
                    self.draw_centered_text("Total de pontos:", SCREEN_H / 2 - 16, 7)
                    self.draw_centered_text(str(player.scores), SCREEN_H / 2, 7)
                    self.draw_centered_text("Enter para retornar", SCREEN_H - 16, 7)
                    self.draw_centered_text("ao menu inicial", SCREEN_H - 8, 7)
            
            # Tutorial
            else:
                self.draw_centered_text("Mova-se e pegue o cajado...", 5, 7)
                # Desenha e anima a art dos controles  W A S D E
                if pyxel.frame_count % 10 == 0:
                    controls_animation.update_sprite()
                controls_animation.draw()
        
        # Menu Inicial
        else:
            pyxel.blt(0, 0, 0, 0, 0, 140, 100, 0)
            self.draw_centered_text("Enter para continuar", SCREEN_H - 16, 7)
    
if __name__ == "__main__":
    Game()