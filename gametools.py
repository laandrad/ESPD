import inspect
import os
import sys
import pygame
import random

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

    def __init__(self, window_width, window_height, limit_up, limit_down,
                 color_red, color_blue, images_path):
        self.window_width = window_width
        self.window_height = window_height
        self.limit_up = limit_up
        self.limit_down = limit_down
        self.color_red = color_red
        self.color_blue = color_blue
        self.images_path = images_path

        # declare global variables
        global fox
        global rabbit
        global foxes1
        global foxes2
        global foxes3
        global foxes4
        global rabbits1
        global rabbits2
        global rabbits3
        global rabbits4
        # global screen
        global clock
        global listener
        global controller
        # global screen2
        global text1
        global text2

        # initialize pygame setup
        pygame.init()
        # screen = pygame.display.set_mode((window_width, window_height))
        clock = pygame.time.Clock()

        # get images
        fox = pygame.image.load(images_path + 'fox-drawing.jpg')
        fox = pygame.transform.scale(fox, (80, 80))

        rabbit = pygame.image.load(images_path + 'rabbit-drawing.jpg')
        rabbit = pygame.transform.scale(rabbit, (50, 80))

        foxes1 = pygame.image.load(images_path + "foxes1.png")
        foxes1 = pygame.transform.scale(foxes1, (180, 80))
        foxes2 = pygame.image.load(images_path + "foxes2.png")
        foxes2 = pygame.transform.scale(foxes2, (180, 80))
        foxes3 = pygame.image.load(images_path + "foxes3.png")
        foxes3 = pygame.transform.scale(foxes3, (180, 80))
        foxes4 = pygame.image.load(images_path + "foxes4.png")
        foxes4 = pygame.transform.scale(foxes4, (180, 80))

        rabbits1 = pygame.image.load(images_path + "rabbits1.png")
        rabbits1 = pygame.transform.scale(rabbits1, (180, 80))
        rabbits2 = pygame.image.load(images_path + "rabbits2.png")
        rabbits2 = pygame.transform.scale(rabbits2, (180, 80))
        rabbits3 = pygame.image.load(images_path + "rabbits3.png")
        rabbits3 = pygame.transform.scale(rabbits3, (180, 80))
        rabbits4 = pygame.image.load(images_path + "rabbits4.png")
        rabbits4 = pygame.transform.scale(rabbits4, (180, 80))

        # Create a sample listener and controller for the LeapMotion sensor
        listener = SampleListener()
        controller = Leap.Controller()

        # Create end of task window
        pygame.font.init()
        font = pygame.font.SysFont("comicsansms", 50)
        text1 = font.render("End of Task", 4, (0, 0, 0))
        text2 = font.render("Press Space to Continue", 4, (0, 0, 0))

    def task_1(self):
        # screen = pygame.display.set_mode((self.window_width, self.window_height))
        # pygame.display.set_caption('ESPD - Task 1')
        #
        # # create two vectors with random marks
        # mark1 = random.sample(xrange(self.limit_up + 100, self.limit_down - 100), 7)
        # mark2 = random.sample(xrange(self.limit_up + 100, self.limit_down - 100), 7)
        # i = 0
        #
        # # initialize task 1
        # while i < 6:
        #     for event in pygame.event.get():
        #         if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        #             pygame.quit()
        #             return
        #     # get hands positions
        #     frame, right_hand, left_hand = listener.on_frame(controller)
        #     left_hand = self.limit_down - left_hand
        #     right_hand = self.limit_down - right_hand
        #
        #     # compare whether hands are within screen limits
        #     if right_hand < self.limit_up:
        #         right_hand = self.limit_up
        #     if right_hand > self.limit_down:
        #         right_hand = self.limit_down
        #
        #     if left_hand < self.limit_up:
        #         left_hand = self.limit_up
        #     if left_hand > self.limit_down:
        #         left_hand = self.limit_down
        #
        #     # print "Frame id: %d, right_hand_position: %d, left_hand_position: %d" % (
        #     #     frame, right_hand, left_hand)
        #
        #     # select what top image to display
        #     if left_hand > self.limit_up * 3 / 4:
        #         foxes_image = foxes3
        #     elif left_hand > self.limit_up * 2 / 4:
        #         foxes_image = foxes2
        #     elif left_hand > self.limit_up * 1 / 4:
        #         foxes_image = foxes1
        #     else:
        #         foxes_image = foxes4
        #
        #     if right_hand > self.limit_up * 3 / 4:
        #         rabbits_image = rabbits3
        #     elif right_hand > self.limit_up * 2 / 4:
        #         rabbits_image = rabbits2
        #     elif right_hand > self.limit_up * 1 / 4:
        #         rabbits_image = rabbits1
        #     else:
        #         rabbits_image = rabbits4
        #
        #     # set condition for new marker
        #     if mark1[i] - 5 <= left_hand <= mark1[i] + 5 and \
        #        mark2[i] - 5 <= right_hand <= mark2[i] + 5:
        #         # print i
        #         i += 1
        #
        #     # draw images
        #     screen.fill((255, 255, 255))
        #     screen.blit(fox, (85, self.limit_down + 5))
        #     screen.blit(rabbit, (270, self.limit_down + 5))
        #     screen.blit(foxes_image, (25, self.limit_up - 100))
        #     screen.blit(rabbits_image, (200, self.limit_up - 100))
        #
        #     # create bar graphs
        #     pygame.draw.rect(screen, self.color_red,
        #                      pygame.Rect(85, left_hand, 50, self.limit_down - left_hand))
        #     pygame.draw.rect(screen, self.color_blue,
        #                      pygame.Rect(270, right_hand, 50, self.limit_down - right_hand))
        #     pygame.draw.line(screen, (0, 0, 0), (85, mark1[i]), (85 + 50, mark1[i]), 5)
        #     pygame.draw.line(screen, (0, 0, 0), (270, mark2[i]), (270 + 50, mark2[i]), 5)
        #
        #     # display and wait for tick
        #     pygame.display.flip()
        #     clock.tick(60)

        # when task ends print end of task screen
        screen2 = pygame.display.set_mode((800, 400))
        pygame.display.set_caption('End of Task 1')

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    pygame.quit()
                    return

            screen2.fill((255, 255, 255))
            screen2.blit(text1, (400 - text1.get_width() / 2, 100))
            screen2.blit(text2, (400 - text2.get_width() / 2, 200))

            # display and wait for tick
            pygame.display.flip()
            clock.tick(60)

    def task_2(self):
        screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption('ESPD - Task 2')
        running = True
        # create two vectors
        mark1 = range(100, 200)
        mark2 = [300 - x for x in range(100, 200)]
        i = 0

        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
            # get hands positions
            frame, right_hand, left_hand = listener.on_frame(controller)
            left_hand = self.limit_down - left_hand
            right_hand = self.limit_down - right_hand

            # compare whether hands are within screen limits
            if right_hand < self.limit_up:
                right_hand = self.limit_up
            if right_hand > self.limit_down:
                right_hand = self.limit_down

            if left_hand < self.limit_up:
                left_hand = self.limit_up
            if left_hand > self.limit_down:
                left_hand = self.limit_down

            print "Frame id: %d, right_hand_position: %d, left_hand_position: %d" % (
                frame, right_hand, left_hand)

            # select what top image to display
            if left_hand > self.limit_up * 3 / 4:
                foxes_image = foxes3
            elif left_hand > self.limit_up * 2 / 4:
                foxes_image = foxes2
            elif left_hand > self.limit_up * 1 / 4:
                foxes_image = foxes1
            else:
                foxes_image = foxes4

            if right_hand > self.limit_up * 3 / 4:
                rabbits_image = rabbits3
            elif right_hand > self.limit_up * 2 / 4:
                rabbits_image = rabbits2
            elif right_hand > self.limit_up * 1 / 4:
                rabbits_image = rabbits1
            else:
                rabbits_image = rabbits4

            # set condition for new marker
            if i == len(mark1):
                running = False
            i += 1

            # draw images
            screen.fill((255, 255, 255))
            screen.blit(fox, (85, self.limit_down + 5))
            screen.blit(rabbit, (270, self.limit_down + 5))
            screen.blit(foxes_image, (25, self.limit_up - 100))
            screen.blit(rabbits_image, (200, self.limit_up - 100))

            # create bar graphs
            pygame.draw.rect(screen, self.color_red,
                             pygame.Rect(85, left_hand, 50, self.limit_down - left_hand))
            pygame.draw.rect(screen, self.color_blue,
                             pygame.Rect(270, right_hand, 50, self.limit_down - right_hand))
            pygame.draw.line(screen, (0, 0, 0), (85, mark1[i]), (85 + 50, mark1[i]), 5)
            pygame.draw.line(screen, (0, 0, 0), (270, mark2[i]), (270 + 50, mark2[i]), 5)

            # display and wait for tick
            pygame.display.flip()
            clock.tick(60)

        # when task ends print end of task screen
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    pygame.quit()
                    return

            screen2.fill((255, 255, 255))
            screen2.blit(text1, (400 - text1.get_width() / 2, 100))
            screen2.blit(text2, (400 - text2.get_width() / 2, 200))

            # display and wait for tick
            pygame.display.flip()
            clock.tick(60)

