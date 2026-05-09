import pygame
import sys

from config.settings import *
from entities.jugador import Jugador
from entities.enemigo import Enemigo
from world.mapa import paredes, salida
from systems.camera import Camera

pygame.init()

ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption(TITULO)

reloj = pygame.time.Clock()

jugador = Jugador()

enemigos = [
    Enemigo(800, 1500),
    Enemigo(1400, 600)
]

camera = Camera()

running = True

while running:

    ventana.fill(NEGRO)

    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:
            running = False

        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_SPACE:
                jugador.emitir()

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