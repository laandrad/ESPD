import pygame
import sys


class EndTask:
    def __init__(self, window_width, window_height, screen, color_green):
        self.window_width = window_width
        self.window_height = window_height
        self.screen = screen
        self.color_green = color_green

    def end(self, task_number, control=False):

        if control:
            task_number2 = task_number - 9
            total_tasks = 7
        else:
            task_number2 = task_number
            total_tasks = 9

        # screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption('ESPD - Task ' + str(task_number2))

        # initialize pygame setup
        pygame.init()

        # Create end of task window
        pygame.font.init()
        font = pygame.font.SysFont("comicsansms", 30)
        text1 = font.render("End of Task: " + str(task_number2) + " of " + str(total_tasks), 4, self.color_green)
        text2 = font.render("Good Job!", 4, self.color_green)
        text3 = font.render("Press Space to Continue", 4, self.color_green)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    pygame.quit()
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit(0)

            # self.screen.fill((255, 255, 255))
            self.screen.blit(text1, (self.window_width / 2 - text1.get_width() / 2, 30))
            self.screen.blit(text2, (self.window_width / 4, self.window_height * 2 / 6))
            self.screen.blit(text3, (self.window_width / 2 - text3.get_width() / 2, self.window_height * 7 / 8))

            # display and wait for tick
            pygame.display.flip()
