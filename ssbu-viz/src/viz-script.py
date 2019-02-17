import matplotlib.pyplot as plt
import numpy as np
import csv

x = []
y = []

with open('./data/initDash.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(str(row[0]))
        y.append(float(row[1]))

plt.figure(figsize=(200, 8))
plt.plot(x,y, 'ro')

plt.xlabel('Fighter')
plt.xticks(rotation=90)
plt.ylabel('Initial Dash')
plt.title('Smash Ultimate\nInitial Dash Values by Fighter\nSorted by Weight')
plt.legend()
plt.show()
