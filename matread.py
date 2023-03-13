import scipy.io
import matplotlib.pyplot as plt
import numpy as np
import math
import scipy.stats
mat = scipy.io.loadmat(r'G:\_FAU matierals\Nerorscience movement\Exercise 1\Exercise 1\Slow_Contraction.mat')
mat2 = scipy.io.loadmat(r'G:\_FAU matierals\Nerorscience movement\Exercise 1\Exercise 1\Rapid_Contractions.mat')







print (len(mat["SIG"]))
print(mat["SIG"][0])
print (len(mat["SIG"][0][0]))
print (len(mat["SIG"][0][0][0]))





EMG=mat["SIG"][0][0][0]
ref_signal=mat["ref_signal"][0]
ref_signal_fast=mat2["ref_signal"][0]



for i in range (0,len(ref_signal)):
    ref_signal[i]=(ref_signal[i]/0.02)*9.81

for i in range (0,len(ref_signal_fast)):
    ref_signal_fast[i]=(ref_signal_fast[i]/0.02)*9.81



T=[]
for i in range (0,len(ref_signal)):
    T.append((1/2048)*i)


T2=[]
for i in range (0,len(ref_signal_fast)):
    T2.append((1/2048)*i)




print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
print(len(ref_signal_fast))


allSamplesArray=[]
for m in range(0,len(mat2["MUPulses"][0])):
    for s in range(0,len(mat2["MUPulses"][0][m][0])):
        allSamplesArray.append(mat2["MUPulses"][0][m][0][s])


print(max(allSamplesArray))







# plt.plot(T, ref_signal, color='r',label='Force')

# plt.plot(T, EMG, color='g',label='EMG')

plt.plot(T2, ref_signal_fast, color='g',label='Force_fast')


plt.xlabel('Time')
plt.ylabel('Tension')
plt.show()

samplinTimes=[]




for K in range(0,round(T2[len(T2)-1]/0.5)):
    T1= K*0.5
    # print(K)
    for K2 in range(0,len(T2)):
        # print(K2)
        if T2[K2]>T1:
            samplinTimes.append(K2-1)
            break

print("TheSamplingsAre" + str(len(samplinTimes)))

MaxArray=[]
for s in range (0,len(samplinTimes)-1):
    Max=0
    for timeM in range (samplinTimes[s],samplinTimes[s+1]):
        if(Max <ref_signal_fast[timeM]):
            Max=ref_signal_fast[timeM]
    MaxArray.append(Max)
    

RFDArray=[]
for Kr in range(0,len(MaxArray)):
    RFDArray.append(MaxArray[Kr]/0.5 )


print("!!!!!!!!!!!!!!")



rc=[]
for MKK in range(0,len(RFDArray)):
    rc.append(MKK)





mms=np.array(RFDArray)

print(mms)




plt.plot(rc, RFDArray, color='r',label='Force_fast')


plt.xlabel('ForceCases')
plt.ylabel('RFD')
plt.show()


RFDMean=np.mean(mms)
RFDMax=np.max(mms)

print("The mean is " + str(RFDMean) )
print("The Max is " + str(RFDMax) )







print("!!!!!!!!!!!!!!")






for s in range (0,len(ref_signal_fast)):
    pass
    #if (s%)




# plt.plot(T, signal, color='g', label='Signal')
# plt.plot(T, EMG, color='g',label='EMG')



npD=np.array(ref_signal)
CV=(np.std(npD)/np.mean(npD))*100
print("CV is")
print(CV)



TwoDArray=[]

for BigArray in mat["SIG"]:
    for smallArray in BigArray:
        TwoDArray.append(smallArray)



# so the idea here is taking avg of each 200 ms then go and take this RMS as the value, while the force we will take the avg then normalize both as graph later and get correlation


ActualTimeOfData=[]
for i in range (0,len(TwoDArray[0][0])):
    ActualTimeOfData.append((1/2048)*i)



print("The len of ActualTimeOfData of channel  is " + str(len(ActualTimeOfData)))


samplinTimes2=[]
for K in range(0,round(ActualTimeOfData[len(ActualTimeOfData)-1]/0.2)):
    T1= K*0.2
    print(K)
    for K2 in range(0,len(ActualTimeOfData)):
        # print(K2)
        if ActualTimeOfData[K2]>T1:
            samplinTimes2.append(K2-1)
            break

print("The len of AVG of channel  is " + str(len(samplinTimes2)))

AVGGArray=[]
TheMeanForceArray=[]
for s in range (0,len(samplinTimes2)-1):
    Themean=0
    TheMeanForce=0
    R=0
    for timeM in range (samplinTimes2[s],samplinTimes2[s+1]):
        Themean+=(TwoDArray[0][0][timeM])*(TwoDArray[0][0][timeM])
        TheMeanForce+=ref_signal[timeM]
        R=R+1
    if(R!=0):
        AVGGArray.append(math.sqrt(Themean/R))
        TheMeanForceArray.append(TheMeanForce/R)
    




rcmds=[]

for kn in range(0,len(AVGGArray)):
    rcmds.append(kn)




plt.plot(rcmds, AVGGArray, color='y',label='Force_fast')


plt.xlabel('cases')
plt.ylabel('RMS')
plt.show()


print("The len of RMS of channel  is " + str(len(AVGGArray)))

print("The len of ForceArray of channel  is " + str(len(TheMeanForceArray)))



#Normalization 


minForceee=9999
maxForceee=0

for m in TheMeanForceArray:
    if(m>=maxForceee):
        maxForceee=m
    if(m<=minForceee):
        minForceee=m


minRMS=9999
maxRMS=0

for m in AVGGArray:
    if(m>=maxRMS):
        maxRMS=m
    if(m<=minRMS):
        minRMS=m


for l in range(0,len(AVGGArray)):
    AVGGArray[l]=(AVGGArray[l]-minRMS)/(maxRMS-minRMS)
    TheMeanForceArray[l]=(TheMeanForceArray[l]-minForceee)/(maxForceee-minForceee)







plt.scatter( AVGGArray, TheMeanForceArray, color='b',label='RMS/Force')

plt.xlabel('RMS')
plt.ylabel('Tension')
plt.show()
print("The correlation is" + str(scipy.stats.pearsonr( AVGGArray, TheMeanForceArray)[0]))