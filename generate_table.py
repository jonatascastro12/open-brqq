import csv
import json
from json import JSONDecodeError

from main.models import City

cities = City.objects.filter(treated_subtitle_part__isnull=False)

with open('google-nlp.csv', mode='w', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile, delimiter=',',
                        quotechar='|', quoting=csv.QUOTE_MINIMAL, dialect='excel',)

    writer.writerow(['CITY', 'UF', 'TERM', 'TYPE', 'SALIENCE'])

    for city in cities:
        try:
            nlp = city.content1
            nlp = json.loads(nlp)

            for entity in nlp.get('entities'):
                writer.writerow([city.name,
                                 city.uf,
                                 # city.region,
                                 entity.get('name'),
                                 str(entity.get('type')),
                                 str(entity.get('salience')),
                                 ])
        except JSONDecodeError:
            pass
