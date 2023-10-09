# -*- coding: utf-8 -*-
from forex_python.converter import CurrencyRates

"""CONVERTIDOR DE MONEDAS

Con la librería forex-python podemos realizar conversiones
entre distintos tipos de divisas.

El glosario de códigos de las diferetnes divisas se encuentra
en: https://taxsummaries.pwc.com/glossary/currency-codes
"""

# instancia de CurrencyRates
converter = CurrencyRates()


def currency_converter():
    amount = int(input('Enter amount to convert: '))
    from_currency = input('Enter the currency code '
                          'of amount you are converting: ').upper()
    to_currency = input('Enter the currency code you'
                        ' are converting to: ').upper()

    converted_amount = converter.convert(from_currency, to_currency, amount)
    return f'The amount is {converted_amount:.2f} and ' \
           f'the currency is {to_currency}'


print(currency_converter())
