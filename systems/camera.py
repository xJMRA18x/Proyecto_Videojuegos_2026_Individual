import pygame

from config.settings import *


class Camera:

    def __init__(self):

        self.offset = pygame.Vector2(0, 0)

    def actualizar(self, rect):

        self.offset.x = (
            rect.centerx - ANCHO // 2
        )

        self.offset.y = (
            rect.centery - ALTO // 2
        )