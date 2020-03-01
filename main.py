import sys

version = 0.1

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

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print('документация')

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
