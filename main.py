import pygame

from gametools import *


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

    # initialize pygame setup
    pygame.init()
    screen = pygame.display.set_mode((window_width, window_height))
    pygame.display.set_caption('ESPD')
    clock = pygame.time.Clock()

    # get images
    fox = pygame.image.load(images_path + 'fox-drawing.jpg')
    fox = pygame.transform.scale(fox, (80, 80))
    rabbit = pygame.image.load(images_path + 'rabbit-drawing.jpg')
    rabbit = pygame.transform.scale(rabbit, (50, 80))

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

        screen.fill((255, 255, 255))
        screen.blit(fox, (50, limit_down))
        screen.blit(rabbit, (200, limit_down))
        pygame.draw.rect(screen, color_red, pygame.Rect(50, left_hand, 50, limit_down - left_hand))
        pygame.draw.rect(screen, color_blue, pygame.Rect(200, right_hand, 50, limit_down - right_hand))

        pygame.display.flip()
        clock.tick(60)

    # # Have the sample listener receive events from the controller
    # controller.add_listener(listener)

    # Keep this process running until Enter is pressed
    # print "Press Enter to quit..."
    # try:
    #     sys.stdin.readline()
    # except KeyboardInterrupt:
    #     pass


if __name__ == "__main__":
    main()
