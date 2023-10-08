# -*- coding: utf-8 -*-
import pandas as pd

"""DATAFRAMES (MARCOS DE DATOS) A PARTIR DE LISTAS

La forma más fácil de generar dataframes es empleando la librería
pandas:
pip install pandas

Los dataframes son muy flexibles, podemos agregarles o 
eliminarles columnas.

Agregamos una columna empleando el nombre de data frame de laforma
nombre_df['nombre_columna'] = [dato1, dato2, ..., daton]

El método drop se emplea para eliminar columnas o filas en

"""

marcas_lst = ['tesla', 'ford', 'fiat']
models_lst = ['x', 'focus', 'doblo']
df = pd.DataFrame(data=list(zip(marcas_lst, models_lst)),
                  index=[1, 2, 3], columns=['Marca', 'Modelo'])

# show data frame
print(df)
print('-'*30)

# agregamos columna al datafrabe
df['Age'] = [2, 4, 3]
print(df)
print('-'*30)

# eliminamos columnas/renglones de un data frame
df.drop('Modelo', inplace=True, axis=1)
print(df)
