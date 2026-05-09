import pygame


class Enemigo:

    def __init__(self, x, y):

        self.pos = pygame.Vector2(x, y)

        self.velocidad = 1.5

        self.activo = False

    def actualizar(self, jugador_pos):

        if self.activo:

            direccion = jugador_pos - self.pos

            if direccion.length() != 0:

                self.pos += (
                    direccion.normalize()
                    * self.velocidad
                )

    def dibujar(self, ventana, camera):

        pygame.draw.circle(
            ventana,
            (150, 0, 0),
            (
                int(self.pos.x - camera.x),
                int(self.pos.y - camera.y)
            ),
            8
        )

    def colision_jugador(self, jugador_pos):

        return self.pos.distance_to(jugador_pos) < 15