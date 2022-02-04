#created by twitter.com/orin_anshuman

from dbhelper import DBHelper

def main():
    db=DBHelper()
    while True:
        print("****** Hi, Welcome to User management system Database. ******")
        print("Press 1 to insert new user")
        print("Press 2 to display all user")
        print("Press 3 to delete a user")
        print("Press 4 to update user")
        print("Press 5 to exit the program\n")
        try:
            choice=int(input())
            if choice==1:
                userid=int(input("Enter user id:"))
                username=input("Enter username:")
                userphone=input("Enter phone number:")
                db.insert_user(userid, username, userphone)

            elif choice==2:
                db.fetch_all()
                print()

            elif choice==3:
                userid=int(input("Enter the user id you want to delete:"))
                db.delete_user(userid)

            elif choice==4:
                userid=int(input("Enter user id you want to update:"))
                newname=input("Enter the new name you want to update:")
                newphone=input("Enter the new phone number you want to update:")
                db.update_user(userid,newname,newphone)
                
            elif choice==5:
                print("*** Exited from database ***")
                break
            else:
                print("Invalid input! Try again.")

        except Exception as e:
            print(e)
            print("Invalid details! Try again.")
            print()
            print()


if __name__=="__main__":
    main()

#created by twitter.com/orin_anshuman

