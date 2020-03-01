import sys
import os.path
import peewee
import classes_error as Error

version = 0.3

if __name__ == '__main__':

    if len(sys.argv) == 1 or sys.argv[1] == '--help':
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
            raise Error.TableNameError('Не существует такой таблицы в БД')

    else:
        raise Error.ArgsInputError('Неправильный ввод аргументов программы')
