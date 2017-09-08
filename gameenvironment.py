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

    def on_task(self, mark1, mark2, red_pointlist, blue_pointlist, task_number,
                track_right=True, track_left=True, plot=True, markers=True):

        screen = pygame.display.set_mode((self.window_width, self.window_height))

        pygame.display.set_caption('ESPD - Task ' + str(task_number))

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                return
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit(0)

        # get hands position
        frame, right_hand, left_hand, foxes_size, rabbits_size = listener.on_frame(controller,
                                                                                   self.limit_down,
                                                                                   self.limit_up,
                                                                                   track_right,
                                                                                   track_left)

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
        if track_left:
            pygame.draw.rect(screen, self.color_red,
                             pygame.Rect(85, left_hand, 50, self.limit_down - left_hand))
        elif not track_left:
            pygame.draw.rect(screen, self.color_red,
                             pygame.Rect(85, mark1, 50, self.limit_down - mark1))
        else:
            print "error on gameenvironment.py(on_task)"

        if track_right:
            pygame.draw.rect(screen, self.color_blue,
                             pygame.Rect(270, right_hand, 50, self.limit_down - right_hand))
        elif not track_right:
            pygame.draw.rect(screen, self.color_blue,
                             pygame.Rect(270, mark2, 50, self.limit_down - mark2))
        else:
            print "error on gameenvironment.py(on_task)"

        # Print markers
        if markers:
            pygame.draw.line(screen, (0, 0, 0), (85, mark1), (85 + 50, mark1), 5)
            pygame.draw.line(screen, (0, 0, 0), (270, mark2), (270 + 50, mark2), 5)
        else:
            pygame.draw.line(screen, (255, 255, 255), (85, mark1), (85 + 50, mark1), 5)
            pygame.draw.line(screen, (255, 255, 255), (270, mark2), (270 + 50, mark2), 5)

        # draw plot canvas
        if plot:
            pygame.draw.line(screen, (0, 0, 0), (600, self.limit_down),
                             (self.window_width - 20, self.limit_down), 5)  # Time axis
            pygame.draw.line(screen, (0, 0, 0), (600, self.limit_up - 50),
                             (600, self.limit_down), 5)  # population size axis
            pygame.font.init()
            font = pygame.font.SysFont("comicsansms", 20)
            x_lab = font.render("Time", 4, (0, 0, 0))
            y_lab = font.render("Population Size", 4, (0, 0, 0))
            y_lab = pygame.transform.rotate(y_lab, 90)
            screen.blit(x_lab, (self.window_width * 2 / 3 - x_lab.get_width() / 2, self.limit_down + 10))
            screen.blit(y_lab, (550, self.window_height / 2 - y_lab.get_height() / 2))

            # draw line plot
            pygame.draw.lines(screen, self.color_blue, False, blue_pointlist, 2)
            pygame.draw.lines(screen, self.color_red, False, red_pointlist, 2)

        # display and wait for tick
        pygame.display.flip()
        clock.tick(60)

        return frame, right_hand, left_hand, screen


