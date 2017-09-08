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
    color_blue = (33, 113, 181)
    color_red = (203, 24, 29)
    color_green = (35, 132, 67)

    # set student number
    student = sys.argv[1]

    # set plotting coordinates
    a = LVSystem(400, 100, 0.01, 2.5 / 40000, 0.01, 1.2 / 40000)
    time, fox_size, rabbit_size = a.simulate(int(window_width * 2))
    b0 = -20
    b1 = 0.6
    fox_size = [limit_down - m * b1 + b0 for m in fox_size]
    rabbit_size = [limit_down - m * b1 + b0 for m in rabbit_size]

    # initialize game environment
    env = Task(window_width, window_height, limit_up, limit_down,
               color_red, color_blue, color_green, images_path)

    # Task 1
    env.task_3(9)

    # Task 2
    env.task_4(10, student, time, fox_size, rabbit_size, canvas=False)

    # task 3
    env.task_4(11, student, time, fox_size, rabbit_size)

    # task 4
    env.task_4(12, student, time, fox_size, rabbit_size, track_right=True)

    # task 5
    env.task_4(13, student, time, fox_size, rabbit_size, track_left=True)

    # task 6
    env.task_4(14, student, time, fox_size, rabbit_size, canvas=False)

    # task 7
    env.task_4(15, student, time, fox_size, rabbit_size, canvas=False)

    # task 8
    env.task_4(16, student, time, fox_size, rabbit_size)


if __name__ == "__main__":
    main()
