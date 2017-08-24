from gametools import *
import random


def main():
    # set constants
    images_path = "/Users/alejandro/Dropbox (Personal)/Dissertation/Python Files/ESPD/images/"
    window_width = 1366
    window_height = 600
    limit_up = 150
    limit_down = window_height - 100
    color_blue = (0, 0, 255)
    color_red = (255, 0, 0)
    running = True

    mark1_t1 = random.sample(xrange(limit_up, limit_down), 5)
    mark2_t1 = random.sample(xrange(limit_up, limit_down), 5)

    mark1_t2 = range(100, 200)
    mark2_t2 = [300 - x for x in range(100, 200)]

    i = 1

    # initialize pygame setup
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('ESPD')
    clock = pygame.time.Clock()

    # Create a sample listener and controller for the LeapMotion sensor
    listener = SampleListener()
    controller = Leap.Controller()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                # running = False

        # get hands positions
        frame, right_hand, left_hand = listener.on_frame(controller)
        left_hand = limit_down - left_hand
        right_hand = limit_down - right_hand

        env1 = GameEnvironment(screen, frame, left_hand, right_hand, limit_up, limit_down,
                               color_red, color_blue, images_path)

        # if i >= 6:
        #     break
        # env1.task_1(mark1_t1[i], mark2_t1[i], i)

        env1.task_2(mark1_t2[i], mark2_t2[i])
        i += 1

        # display and wait for tick
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    main()
