import numpy as np 
import pandas as pd
from numpy import genfromtxt
from IPython.display import display
import array
import math

in_file = 'titanic_train_data.csv'
full_data = pd.read_csv(in_file)
cabin_data = full_data['Cabin']

for data in cabin_data:
	x = data
	final = []
	if x == 'nan':
		final.append(x)
	print(final)


	



