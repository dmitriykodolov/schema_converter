import os
import json
from tilda_combine.enginie.product_objects import CardObject


class ChemaConverter:
    def __init__(self, db_name, table_name, query):
        self.db_name = db_name
        self.table_name = table_name
        self.query = query
        self.card = CardObject(self.db_name, self.table_name, self.query)

    def created_schema(self):
        for row in range(self.card.counter()):
            name = f'{self.card.price[row]}.json'.replace(' ', '_').replace(',', '')
            with open(name, 'a', newline='\n') as file:
                score = 90 if self.card.score_rp[row] == '' else 90
                dict_ = {
                    "@context": "http://schema.org/",
                    "@type": "Product",
                    "name": self.card.title[row],
                    "image": self.card.photo[row],
                    "description": self.card.description[row],
                    "brand": {
                        "@type": "Brand",
                        "name": self.card.brand[row]
                    },
                    "offers": {
                        "@type": "Offer",
                        "priceCurrency": "RUB",
                        "price": self.card.price[row],
                        "url": self.card.url[row],
                        "availability": "https://schema.org/InStock",
                        "itemCondition": "https://schema.org/NewCondition"
                    },
                    "aggregateRating": {
                        "@type": "AggregateRating",
                        "ratingValue": score,
                        "ratingCount": "1",
                        "worstRating": "50",
                        "bestRating": "100"
                    }
                }
                json_ = json.dumps(dict_, indent=4, ensure_ascii=False)
                file.write(json_)
                file.close()


converter = ChemaConverter('../winetime', 'db', 'Margaux')
converter.created_schema()