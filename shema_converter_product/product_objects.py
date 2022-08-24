import sqlite3
import json


bd_name = '../winetime'
table_name = 'db'


def get_db_columns():
    columns = []
    connection = sqlite3.connect(bd_name)
    cursor = connection.cursor()
    query = f'''
    PRAGMA table_info({table_name})
    '''
    db_columns = cursor.execute(query).fetchall()
    for i in db_columns:
        columns.append(i[1])
    return columns


def connection(func):
    def inner(*args, **kwargs):
        columns = get_db_columns()
        connection = sqlite3.Connection(bd_name)
        cursor = connection.cursor()
        query = func(*args, **kwargs)
        cursor.execute(query)
        c = cursor.fetchall()
        new_list = []
        for x in c:
            x = list(x)
            new_dict = dict(zip(columns, x))
            new_list.append(new_dict)
        return new_list
    return inner


@connection
def get_from_title(title, table_name='db'):
    query = f'''
    SELECT * FROM {table_name} WHERE Title LIKE '%{title}%'
    '''
    return query


for row in get_from_title('Petrus'):
    with open('schema5.json', 'a', newline='\n') as file:
        dict_ = {
            "@context": "http://schema.org/",
            "@type": "Product",
            "name": row.get('Title'),
            "image": row.get('Photo'),
            "description": row.get('Text'),
            "brand": {
                "@type": "Brand",
                "name": row.get('Brand')
            },
            "offers": {
                "@type": "Offer",
                "priceCurrency": "RUB",
                "price": row.get('Price'),
                "url": row.get('Url'),
                "availability": "https://schema.org/InStock",
                "itemCondition": "https://schema.org/NewCondition"
            },
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": row.get('Characteristics_RP'),
                "ratingCount": "1",
                "worstRating": "50",
                "bestRating": "100"
            }
        }
        json_ = json.dumps(dict_, indent=4, ensure_ascii=False)
        file.write(json_)
        file.write('\n\n\n\n')


