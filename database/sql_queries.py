CREATE_USER_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS telegram_users 
        (
        ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        USERNAME CHAR(50),
        FISRT_NAME CHAR(50),
        LAST_NAME CHAR(50),
        UNIQUE (TELEGRAM_ID)
        )
"""

CREATE_BAN_USER_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS ban_users 
        (
        ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        USERNAME CHAR(50),
        COUNT INTEGER,
        LAST_NAME CHAR(50),
        UNIQUE (TELEGRAM_ID)
        )
"""

CREATE_USER_FORM_TABLE_QUERY = """
        CREATE TABLE IF NOT EXISTS user_form 
        (
        ID INTEGER PRIMARY KEY,
        TELEGRAM_ID INTEGER,
        NICKNAME CHAR(50),
        BIO TEXT,
        AGE INTEGER,
        OCCUPATION CHAR(50),
        PHOTO TEXT,
        UNIQUE (TELEGRAM_ID)
        )
"""

INSERT_USER_QUERY = """
INSERT OR IGNORE INTO telegram_users VALUES (?,?,?,?,?)
"""
INSERT_USER_FORM_QUERY = """
INSERT INTO user_form VALUES (?,?,?,?,?,?,?)
"""

SELECT_ALL_USER_QUERRY = """
SELECT * FROM telegram_users
"""

SELECT_USER_QUERRY = """
SELECT * FROM telegram_users WHERE TELEGRAM_ID = ?
"""

INSERT_BAN_USER_QUERY = """
INSERT INTO ban_users VALUES (?,?,?,?)
"""

UPDATE_BAN_USER_COUNT_QUERY = """
UPDATE ban_users SET COUNT = COUNT + 1 WHERE TELEGRAM_ID = ?
"""

SELECT_USER_FORM_QUERRY = """
SELECT * FROM user_form WHERE TELEGRAM_ID = ?
"""
