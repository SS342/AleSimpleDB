import AleSimpleDB

connection, cursor = AleSimpleDB.Connect(path = "usr.db")

sql = """CREATE TABLE IF NOT EXISTS users(
                    name STRING,
                    device STRING,
                    status STRING,
                    time STRING);
                """

AleSimpleDB.create_table(connection, cursor, data = {
                                                        "name" : "users",
                                                        "fields" : {
                                                            "name" : AleSimpleDB.types().STR,
                                                            "device": AleSimpleDB.types().STR,
                                                            "status": AleSimpleDB.types().STR,
                                                            "time": AleSimpleDB.types().STR
                                                        }
                                                    }
                            )

print(AleSimpleDB.get_all_writes(cursor = cursor, tableName="users"))
print(AleSimpleDB.get_writes_by(cursor=cursor, tableName="users", param="name", query='5'))
print(AleSimpleDB.get_last(cursor = cursor, tableName="users"))
#print(AleSimpleDB.new_write(connection = connection, cursor = cursor, tableName="users", data=["q", 'w', 'e', 'r3']))
print(AleSimpleDB.get_last_by(cursor = cursor, tableName="users", param="name", query="q"))