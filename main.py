from gametools import *
from endtask import EndTask
from plots import LVSystem

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
    # Task 1
    env1 = GameEnvironment(window_width, window_height, limit_up, limit_down,
                               color_red, color_blue, images_path, 1)
    env1.task_1()
    task1 = EndTask(window_width, window_height)
    task1.end(1)

    # Task 2
    a = LVSystem()
    time, fox_size, rabbit_size = a.log_plot()
    env2 = GameEnvironment(window_width, window_height, limit_up, limit_down,
                               color_red, color_blue, images_path, 2)
    env2.task_2(time, fox_size, rabbit_size)
    task2 = EndTask(window_width, window_height)
    task2.end(2)

if __name__ == "__main__":
    main()
