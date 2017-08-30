import numpy as np


class LVSystem:
    def __init__(self, height=600, width=800, offset=60, frequency=5):
        self.height = height
        self.width = width
        self.offset = offset
        self.frequency = frequency

    def log_plot(self):
        wave_height = self.height / 5
        f = self.frequency
        fs = self.width * 2  # sample rate
        t = np.arange(fs)  # the points on the x axis for plotting

        # compute wave length
        fox_size = [int(wave_height * np.sin(2 * np.pi * f * (i + self.offset) / fs)) for i in t]  # Red line
        fox_size = [a + wave_height * 1 + 125 for a in fox_size]

        rabbit_size = [int(wave_height * np.sin(2 * np.pi * f * i / fs)) for i in t]  # Blue line
        rabbit_size = [a + wave_height * 2 + 125 for a in rabbit_size]

        return t, fox_size, rabbit_size


# import plotly
# from plotly.graph_objs import Scatter, Layout
# a = LVSystem()
# time, fox_size, rabbit_size = a.log_plot()
#
# plotly.offline.plot({
#     "data": [Scatter(x=time, y=fox_size, name="Fox"),
#              Scatter(x=time, y=rabbit_size, name="Rabbit")],
#     "layout": Layout(title="Predator-Prey Dynamic System")
# })
