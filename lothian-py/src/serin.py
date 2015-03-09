'''
Created on Mar 8, 2015

@author: Henry Hinton, Pavle Jeremic, Eduardo Hirata
'''

from sys import argv
import numpy
import scipy
import matplotlib.pyplot as plt

time = []
vol = []

filename = argv[1]

txt = open(filename, 'r')
print('Using file: ' + filename)
for line in txt:
    if line.startswith('#'):
        continue
    fields = map(float, line.split())
    if len(fields) >= 2:
        time.append(fields[0])
        vol.append(fields[1])
print("Using %d values" % len(time))

for i in range (0, len(time)):
    print("%.7f  %.7f" % (time[i], vol[i]))
plt.plot(time, vol)

plt.show()
txt.close()
