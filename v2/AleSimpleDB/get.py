import sqlite3

def get_all_writes(cursor : sqlite3.Cursor, tableName : str):
    return cursor.execute(f"SELECT * FROM {tableName}").fetchall()


def get_writes_by(cursor : sqlite3.Cursor, tableName : str, param: str, query : str): 
    return cursor.execute(f"SELECT * FROM {tableName} WHERE {param} = '{query}'").fetchall()


def get_last(cursor : sqlite3.Cursor, tableName : str):
    return cursor.execute(f'SELECT * FROM {tableName}').fetchall()[-1]