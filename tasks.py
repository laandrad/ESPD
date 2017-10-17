from gameenvironment import GameEnvironment
from endtask import EndTask
from inittask import InitTask
import random
import pandas as pd
import pygame


class Task:
    def __init__(self, window_width, window_height, limit_up, limit_down,
                 color_red, color_blue, color_green, images_path):
        self.window_width = window_width
        self.window_height = window_height
        self.limit_up = limit_up
        self.limit_down = limit_down
        self.color_red = color_red
        self.color_blue = color_blue
        self.color_green = color_green
        self.images_path = images_path

    def task_1(self, task_number):
        init_window = InitTask(self.window_width, self.window_height)
        init_window.start(task_number)

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

        while i < 6:
            environment = env.on_task(mark1[i], mark2[i], red_line, blue_line, task_number, plot=False)
            if environment is not None:
                frame, right_hand, left_hand, screen = environment
            else:
                return

            # set condition for new marker
            if mark1[i] - 5 <= left_hand <= mark1[i] + 5 and \
               mark2[i] - 5 <= right_hand <= mark2[i] + 5:
                    # print i
                i += 1

        task = EndTask(self.window_width, self.window_height, screen, self.color_green)
        task.end(task_number)

    def task_2(self, task_number, student_number, time, fox_size, rabbit_size,
               track_right=True, track_left=True, canvas=True, markers=True):
        init_window = InitTask(self.window_width, self.window_height)
        init_window.start(task_number)

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

        while i <= n_iter - 10:
            environment = env.on_task(mark1[i], mark2[i], red_line, blue_line, task_number,
                                      track_right, track_left, canvas, markers)
            if environment is not None:
                f, right, left, screen = environment
            else:
                return

            right_hand.append(right)
            left_hand.append(left)
            frame.append(f)
            mark_right.append(mark1[i])
            mark_left.append(mark2[i])

            i += 3
            x += 0.75

            if track_left:
                red_line.append((x, left))
            elif not track_left:
                red_line.append((x, mark1[i]))
            else:
                print "error on task.py(task_2)"

            if track_right:
                blue_line.append((x, right))
            elif not track_right:
                blue_line.append((x, mark2[i]))
            else:
                print "error on task.py(task_2)"

        d = {"right_hand": pd.Series(right_hand),
             "left_hand": pd.Series(left_hand),
             "mark_right": pd.Series(mark_right),
             "mark_left": pd.Series(mark_left)}
        df = pd.DataFrame(d)

        file_folder = "/Users/alejandro/Dropbox (Personal)/Dissertation/Python Files/Student_files/"
        file_name = "S" + format(int(student_number), "03d") + \
                    "_task" + format(int(task_number), "03d") + ".csv"

        df.to_csv(file_folder + file_name, index=False)

        pygame.image.save(screen, file_folder + file_name[:-4] + ".png")

        task = EndTask(self.window_width, self.window_height, screen, self.color_green)
        task.end(task_number)

    def task_3(self, task_number):
        init_window = InitTask(self.window_width, self.window_height)
        init_window.start(task_number, control=True)

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

        while i < 6:
            environment = env.on_task(mark1[i], mark2[i], red_line, blue_line, task_number, plot=False,
                                      track_left=False, track_right=False, markers=False)
            if environment is not None:
                f, right, left, screen = environment
            else:
                return

            # set condition for new marker
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    i += 1

        task = EndTask(self.window_width, self.window_height, screen, self.color_green)
        task.end(task_number, control=True)

    def task_4(self, task_number, student_number, time, fox_size, rabbit_size,
               track_right=False, track_left=False, canvas=True, markers=False):
        init_window = InitTask(self.window_width, self.window_height)
        init_window.start(task_number, control=True)

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

        while i <= n_iter - 10:
            environment = env.on_task(mark1[i], mark2[i], red_line, blue_line, task_number,
                                      track_right, track_left, canvas, markers)
            if environment is not None:
                f, right, left, screen = environment
            else:
                return

            right_hand.append(right)
            left_hand.append(left)
            frame.append(f)
            mark_right.append(mark1[i])
            mark_left.append(mark2[i])

            i += 2
            x += 0.5

            if track_left:
                red_line.append((x, left))
            elif not track_left:
                red_line.append((x, mark1[i]))
            else:
                print "error on task.py(task_2)"

            if track_right:
                blue_line.append((x, right))
            elif not track_right:
                blue_line.append((x, mark2[i]))
            else:
                print "error on task.py(task_2)"

        task = EndTask(self.window_width, self.window_height, screen, self.color_green)
        task.end(task_number, control=True)
