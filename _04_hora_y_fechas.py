# -*- coding: utf-8 -*-
from datetime import datetime, date

"""HORA Y FECHAS ACTUALES

Para el manejo de horas y fechas tenemos disponible el módulo
datetime.

datetime.now()
Retorna un datetime a patrir del time.time()

datetime.strftime()
Otorga un formato de salida a la hora .

Si se requiere trabajar con dias, podemos emplear la clase date
del mismo módulo.
"""

# ejemplo 1, hora actual
ahorita = datetime.now().strftime('%H:%M:%S')
print(f'Ahorita la hora es {ahorita}')

# ejemplo 2, dia actual
dia_de_hoy = date.today()
print(f'Hoy estamos a {dia_de_hoy}')
