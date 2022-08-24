import sqlite3


class CardObject:
    def __init__(self, db_name, table_name, group):
        """
        :param db_name: name of connection to DataBase
        :param table_name: name of table of DataBase
        :param group: searching by Brand or Product Name
        """
        self.db_name = db_name
        self.table_name = table_name
        self.group = group
        self.id = self.get_row('id')
        self.brand = self.get_row('Brand')
        self.category = self.get_row('Category')
        self.title = self.get_row('Title')
        self.description = self.get_row('Description')
        self.price = self.get_row('Price')
        self.photo = self.get_row('Photo')
        self.country = self.get_row('Characteristics_Страна')
        self.vintage = self.get_row('Characteristics_Винтаж')
        self.score_rp = self.get_row('Characteristics_RP')
        self.url = self.get_row('Url')
        self.region = self.get_row('Characteristics_Регион')
        self.sub_region = self.get_row('Characteristics_Субрегион')
        self.blend = self.get_row('Characteristics_Состав')
        self.value = self.get_row('Characteristics_Объем')
        self.vol = self.get_row('Characteristics_Алк_')

    def __dir__(self):
        """
        :return: methods and attributes of CardObject class
        """
        return ('id', 'brand', 'category', 'title', 'description', 'price', 'photo', 'country','vintge', 'score_rp',
                'url', 'region', 'blend', 'value', 'vol')

    def __repr__(self):
        return f'Object of products by {self.group}'

    def get_db_columns(self):
        columns = []
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        query = f'''
        PRAGMA table_info({self.table_name})
        '''
        db_columns = cursor.execute(query).fetchall()
        for i in db_columns:
            columns.append(i[1])
        return columns

    def connection(func):
        def inner(self, *args, **kwargs):
            columns = self.get_db_columns()
            connection = sqlite3.Connection(self.db_name)
            cursor = connection.cursor()
            query = func(self, *args, **kwargs)
            cursor.execute(query)
            c = cursor.fetchall()
            new_list = []
            for x in c:
                x = list(x)
                new_dict = dict(zip(columns, x))
                new_list.append(new_dict)
            return new_list
        return inner

    @connection
    def get_from_title(self):
        query = f'''
        SELECT * FROM {self.table_name} WHERE Title LIKE '%{self.group}%'
        '''
        return query

    def get_row(self, row_name):
        list_ = []
        for row in self.get_from_title():
            list_.append(row[row_name])
        return list_

    def counter(self):
        return len(self.title)