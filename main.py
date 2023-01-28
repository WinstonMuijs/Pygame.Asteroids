import pygame
import sys


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, groups):
        # When creating Sprite Class you need this three things:

        # 1. init parent class sprite.Sprite
        super().__init__(groups)
        # 2. making a surface --> images
        self.image = pygame.image.load("./graphics/ship.png").convert_alpha()
        # 3. making a rectangle
        self.rect = self.image.get_rect(center=(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2))

        # timer
        self.can_shoot = True
        self.shoot_time = None

    # laser timer
    def laser_timer(self):
        if not self.can_shoot:
            current_time = pygame.time.get_ticks()
            if current_time - self.shoot_time > 500:
                self.can_shoot = True

    # positioning spaceship with mouse
    def spaceship_position(self):
        pos = pygame.mouse.get_pos()
        self.rect.center = pos

    # laser shooting
    def laser_shoot(self):
        if pygame.mouse.get_pressed()[0] and self.can_shoot:
            print('shoot laser')
            self.can_shoot = False
            self.shoot_time = pygame.time.get_ticks()

    # Creates lots of other methods within update and then in de game loop
    def update(self):
        self.laser_timer()
        self.spaceship_position()
        self.laser_shoot()


class Laser(pygame.sprite.Sprite):
    def __init__(self, groups, pos):
        # When creating Sprite Class you need this three things:

        # 1. init parent class sprite.Sprite
        super().__init__(groups)
        # 2. making a surface --> image
        self.image = pygame.image.load("./graphics/laser.png").convert_alpha()
        # 3. making a rectangle
        self.rect = self.image.get_rect(midbottom=pos)
        # 4. making a vector for the laser position
        self.pos = pygame.math.Vector2(self.rect.topleft)
        # 5. direction
        self.direction = pygame.math.Vector2(0, -1)
        # 6. speed
        self.speed = 600

    # laser position
    def laser_position(self):
        self.pos += self.direction * self.speed * dt
        self.rect.topleft = (round(self.pos.x), round(self.pos.y))

    def update(self):
        self.laser_position()


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

# Sprite Group gives an object

laser_group = pygame.sprite.Group()
asteroids_group = pygame.sprite.Group()
spaceship_group = pygame.sprite.Group()

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

    # update groups
    spaceship_group.update()
    laser_group.update()

    # images : draws images on screen

    laser_group.draw(screen)
    asteroids_group.draw(screen)
    spaceship_group.draw(screen)

    # draw screen
    pygame.display.update()
