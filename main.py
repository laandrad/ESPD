import sys
import timeit

from dynamic import LVSystem
from tasks import Task


def main():

    big_tic = timeit.default_timer()

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
    env.task_1(1)

    # task 2
    env.task_2(2, student, time, fox_size, rabbit_size, track_right=False)

    # task 3
    env.task_2(3, student, time, fox_size, rabbit_size, track_left=False)

    # task 4
    env.task_2(4, student, time, fox_size, rabbit_size)

    # task 5
    env.task_2(5, student, time, fox_size, rabbit_size, markers=False, track_right=False)

    # task 6
    env.task_2(6, student, time, fox_size, rabbit_size, markers=False, track_left=False)

    # task 7
    env.task_2(7, student, time, fox_size, rabbit_size, markers=False)

    # compute total time
    big_toc = timeit.default_timer()
    print "total interview time:", (big_toc - big_tic) / 60

if __name__ == "__main__":
    main()
