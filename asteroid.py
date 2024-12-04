from circleshape import CircleShape
import constants as c
import pygame
import random


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= c.ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)
            velocity1 = self.velocity.rotate(random_angle)

            velocity2 = self.velocity.rotate(-random_angle)
            asd1 = Asteroid(
                self.position.x, self.position.y, self.radius - c.ASTEROID_MIN_RADIUS
            )
            asd2 = Asteroid(
                self.position.x, self.position.y, self.radius - c.ASTEROID_MIN_RADIUS
            )
            asd1.velocity = velocity1 * 1.2
            asd2.velocity = velocity2 * 1.2
