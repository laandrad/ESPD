from dynamic import LVSystem
import pandas as pd

a = LVSystem(400, 100, 0.01, 2.5 / 40000, 0.01, 1.2 / 40000)
time, prey, pred = a.simulate(3000)

d = {"prey": pd.Series(prey),
     "pred": pd.Series(pred)}
df = pd.DataFrame(d)

# compute velocity
df['vel_pred'] = df['pred'].shift(-1) - df['pred']
df['vel_prey'] = df['prey'].shift(-1) - df['prey']

# compute acceleration
df['acc_pred'] = df['vel_pred'].shift(-1) - df['vel_pred']
df['acc_prey'] = df['vel_prey'].shift(-1) - df['vel_prey']

# compute means
pred_mean, prey_mean = df.loc[:, ['vel_pred', 'vel_prey']].mean()
pred_sd, prey_sd = df.loc[:, ['vel_pred', 'vel_prey']].std()

# compute direction
df['dir_pred'] = (df['vel_pred'] - pred_mean) / pred_sd
df['dir_prey'] = (df['vel_prey'] - prey_mean) / prey_sd

dir_prey = []
for x in df['dir_prey']:
    if x > 0.5:
        dir_prey.append('up')
    elif x < -0.5:
        dir_prey.append('down')
    else:
        dir_prey.append('static')

dir_pred = []
for x in df['dir_pred']:
    if x > 0.5:
        dir_pred.append('up')
    elif x < -0.5:
        dir_pred.append('down')
    else:
        dir_pred.append('static')

df['dir_pred'] = dir_pred
df['dir_prey'] = dir_prey

dat = df.loc[:, ['dir_pred', 'vel_pred', 'acc_pred', 'dir_prey', 'vel_prey', 'acc_prey']]

dat.to_csv("/Users/alejandro/Dropbox (Personal)/Dissertation/Python Files/hmm_input.csv",
          index=False)
