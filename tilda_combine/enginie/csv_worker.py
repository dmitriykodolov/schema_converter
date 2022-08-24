'''
СОБИРАЕМ ФУНКЦИОНАЛ РАБОТЫ С ТАБЛИЦАМИ
TODO: 1) Чтение таблицы (ВОЗМОЖНО ИСПОЛЬЗОВАТЬ ДЕКОРАТОР)
TODO: 3) Получаем количистевство заголовков таблциы
TODO: 4) ПОЛУЧАЕМ КОЛИЧСТВО СТРОЧЕК В ТАБЛИЦЕ
TODO: 5) Получаем все данные
НЕОБХОДИМЫЕ МОДУЛИ: csv, os, sys
'''

import os
import csv


class CsvToBd:
    def __init__(self, table_path, delimiter):
        self.table_path = table_path
        self.delimiter = delimiter

    def get_columns_name(self):
        with open(self.table_path, newline='', encoding='utf-8-sig') as table:
            get_col = csv.reader(table, delimiter=self.delimiter)
            cols_name = next(iter(get_col))
            cols = []
            for i in cols_name:
                i = i.replace(':', '_')
                i = i.replace(' ', '_')
                i = i.replace('.', '_')
                cols.append(i)
            table.close()
            return cols

    def values_count(self):
        cols = self.get_columns_name()
        sum_ = len(cols)
        return sum_

    def values_formatter(self):
        sum_ = self.values_count()
        str_ = ('?' + ',') * sum_
        formatting_str = str_.rstrip(str_[-1])
        return formatting_str

    def get_columns(self):
        get_col = []
        with open(self.table_path, newline='', encoding='utf-8-sig') as table:
            get = csv.DictReader(table, delimiter=self.delimiter)
            for i in get:
                get_col.append(i)
            table.close()
        return get_col
