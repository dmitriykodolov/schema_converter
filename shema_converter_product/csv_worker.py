import os
import csv
# from bd_worker import DataShema, Data


# class CsvToBd(Data):
#     def __init__(self, table_path, db_name, table_name):
#         super().__init__(db_name, table_name)
#         self.table_path = table_path
#
#
#     def csv_read(self):
#         d = DataShema(self.db_name, self.table_name)
#         d.create_db()
#         d2 = Data(self.db_name, self.table_name)
#         with open(self.table_path, newline='') as csvfile:
#             csvreader = csv.DictReader(csvfile, delimiter=';')
#             for row in csvreader:
#                 d2.add_data(row['\ufeffbrands'], row['name'], row['vintage'], row['description'], row['RP'],
#                             row['price'], row['Photo'], row['Url'])
#         csvfile.close()


# d = CsvToBd('Margaux2.csv', 'wtdb', 'winetime')
# d.csv_read()

def get_columns_name(path, delimiter):
    with open(path, newline='') as table:
        get_col = csv.reader(table, delimiter=delimiter)
        cols_name = next(iter(get_col))
        return cols_name


# TODO: объединить функции в 1 класс. Сделать этот класс родительским

columns = get_columns_name('store.csv', ';')


def change_symbols(columns):
    for i in columns:
        i = i.replace(':', '_')
        i = i.replace(' ', '_')
        i = i.replace('.', '_')


# for i in columns:
#     i = i.replace(':', '_')
#     i = i.replace(' ', '_')
#     i = i.replace('.', '_')
#     print(i)


