
import mne # mne package used to read in the brain vision EEG and variable header data  
import numpy as np # used to perfrom mathematical compuations
from matplotlib import pyplot as plt # used for vizualizing data through plots
from scipy.stats import skew, kurtosis
import pywt

#reads in the sample .vhdr file. 
dat = mne.io.read_raw_brainvision('mTBI_P01_spectralContinuous.vhdr', 
                         montage=None,
                         eog=('HEOGL', 'HEOGR', 'VEOGb'), misc='auto',
                       scale=1., preload=True, response_trig_shift=0,
                        event_id=None, verbose='INFO');
    
#dat.plot(n_channels=64, scalings={"eeg": 75e-6}, events=events,
#         event_color={2: "green", 30: "blue", 4: "red"})

#saves the samlping frequency
sfreq = dat.info["sfreq"];
Ts = 1/sfreq;

#extracts the events from the EEG data
events = mne.find_events(dat,shortest_event=1,);

#counts the number of times each event occurs
eventCounts = np.unique(events[:,2], return_counts=True)

#extracts the event information for stimulus S40
epoch40 = events[np.where(events[:,2] ==  40 )];

#extracts the time stamps when stimulus S40 is applied
epochT40 = epoch40[:,0];

#determines the number of events
numEpochs40 = len(epochT40);

#creates a 3d array of zeros used to store 500ms of 64 channel eeg data 
epochDat40 = np.zeros((64,256,numEpochs40))

#loops through each time the event occurs
i = 0;
while i < numEpochs40:

    # extracts 500ms of EEEG data starting from when the event occurs
    data, times = dat[0:64, epochT40[i]:int(epochT40[i]+256)]
    
    #saves this event data to a new dimension
    epochDat40[:,:,i] = data;

    #adds 1 to counter variable i to continue the loop
    i = i + 1;

#calculates the average EEG value of each channel from all the events
meanDat40 = np.mean(epochDat40, axis=2);

#calculates the average EEG value from all of the channels 
meanDat40 = np.mean(meanDat40, axis=0);

#creates a 500ms time vector of 256 points     
times =  np.linspace(0, 500, num=256, endpoint=True);

#plots the average ERP from the stimulus
plt.plot(times,meanDat40, color = 'r', label = 'S40')
plt.title('average ERP from stimulus S40')
plt.ylabel('EEG Amplitude')
plt.xlabel('time (ms)')

epoch20 = events[np.where(events[:,2] ==  20 )];

epochT20 = epoch20[:,0];
numEpochs20 = len(epochT20);

#dat.plot(n_channels=64, scalings={"eeg": 75e-6}, events=events,
#         event_color={2: "green", 30: "blue", 4: "red"})

epochDat20 = np.zeros((64,256,numEpochs20))
i = 0;
while i < numEpochs20:


    data, times = dat[0:64, epochT20[i]:int(epochT20[i]+256)]
    
    epochDat20[:,:,i] = data;
    
    i = i + 1;

meanDat20 = np.mean(epochDat20, axis=2);

meanDat20 = np.mean(meanDat20, axis=0);
    
times =  np.linspace(0, 500, num=256, endpoint=True);

plt.plot(times,meanDat20, color = 'g', label = 'S20')
plt.title('average ERP from stimulus S40')
plt.ylabel('EEG Amplitude')
plt.xlabel('time (ms)')

epoch30 = events[np.where(events[:,2] ==  30 )];

epochT30 = epoch30[:,0];
numEpochs30 = len(epochT20);

#dat.plot(n_channels=64, scalings={"eeg": 75e-6}, events=events,
#         event_color={2: "green", 30: "blue", 4: "red"})

epochDat30 = np.zeros((64,256,numEpochs30))
i = 0;
while i < numEpochs30:


    data, times = dat[0:64, epochT30[i]:int(epochT30[i]+256)]
    
    epochDat30[:,:,i] = data;
    
    i = i + 1;

meanDat30 = np.mean(epochDat30, axis=2);

meanDat30 = np.mean(meanDat30, axis=0);
    
times =  np.linspace(0, 500, num=256, endpoint=True);

plt.plot(times,meanDat30, color = 'b', label = 'S30')
plt.title('average ERP from stimulus S30')
plt.ylabel('EEG Amplitude')
plt.xlabel('time (ms)')
plt.legend(loc='best')

skew20 = skew(meanDat20)
skew30 = skew(meanDat30)
skew40 = skew(meanDat40)

kurtosis20 = kurtosis(meanDat20)
kurtosis30 = kurtosis(meanDat30)
kurtosis40 = kurtosis(meanDat40)

fft20 = abs(np.fft.fft(meanDat20))
fft30 = abs(np.fft.fft(meanDat30))
fft40 = abs(np.fft.fft(meanDat40))

cA20, cD20 = pywt.dwt(meanDat20, 'db1')
cA30, cD30 = pywt.dwt(meanDat30, 'db1')
cA40, cD40 = pywt.dwt(meanDat40, 'db1')


freqs = np.arange(256);
T = 256/sfreq;
frq = freqs//T;
frq = int(frq)
ranges = 256/2;
ranges=int(range)
#frq = frq[range(256//2)];
#yOut = np.fft.fft(meanDat20)/256
#fft20 = yOut[range(256/2)]
#
#plt.plot(frq,abs(fft20))
