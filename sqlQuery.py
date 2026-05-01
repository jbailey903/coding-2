import sqlite3

def getAllData():
    connect= sqlite3.connect('myDb_3.db')
    cursor= connect.cursor()

    query = "SELECT platform FROM gameSales"

    cursor. execute(query)

    result= cursor. fetchall()

    print(results)

    