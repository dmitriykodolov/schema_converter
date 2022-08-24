import sqlite3
import json
from product_objects import get_from_title, get_db_columns, connection



        
for row in get_from_title(''):
    with open('schema2.json', 'a', newline='\n') as file:
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
