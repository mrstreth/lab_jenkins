import sys
import os.path
import peewee

version = 0.2

class BaseError(Exception):
    """Определение собственных классов ошибок"""
    
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    
class ArgsInputError(BaseError):
    """Неправильный ввод аргументов программы"""
    pass

class TableNameError(BaseError):
    """Не существует такой таблицы в БД"""
    pass

class NotFoundDocFile(BaseError):
    """Файл doc.txt не найден"""
    pass

class OpenDocFileError(BaseError):
    """Не удалось открыть doc.txt"""
    pass

if __name__ == '__main__':

    if len(sys.argv) == 1 or sys.argv[1] == '--help':
        if not os.path.exists('doc.txt'):
            raise NotFoundDocFile('Файл doc.txt не найден')
        try:
            file_doc = open('doc.txt')
            for line in file_doc:
                print(line)
            file_doc.close()
        except:
            raise OpenDocFileError('Не удалось открыть doc.txt')

    elif len(sys.argv) == 2 and sys.argv[1] == '--version' or sys.argv[1] == '-v':
        print(f'{version}')
        
    elif len(sys.argv) == 2 and sys.argv[1] == 'init':
        print('create DB')

    elif len(sys.argv) == 2 and sys.argv[1] == 'fill':
        print('fill DB')

    elif len(sys.argv) == 3 and sys.argv[1] == 'show':
        A = ['CLIENTS','ODDERS']
        if sys.argv[2].upper() in A:
            print('показать')
        else:
            raise TableNameError('Не существует такой таблицы в БД')

    else:
        raise ArgsInputError('Неправильный ввод аргументов программы')
