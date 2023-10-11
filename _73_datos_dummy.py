# -*- coding: utf-8 -*-
import pandas as pd
from faker import Faker


"""GENERACIÓN DE DATOS DUMMY

Empleando la librería Faker podemos generar diferentes tipos de
datos falsos."""

# faker instance
fake = Faker()

# show ten countries
for _ in range(10):
    print(fake.country())

profiles = [fake.simple_profile() for _ in range(10)]
df = pd.DataFrame(profiles)
print(df)
