# test-code-review
def get_user(db, username):
    # Bug / Security issue: Unsafe SQL concatenation
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    return db.execute(query)
