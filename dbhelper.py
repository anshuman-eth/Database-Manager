#created by twitter.com/orin_anshuman

import mysql.connector as connector
class DBHelper:
    def __init__(self) -> None:
        self.con=connector.connect(host='localhost',port='3306',user='root',password='admin',database='pythontest')
    
        query='create table if not exists user (userId int primary key, userName varchar(200), phone varchar(12))'
        cur=self.con.cursor()
        cur.execute(query)
        print("Table Created")
    
    #insert
    def insert_user(self,userid,username,phone):
        query=f"insert into user(userId, userName, phone) values({userid},'{username}','{phone}')"
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User successfully inserted to the Database.")
        print()

    #fetch all
    def fetch_all(self):
        query="select * from user"
        cur=self.con.cursor()
        cur.execute(query)
        for row in cur:
            print("user Id :",row[0])
            print("user Name :",row[1])
            print("user Phone :",row[2])

    #delete user
    def delete_user(self,userid):
        query="delete from user where userId = {}".format(userid)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User successfully deleted from the Database.")
        print()
        
    #update
    def update_user(self,userid,newname,newphone):
        query="update user set userName = '{}',phone = '{}' where userid = {}".format(newname,newphone,userid)
        cur=self.con.cursor()
        cur.execute(query)
        self.con.commit()
        print("User successfully updated to the Database.")
        print()

#created by twitter.com/orin_anshuman
