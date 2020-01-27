#importing the data
import pandas as pd
data=pd.read_table(r"/home/pi/pulse.txt",header=None,usecols=[0,1,2,3])
print (data)
import statistics
 #getting mode of Temperature
Temp=statistics.mode(data[1])
print (Temp)
#print ("Temp is % s" % Temp)
#getting mode of Pulse rate
HBM=statistics.mode(data[3])
print (HBM)
#print ("Pulse Rate is % s" % HBM)
