import sqlite3
import random
import string

#creat or connect to database
conn = sqlite3.connect('ex2.db')

print("open database successfully.")

cur = conn.cursor()
cur.execute('''CREATE TABLE USERS
        (USERNAME STRING PRIMARY KEY,
        PASSWORD STRING,
        SPUBLICKEY STRING,
        SPRIVATEKEY STRING,
        EPUBLICKEY STRING,
        EPRIVATEKEY STRING);''')
print("create database successfully.")

conn.commit()


#ajouter un utilisateur a la bdd
def insert_user(name,password):
        
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(128)]
        key1 = ''.join(str_list)
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(128)]
        key2 = ''.join(str_list)
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(128)]
        key3 = ''.join(str_list)
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(128)]
        key4 = ''.join(str_list)
        
        cur.execute("INSERT INTO USERS (USERNAME, PASSWORD, SPUBLICKEY, SPRIVATEKEY, EPUBLICKEY, EPRIVATEKEY) \
                VALUES ('" + name + "', '" + password + "', '" + key1 + "', '" + key2 + "', '" + key3 + "', '" + key4 + "')")

        conn.commit()


#fonction de logging
def logging(name, password):
        cursor = conn.execute("SELECT USERNAME, PASSWORD  from USERS")
        for row in cursor:
                if password != row[1]:
                        print("your password is wrong.")
                        return False
                else:
                        print("login successfully.")
                        return True



#return clef
def return_clef(name, password):
        cursor = conn.execute("SELECT USERNAME, PASSWORD  from USERS WHERE USERNAME IS " + name)
        for row in cursor:
                if password != row[1]:
                        print("your password is wrong.")
                        return "0","0","0","0"
                else:
                        print("login successfully.")
                        return row[2],row[3],row[4],row[5]



#verify bdd is right
def verify():
        cursor = conn.execute("SELECT USERNAME, PASSWORD  from USERS")
        s = set()
        for row in cursor:
                maj = 0
                spe = 0
                num = 0
                
                #username is more than 3 chars
                if len(row[0]) < 3:
                        print("The length of username: ",row[0]," is shorter than 3.")
                        return False
                
                #username only contain letters and numbers
                for c in row[0]:
                        if c < '0' or (c>'9' and c<'A') or (c>'Z' and c<'a') or c > 'z':
                                print("The username ",row[0]," not only contain letters and numbers.")
                                return False
                
                # username is uniq
                if row[0] in s:
                        print("username: ",row[0]," is already in database.")
                        return False
                else:
                        s.add(row[0])

                # password has at least 8 chars
                if len(row[1]) < 8:
                        print("The length of password of ",row[0]," is shorter than 8.")
                        return False
                
                for c in row[1]:
                        # at least 1 uppercase leeter
                        if c > 'A' and c < 'Z':
                                maj = 1
                        # at least 1 special char
                        if c > 33 and c < 47:
                                spe = 1
                        # at least 1 number
                        if c > '1' and c < '9':
                                num = 1
                if (not maj) or (not spe) or (not num):
                        print("The format of the password does not meet the rules.")
                        return False
                
                for i in range(2,6):
                        if len(row[i]) != 128:
                                print("The length of key of ",row[0]," is not 128.")
                                return False
                 
        return True


def main():
        insert_user("Chen","X1mk.fioe")
        conn.close()

if __name__ == "__main__":
        main()