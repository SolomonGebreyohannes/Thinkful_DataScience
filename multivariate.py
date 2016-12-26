import pandas as pd
import numpy as np
import statsmodels.api as sm

# Load the Lending Club Statistics 
loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')

int_rate = [float(value.rstrip('%')) for value in loansData['Interest.Rate']]
annual_inc = loansData['Monthly.Income']
fico = [int(val.split('-')[0]) for val in loansData['FICO.Range']]
 
# Use income (annual_inc) to model interest rates (int_rate)   
y = np.matrix(int_rate).transpose()
x1 = np.matrix(fico).transpose()
x2 = np.matrix(annual_inc).transpose()

x = np.column_stack([x1,x2])

X = sm.add_constant(x)
model = sm.OLS(y,X)
f = model.fit() 

print f.summary() 

# Add home ownership (home_ownership) to the model 
# TODO   