import sqlite3
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS user(
    name VARCHAR(255) NOT NULL,
    username VARCHAR(123) NOT NULL,
    user_id integer NOT NULL
)""")

conn.commit()

class Database:
    def __init__(self,db_file):
        self.conn = sqlite3.connect(db_file)
        self.cursor=self.conn.cursor()

    def add_user(self,name,username,user_id):
        with self.conn:
            return self.cursor.execute("INSERT INTO user(name,username,user_id) VALUES (?,?,?)",(name,username,user_id))
    def get_all_users(self):
        with self.conn:
            return self.cursor.execute("SELECT name,usernmae,user_id FROM user").fetchall()