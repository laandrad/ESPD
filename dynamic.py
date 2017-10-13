
class LVSystem:
    def __init__(self, init_prey, init_pred, prey_birth_rate, prey_predation_rate, pred_death_rate, pred_reprod_rate):
        self.x = init_prey
        self.y = init_pred
        self.a = prey_birth_rate
        self.b = prey_predation_rate
        self.m = pred_death_rate
        self.n = pred_reprod_rate

    def simulate(self, n_iter):
        x = self.x
        y = self.y

        prey = [x]
        pred = [y]

        for i in xrange(n_iter):
            x += self.a * x - self.b * x * y
            y += -self.m * y + self.n * x * y

            if x < 0:
                x = 0
            if y < 0:
                y = 0

            prey.append(x)
            pred.append(y)

        return range(0, n_iter), prey, pred


# a = LVSystem(800, 5, 0.005, 0.000625, 0.2, 0.0003)
# a = LVSystem(40, 20, 0.1, 0.003125, 0.02, 0.0025)
# a = LVSystem(400, 100, 0.01, 2.5 / 40000, 0.01, 1.2 / 40000)
# time, prey, pred = a.simulate(3000)
#
# import pandas as pd
#
# d = {"prey": pd.Series(prey),
#      "pred": pd.Series(pred)}
# df = pd.DataFrame(d)
# df.to_csv("/Users/alejandro/Dropbox (Personal)/Dissertation/Python Files/LVdynamic.csv")
#
# from plotly.graph_objs import Scatter, Layout
# plotly.offline.plot({
#     "data": [Scatter(x=time, y=prey, name="Prey", mode="lines"),
#              Scatter(x=time, y=pred, name="Predator", mode="lines")],
#     "layout": Layout(title="Predator-Prey Dynamic System")
# })
