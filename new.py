import numpy as np 
import pandas as pd
from numpy import genfromtxt
from IPython.display import display
import array
import math

in_file = 'titanic_train_data.csv'
full_data = pd.read_csv(in_file)
cabin_data = full_data['Cabin']
cabin_list = cabin_data.tolist()

x = []
i=0
for i in range(len(cabin_list)):
	if type(cabin_list[i]) == float:
		x.append(cabin_list[i])
	i=i+1
print(x)

print(len(cabin_list))
print(len(x))

new_full_data = full_data.drop('Cabin',1)
print(new_full_data.head())
print(len(new_full_data))
print(new_full_data.shape[1])
print(new_full_data.shape[0])
print(full_data.shape[1])

age_data = full_data['Age']
age_list = age_data.tolist()
print(len(age_list))
y=[]
age_array = np.asarray(age_list)
for j in range(len(age_list)):
	if np.isnan(age_array[j]):
		y.append(age_array[j])
	j=j+1
print(y)
print(len(y))
print(len(full_data))
age_array[np.isnan(age_array)] = 29.6991176471
final = age_array.tolist()
print(final)
