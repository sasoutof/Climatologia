import data_processing as dp
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt


def calculate_average(data):
    return data.mean()


def calculate_anomaly(data):
    return data - calculate_average(data)


# Esta función calcula la covarianza de 2 series
def get_covariance(data_array_1, data_array_2): return np.cov(data_array_1, data_array_2)


# Esta función calcula la correlación entre las dos series introducidas
def get_correlation(data_1, data_2): return np.corrcoef(data_1, data_2)



