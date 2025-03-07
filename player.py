import circleshape
import pygame
from shot import Shot
import constants as c


class Player(circleshape.CircleShape):
    rotation = 0
    timer = 0

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += c.PLAYER_TURN_SPEED * dt

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * c.PLAYER_SPEED * dt

    def shoot(self):
        if self.timer <= 0:
            shot = Shot(self.position.x, self.position.y, c.SHOT_RADIUS)
            forward = pygame.Vector2(0, 1).rotate(self.rotation)
            shot.velocity += forward * c.PLAYER_SHOOT_SPEED
            self.timer = c.PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()

        self.timer -= dt

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()
