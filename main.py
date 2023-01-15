import pygame
import sys


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, groups):
        # When creating Sprite Class you need this three things:

        # 1. init parent class sprite.Sprite
        super().__init__(groups)
        # 2. making a surface --> image
        self.image = pygame.image.load("./graphics/ship.png").convert_alpha()
        # 3. making a rectangle
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))


class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        # When creating Sprite Class you need this three things:

        # 1. init parent class sprite.Sprite
        super().__init__(groups)
        # 2. making a surface --> image
        self.image = pygame.image.load("./graphics/laser.png").convert_alpha()
        # 3. making a rectangle
        self.rect = self.image.get_rect(midbottom=pos)


class Asteroids(pygame.sprite.Sprite):
    def __init__(self, groups):
        # When creating Sprite Class you need this three things:

        # 1. init parent class sprite.Sprite
        super().__init__(groups)
        # 2. making a surface --> image
        self.image = pygame.image.load("./graphics/meteor.png").convert_alpha()
        # 3. making a rectangle
        self.rect = self.image.get_rect(midtop=(100, 100))

# basic setup
pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Asteroids")
clock = pygame.time.Clock()

# background screen
background = pygame.image.load("./graphics/background.png").convert()

# Sprite Group gives a object
spaceship_group = pygame.sprite.Group()
laser_group = pygame.sprite.Group()
asteroids_group = pygame.sprite.Group()

# create objects of Sprite Class
# Not yet visible because the sprite has tobe put into a group
spaceship = Spaceship(spaceship_group)
laser = Laser(laser_group, spaceship.rect.midtop)
asteroids = Asteroids(asteroids_group)

# game loop
while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # delta time
    dt = clock.tick() / 1000

    # drawing background
    screen.blit(background, (0, 0))
    # images : draws images on screen
    spaceship_group.draw(screen)
    laser_group.draw(screen)
    asteroids_group.draw(screen)
    # draw screen
    pygame.display.update()
