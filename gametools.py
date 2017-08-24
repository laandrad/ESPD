import inspect
import os
import sys
import pygame

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# Windows and Linux
# arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
# Mac
arch_dir = os.path.abspath(os.path.join(src_dir, '../ESPD'))
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap


class SampleListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        frame = controller.frame()
        right_hand = frame.hands.rightmost
        left_hand = frame.hands.leftmost

        if right_hand.is_right:
            right_hand_position = right_hand.palm_position[1]
        else:
            right_hand_position = 0

        if left_hand.is_left:
            left_hand_position = left_hand.palm_position[1]
        else:
            left_hand_position = 0

        return frame.id, right_hand_position, left_hand_position


class GameEnvironment:

    def __init__(self, screen, frame, left_hand, right_hand, limit_up, limit_down,
                 color_red, color_blue, images_path):
        self.screen = screen
        self.frame = frame
        self.left_hand = left_hand
        self.right_hand = right_hand
        self.limit_up = limit_up
        self.limit_down = limit_down
        self.color_red = color_red
        self.color_blue = color_blue
        self.images_path = images_path

        if right_hand < limit_up:
            right_hand = limit_up
        if right_hand > limit_down:
            right_hand = limit_down

        if left_hand < limit_up:
            left_hand = limit_up
        if left_hand > limit_down:
            left_hand = limit_down

        print "Frame id: %d, right_hand_position: %d, left_hand_position: %d" % (
            frame, right_hand, left_hand)

        # get images
        fox = pygame.image.load(images_path + 'fox-drawing.jpg')
        fox = pygame.transform.scale(fox, (80, 80))
        rabbit = pygame.image.load(images_path + 'rabbit-drawing.jpg')
        rabbit = pygame.transform.scale(rabbit, (50, 80))

        if left_hand > limit_up * 3 / 4:
            foxes_image = 'foxes3.png'
        elif left_hand > limit_up * 2 / 4:
            foxes_image = 'foxes2.png'
        elif left_hand > limit_up * 1 / 4:
            foxes_image = 'foxes1.png'
        else:
            foxes_image = 'foxes4.png'

        if right_hand > limit_up * 3 / 4:
            rabbits_image = 'rabbits3.png'
        elif right_hand > limit_up * 2 / 4:
            rabbits_image = 'rabbits2.png'
        elif right_hand > limit_up * 1 / 4:
            rabbits_image = 'rabbits1.png'
        else:
            rabbits_image = 'rabbits4.png'

        foxes = pygame.image.load(images_path + foxes_image)
        foxes = pygame.transform.scale(foxes, (180, 80))
        rabbits = pygame.image.load(images_path + rabbits_image)
        rabbits = pygame.transform.scale(rabbits, (180, 80))

        # draw images
        screen.fill((255, 255, 255))
        screen.blit(fox, (85, limit_down + 5))
        screen.blit(rabbit, (270, limit_down + 5))
        screen.blit(foxes, (25, limit_up - 100))
        screen.blit(rabbits, (200, limit_up - 100))

        # create bar graphs
        pygame.draw.rect(screen, color_red, pygame.Rect(85, left_hand, 50, limit_down - left_hand))
        pygame.draw.rect(screen, color_blue, pygame.Rect(270, right_hand, 50, limit_down - right_hand))

    def task_1(self, mark1, mark2, i):

        if self.left_hand >= mark1 - 5 or self.left_hand <= mark1 + 5 and \
           self.right_hand >= mark2 - 5 or self.right_hand <= mark2 + 5:
                i += 1

        if i <= 5:
            pygame.draw.line(self.screen, (0, 0, 0), (85, mark1), (85 + 50, mark1), 5)
            pygame.draw.line(self.screen, (0, 0, 0), (270, mark2), (270 + 50, mark2), 5)
        else:
            pygame.quit()

    def task_2(self, mark1, mark2):
        pygame.draw.line(self.screen, (0, 0, 0), (85, mark1), (85 + 50, mark1), 5)
        pygame.draw.line(self.screen, (0, 0, 0), (270, mark2), (270 + 50, mark2), 5)

