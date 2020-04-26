import pandas as pd
import numpy as ny
import matplotlib.pyplot as ply
from statistics import mean


corona = pd.read_csv('almostthere.csv')
everylog = corona['Everylog']
days = corona['days']
ys = ny.array(everylog)
xs = ny.array(days)


def slope_and_intercept(xs, ys):
    slope = ((mean(xs)*mean(ys))-mean(xs*ys))/((mean(xs)*mean(xs))-mean(xs*xs))
    intercept = mean(ys) - slope*(mean(xs))
    return slope, intercept


m, c = slope_and_intercept(xs, ys)
print(m, c)


def regression(xs, slope, intercept):
    u = ny.array(slope*xs + intercept)
    return u


s = regression(xs, m, c)
print(s)

day = 69
predict = (m*day)+c
print(predict)
ply.scatter(xs, ys)
ply.plot(xs, s, color='green')
ply.scatter(day, predict, color='red')
ply.show()
