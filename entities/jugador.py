import pygame
import math

from entities.eco import Eco
from config.settings import *


class Jugador:

    def __init__(self):

        self.rect = pygame.Rect(200, 200, 10, 10)

        self.vel = 2.2

        self.ecos = []

    def mover(self, paredes):

        teclas = pygame.key.get_pressed()

        dx, dy = 0, 0

        if teclas[pygame.K_w]:
            dy = -self.vel

        if teclas[pygame.K_s]:
            dy = self.vel

        if teclas[pygame.K_a]:
            dx = -self.vel

        if teclas[pygame.K_d]:
            dx = self.vel

        self.rect.x += dx

        colisiones = [
            p for p in paredes
            if self.rect.colliderect(p)
        ]

        for p in colisiones:

            if dx > 0:
                self.rect.right = p.left

            elif dx < 0:
                self.rect.left = p.right

        self.rect.y += dy

        colisiones = [
            p for p in paredes
            if self.rect.colliderect(p)
        ]

        for p in colisiones:

            if dy > 0:
                self.rect.bottom = p.top

            elif dy < 0:
                self.rect.top = p.bottom

    def emitir(self):

        for i in range(120):

            angulo = math.radians(
                i * (360 / 120)
            )

            self.ecos.append(
                Eco(
                    self.rect.centerx,
                    self.rect.centery,
                    angulo
                )
            )

    def actualizar_ecos(
        self,
        ventana,
        paredes,
        salida,
        enemigos,
        camera
    ):

        for eco in self.ecos[:]:

            eco.actualizar()

            for pared in paredes:

                if pared.collidepoint(eco.pos):

                    eco.vel *= -0.6

                    eco.vida -= 20

                    pygame.draw.rect(
                        ventana,
                        BLANCO,
                        pared.move(
                            -camera.x,
                            -camera.y
                        )
                    )

            if salida.collidepoint(eco.pos):

                pygame.draw.rect(
                    ventana,
                    AZUL,
                    salida.move(
                        -camera.x,
                        -camera.y
                    ),
                    2
                )

            for enemigo in enemigos:

                if enemigo.pos.distance_to(eco.pos) < 50:

                    enemigo.activo = True

            if eco.vida > 0:

                pygame.draw.circle(
                    ventana,
                    (eco.vida, eco.vida, eco.vida),
                    (
                        int(eco.pos.x - camera.x),
                        int(eco.pos.y - camera.y)
                    ),
                    2
                )

            else:

                self.ecos.remove(eco)