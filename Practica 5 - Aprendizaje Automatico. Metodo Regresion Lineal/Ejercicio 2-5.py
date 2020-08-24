#!/usr/bin/python3

import pandas as pd
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv('dataset.csv')

data_X = []
data_Y = []

for i,row in data.iterrows():

	dataX = [1, row['ns'],row['mc'],row['ca']]
	dataY = row['vp']
	
	data_X.append(dataX)
	data_Y.append(dataY)

sampleLimit = round(len(data_Y) * 0.2)

data_X_train = data_X[:-sampleLimit]
data_X_test = data_X[-sampleLimit:]

data_Y_train = data_Y[:-sampleLimit]
data_Y_test = data_Y[-sampleLimit:]

regr = linear_model.LinearRegression()
regr.fit(data_X_train, data_Y_train)
data_Y_pred = regr.predict(data_X_test)

print('Coeficientes: \n', regr.coef_)
print("Error medio cuadrado: %.2f"
      % mean_squared_error(data_Y_test, data_Y_pred))
print('Puntaje de varianza: %.2f' % r2_score(data_Y_test, data_Y_pred))

