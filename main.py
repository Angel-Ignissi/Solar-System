import pygame
import math

pygame.init()
WIDTH, HEIGHT = 800, 800
# WIN means window
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Solar System')

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
BLUE = (100, 149, 237)

class Planet:
    # e - означает умножение на 10
    # e6 - 10^6 и тд
    AU = 149.6e6 * 1000
    G = 6.67428e-11
    # масштаб
    SCALE = 250 / AU  # 1A.Е. = 100 пикселей
    TIMESTEP = 3600*24  # 1 день

    def __init__(self, x, y, radius, color, mass):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.mass = mass

        self.orbit = []
        self.sun = False
        self.distance_to_sun = 0

        self.x_vel = 0
        self.y_vel = 0

    def draw(self, win):
        x = self.x * self.SCALE + WIDTH / 2
        y = self.y * self.SCALE + HEIGHT / 2
        pygame.draw.circle(win, self.color, (x, y), self.radius)


def main():
    run = True
    clock = pygame.time.Clock()

    sun = Planet(0, 0, 30, YELLOW, 1.98892 * 10**30)
    sun.sun = True

    earth = Planet(-1 * Planet.AU, 0, 16, BLUE, 5.9742 * 10 ** 24)

    planets = [sun, earth]

    while run:
        clock.tick(60)  # сколько раз обновляем этот цикл в секунду

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        for planet in planets:
            # ('что').draw('где')
            planet.draw(WIN)

        pygame.display.update()

    pygame.quit()

main()
