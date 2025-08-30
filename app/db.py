import sqlite3
from flask import g, current_app

def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect(current_app.config["DATABASE"])
        db.row_factory = sqlite3.Row
    return db

def close_db(e=None):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()

def init_app(app):
    app.teardown_appcontext(close_db)

def init_db_data():
    db = get_db()
    cur = db.cursor()
    cur.executescript("""
        DROP TABLE IF EXISTS users;
        DROP TABLE IF EXISTS products;
        CREATE TABLE users(id INTEGER PRIMARY KEY, username TEXT UNIQUE, password TEXT);
        CREATE TABLE products(id INTEGER PRIMARY KEY, name TEXT, price INTEGER);
    """)
    cur.execute("INSERT INTO users(username,password) VALUES('admin','1234');")
    cur.execute("INSERT INTO users(username,password) VALUES('user','abcd');")
    cur.executemany("INSERT INTO products(name,price) VALUES(?,?)", [
        ("iPhone 15", 999), ("Galaxy S24", 899), ("Pixel 9", 799),
        ("ThinkPad X1", 1699), ("MacBook Air", 1299), ("iPad Pro", 1099)
    ])
    db.commit()
