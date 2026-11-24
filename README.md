# test-code-review
import sqlite3

def get_user(user_id):
    conn = sqlite3.connect("app.db")
    query = "SELECT * FROM users WHERE id = " + user_id
    result = conn.execute(query).fetchone()
    return result["age"]

password = "admin123"
