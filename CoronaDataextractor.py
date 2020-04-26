import pandas as pd
import requests as rq
import json
import numpy as ny
from numpy import array

url = 'https://corona.lmao.ninja/v2/historical/India?lastdays=55'
r = rq.get(url)


timeline = json.loads(r.text)['timeline']
cases = (timeline['cases'])
deaths = timeline['deaths']
recovery = timeline['recovered']

datec = cases.keys()
numbers = (cases.values())

dated = deaths.keys()
bodies = deaths.values()

dateh = recovery.keys()
healthy = recovery.values()

cas = []
dc = []
dea = []
dd = []
rec = []
drec = []

for i in numbers:
    temp = i
    cas.append(temp)
for d in datec:
    temp = d
    dc.append(d)

for b in bodies:
    temp = b
    dea.append(b)
for d in dated:
    temp = d
    dd.append(d)

for h in healthy:
    temp = h
    rec.append(h)
for d in dateh:
    temp = d
    drec.append(d)

#(dc)
#(cas)
#(dd)
#(dea)
#(drec)
#(rec)

corona = pd.DataFrame({'Date': dc, 'Cases found': cas, 'Deaths dates': dd, 'Deaths': dea, 'Recovery date': drec, 'Recovered': rec})
#print(corona)

#corona.to_csv('CoronaData.csv')

cases = corona['Cases found']
new_cases = ny.array([cases])
new_cases = new_cases.reshape(-1,1)
#print(new_cases)

everyday = []
i = 0
j = i+1
while i < len(cas)-2 & j < len(cas)-1:
    everyday.append(cas[j]-cas[i])
    i += 1
    j += 1

print(everyday)
