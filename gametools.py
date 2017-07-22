import inspect
import os
import sys

src_dir = os.path.dirname(inspect.getfile(inspect.currentframe()))
# Windows and Linux
arch_dir = '../lib/x64' if sys.maxsize > 2**32 else '../lib/x86'
# Mac
# arch_dir = os.path.abspath(os.path.join(src_dir, '../lib'))
sys.path.insert(0, os.path.abspath(os.path.join(src_dir, arch_dir)))

import Leap


class SampleListener(Leap.Listener):

    def on_connect(self, controller):
        print "Connected"

    def on_frame(self, controller):
        frame = controller.frame()
        right_hand = frame.hands.rightmost
        left_hand = frame.hands.leftmost

        if right_hand.is_right:
            right_hand_position = right_hand.palm_position[1]
        else:
            right_hand_position = 0

        if left_hand.is_left:
            left_hand_position = left_hand.palm_position[1]
        else:
            left_hand_position = 0

        return frame.id, right_hand_position, left_hand_position
