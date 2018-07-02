import csv
from main.models import City

cities = City.objects.all()

regioes = {'AC': 'Norte',
           'AL': 'Nordeste',
           'AP': 'Norte',
           'AM': 'Norte',
           'BA': 'Nordeste',
           'CE': 'Nordeste',
           'DF': 'Centro-Oeste',
           'ES': 'Sudeste',
           'GO': 'Centro-Oeste',
           'MA': 'Nordeste',
           'MT': 'Centro-Oeste',
           'MS': 'Centro-Oeste',
           'MG': 'Sudeste',
           'PA': 'Norte',
           'PB': 'Nordeste',
           'PR': 'Sul',
           'PE': 'Nordeste',
           'PI': 'Nordeste',
           'RJ': 'Sudeste',
           'RN': 'Nordeste',
           'RS': 'Sul',
           'RO': 'Norte',
           'RR': 'Norte',
           'SC': 'Sul',
           'SP': 'Sudeste',
           'SE': 'Nordeste',
           'TO': 'Norte',
           }

for city in cities:
    city.region = regioes[city.uf]
    city.save()
