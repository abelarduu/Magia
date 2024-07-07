import pyxel

#Constantes
MOVE_HOLD = 12
MOVE_REPEAT = 3
JUMP_HEIGHT = 15
MOVE_SPEED = 2
GRAVITY = 0.4
GROUND_LEVEL = 100 - 16

class Object:
    def __init__(self, x, y, img, imgx, imgy, w, h):
        self.x = x
        self.y = y
        self.img = img
        self.imgx = imgx
        self.imgy = imgy
        self.w = w
        self.h = h
        self.total_frames = 8
        
    def update_sprite(self):
        """Atualiza o sprite do jogador para a próxima imagem de animação."""
        self.imgx = (self.imgx + self.w) % (self.w * self.total_frames)
    
    def check_collision(self, obj) -> bool:
        """Verifica se há colisão com um determinado objeto."""
        if (obj.y <= self.y + self.h and
            self.y <= obj.y + obj.h):
            
            if (obj.x+2 <= self.x + self.w and
                self.x+2 <= obj.x + obj.w):
                return True
        return False
    
    def apply_gravity(self):
        """Aplica a gravidade ao jogador."""
        if self.y < GROUND_LEVEL - self.h:
            self.y += GRAVITY
        else:
            self.jump = True
    
    def draw(self):
        """Desenha o jogador na tela."""
        pyxel.blt(self.x, 
                  self.y,
                  self.img,
                  self.imgx,
                  self.imgy,
                  self.w,
                  self.h,
                  0)
                  
    def move_off_screen(self):
        """Remove/move objeto para fora da tela."""
        self.y = -16
                        

    
class Entity(Object):
    def __init__(self, *args):
        super().__init__(*args)
        
        self.life = 3
        self.score = 0
        self.jump = True
        self.power = False
        self.attacked = False
        self.staff = False
        
    def move(self, left, right= None, jump= None, attack= None):
        """Atualiza a posição do jogador com base na entrada do usuário e aplica a gravidade."""
        if self.life:
            #Mov
            if left:
                self.move_left()
                
            if right:
                self.move_right()

            if jump:
                self.jump_action()

            #Atack
            if attack:
                self.attack()

            self.apply_gravity()


    def move_left(self):
        """Move o jogador para a esquerda."""
        if self.x > 0:
            self.update_sprite()
            self.x -= MOVE_SPEED

    def move_right(self):
        """Move o jogador para a direita."""
        if self.x < 140 - self.w:
            self.update_sprite()
            self.x += MOVE_SPEED
            
    def jump_action(self):
        """Executa a ação de pular."""
        if self.jump:
            self.update_sprite()
            self.jump = False
            self.y -= JUMP_HEIGHT

    def attack(self):
        """Muda para a sprite de ataque e executa o ataque."""
        self.attacked= True
        self.imgx = 128
        
    def animate_and_apply_damage(self):
        """Muda para a sprite de HIT e aplica dano."""
        if self.power:
            self.imgy= 16
            self.power= False
            
        self.imgx=  144
        if self.x >=11:
            self.x -= 10