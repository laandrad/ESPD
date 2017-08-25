from gametools import *

# set constants
images_path = "/Users/alejandro/Dropbox (Personal)/Dissertation/Python Files/ESPD/images/"
window_width = 1366
window_height = 600
limit_up = 150
limit_down = window_height - 100
color_blue = (0, 0, 255)
color_red = (255, 0, 0)
running = True




def main():
        env1 = GameEnvironment(window_width, window_height, limit_up, limit_down,
                               color_red, color_blue, images_path)

        # if i >= 6:
        #     break
        env1.task_2()
        # for i in xrange(mark1_t2):
        #     env1.task_2(mark1_t2[i], mark2_t2[i])
        # i += 1


if __name__ == "__main__":
    main()
