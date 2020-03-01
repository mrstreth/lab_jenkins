import sys
import os.path
from peewee import *
import classes_error as Error
import datetime

version = 0.4
name_databade = 'database.db'

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
        if os.path.exists(name_databade):
            os.remove(name_databade)
            
        db = SqliteDatabase(name_databade)
        
        class BaseModel(Model):
            class Meta:
                database = db
                
        class CLIENTS(BaseModel):
            """Таблица CLIENTS"""
            NAME = CharField(max_length=50, unique=True, primary_key=True)
            CITY = CharField(max_length=50)
            ADDRESS = CharField(max_length=50)
            
            class Meta:
                db_table = 'CLIENTS'
                
        class ODDERS(BaseModel):
            """Таблица ODDERS"""
            CLIENT = ForeignKeyField(CLIENTS, field='NAME')
            DATE = DateTimeField(default=datetime.datetime.now())
            AMOUNT = IntegerField()
            DESCRIPTION = CharField(max_length=100)
            
        class Meta:
            db_table = 'ODDERS'

        try:
            db.connect()
            CLIENTS.create_table()
            ODDERS.create_table()
        except peewee.InternalError as px:
            print(str(px))
        
            
            

    elif len(sys.argv) == 2 and sys.argv[1] == 'fill':
        print('fill DB')

    elif len(sys.argv) == 3 and sys.argv[1] == 'show':
        A = ['CLIENTS','ODDERS']
        if sys.argv[2].upper() in A:
            print('показать')
        else:
            raise Error.TableNameError('Не существует такой таблицы в БД')

    else:
        raise Error.ArgsInputError('Неправильный ввод аргументов программы')
