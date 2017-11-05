import time
from game import *

# Main

# Input de usuario y password

# Conectar a la base y validar credenciales

# Instanciar juego e iniciar el loop
g = Game()
while True:
    g.new()
    g.run()
    if Partida.gano:
        g.show_ganaste()
    elif Partida.perdio:
        g.show_perdiste()
    time.sleep(2)
    g.quit()
