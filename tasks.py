from gameenvironment import GameEnvironment
from endtask import EndTask
import random


class Task:
    def __init__(self, window_width, window_height, limit_up, limit_down,
                 color_red, color_blue, images_path, task_number):
        self.window_width = window_width
        self.window_height = window_height
        self.limit_up = limit_up
        self.limit_down = limit_down
        self.color_red = color_red
        self.color_blue = color_blue
        self.images_path = images_path
        self.task_number = task_number

    def task_1(self, task_number):
        env = GameEnvironment(self.window_width, self.window_height, self.limit_up, self.limit_down,
                              self.color_red, self.color_blue, self.images_path)

        # create two vectors with random marks
        mark1 = random.sample(xrange(self.limit_up + 100, self.limit_down - 100), 7)
        mark2 = random.sample(xrange(self.limit_up + 100, self.limit_down - 100), 7)
        i = 0

        # initialize task 1
        while env.on_task(mark1[i], mark2[i], task_number) is not None:
            right_hand, left_hand = env.on_task(mark1[i], mark2[i], task_number)

            # set condition for new marker
            if i < 6:
                if mark1[i] - 5 <= left_hand <= mark1[i] + 5 and \
                 mark2[i] - 5 <= right_hand <= mark2[i] + 5:
                    # print i
                    i += 1
            else:
                return

        task = EndTask(self.window_width, self.window_height)
        task.end(self.task_number)

    def task_2(self, task_number, time, fox_size, rabbit_size):
        env = GameEnvironment(self.window_width, self.window_height, self.limit_up, self.limit_down,
                              self.color_red, self.color_blue, self.images_path)

        # load two vectors
        mark1 = rabbit_size
        mark2 = fox_size
        n_iter = len(time)
        i = 0

        # initialize task 1
        while env.on_task(mark1[i], mark2[i], task_number) is not None:

            if i >= n_iter:
                return
            else:
                right_hand, left_hand = env.on_task(mark1[i], mark2[i], task_number)
                i += 2

        task = EndTask(self.window_width, self.window_height)
        task.end(task_number)
