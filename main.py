from tasks import Task
from dynamic import LVSystem
import sys


def main():
    # set constants
    images_path = "/Users/alejandro/Dropbox (Personal)/Dissertation/Python Files/ESPD/images/"
    window_width = 1366
    window_height = 600
    limit_up = 150
    limit_down = window_height - 100
    color_blue = (0, 0, 255)
    color_red = (255, 0, 0)

    # set student number
    student = sys.argv[1]

    # # Task 1
    # env = Task(window_width, window_height, limit_up, limit_down,
    #            color_red, color_blue, images_path, 1)
    # env.task_1(1)

    # Task 2
    a = LVSystem(400, 100, 0.01, 2.5 / 40000, 0.01, 1.2 / 40000)
    time, fox_size, rabbit_size = a.simulate(int(window_width * 0.1))
    b0 = 30
    b1 = 0.8
    fox_size = [limit_down - m * b1 + b0 for m in fox_size]
    rabbit_size = [limit_down - m * b1 + b0 for m in rabbit_size]

    env = Task(window_width, window_height, limit_up, limit_down,
               color_red, color_blue, images_path, 1)
    env.task_2(2, student, time, fox_size, rabbit_size)


if __name__ == "__main__":
    main()
