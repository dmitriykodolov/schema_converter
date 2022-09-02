import os
import json
from jinja2 import Environment, FileSystemLoader
from tilda_combine.enginie.product_objects import CardObject


class ChemaConverter:
    def __init__(self, db_name, table_name, query):
        self.db_name = db_name
        self.table_name = table_name
        self.query = query
        self.card = CardObject(self.db_name, self.table_name, self.query)

    def created_schema(self):
        for row in range(self.card.counter()):
            name = f'{self.card.brand[row].lower().replace(" ", "_")}_{self.card.vintage[row]}.json'
            with open(name, 'a', newline='\n') as file:
                dict_ = {
                    "@context": "http://schema.org/",
                    "@type": "Product",
                    "name": f'{self.card.brand[row]} {self.card.vintage[row]}',
                    "image": self.card.photo[row],
                    "description": self.card.factory_process[row],
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
                        "ratingValue": self.card.score_rp[row],
                        "ratingCount": "1",
                        "worstRating": "50",
                        "bestRating": "100"
                    }
                }
                json_ = json.dumps(dict_, indent=4, ensure_ascii=False)
                file_loader = FileSystemLoader('')
                env = Environment(loader=file_loader)
                tm = env.get_template('template/template.html')
                msg = tm.render(json_dict=json_)
                file.write(msg)
                file.close()


d = ChemaConverter('../winetime', 'bordeaux', 'Mouton')
d.created_schema()