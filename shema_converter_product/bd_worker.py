import sqlite3
from sqlite3 import Error
import csv
import os
import colorama


class CsvToBd:
    def __init__(self, path, delimiter):
        self.path = path
        self.delimiter = delimiter

    def get_columns_name(self):
        with open(self.path, newline='') as table:
            get_col = csv.reader(table, delimiter=self.delimiter)
            cols_name = next(iter(get_col))
            return cols_name


class DataShema:
    def create_db(self, bd_name, table_name, path, delimiter):
        # TODO: ЭТО ПРОСТО ШЛАКОВЫЙ КОД И ПОЛНЫЙ УЖАС! РЕШИТЬ ИНАЧЕ

        def change_symbols(columns):
            formatting_columns = []
            for i in columns:
                i = i.replace(':', '_')
                i = i.replace(' ', '_')
                i = i.replace('.', '_')
                formatting_columns.append(i)
            return formatting_columns

        connection = sqlite3.connect(bd_name)
        cursor = connection.cursor()
        table = table_name
        query = '''
            CREATE TABLE {table_name}
            (id INTEGER PRIMARY KEY AUTOINCREMENT)
            '''
        if table_name:
        # TODO: ВООБЩЕ НЕ ПОНЯЛ УСЛОВИЯ. РАЗОБРАТЬСЯ. ЧТО ДЕЛАЕТ -- НЕ ЯСНО. В ЛЮБОМ СЛУЧАЕ ЭТО УСЛОВИЕ НЕ РАБОТАЕТ
            try:
                cursor.execute(query.format(table_name=table))
                connection.commit()
                cols_name = CsvToBd(path, delimiter).get_columns_name()
                cols_name = change_symbols(cols_name)
                for col in cols_name:
                    query = '''
                    ALTER TABLE {table_name}
                    ADD {row_} VARCHAR NULL
                    '''
                    cursor.execute(query.format(table_name=table, row_=col))
                else:
                    # TODO: В ЭТОМ УЧАСТКЕ ПРОДУМАТЬ МЕХАНИКУ С СОЗДАННЫМИ УЖЕ БАЗАМИ ДАННЫХ. МОЖНО СОЗДАТЬ ОДНУ БД,
                    #  И НЕСКОЛЬКО ТАБЛИЦ. НЕЛЬЗЯ СОЗДАВАТЬ ОДНИАКОВЫЕ ТАБЛИЦЫ.
                    connection.close()
                    print(f'Success created DB: {colorama.Fore.GREEN} \'{table_name}\' \nTable name: {colorama.Fore.GREEN}'
                          f'{table} ')
            except Error as e:
                print(f'We have a problem: {colorama.Fore.RED} \n{e}')
                return f'We have a problem: \n{e}'
        else:
            print(f'{table_name} is exist')


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