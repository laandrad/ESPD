from myleaptools import *
from pygametools import *


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
        global clock
        global listener
        global controller

        # initialize pygame setup
        pygame.init()
        clock = pygame.time.Clock()

        # Create a sample listener and controller for the LeapMotion sensor
        listener = SampleListener()
        controller = Leap.Controller()

    def on_task(self, mark1, mark2, task_number):
        screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption('ESPD - Task ' + str(task_number))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                return

        # get hands position
        frame, right_hand, left_hand, foxes_size, rabbits_size = listener.on_frame(controller,
                                                                                   self.limit_down,
                                                                                   self.limit_up)

        # Load images as sprites
        fox = Fox(self.limit_down)
        rabbit = Rabbit(self.limit_down)
        foxes = Foxes(self.limit_up, foxes_size)
        rabbits = Rabbits(self.limit_up, rabbits_size)
        all_sprites = pygame.sprite.RenderPlain((fox, rabbit), foxes, rabbits)

        # draw images
        screen.fill((255, 255, 255))
        all_sprites.draw(screen)

        # create bar graphs
        pygame.draw.rect(screen, self.color_red,
                         pygame.Rect(85, left_hand, 50, self.limit_down - left_hand))
        pygame.draw.rect(screen, self.color_blue,
                         pygame.Rect(270, right_hand, 50, self.limit_down - right_hand))
        pygame.draw.line(screen, (0, 0, 0), (85, mark1), (85 + 50, mark1), 5)
        pygame.draw.line(screen, (0, 0, 0), (270, mark2), (270 + 50, mark2), 5)

        # display and wait for tick
        pygame.display.flip()
        clock.tick(60)

        return right_hand, left_hand


