'''
<<<<<<< HEAD
Created on Mar 8, 2015
=======
Created on Mar 10, 2015

>>>>>>> origin/master
@author: Henry Hinton, Pavle Jeremic, Eduardo Hirata
'''

from sys import argv
import numpy
import scipy
import scipy.signal
import matplotlib.pyplot as plt

filename = argv[1]
raw = []
time, vdiff = [], []
mainsfreq = 60.0 #Hz Mains frequency in the US

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

# #For the Passband filters a High cut-off and lowband cutoff is needed
# #Cutoff of high band should be < .5*samp_freq
# low_cutoff =
# high_cutoff =

# #Possible bandpass filters Bessell or Butter
# def butter_bandpass(lowcut, highcut, fs, order=5):
    # nyq = 0.5 * fs
    # low = lowcut / nyq
    # high = highcut / nyq
    # b, a = butter(order, [low, high], btype='band')
    # return b, a
	
# def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    # b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    # y = lfilter(b, a, data)
    # return 
	
# # # Scale cutoff frequencies in the manner needed by the iirfilter routine
# # low_over_Nyquist = low_band_cutoff/(0.5*sampling_frequency)
# # high_over_Nyquist = high_band_cutoff/(0.5*sampling_frequency)

# #Bessel Filter to preserve the wave shape of filtered signals in the passband

    # bessel_1,bessel_2 = scipy.signal.iirfilter(5, Wn=[low_over_Nyquist,high_over_Nyquist],btype="bandpass", ftype='bessel')
    # filtered = scipy.signal.filtfilt(bessel_1,bessel_2,vdiff)
    # print("# Bessel bandpass filtered to {:.6g}Hz to {:.6g}Hz".format(low_band_cutoff, high_band_cutoff))
	
# # #Cutoff Frequencies for Bandpass in Hz
# # low_band_cutoff = 0.3 
# # high_band_cutoff = min(100., 0.49*sampling_frequency)

# # if mainsfreq<high_band_cutoff:
    # # # mains frequency is in the pass band, 
    # # # so filter with a notch filter to remove it.
    # # mains_over_Nyquist = mainsfreq/(0.5*sampling_frequency)
    # # notch_b,notch_a = scipy.signal.iirfilter(5, Wn=[mains_over_Nyquist*0.95, mains_over_Nyquist*1.05],btype="bandstop",ftype='bessel')
    # # filtered = scipy.signal.filtfilt(notch_b,notch_a,filtered)
    # # print("# followed by notch {:.6g}Hz -- {:.6g}Hz".format(mains_freq*0.95, mains_freq*1.05))
    


plt.plot(time, vdiff) #plot points
plt.show() #display points
