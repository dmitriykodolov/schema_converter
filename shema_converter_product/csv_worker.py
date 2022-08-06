import os
import csv
from bd_worker import DataShema, Data


class CsvToBd(Data):
    def __init__(self, table_path, db_name, table_name):
        super().__init__(db_name, table_name)
        self.table_path = table_path


    def csv_read(self):
        d = DataShema(self.db_name, self.table_name)
        d.create_db()
        d2 = Data(self.db_name, self.table_name)
        with open(self.table_path, newline='') as csvfile:
            csvreader = csv.DictReader(csvfile, delimiter=';')
            for row in csvreader:
                d2.add_data(row['\ufeffbrands'], row['name'], row['vintage'], row['description'], row['RP'],
                            row['price'], row['Photo'], row['Url'])
        csvfile.close()
