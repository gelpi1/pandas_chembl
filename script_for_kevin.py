import pandas
import csv
import pandas as pd
import numpy as np
from pandas import DataFrame
import matplotlib.pyplot as plt
import glob
from sklearn import datasets, linear_model
from scipy import linspace, polyval, polyfit, sqrt, stats, randn

fields = ['ASA']

#File1
data1 = pd.read_csv('data1_sample_file.csv',usecols=fields,low_memory=False) #read large csv filei



#File2
data2 = pd.read_csv('data2_sample_file.csv',usecols=fields,low_memory=False, index_col=False, header=0)

#create my x and y column for linear regression comparison based only on the ASA header
x = data1.ASA.values
y = data2.ASA.values



#print(x)
#print(y)



#plot it
slope, intercept, r_value, p_value, std_err = stats.linregress(x, y)
plt.plot(x,y, 'o')
plt.plot(x,intercept + slope*x, color="black", label='fitted line' + ',' + '$R^2$={:.4f}'.format(r_value))
plt.suptitle('MOE ASA Descriptor Correlation Plot', fontsize=14)
plt.xlabel('Ab Initio ASA', fontsize=16)
plt.ylabel('2-D ASA', fontsize=16)
plt.legend(loc=4)
plt.show()


