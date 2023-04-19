import csv
import pandas as pd
import file_processing as fp
import re

def read_data(file, data="TMEDIA", upper_date="20000101", lower_date="20201231"):
    return file.loc[upper_date:lower_date, [data]]


# --------------------------------FUNCIONES DE TRATAMIENTO DE FECHAS----------------------------------------------------
# Esta función devuelve la fecha de una serie según el índice
def get_date(data, i): return str(data.index[i]).split('-')[0]


# Esta función devuelve la fecha inicial de una serie
def get_first_date(data): return get_date(data, 0)


# Esta función devuelve el último año de una serie
def get_last_date(data): return get_date(data, (len(data) - 1))


# Esta función obtiene una lista con todos los años de una serie
def get_years(data):
    first_year = get_first_date(data).split('-')[0]
    last_year = get_last_date(data).split('-')[0]


# Esta función crea una serie temporal completa entre un año de inicio y un año final
def get_complete_date_serie(data): return pd.period_range(get_first_date(data), get_last_date(data))


# --------------------------------FUNCIONES DE TRATAMIENTO DE DATOS----------------------------------------------------
# Esta función rellena el array vacío creado en la función 'get_empty_array', con datos del array original
def fill_data_gaps(data, complete_date): return data.reindex(complete_date)


# Esta función coge solo los datos que tienen un valor distinto de cero
def get_not_null_values(data): return data[data.notnull()]


# Esta función coge solo los datos que tienen un valor de cero
def get_null_values(data): return data[data.isnull()]


# Esta función transforma los datos en str
def str_change(data):
    str_array = []
    for row in data:
        str_array.append(str(row))
    return str_array


# Esta función acota una serie de datos
def delimit_serie(data, upper_date, lower_date, column): return data.loc[upper_date:lower_date, [column]]

# ----------------------------------------------------------------------------------------------------------------
#
# for row in file_name_array:
#     # print(row)
#     data = dp.delimit_serie(fp.read_file(path, row), upper_date, lower_date, column)
#     filtro = (len(data) / total_number_data)
#     if filtro >= number_data_filter:
#         index = file_name_array.index(row)
#         data_array.append(data)
#         filtered_file_name_array.append(file_name_array[index])
#
#
# # Esta función obtiene el número total de datos de una serie
# def get_total_number_data(data): return len(data)
#
#
# # Esta función establece un filtro que discrimina estaciones con un % pobre de datos
# def get_discrime_data(data, total_number_data): return (len(data) / total_number_data)
#
#
# # Esta función obtiene una lista con todos los DataFrame de los archivos del directorio
# def get_data_frame_list(data, file_name_array, number_data_filter):
#     index = []
#     data_array = []
#     for row in file_name_array:
#         if get_discrime_data(data, get_total_number_data(data)) >= number_data_filter:
#                 index = file_name_array.index(row)
#                 data_array.append(data)
#                 filtered_file_name_array.append(file_name_array[index])

