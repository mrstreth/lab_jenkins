import sys
import os.path
from peewee import *
import peewee
import classes_error as Error
import datetime
import random as rnd

version = 1.2
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
        order_by = ('ID',)
                
class ODDERS(BaseModel):
    """Таблица ODDERS"""
    
    ID = PrimaryKeyField()
    CLIENT = ForeignKeyField(CLIENTS,backref='client')
    DATE = DateTimeField(default=datetime.datetime.today())
    AMOUNT = IntegerField()
    DESCRIPTION = CharField(max_length=100)
    
    class Meta:
        db_table = 'odders'
        order_by = ('ID',)

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
        """Показать таблицу по имени"""
        
        TABLES_NAME = ['CLIENTS','ODDERS']
        if sys.argv[2].upper() not in TABLES_NAME:
            raise Error.TableNameError('Не существует такой таблицы в БД')
        try:
            db.connect()
            if sys.argv[2].upper()=='CLIENTS':
                print('--------TABLES CLIENTS--------')
                print(f' ID\tNAME\tCITY\tADDRESS')
                for row in CLIENTS.select():
                    print(f' {row.ID}\t{row.NAME}\t{row.CITY}\t{row.ADDRESS}')

            if sys.argv[2].upper()=='ODDERS':
                print('--------TABLES ODDERS--------')
                print(f' ID\tCLIENT_id\tDATE\t\t\tAMOUNT\tDESCRIPTION')
                for row in ODDERS.select():
                    print(f' {row.ID}\t{row.CLIENT_id}\t{row.DATE}\t{row.AMOUNT}\t{row.DESCRIPTION}')
                
        except peewee.InternalError as px:
            print(str(px))

    else:
        raise Error.ArgsInputError('Неправильный ввод аргументов программы')
