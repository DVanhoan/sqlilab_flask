from typing import Tuple, Optional, List
import sqlite3

def login_vulnerable(db: sqlite3.Connection, username: str, password: str) -> Tuple[Optional[sqlite3.Row], str]:
    sql = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
    print("[VULN] Executing:", sql)
    cur = db.cursor()
    try:
        cur.execute(sql)
        user = cur.fetchone()
        return (user, sql)
    except Exception as e:
        return (None, f"{sql}\n-- ERROR: {e}")

def login_safe(db: sqlite3.Connection, username: str, password: str) -> Tuple[Optional[sqlite3.Row], str, list]:
    sql = "SELECT * FROM users WHERE username = ? AND password = ?"
    bindings = [username, password]
    print("[SAFE] Executing:", sql, "Bindings:", bindings)
    cur = db.cursor()
    cur.execute(sql, bindings)
    user = cur.fetchone()
    return (user, sql, bindings)
