import pygame
import random
import sys

from config.settings import *
from entities.jugador import Jugador
from entities.enemigo import Enemigo
from world.mapa import paredes, salida
from systems.camera import Camera
from sounds import *

pygame.init()

# --------------------------------------------------------------------------------
# Inicializar mixer de audio
# frecuancia=44100 Hz (calidad CD), size=16 bits, channels = 2 (estereo)
pygame.mixer.init(frequency=44100, size=16, channels=2, buffer=512)

# Numero de sonidos que pueden sonar al mismo tiempo
pygame.mixer.set_num_channels(8)

sonido_paso4 = pygame.mixer.Sound("sounds/paso4.wav")
sonido_paso1 = pygame.mixer.Sound("sounds/paso1.wav")
sonido_paso2 = pygame.mixer.Sound("sounds/paso2.wav")
sonido_paso3 = pygame.mixer.Sound("sounds/paso3.wav")
sonido_paso5 = pygame.mixer.Sound("sounds/paso5.wav")

sonido_aplauso = pygame.mixer.Sound("sounds/clap.wav")
sonido_aplauso.set_volume(0.2)

sonido_fondo = pygame.mixer.Sound("sounds/ambient.ogg")

#Variables para controlar cuando suena el paso
tiempo_ultimo_paso = 0
intervalo_pasos = 400 # ms entre cada paso
sonidos_base = [sonido_paso1, sonido_paso2, sonido_paso3, sonido_paso4, sonido_paso5]

#---------------------------------------------------------------------------------

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(TITULO)

reloj = pygame.time.Clock()

jugador = Jugador()

enemigos = [
    Enemigo(800, 1500),
    Enemigo(1400, 600)
]

camera = Camera()

#---------------------------------------------
# BUCLE DE EVENTOS
#---------------------------------------------
running = True

while running:

    ventana.fill(NEGRO)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            running = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jugador.emitir()
                sonido_aplauso.stop()
                sonido_aplauso.play()

    jugador.mover(paredes)

    camera.actualizar(jugador.rect)

    jugador.actualizar_ecos(
        ventana,
        paredes,
        salida,
        enemigos,
        camera.offset
    )

    for enemigo in enemigos:

        enemigo.actualizar(
            pygame.Vector2(jugador.rect.center)
        )

        enemigo.dibujar(
            ventana,
            camera.offset
        )

        if enemigo.colision_jugador(jugador.rect.center):

            print("GAME OVER")

            jugador = Jugador()

            enemigos = [
                Enemigo(800, 1500),
                Enemigo(1400, 600)
            ]

    pygame.draw.circle(
        ventana,
        ROJO,
        (ANCHO // 2, ALTO // 2),
        5
    )

    if salida.collidepoint(jugador.rect.center):

        print("ESCAPASTE")

        running = False

    pygame.display.flip()

    reloj.tick(FPS)

pygame.quit()
sys.exit()