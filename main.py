import sys
import os.path
from peewee import *
import peewee
import classes_error as Error
import datetime
import random as rnd

version = 0.6
name_database = 'database.db'

db = SqliteDatabase(name_database)
        
class BaseModel(Model):
    class Meta:
        database = db
                
class CLIENTS(BaseModel):
    """Таблица CLIENTS"""
    ID = PrimaryKeyField()
    NAME = CharField(max_length=50)
    CITY = CharField(max_length=50)
    ADDRESS = CharField(max_length=50)
    class Meta:
        db_table = 'clients'
                
class ODDERS(BaseModel):
    """Таблица ODDERS"""
    ID = PrimaryKeyField()
    CLIENT = ForeignKeyField(CLIENTS)
    DATE = DateTimeField(default=datetime.datetime.now())
    AMOUNT = IntegerField()
    DESCRIPTION = CharField(max_length=100)    
    class Meta:
        db_table = 'odders'

if __name__ == '__main__':

    if len(sys.argv) == 1 or sys.argv[1] == '--help':
        """Вызов справки"""
        if not os.path.exists('doc.txt'):
            raise Error.NotFoundDocFile('Файл doc.txt не найден')
        try:
            file_doc = open('doc.txt')
            for line in file_doc:
                print(line)
            file_doc.close()
        except:
            raise Error.OpenDocFileError('Не удалось открыть doc.txt')

    elif len(sys.argv) == 2 and sys.argv[1] == '--version' or sys.argv[1] == '-v':
        """Показать версию программы"""
        print(f'{version}')
        
    elif len(sys.argv) == 2 and sys.argv[1] == 'init':
        """Инициализация БД (создание пустой)"""
        if os.path.exists(name_database):
            os.remove(name_database)
        
        try:
            db.connect()
            CLIENTS.create_table()
            ODDERS.create_table()
        except peewee.InternalError as px:
            print(str(px))
        
    elif len(sys.argv) == 2 and sys.argv[1] == 'fill':
        """Заполнение случайными записями (10)"""
        try:
            db.connect()
            for i in range(10):
                CLIENTS.create(NAME=f'NAME{i+1}',CITY=f'CITY{i+1}',ADDRESS=f'ADDRESS{i+1}')
                ODDERS.create(CLIENT=rnd.randint(0,10),AMOUNT=i+1,DESCRIPTION=f'test')
        except peewee.InternalError as px:
            print(str(px))
            
    elif len(sys.argv) == 3 and sys.argv[1] == 'show':
        A = ['CLIENTS','ODDERS']
        if sys.argv[2].upper() in A:
            print('показать')
        else:
            raise Error.TableNameError('Не существует такой таблицы в БД')

    else:
        raise Error.ArgsInputError('Неправильный ввод аргументов программы')
