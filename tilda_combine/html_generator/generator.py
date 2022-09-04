#!/usr/bin/env python
#-*- coding:utf-8 -*-

from typing import List

# from jinja2 import Environment, FileSystemLoader
from tilda_combine.enginie.product_objects import CardObject

card_name_ = 'Cheval'

card = CardObject('../winetime', 'bordeaux', card_name_)

counter = card.counter()


'''
Левый блок с интересными фактами, терруаром, кнопкой
и особенностями производства
'''
card_name = card.brand
vintage = card.vintage
fact = card.fact
landscape = card.landscape
factory_process = card.factory_process
button_url = card.button_url

'''
Блок с таблицей харакетеристик
'''
wine = card.wine
country = card.country
region = card.region
sub_region = card.sub_region
blend = card.blend
square = card.square
vin_age = card.vin_age
value = card.value
vol = card.vol
potential = card.potential

'''
Блок с оценками и рекомендациями
'''
decanter = card.decanter
collection = card.collection
rp = card.score_rp
ws = card.score_ws
jr = card.score_jr

france = 'sss'


def create_html():
    for row in range(counter):
        with open(f'output/{card_name[row].lower().replace(" ", "_")}_{vintage[row]}.html' , 'a') as file:
            if region[row]:
                re_url = f'https://winetime.moscow/shop?tfc_charact:64922[138361030]={region[row]}&tfc_div=:::'
                region_url = [re_url for _ in range(counter)]
            if sub_region[row]:
                sub_url = f'https://winetime.moscow/shop?tfc_charact:66641[138361030]={sub_region[row]}&tfc_div=:::'
                sub_region_url = [sub_url for _ in range(counter)]
            if country[row]:
                co_url = f'https://winetime.moscow/shop?tfc_charact:60386[138361030]={country[row]}&tfc_div=:::'
                country_url = [co_url for _ in range(counter)]
            if int(rp[row]) > 90:
                rp_class = 'rp_green_class'
            else:
                rp_class = 'rp_yellow_class'
            if int(ws[row]) > 90:
                ws_class = 'ws_green_class'
            else:
                ws_class = 'ws_yellow_class'
            file_loader = FileSystemLoader('')
            env = Environment(loader=file_loader)
            tm = env.get_template('template/tamplate.html')
            msg = tm.render(card_name=card_name[row], vintage=vintage[row], fact=fact[row],
                            landscape=landscape[row], factory_process=factory_process[row],
                            button_url=button_url[row], country=country[row],
                            region=region[row], sub_region=sub_region[row], blend=blend[row],
                            square=square[row], vin_age=vin_age[row], value=value[row], vol=vol[row],
                            potential=potential[row], wine=wine[row], decanter=decanter[row], rp=rp[row],
                            ws=ws[row], jr=jr[row], collection=collection[row], region_url=region_url[row],
                            country_url=country_url[row], sub_region_url=sub_region_url[row], rp_class=rp_class,
                            ws_class=ws_class)
            file.write(msg)
            file.close()


def create_alt_seo():
    for row in range(counter):
        with open(f'alt_seo_tags/{card_name[row].lower().replace(" ", "_")}.txt', 'a') as file:
            msg = f'{card_name[row]} {vintage[row]} в винотеке WineTime (Москва, Бутлерова 17Б) \n'
            file.write(msg)
            file.close()


create_alt_seo()
