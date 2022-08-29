from jinja2 import Environment, FileSystemLoader
from tilda_combine.enginie.product_objects import CardObject

card_name_ = 'Margaux'

card = CardObject('../winetime', 'db', card_name_)

counter = card.counter()

card_name = card.title
description = card.description
url = card.url

country = card.country
region = card.region
subregion = card.sub_region
blend = card.blend
value = card.value
vol = card.vol
score_rp = card.score_rp

for row in range(counter):
    with open(f'output/{card_name_}_{row}.html', 'a') as file:
        file_loader = FileSystemLoader('')
        env = Environment(loader=file_loader)
        tm = env.get_template('template/tamplate.html')
        msg = tm.render(card_name=card_name[row], description=description[row], url=url[row],
                        country=country[row], region=region[row], subregion=subregion[row],
                        blend=blend[row], value=value[row], vol=vol[row], score_rp=score_rp[row])
        file.write(msg)
        file.close()