import sqlite3


if __name__ == '__main__':
    pass


def createdb():
    db = sqlite3.connect("db.db")
    cur = db.cursor()
    cur.execute("CREATE TABLE products(name, type, price, shop, date)")
    print("Created the database!")