from src.objects import Object, Entity
from random import randint

SCREEN_W = 140
SCREEN_H = 100

# Objects/Itens
STONE_CENTER_X = SCREEN_W / 2 - 13 / 2
STONE_CENTER_Y = (SCREEN_H / 2 - 34 / 2) - 8
mystic_stone = Object(STONE_CENTER_X, -34, 0, 0, 136, 16, 27)

coin = Object(0, -16, 1, 0, 154, 6, 6)
coin.x = randint(0, SCREEN_W - coin.w*3)

mushroom = Object(0, -16, 1, 0, 146, 8, 8)
mushroom.x = randint(0, SCREEN_W -  mushroom.w*3)

staff = Object(SCREEN_W / 2 - 2, SCREEN_H - 32, 1, 0, 160, 3, 15)

fireball = Object(-16, -16, 1, 0, 128, 9, 9)
dark_fireball  = Object(-16, -16, 1, 0, 137, 9, 9)

spear = Object(-16, 76, 1, 128, 113, 15, 3)
items_list = [mystic_stone, coin, mushroom, staff, fireball, dark_fireball, spear]

# Entities
player = Entity(10, 68, 1, 0, 0, 16, 16, life= 3)
player.attack_item = fireball
player.staff = False

goblin_lancer = Entity(160, 68, 1, 0, 48, 16, 16, life= 3)
goblin_lancer.attack_item = spear

goblin_bomber = Entity(160, 68, 1, 0, 64, 16, 16, life= 2)

goblin_shaman = Entity(160, 68, 1, 0, 80, 16, 16, life= 4)
goblin_shaman.attack_item = dark_fireball

revived_goblin_shaman = Entity(160, 68, 1, 0, 96, 16, 16, life= 5)
revived_goblin_shaman.attack_item = dark_fireball

seller = Entity(160, 68, 1, 0, 112, 16, 16, life= 3)

# HUD
# Arte dos controles W A S D E
CONTROLS_CENTER_X = SCREEN_W/2 - (50/2)
CONTROLS_ENTER_Y = SCREEN_H/2 - (34/2) - 8
controls_animation = Object(CONTROLS_CENTER_X, CONTROLS_ENTER_Y, 0, 0, 100, 50, 34)
controls_animation.total_frames = 5