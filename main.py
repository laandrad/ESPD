from tasks import Task
from plots import LVSystem

# set constants
images_path = "/Users/alejandro/Dropbox (Personal)/Dissertation/Python Files/ESPD/images/"
window_width = 1366
window_height = 600
limit_up = 150
limit_down = window_height - 100
color_blue = (0, 0, 255)
color_red = (255, 0, 0)


def main():
    # Task 1
    env = Task(window_width, window_height, limit_up, limit_down,
               color_red, color_blue, images_path, 1)
    env.task_1(1)

    # Task 2
    a = LVSystem()
    time, fox_size, rabbit_size = a.log_plot()
    env = Task(window_width, window_height, limit_up, limit_down,
               color_red, color_blue, images_path, 1)
    env.task_2(2, time, fox_size, rabbit_size)


if __name__ == "__main__":
    main()
