'''
Created on Mar 10, 2015

@author: Henry Hinton, Pavle Jeremic, Eduardo Hirata
'''

from sys import argv
import numpy
import scipy
import matplotlib.pyplot as plt

filename = argv[1]
raw = []
time, vdiff = [], []
# print('Using file: ' + filename)

with open(filename, 'r') as txt: #open file
    for line in txt:
        if line.startswith('#'): #skip commented lines in header
            continue
        raw.append(line.rstrip('\n')) #strip newline delimiter
print("Using %d points." % len(raw)) #verify data
for index, x in enumerate(raw):
    raws = x.split('\t') #split raw lines into time & vdif values
    print("%d, %s, %s" % (index, raws[0], raws[1])) #print values to console
    time.append(float(raws[0]))
    vdiff.append(float(raws[1]))
    
plt.plot(time, vdiff) #plot points
plt.show() #display points
