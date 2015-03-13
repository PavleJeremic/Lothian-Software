'''
Created on Mar 13, 2015

@author: Henry Hinton, Pavle Jeremic, Eduardo Hirata
'''
from __future__ import print_function, division

from sys import argv
import numpy as np
import scipy
import matplotlib.pyplot as plt
import scipy.signal

try:
    from itertools import izip as zip
except ImportError: # will be 3.x series
    pass

# variables we want
filename = argv[1]
raw = []
time, vdiff = [], []
mains_freq = 60.0  # Hz  (Use 50Hz in Europe)
numpoints = 0

with open(filename, 'r') as txt:  # open file
    for line in txt:
        if line.startswith('#'):  # skip commented lines in header
            continue
        raw.append(line.rstrip('\n'))  # strip newline delimiter
print("Using %d points." % len(raw))  # verify data
for index, x in enumerate(raw):
    raws = x.split('\t')  # split raw lines into time & vdiff values
    print("%d, %s, %s" % (index, raws[0], raws[1]))  # print values to console
    time.append(float(raws[0]))
    vdiff.append(float(raws[1]))

numpoints = len(time)


# At this point, we have two lists: [time] and [vdiff]

# compute the sampling frequency (in Hz) 
# from the number of samples and the total duration
<<<<<<< HEAD
sampling_frequency= (len(time)-1)/ (time[-1] - time[0])  #Cite Karplus's Code
=======
sampling_frequency = (numpoints - 1) / (time[-1] - time[0])  # read and write speed
nyquist = (0.5 * sampling_frequency)
>>>>>>> origin/master


print("# sampling_frequency set to %.6g Hz" % sampling_frequency)

# set the cutoff frequencies (but stay below nyquist frequency (sampling_fequency/2))
low_band_cutoff = 0.3  # Hz
high_band_cutoff = min(100.0, 0.49 * sampling_frequency)

# Scale cutoff frequencies in the manner needed by the iirfilter routine
low_over_nyquist = low_band_cutoff / nyquist
high_over_nyquist = high_band_cutoff / nyquist

# Construct a Bessel bandpass filter.
# Bessel was chosen to minimize time-domain distortion.
bess_b, bess_a = scipy.signal.iirfilter(5, Wn=[low_over_nyquist, high_over_nyquist], btype="bandpass", ftype='bessel')  # initial frequency filtering
filtered = scipy.signal.filtfilt(bess_b, bess_a, vdiff)  # filter error from bessel filter (non-ideal)

print("# Bessel bandpass filtered to {:.6g}Hz to {:.6g}Hz".format(low_band_cutoff, high_band_cutoff))

if mains_freq < high_band_cutoff:
    # mains frequency is in the pass band, 
    # so filter with a notch filter to remove it.
<<<<<<< HEAD
    mains_over_Nyquist = mains_freq/(0.5*sampling_frequency)

    notch_b,notch_a = scipy.signal.iirfilter(5,Wn=[mains_over_Nyquist*0.95, mains_over_Nyquist*1.05],btype="bandstop",ftype='bessel')
	
    filtered = scipy.signal.filtfilt(notch_b,notch_a,filtered)
	
print("# followed by notch {:.6g}Hz -- {:.6g}Hz".format(mains_freq*0.95, mains_freq*1.05))

for t,n in izip(times,filtered):
	print("{:.7f}\t{:.6f}".format(t,n))
	
plt.plot() (t,n)
=======
    mains_over_nyquist = mains_freq / nyquist
    # fifth order function, 5% around mains
    notch_b, notch_a = scipy.signal.iirfilter(5, Wn=[mains_over_nyquist * 0.95, mains_over_nyquist * 1.05], btype="bandstop", ftype='bessel')
    
    # error attentuation
    filtered = scipy.signal.filtfilt(notch_b, notch_a, filtered)
print("# followed by notch {:.6g}Hz -- {:.6g}Hz".format(mains_freq * 0.95, mains_freq * 1.05))
    
for t, n in zip(time, filtered):
    print("%.7f'\t'%.6f" % (t, n))
    
plt.plot(time, filtered)
>>>>>>> origin/master
plt.show()
txt.close()
