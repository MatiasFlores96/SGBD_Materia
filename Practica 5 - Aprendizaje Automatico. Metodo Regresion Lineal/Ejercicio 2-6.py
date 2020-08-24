#!/usr/bin/python3

import pandas as pd
import numpy as np
import statistics
from linear_algebra import vector_subtract, scalar_multiply
from stats import mean, correlation, standard_deviation, de_mean
from gradient_descent import minimize_stochastic
import math,random

data = pd.read_csv('dataset.csv')
caracteristicasPropiedades = []
valoresPropiedades = []
#random.seed(0)

for i, row in data.iterrows():
    ns = row['ns']
    mc = row['mc']
    ca = row['ca']
    caracteristicasPropiedad = [1, ns, mc, ca]
    caracteristicasPropiedades.append(caracteristicasPropiedad)
    
    valorPropiedad = row['vp']
    valoresPropiedades.append(valorPropiedad)

def in_random_order(data):
    indexes = [i for i, _ in enumerate(data)] 
    random.shuffle(indexes) 
    for i in indexes:
        yield data[i]

def minimize_stochastic(errorCuadratico, gradient_fn, caracteristicasPropiedades, valoresPropiedades, theta_0, alpha_0=0.01):
    data = list(zip(caracteristicasPropiedades, valoresPropiedades))
    theta = theta_0 
    alpha = alpha_0 
    min_theta, min_value = None, float("inf") 
    iterations_with_no_improvement = 0 
    while iterations_with_no_improvement < 100:
        value = sum(errorCuadratico(caracteristicasPropiedad_i, valorPropiedad_i, theta) for caracteristicasPropiedad_i, valorPropiedad_i in data)
        if value < min_value:
            min_theta, min_value = theta, value
            iterations_with_no_improvement = 0
            alpha = alpha_0
        else:
            iterations_with_no_improvement += 1
            alpha *= 0.9
        for caracteristicasPropiedad_i, valorPropiedad_i in in_random_order(data):
            gradient_i = gradient_fn(caracteristicasPropiedad_i, valorPropiedad_i, theta)
            theta = vector_subtract(theta, scalar_multiply(alpha, gradient_i))
    return min_theta

def estimarValor(caracteristicasPropiedad_i, betas):
    return np.dot(caracteristicasPropiedad_i, betas)

def errorCuadratico(caracteristicasPropiedad_i, valorPropiedad_i, betas):
    return ((valorPropiedad - (error(caracteristicasPropiedad_i, valorPropiedad_i, betas)) ** 2))

def error(caracteristicasPropiedad_i, valorPropiedad_i, betas):
    return valorPropiedad_i - estimarValor(caracteristicasPropiedad_i, betas)

def squared_error_gradient(caracteristicasPropiedad_i, valorPropiedad_i, betas):
    return [-2 * caracteristica * error(caracteristicasPropiedad_i, valorPropiedad_i, betas) for caracteristica in caracteristicasPropiedad_i]

def estimate_beta(caracteristicasPropiedades, valoresPropiedades):
    primerosBetas = [random.random() for caracteristicasPropiedad_i in caracteristicasPropiedades[0]]
    return minimize_stochastic(errorCuadratico, squared_error_gradient, caracteristicasPropiedades, valoresPropiedades, primerosBetas, 0.01)

def de_mean(x):
    x_bar = statistics.mean(x)
    return [x_i - x_bar for x_i in x]

def sum_of_squared_errors(caracteristicasPropiedades, valoresPropiedades, betas):
    return sum(error(caracteristicasPropiedad_i, valorPropiedad_i, betas) ** 2 for caracteristicasPropiedad_i, valorPropiedad_i in list(zip(caracteristicasPropiedades, valoresPropiedades)))

def total_sum_of_squares(arrayValoresPropiedades):
    return sum(v ** 2 for v in de_mean(arrayValoresPropiedades))

def multiple_r_squared(caracteristicasPropiedades, valoresPropiedades, betas):
    sum_of_squared_errors = sum(error(caracteristicasPropiedad_i, valorPropiedad_i, betas) ** 2 for caracteristicasPropiedad_i, valorPropiedad_i in list(zip(caracteristicasPropiedades, valoresPropiedades)))
    return 1.0 - sum_of_squared_errors / total_sum_of_squares(valoresPropiedades)

def bootstrap_sample(data):
	return [random.choice(data) for _ in data]

def estimate_sample_beta(sample):
    x_sample, y_sample = list(zip(*sample))
    return estimate_beta(x_sample, y_sample)
	
def bootstrap_statistic(data, num_samples):
	return [estimate_sample_beta(bootstrap_sample(data)) for _ in range(num_samples)]

print(bootstrap_statistic(list(zip(caracteristicasPropiedades, valoresPropiedades)), 100))
