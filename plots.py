import math
import plotly
from plotly.graph_objs import Scatter, Layout


# logistic map
class LogisticMap:
    def __init__(self, birth_death_rate, carrying_fraction):
        self.R = birth_death_rate
        self.x = carrying_fraction

    def log_plot(self, n_iter):
        x = self.x
        vector = []

        for i in xrange(n_iter):
            y = self.R * x * (1 - x)
            x = y
            vector.append(y)

        return vector


a = LogisticMap(3.49, 0.2)
a = a.log_plot(50)
h = [h * 500 for h in a]
p = [p * 500 for p in a]


# plotly.offline.plot({
#     "data": [Scatter(x=range(0, len(a)), y=a)],
#     "layout": Layout(title="hello world")
# })


class LVSystem:
    def __init__(self, num_pred, num_prey,
                 birth_rate_prey, death_rate_pred,
                 death_rate_preyOverPred, birth_rate_predOverprey):
        self.P = num_pred
        self.H = num_prey
        self.a = birth_rate_prey
        self.b = death_rate_preyOverPred
        self.m = death_rate_pred
        self.n = birth_rate_predOverprey

    def log_plot(self, n_iter):
        y = self.P
        x = self.H

        pred = [y]
        prey = [x]

        for i in xrange(n_iter):
            y += -y * self.m + self.n * x * y
            x += x * self.a - self.b * x * y

            if x <= 0:
                x = 0
            if y <= 0:
                x = 0

            y = int(math.floor(y))
            x = int(math.floor(x))

            pred.append(y)
            prey.append(x)

        return pred, prey

# a = LVSystem(5, 30, 0.5, 0.08, 0.03, 0.020)
a = LVSystem(5, 30, 0.5, 0.08, 0.03, 0.02)
p, h = a.log_plot(50)

print a

plotly.offline.plot({
    "data": [Scatter(x=range(0, len(p)), y=p, name="Fox"),
             Scatter(x=range(0, len(h)), y=h, name="Rabbit")],
    "layout": Layout(title="Predator-Prey Dynamic System")
})
