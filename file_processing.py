import pandas as pd
import os

def read_file(folder_path, file_name):
    # file_path = folder_path + '/' + file_name + '.csv'
    file_path = folder_path + '/' + str(file_name)
    station_file = pd.read_csv(file_path, sep=';', index_col='FECHA', encoding='latin-1')
    return station_file

# ----------------------------------------------------------------------------------------------------------

# Esta función obtiene una lista con todos los nombres de archivos guardados en el directorio
def get_names_files(folder_path): return os.listdir(folder_path)



