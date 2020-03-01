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
