from typing import Tuple, List, Optional
import sqlite3

def search_vulnerable(db: sqlite3.Connection, q: str) -> Tuple[List[sqlite3.Row], str]:
    sql = f"SELECT * FROM products WHERE name LIKE '%{q}%'"
    print("[VULN] Executing:", sql)
    cur = db.cursor()
    cur.execute(sql)
    return (cur.fetchall(), sql)

def search_safe(db: sqlite3.Connection, q: str) -> Tuple[List[sqlite3.Row], str, list]:
    sql = "SELECT * FROM products WHERE name LIKE ?"
    bindings = [f"%{q}%"]
    print("[SAFE] Executing:", sql, "Bindings:", bindings)
    cur = db.cursor()
    cur.execute(sql, bindings)
    return (cur.fetchall(), sql, bindings)

def list_vulnerable(db: sqlite3.Connection, order: str) -> Tuple[List[sqlite3.Row], str, Optional[str]]:
    sql = f"SELECT * FROM products ORDER BY {order}"
    print("[VULN] Executing:", sql)
    cur = db.cursor()
    try:
        cur.execute(sql)
        return (cur.fetchall(), sql, None)
    except Exception as e:
        return ([], sql, str(e))

def list_safe(db: sqlite3.Connection, order: str) -> Tuple[List[sqlite3.Row], str]:
    allowed = {"id", "name", "price"}
    if order not in allowed:
        order = "id"
    sql = f"SELECT * FROM products ORDER BY {order}"
    print("[SAFE] Executing:", sql, "(whitelisted)")
    cur = db.cursor()
    cur.execute(sql)
    return (cur.fetchall(), sql)
