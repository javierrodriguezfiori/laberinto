import pygame as pg
from settings import *
import sys
import socket
from sprites import *
from os import path
import pickle
from mapeo import *

class Game:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        pg.key.set_repeat(500, 100)
        self.request_map()

    def request_map(self):
        try:
            sock = socket.socket()
            sock.connect((host,port))
            try:
                sock.sendall("map")
            except:
                print "No se pudo enviar la peticion"
            try:
                data = sock.recv(4096)
                data_string = pickle.loads(data)
                self.map_data = data_string
            except:
                print("No se pudo recibir el mapa")
        except:
            print("No se pudo contactar al servidor")
            sys.exit()

    def new(self):
        # initialize all variables and do all the setup for a new game
        self.all_sprites = pg.sprite.Group()
        self.walls = pg.sprite.Group()
        self.llaves = pg.sprite.Group()
        self.entradas = pg.sprite.Group()
        self.salidas = pg.sprite.Group()
        self.oros = pg.sprite.Group()
        self.guardias = pg.sprite.Group()
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == 'P':
                    Wall(self, col, row)
                if tile == 'J':
                    self.player = Player(self, col, row)
                if tile == 'L':
                    Llave(self, col, row)
                if tile == 'E':
                    Entrada(self, col, row)
                if tile == 'S':
                    Salida(self, col, row)
                if tile == 'O':
                    Oro(self, col, row)
                if tile == 'G':
                    Guardia(self, col, row)
        self.camera = Camera(1024, 768)

    def run(self):
        # Loop del juego
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(FPS) / 1000
            self.events()
            self.update()
            self.draw()
            if Partida.gano or Partida.perdio:
                self.playing = False

    def quit(self):
        # Metodo de salida del juego
        pg.quit()
        sys.exit()

    def update(self):
        # Actualizar imagen
        self.all_sprites.update()
        self.camera.update(self.player)

    def draw_grid(self):
        # Metodo de dibujo de grilla
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (x, 0), (x, HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.screen, LIGHTGREY, (0, y), (WIDTH, y))

    def draw(self):
        # Dibujar fondo, grilla y sprites
        self.screen.fill(BGCOLOR)
        # self.draw_grid()
        #self.all_sprites.draw(self.screen)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        pg.display.flip()

    def events(self):
        # Eventos
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
                if event.key == pg.K_LEFT:
                    self.player.move(dx=-1)
                if event.key == pg.K_RIGHT:
                    self.player.move(dx=1)
                if event.key == pg.K_UP:
                    self.player.move(dy=-1)
                if event.key == pg.K_DOWN:
                    self.player.move(dy=1)

    def show_ganaste(self):
        fondo = pg.image.load("images/youwin.jpg")
        self.screen.blit(fondo, (0, 0))
        pg.display.flip()
        for event in pg.event.get():
            if event.key == pg.K_ESCAPE:
                self.quit()

    def show_perdiste(self):
        fondo = pg.image.load("images/gameover.png")
        self.screen.blit(fondo, (0, 0))
        pg.display.flip()
        for event in pg.event.get():
            if event.key == pg.K_ESCAPE:
                self.quit()
