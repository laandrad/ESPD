import inspect
import sys
import os

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# Windows and Linux
# arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
# Mac
arch_dir = os.path.abspath(os.path.join(src_dir, '../ESPD'))
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap


class SampleListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller, limit_down, limit_up):
        frame = controller.frame()
        right_hand = frame.hands.rightmost
        left_hand = frame.hands.leftmost

        if right_hand.is_right:
            right_hand = right_hand.palm_position[1]
        else:
            right_hand = 0

        if left_hand.is_left:
            left_hand = left_hand.palm_position[1]
        else:
            left_hand = 0

        left_hand = limit_down - left_hand
        right_hand = limit_down - right_hand

        # compare whether hands are within screen limits
        if right_hand < limit_up:
            right_hand = limit_up
        if right_hand > limit_down:
            right_hand = limit_down

        if left_hand < limit_up:
            left_hand = limit_up
        if left_hand > limit_down:
            left_hand = limit_down

        print "Frame id: %d, right_hand_position: %d, left_hand_position: %d" % (
            frame.id, right_hand, left_hand)

        # select what top image to display
        if left_hand > limit_down * 5 / 6:
            foxes_size = 1
        elif left_hand > limit_down * 4 / 6:
            foxes_size = 2
        elif left_hand > limit_down * 3 / 6:
            foxes_size = 3
        else:
            foxes_size = 4

        if right_hand > limit_down * 5 / 6:
            rabbits_size= 1
        elif right_hand > limit_down * 4 / 6:
            rabbits_size = 2
        elif right_hand > limit_down * 3 / 6:
            rabbits_size = 3
        else:
            rabbits_size = 4

        return frame.id, right_hand, left_hand, foxes_size, rabbits_size
