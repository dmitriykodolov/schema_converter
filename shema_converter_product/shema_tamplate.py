import sqlite3
import json


def json_generated(db_name, table_name, column_, name_):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    query = '''
    SELECT * FROM {table_name} WHERE {column_} LIKE ?
    '''
    get = cursor.execute(query.format(table_name=table_name, column_=column_), (name_,))
    s = get.fetchall()

    for row in s:
        with open('schema.json', 'a', newline='\n') as file:
            dict_ = {
                "@context": "http://schema.org/",
                "@type": "Product",
                "name": row[2],
                "image": row[7],
                "description": row[4],
                "brand": {
                    "@type": "Brand",
                    "name": row[1]
                },
                "offers": {
                    "@type": "Offer",
                    "priceCurrency": "RUB",
                    "price": row[6],
                    "url": row[8],
                    "availability": "https://schema.org/InStock",
                    "itemCondition": "https://schema.org/NewCondition"
                },
                "aggregateRating": {
                    "@type": "AggregateRating",
                    "ratingValue": row[5],
                    "ratingCount": "1",
                    "worstRating": "50",
                    "bestRating": "100"
                }
            }
            json_ = json.dumps(dict_, indent=4, ensure_ascii=False)
            file.write(json_)
            file.write('\n\n\n\n')


json_generated('mydb', 'table2', 'brand', 'Chateau Margaux')

# print(dir(json.dumps))