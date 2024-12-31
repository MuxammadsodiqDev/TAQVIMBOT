import sqlite3

#Adding users table
def usersInsert(user_id,manzil):
    try:
        con = sqlite3.connect("taqvimbot.db")
        cursor = con.cursor()
        cursor.execute("""insert into users(user_id,manzil) values(?,?)""",(user_id,manzil))
        con.commit()
        cursor.close()
    except(Exception,sqlite3.Error) as error:
        print(error)
    finally:
        if con:
            con.close()
            print("yangi foydalanuvchi qo'shildi.")

#Reading users table
def usersRead():
    try:
        con = sqlite3.connect("taqvimbot.db")
        cursor = con.cursor()
        cursor.execute(f"""select * from users where user_id""")
        a = cursor.fetchall()
        cursor.close()
        return a 
    except(Exception, sqlite3.Error)as error:
        print("error",error)
    finally:
        if con:
            con.close()




#Delete user of users table
def usersDelete(user_id):
    try :
        con = sqlite3.connect("taqvimbot.db")
        cursor = con.cursor()
        cursor.execute(f"DELETE FROM users WHERE user_id = {user_id}")
        con.commit()
    except(Exception,sqlite3.Error) as error:
        print(error)
    finally:
        if con:
            cursor.close()
            con.close()
            print("user o'chirildi")

#update users' info
def usersUpdate(user_id,manzil):
    try :
        con = sqlite3.connect("taqvimbot.db")
        cursor = con.cursor()
        cursor.execute(f"UPDATE users SET manzil = ? WHERE user_id = ?  ",(manzil,user_id))
        con.commit()
    except(Exception,sqlite3.Error) as error:
        print(error)
    finally:
        if con:
            cursor.close()
            con.close()
            print("user's info yangilandi")












    #Create taqvimbot database
# try:
#     con = sqlite3.connect("taqvimbot.db")
#     cursor = con.cursor()
#     cursor.execute(""" create table users(
#                    user_id integer primary key not null ,
#                    manzil text not null);""")
#     con.commit()
#     cursor.close()
#     print("tabla yaratildi")
# except(Exception,sqlite3.Error) as error:
#     print("error",error)
# finally:
#     if con:
#         cursor.close()
#         con.close()