import pygame
import os


def load_image(name, (width, height)):
    fullname = os.path.join('images', name)
    try:
        image = pygame.image.load(fullname)
        image = pygame.transform.scale(image, (width, height))
    except pygame.error, message:
        print 'Cannot load image:', name
        raise SystemExit, message
    return image, image.get_rect()


class Fox(pygame.sprite.Sprite):
    def __init__(self, limit_down):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image("fox-drawing.jpg", (80, 80))
        self.rect.topleft = 85, limit_down + 5


class Rabbit(pygame.sprite.Sprite):
    def __init__(self, limit_down):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        self.image, self.rect = load_image("rabbit-drawing.jpg", (50, 80))
        self.rect.topleft = 270, limit_down + 5


class Foxes(pygame.sprite.Sprite):

    def __init__(self, limit_up, pop_size):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        if pop_size == 1:
            self.image, self.rect = load_image("foxes1.png", (180, 80))
        elif pop_size == 2:
            self.image, self.rect = load_image("foxes2.png", (180, 80))
        elif pop_size == 3:
            self.image, self.rect = load_image("foxes3.png", (180, 80))
        else:
            self.image, self.rect = load_image("foxes4.png", (180, 80))

        self.rect.topleft = 25, limit_up - 100


class Rabbits(pygame.sprite.Sprite):

    def __init__(self, limit_up, pop_size):
        pygame.sprite.Sprite.__init__(self)  # call Sprite initializer
        if pop_size == 1:
            self.image, self.rect = load_image("rabbits1.png", (180, 80))
        elif pop_size == 2:
            self.image, self.rect = load_image("rabbits2.png", (180, 80))
        elif pop_size == 3:
            self.image, self.rect = load_image("rabbits3.png", (180, 80))
        else:
            self.image, self.rect = load_image("rabbits4.png", (180, 80))

        self.rect.topleft = 200, limit_up - 100
