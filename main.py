import asteroid
import constants as c
import pygame
import player as p
import asteroid as a
import asteroidfield as af
from shot import Shot


def main():
    pygame.init()
    print("Starting asteroids!")
    screen = pygame.display.set_mode((c.SCREEN_WIDTH, c.SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    p.Player.containers = (updatable, drawable)
    a.Asteroid.containers = (updatable, drawable, asteroids)
    af.AsteroidField.containers = updatable
    Shot.containers = (updatable, drawable, shots)

    asteroid_field = af.AsteroidField()
    player = p.Player(c.SCREEN_WIDTH // 2, c.SCREEN_HEIGHT // 2, c.PLAYER_RADIUS)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for obj in updatable:
            obj.update(dt)

        screen.fill((0, 0, 0))

        for entity in drawable:
            entity.draw(screen)

        for ast in asteroids:
            if ast.check_collision(player):
                print("Game Over!")
                return
            for bullet in shots:
                if ast.check_collision(bullet):
                    bullet.kill()
                    ast.split()

        pygame.display.flip()

        dt = time.tick(60) / 1000


if __name__ == "__main__":
    main()
