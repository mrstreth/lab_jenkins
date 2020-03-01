import pytest
import main
import os.path

def test_exists_database():
    """Существует ли база даных"""
    assert os.path.exists(main.name_database) == True

def test_row_count_clients():
    """Кол-во заполненных строк в clients = 10"""
    assert len(main.CLIENTS.select()) == 10

def test_row_count_odders():
    """Кол-во заполненных строк в odders = 10"""
    assert len(main.ODDERS.select()) == 10

def test_coll_clients():
    """Содерзит ли clients необходимые колонки"""
    try:
        x = main.CLIENTS.select(main.CLIENTS.ID,main.CLIENTS.NAME,main.CLIENTS.CITY, main.CLIENTS.ADDRESS)
    except:
        assert False

def test_coll_odders():
    """Содерзит ли odders необходимые колонки"""
    try:
        x = main.ODDERS.select(main.ODDERS.ID,main.ODDERS.CLIENT_id,main.ODDERS.DATE, main.ODDERS.AMOUNT,main.ODDERS.DESCRIPTION)
    except:
        assert False
