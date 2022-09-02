import sqlite3
from sqlite3 import Error
import colorama
from csv_worker import CsvToBd

# TODO: НАСТРОИТЬ БАЗУ ДАННЫХБ ВООБЩЕ ПРОЧИТАТЬ ПРО НАСТРОЙКУ


class DataBaseBuilder(CsvToBd):
    def __init__(self, bd_name, table_name, table_path, delimiter):
        super().__init__(table_path, delimiter)
        self.bd_name = bd_name
        self.table_name = table_name


    def create_db(self):
        connection = sqlite3.connect(self.bd_name)
        cursor = connection.cursor()
        table = self.table_name
        query = '''
            CREATE TABLE {table_name}
            (id INTEGER PRIMARY KEY AUTOINCREMENT)
            '''
        if self.table_name:
        # TODO: ВООБЩЕ НЕ ПОНЯЛ УСЛОВИЯ. РАЗОБРАТЬСЯ. ЧТО ДЕЛАЕТ -- НЕ ЯСНО. В ЛЮБОМ СЛУЧАЕ ЭТО УСЛОВИЕ НЕ РАБОТАЕТ
            try:
                cursor.execute(query.format(table_name=table))
                connection.commit()
                cols = self.get_columns_name()
                for col in cols:
                    query = '''
                    ALTER TABLE {table_name}
                    ADD {col} VARCHAR NULL
                    '''
                    cursor.execute(query.format(table_name=table, col=col))
                else:
                    # TODO: В ЭТОМ УЧАСТКЕ ПРОДУМАТЬ МЕХАНИКУ С СОЗДАННЫМИ УЖЕ БАЗАМИ ДАННЫХ. МОЖНО СОЗДАТЬ ОДНУ БД,
                    #  И НЕСКОЛЬКО ТАБЛИЦ. НЕЛЬЗЯ СОЗДАВАТЬ ОДНИАКОВЫЕ ТАБЛИЦЫ.
                    connection.close()
                    print(f'Success created DB: {colorama.Fore.GREEN} \'{self.table_name}\' \nTable name:'
                          f' {colorama.Fore.GREEN}'
                          f'{table} ')
            except Error as e:
                print(f'We have a problem: {colorama.Fore.RED} \n{e}')
                return f'We have a problem: \n{e}'
        else:
            print(f'{self.table_name} is exist')

    def add_data(self):
        data_ = self.get_columns_name()
        values = self.values_formatter()
        columns = self.get_columns()
        # TODO: ПЕРЕПИСАТЬ ИМЕНА ПЕРЕМЕННЫХ. САМ СЕБЯ ЗАПУТАЛ.
        for row in columns:
            row = tuple(row.values())
            connection = sqlite3.connect(self.bd_name)
            cursor = connection.cursor()
            query = f'''
                            INSERT INTO {self.table_name} {tuple(data_)}
                            VALUES ({values})
                            '''
            cursor.execute(query.format(table=self.table_name, values=values), row)
            connection.commit()
            connection.close()
            print(f'{row}: {colorama.Fore.GREEN} SUCCESFULLY ADDED!')

d = DataBaseBuilder('winetime', 'bordeaux', 'margaux-angelus.csv', ';')
d.create_db()
d.add_data()