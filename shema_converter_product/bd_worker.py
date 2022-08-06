import sqlite3
from sqlite3 import Error
import os
import colorama


class DataShema:
    def __init__(self, name, table_name):
        self.name = name
        self.table_name = table_name

    def create_db(self):
        connection = sqlite3.connect(self.name)
        cursor = connection.cursor()
        table = self.table_name
        query = '''
            CREATE TABLE {table_name} 
            (id INTEGER PRIMARY KEY AUTOINCREMENT, brand VARCHAR(255), name VARCHAR(255), vintage VARCHAR(255), 
            description TEXT, rate VARCHAR(255), price INT, card_url VARCHAR(255), image_url VARCHAR(255))
            '''
        if self.name:
            try:
                cursor.execute(query.format(table_name=table))
                connection.commit()
                connection.close()
                print(f'Success created DB: {colorama.Fore.GREEN} \'{self.name}\' \nTable name: {colorama.Fore.GREEN}'
                      f'{table} ')
                return self.name
            except Error as e:
                print(f'We have a problem: {colorama.Fore.RED} \n{e}')
                return f'We have a problem: \n{e}'
        else:
            print(f'{self.name} is exist')


class Data(DataShema):
    def __init__(self, db_name, table_name):
        super().__init__(db_name, table_name)
        self.db_name = db_name
        self.table_name = table_name

    def add_data(self, brand, name, vintage, decription, rate, price, card_url, image_url):
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        data_touple = (brand, name, vintage, decription, rate, price, card_url, image_url)
        query = '''
                INSERT INTO {table} (brand, name, vintage, description, rate, price, card_url, image_url)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                '''
        try:
            cursor.execute(query.format(table=self.table_name), data_touple)
            connection.commit()
            connection.close()
            print(f'{data_touple}: {colorama.Fore.GREEN} SUCCESFULLY ADDED!')

        except Error as e:
            print(f'We have a problem: {colorama.Fore.RED} {e}')

