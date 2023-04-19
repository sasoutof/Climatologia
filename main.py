import os
import pandas as pd

import data_processing
import data_processing as dp
import file_processing as fp
import data_calculations as dc
import numpy as np


# path = '/home/santiago/Documentos/CLIMATOLOGIA/ESTUDIO CLIMATICO/GALICIA'
path = '/home/santiago/Documentos/CLIMATOLOGIA/DATOS ESTACIONES/DatosPorEstacion - 2022-02-02'
reference_file_name = '1428-19431101-20220202.csv'
upper_date = '1990-01-01'
lower_date = '2020-01-01'
column = 'TMEDIA'
number_data_filter = 0.75
data_array = []
index = []
filtered_file_name_array = []
filled_serie_array = []
# Creamos una lista con todas las estaciones del directorio.
file_name_array = fp.get_names_files(path)
# Eliminamos la estación de referencia de la lista.
file_name_array.remove(reference_file_name)
# Creamos un DF con la estación de referencia
reference_data = dp.delimit_serie(fp.read_file(path, reference_file_name), upper_date, lower_date, column)
# Creamos una variable que contiene el número total de datos del DF de referencia
total_number_data = len(reference_data)
# Creamos una lista con una serie temporal completa
complete_date = dp.get_complete_date_serie(reference_data)

# for row in file_name_array:
#     # print(row)
#     data = dp.delimit_serie(fp.read_file(path, row), upper_date, lower_date, column)
#     filtro = (len(data) / total_number_data)
#     if filtro >= number_data_filter:
#         index = file_name_array.index(row)
#         data_array.append(data)
#         filtered_file_name_array.append(file_name_array[index])


reference_filled_serie = dp.fill_data_gaps(reference_data, dp.str_change(complete_date))
for row in data_array:
    filled_serie_array.append(dp.fill_data_gaps(row, dp.str_change(complete_date)))
data = reference_data
for row in filled_serie_array:
    data = pd.concat([data, row], axis=1)
columns = []
for row in filtered_file_name_array:
    columns.append(column + '-' + filtered_file_name_array[filtered_file_name_array.index(row)].split('-')[0])
columns.insert(0, (column + '-' + reference_file_name.split('-')[0]))
data.columns = columns
clean_data = data.dropna()
correlations_array = []
for row in columns:
    correlations_array.append(
        [columns[columns.index(row)], round(np.corrcoef(clean_data['TMEDIA-1428'], clean_data[row])[0][1], 3)])
# for row in correlations_array:
#     print(row)
# AHORA VAMOS A SACAR LAS CORRELACIONES ESTACIONALES
# VERANO 21 DE JUNIO - 23 DE SEPTIEMBRE
upper_year = 1990
lower_year = 2020
veranos = clean_data.loc[str(upper_year) + '-06-21':str(lower_year) + '-09-23', columns]

for row in columns:
    correlations_array.append(
        [columns[columns.index(row)], round(np.corrcoef(veranos['TMEDIA-1428'], veranos[row])[0][1], 3)])
# print(veranos['TMEDIA-1475X'])
for row in correlations_array:
    if row[1] >= 0.98:
        print('Estacion ' + str(row[0]) + ' ' + 'correlación = ' + str(row[1]))
