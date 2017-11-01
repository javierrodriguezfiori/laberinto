import pygame as pg
from settings import *

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.oro = 0
        self.llave = False
        self.x = x
        self.y = y

    def move(self, dx=0, dy=0):
        if self.collide_with_oro(dx, dy):
            self.oro += 1
            print(self.oro)
        if self.collide_with_llave(dx, dy):
            self.llave = True
            print(self.llave)
        if not self.collide_with_walls(dx, dy) and not self.collide_with_entrada(dx, dy) and not self.collide_with_salida(dx, dy) and not self.collide_with_guardia(dx, dy):
            self.x += dx
            self.y += dy
        if self.collide_with_guardia(dx, dy):
            print("Guardia muerto!")
            self.x += dx
            self.y += dy

        if self.collide_with_salida(dx, dy):
            if self.llave:
                print("Ganaste!")
            else:
                print("Te falta la llave, buscala!")

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def collide_with_oro(self, dx=0, dy=0):
        for oro in self.game.oros:
            if oro.x == self.x + dx and oro.y == self.y + dy:
                oro.kill()
                return True
        return False

    def collide_with_guardia(self, dx=0, dy=0):
        resultado = False
        for guardia in self.game.guardias:
            if guardia.x == self.x + dx and guardia.y == self.y + dy:
                if self.oro>0:
                    guardia.kill()
                    resultado = True
                else:
                    print("Perdiste!")
        return resultado

    def collide_with_llave(self, dx=0, dy=0):
        for llave in self.game.llaves:
            if llave.x == self.x + dx and llave.y == self.y + dy:
                llave.kill()
                return True
        return False

    def collide_with_entrada(self, dx=0, dy=0):
        for entrada in self.game.entradas:
            if entrada.x == self.x + dx and entrada.y == self.y + dy:
                return True
        return False

    def collide_with_salida(self, dx=0, dy=0):
        for salida in self.game.salidas:
            if salida.x == self.x + dx and salida.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * TILESIZE
        self.rect.y = self.y * TILESIZE

class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pg.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(LIGHTGREY)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Llave(pg.sprite.Sprite):
        def __init__(self, game, x, y):
            self.groups = game.all_sprites, game.llaves
            pg.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.image.fill(GREEN)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = x * TILESIZE
            self.rect.y = y * TILESIZE

class Entrada(pg.sprite.Sprite):
        def __init__(self, game, x, y):
            self.groups = game.all_sprites, game.entradas
            pg.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.image.fill(DARKGREY)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = x * TILESIZE
            self.rect.y = y * TILESIZE

class Salida(pg.sprite.Sprite):
        def __init__(self, game, x, y):
            self.groups = game.all_sprites, game.salidas
            pg.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.image.fill(DARKGREY)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = x * TILESIZE
            self.rect.y = y * TILESIZE

class Oro(pg.sprite.Sprite):
        def __init__(self, game, x, y):
            self.groups = game.all_sprites, game.oros
            pg.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.image.fill(YELLOW)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = x * TILESIZE
            self.rect.y = y * TILESIZE

class Guardia(pg.sprite.Sprite):
        def __init__(self, game, x, y):
            self.groups = game.all_sprites, game.guardias
            pg.sprite.Sprite.__init__(self, self.groups)
            self.game = game
            self.image = pg.Surface((TILESIZE, TILESIZE))
            self.image.fill(RED)
            self.rect = self.image.get_rect()
            self.x = x
            self.y = y
            self.rect.x = x * TILESIZE
            self.rect.y = y * TILESIZE
