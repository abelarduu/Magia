from src.objects import Object, Entity
from random import randint

SCREEN_W = 140
SCREEN_H = 100

# Objects/Itens
coin = Object(0, -16, 1, 0, 145, 6, 6)
coin.x = randint(0, SCREEN_W - coin.w*3)

mushroom = Object(0, -16, 1, 0, 137, 8, 8)
mushroom.x = randint(0, SCREEN_W -  mushroom.w*3)

staff = Object(SCREEN_W / 2 - 2, SCREEN_H - 32, 1, 0, 151, 3, 15)

fireball = Object(-16, -16, 1, 0, 128, 9, 9)

spear = Object(-16, 76, 1, 133, 113, 15, 3)
items_list = [coin, mushroom, staff, fireball, spear]

# Arte dos controles W A S D E
CENTER_X = SCREEN_W/2 - (50/2)
CENTER_Y = SCREEN_H/2 - (34/2) - 8
controls_animation = Object(CENTER_X, CENTER_Y, 0, 0, 100, 50, 34)
controls_animation.total_frames = 5

# Entities
player = Entity(10, 68, 1, 0, 0, 16, 16)
player.attack_item = fireball
player.staff = False

goblin_lancer = Entity(160, 68, 1, 0, 48, 16, 16)
goblin_lancer.attack_item = spear

goblin_bomber = Entity(160, 68, 1, 0, 64, 16, 16)

goblin_shaman = Entity(160, 68, 1, 0, 80, 16, 16)

revived_goblin_shaman = Entity(160, 68, 1, 0, 96, 16, 16)

seller = Entity(160, 68, 1, 0, 112, 16, 16)
entities_list = [player, goblin_lancer, goblin_bomber,
                 goblin_shaman, revived_goblin_shaman, seller]