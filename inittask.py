import pygame


class InitTask:
    def __init__(self, window_width, window_height):
        self.window_width = window_width
        self.window_height = window_height

        with open("taskdescription.txt", "r") as f:
            task_description = file.readlines(f)

        task_description = [w.strip("\n") for w in task_description]

        global task_description

    def start(self, task_number):
        screen = pygame.display.set_mode((self.window_width, self.window_height))
        pygame.display.set_caption('ESPD - Task ' + str(task_number))

        # initialize pygame setup
        pygame.init()

        # Create end of task window
        pygame.font.init()
        font1 = pygame.font.SysFont("comicsansms", 30)
        text1 = font1.render("Task: " + str(task_number) + " of 9", 4, (0, 0, 0))
        text2 = font1.render(task_description[task_number], 4, (0, 0, 0))
        text3 = font1.render("Press Space to Start", 4, (0, 0, 0))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    pygame.quit()
                    return

            screen.fill((255, 255, 255))
            screen.blit(text1, (self.window_width / 2 - text1.get_width() / 2, self.window_height * 1 / 6))
            screen.blit(text2, (self.window_width / 2 - text2.get_width() / 2, self.window_height * 2 / 6))
            screen.blit(text3, (self.window_width / 2 - text3.get_width() / 2, self.window_height * 4 / 6))

            # display and wait for tick
            pygame.display.flip()

