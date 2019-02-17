import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import csv

x = []
maxAirAccel = []
baseAirAccel = []
totalAirAccel = []
airSpd = []
maxFallSpd = []
fastFallSpd = []
initDash = []
runSpd = []
walkSpd = []
weight = []

with open('./data/smash.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(str(row[0]))
        maxAirAccel.append(float(row[1]))
        baseAirAccel.append(float(row[2]))
        totalAirAccel.append(float(row[3]))
        airSpd.append(float(row[4]))
        maxFallSpd.append(float(row[5]))
        fastFallSpd.append(float(row[6]))
        initDash.append(float(row[8]))
        runSpd.append(float(row[9]))
        walkSpd.append(float(row[10]))
        weight.append(float(row[11]))


plt.figure(figsize=(200, 8))
plt.scatter(x,initDash, color='red')
plt.scatter(x,runSpd, color='green')
plt.scatter(x,walkSpd, color='yellow')
plt.scatter(x,airSpd, color='blue')
plt.scatter(x,totalAirAccel, color='orange')

red_patch = mpatches.Patch(color='red', label='Initial Dash')
green_patch = mpatches.Patch(color='green', label='Run Speed')
yellow_patch = mpatches.Patch(color='yellow', label='Walk Speed')
blue_patch = mpatches.Patch(color='blue', label='Air Speed')
orange_patch = mpatches.Patch(color='orange', label='Total Air Accel')



plt.xlabel('Fighter')
plt.xticks(rotation=90)
plt.title('Smash Ultimate\nStats by Fighter')
plt.legend(handles=[red_patch, green_patch, yellow_patch, blue_patch, orange_patch])
plt.show()
