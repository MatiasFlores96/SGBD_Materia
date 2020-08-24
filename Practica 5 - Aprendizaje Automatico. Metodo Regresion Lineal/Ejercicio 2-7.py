#!/usr/bin/python3

import pandas as pd
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

data = pd.read_csv('dataset.csv')
caracteristicasPropiedades = []
valoresPropiedades = []

for i, row in data.iterrows():
    ns = row['ns']
    mc = row['mc']
    ca = row['ca']
    caracteristicasPropiedad = [1, ns, mc, ca]
    caracteristicasPropiedades.append(caracteristicasPropiedad)
    
    valorPropiedad = row['vp']
    valoresPropiedades.append(valorPropiedad)

k = 10
cantS = int(len(caracteristicasPropiedades) / k)

v = []
mse = []

for i in range (0,cantS*k+1,cantS):
	v.append(i)

for i in range (0,k):

	data_X_train = caracteristicasPropiedades[:v[i]] + caracteristicasPropiedades[v[i+1]:]
	data_X_test = caracteristicasPropiedades[v[i]:v[i+1]]
	
	data_Y_train = valoresPropiedades[:v[i]] + valoresPropiedades[v[i+1]:]
	data_Y_test = valoresPropiedades[v[i]:v[i+1]]
	
	regr = linear_model.LinearRegression()
	regr.fit(data_X_train, data_Y_train)
	data_Y_pred = regr.predict(data_X_test)
	
	#print(regr.coef_)
	
	mse.append(mean_squared_error(data_Y_test, data_Y_pred))
	print("MSE-", i, "=", mse[i])

cv = (1 / k) * sum(i for i in mse)
print("CV = ", cv)
