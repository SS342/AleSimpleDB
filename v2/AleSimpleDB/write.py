import sqlite3

def new_write(cursor : sqlite3.Cursor, tableName : str, data : list):
    sql = f"INSERT INTO {tableName} values("
    for el in data:
        sql += f"'{el}', "
    sql = sql[:-1] + ')'
    try:
        cursor.execute(sql)
        return False
    except: return "Error write"