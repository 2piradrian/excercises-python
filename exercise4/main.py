import pandas as pd
import numpy as np


def print_something(something):
    print("----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----")
    print(something)


data = pd.read_csv('https://www.datos.gov.co/api/views/qijw-htwa/rows.csv?accessType=DOWNLOAD')

# Example
# print(data.sample(5))

# ¿Cuáles son las columnas? ¿Cuántas filas tiene?
data_shape = data.shape
print_something(f'Columns {data_shape[1]} - Rows {data_shape[0]}')

# Seleccionen los colegios donde la propiedad de la planta física sea de una persona natural o comunidad religiosa.
school_property_filtered = data.query(
    'propiedad_Planta_Fisica == "PERSONA NATURAL"'
    ' or '
    'propiedad_Planta_Fisica == "COMUNIDAD RELIGIOSA"'
)
print_something(school_property_filtered)

# ¿Hay alguno de estos colegios que sea para capacidades excepcionales?
with_special_capacities = school_property_filtered.query(
    'capacidades_Excepcionales == "CAPACIDADES EXCEPCIONALES"'
)
print_something(with_special_capacities)

# ¿Cuáles son los colegios que ofrecen todos los niveles educativos? ¿Qué idiomas ofrecen?
all_levels = data.query(
    'niveles == "PREESCOLAR,MEDIA,BÁSICA SECUNDARIA,BÁSICA PRIMARIA,PRIMERA INFANCIA"'
)
print_something(all_levels)
