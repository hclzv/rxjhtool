
import sqlite3

class Sql():

    def __init__(self):
        self.conn = sqlite3.connect("sql3db")
        pass
        
    def inster(self,messages=None):
        cur = self.conn.cursor()
        sql = '''INSERT INTO rxjhrun
                (messages)
                VALUES (?)'''
        cur.execute(sql,(messages,))
        self.conn.commit()

    
    def query(self):
        cur =  self.conn.cursor()
        cur.execute("select * from rxjhrun")
        d = cur.fetchall()
        return d
        
    def createtab(self):
        cur = self.conn.cursor()
        createsql = '''
                CREATE TABLE `rxjhrun` (
                    `id` INTEGER PRIMARY KEY,
                    `datetime` DATETIME DEFAULT CURRENT_TIMESTAMP,
                    `messages` VARCHAR(500) DEFAULT NULL
                    );
                    '''
        try:
            cur.execute(createsql)
        except sqlite3.OperationalError as err:
            print("rxjhrun 已经存在 不需要重新创建")



if __name__ == "__main__":
    sql = Sql()
    sql.query()
    # sql.inster()