from gameenvironment import GameEnvironment
from endtask import EndTask
from inittask import InitTask
import random
import pandas as pd


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

    def task_1(self, task_number, task_description):
        init_window = InitTask(self.window_width, self.window_height)
        init_window.start(1, task_description)

        env = GameEnvironment(self.window_width, self.window_height, self.limit_up, self.limit_down,
                              self.color_red, self.color_blue, self.images_path)

        # create two vectors with random marks
        mark1 = random.sample(range(self.limit_up + 100, self.limit_down - 100), 7)
        mark2 = random.sample(range(self.limit_up + 100, self.limit_down - 100), 7)
        i = 0

        # initialize task 1
        x = 600
        red_line = [(x, self.limit_down), (x, self.limit_down)]
        blue_line = [(x, self.limit_down), (x, self.limit_down)]

        # running = env.on_task(mark1[i], mark2[i], red_line, blue_line, task_number) is not None

        while i < 6:
            frame, right_hand, left_hand = env.on_task(mark1[i], mark2[i], red_line, blue_line, task_number)

            # set condition for new marker
            if mark1[i] - 5 <= left_hand <= mark1[i] + 5 and \
               mark2[i] - 5 <= right_hand <= mark2[i] + 5:
                    # print i
                i += 1

        task = EndTask(self.window_width, self.window_height)
        task.end(self.task_number)

    def task_2(self, task_number, task_description, student_number, time, fox_size, rabbit_size):
        init_window = InitTask(self.window_width, self.window_height)
        init_window.start(2, task_description)

        env = GameEnvironment(self.window_width, self.window_height, self.limit_up, self.limit_down,
                              self.color_red, self.color_blue, self.images_path)

        # load two vectors
        mark1 = rabbit_size
        mark2 = fox_size
        n_iter = len(time)
        i = 0

        # initialize task
        right_hand = []
        left_hand = []
        frame = []
        mark_right = []
        mark_left = []

        x = 600
        red_line = [(x, self.limit_down), (x, self.limit_down)]
        blue_line = [(x, self.limit_down), (x, self.limit_down)]

        # running = env.on_task(mark1[i], mark2[i], red_line, blue_line, task_number) is not None

        while i <= n_iter - 100:
            f, right, left = env.on_task(mark1[i], mark2[i], red_line, blue_line, task_number)
            right_hand.append(right)
            left_hand.append(left)
            frame.append(f)
            mark_right.append(mark1[i])
            mark_left.append(mark2[i])

            i += 5
            x += 1.4
            # red_line.append((x, left))
            # blue_line.append((x, right))
            red_line.append((x, mark1[i]))
            blue_line.append((x, mark2[i]))

        d = {"right_hand": pd.Series(right_hand),
             "left_hand": pd.Series(left_hand),
             "mark_right": pd.Series(mark_right),
             "mark_left": pd.Series(mark_left)}
        df = pd.DataFrame(d)

        file_folder = "/Users/alejandro/Dropbox (Personal)/Dissertation/Python Files/Student_files/"
        file_name = "S" + format(int(student_number), "03d") + \
                    "_task" + format(int(task_number), "03d") + ".csv"

        df.to_csv(file_folder + file_name, index=False)

        task = EndTask(self.window_width, self.window_height)
        task.end(task_number)
