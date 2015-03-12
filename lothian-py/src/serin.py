'''
Created on Mar 8, 2015

@author: Henry Hinton, Pavle Jeremic, Eduardo Hirata
'''

from sys import argv
import numpy as np
import scipy
import matplotlib.pyplot as plt
import scipy.signal

filename = argv[1]
raw = []
time, vdiff = [], []
mains_freq = 60.0 # Hz  (Use 50Hz in Europe)

with open(filename, 'r') as txt: #open file
    for line in txt:
        if line.startswith('#'): #skip commented lines in header
            continue
        raw.append(line.rstrip('\n')) #strip newline delimiter
print("Using %d points." % len(raw)) #verify data
for index, x in enumerate(raw):
    raws = x.split('\t') #split raw lines into time & vdiff values
    print("%d, %s, %s" % (index, raws[0], raws[1])) #print values to console
    time.append(float(raws[0]))
    vdiff.append(float(raws[1]))
#Need to convert to Hz From Karplus file   
sampling_frequency = (len(time))/ (time[-1]- time [0])/ (time[-1]-time[0])
print("# sampling_frequency set to {:.6g} Hz".format(sampling_frequency))


# compute the sampling frequency (in Hz) 
# from the number of samples and the total duration
sampling_frequency= (len(time)-1)/ (time[-1] - time[0])

print("# sampling_frequency set to {:.6g} Hz".format(sampling_frequency))

#set the cutoff frequencies (but stay below Nyquist frequency (sampling_fequency/2))
low_band_cutoff = 0.3   # Hz
high_band_cutoff = min(100., 0.49*sampling_frequency)

# Scale cutoff frequencies in the manner needed by the iirfilter routine
low_over_Nyquist = low_band_cutoff/(0.5*sampling_frequency)
high_over_Nyquist = high_band_cutoff/(0.5*sampling_frequency)

# Construct a Bessel bandpass filter.
# Bessel was chosen to minimize time-domain distortion.
bess_b,bess_a = scipy.signal.iirfilter(5, 
Wn=[low_over_Nyquist,high_over_Nyquist],btype="bandpass",ftype='bessel')
filtered = scipy.signal.filtfilt(bess_b,bess_a,vdiff)

print("# Bessel bandpass filtered to {:.6g}Hz to {:.6g}Hz".format(low_band_cutoff, high_band_cutoff))

if mains_freq<high_band_cutoff:
    # mains frequency is in the pass band, 
    # so filter with a notch filter to remove it.
    mains_over_Nyquist = mains_freq/(0.5*sampling_frequency)

    notch_b,notch_a = scipy.signal.iirfilter(5,Wn=[mains_over_Nyquist*0.95, mains_over_Nyquist*1.05],btype="bandstop",ftype='bessel')
	
    filtered = scipy.signal.filtfilt(notch_b,notch_a,filtered)
print("# followed by notch {:.6g}Hz -- {:.6g}Hz".format(mains_freq*0.95, mains_freq*1.05))
    
for i in range (0, len(time)):
    print("%.7f  %.7f" % (time[i], vdiff[i]))

plt.plot(time, vdiff)

plt.show()
txt.close()