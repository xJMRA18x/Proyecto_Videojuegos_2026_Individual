import pygame
import math


class Eco:

    def __init__(self, x, y, angulo):

        self.pos = pygame.Vector2(x, y)

        self.vel = pygame.Vector2(
            math.cos(angulo),
            math.sin(angulo)
        ) * 6

        self.vida = 255

    def actualizar(self):

        self.pos += self.vel

        self.vida -= 4