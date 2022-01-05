import ex2
import sqlite3
import unittest
import random
import string

class Test(unittest.TestCase):

    def test_insert_user(self):
        self.assertEqual(ex2.insert_user("Chen","X1mk.fioe"),True)
        self.assertEqual(ex2.insert_user("Zheng","Qi,e0109"),True)
        # name < 3 chars
        self.assertEqual(ex2.insert_user("Zh","Qi,e0109"),False)
        # password < 8 chars
        self.assertEqual(ex2.insert_user("Zheng","Qi,e01"),False)
        # password does not have number
        self.assertEqual(ex2.insert_user("Zheng","Qi,exxxx"),False)
        # password does not have uppercase letter
        self.assertEqual(ex2.insert_user("Zheng","qi,e0109"),False)
        # password does not have special char
        self.assertEqual(ex2.insert_user("Zheng","qixe0109"),False)



    def test_logging(self):
        self.assertEqual(ex2.logging("Chen","X1mk.fioe"),True)
        self.assertEqual(ex2.logging("Chen","123hoFu3"),False)
        self.assertEqual(ex2.logging("Zheng","Qi,e0109"),True)
        self.assertEqual(ex2.logging("Zheng","123hoFu3"),False)


    def test_return_clef(self):
        conn = sqlite3.connect('ex2.db')
        ccursor = conn.execute("SELECT USERNAME, PASSWORD, SPUBLICKEY, SPRIVATEKEY, EPUBLICKEY, EPRIVATEKEY from USERS WHERE USERNAME IS 'Chen'")
        for row in ccursor:
            ckey1 = row[2]
            ckey2 = row[3]
            ckey3 = row[4]
            ckey4 = row[5]
        
        zcursor = conn.execute("SELECT USERNAME, PASSWORD, SPUBLICKEY, SPRIVATEKEY, EPUBLICKEY, EPRIVATEKEY from USERS WHERE USERNAME IS 'Zheng'")
        for row in zcursor:
            zkey1 = row[2]
            zkey2 = row[3]
            zkey3 = row[4]
            zkey4 = row[5]

        self.assertEqual(ex2.return_clef("Chen","X1mk.fioe"),(ckey1,ckey2,ckey3,ckey4))
        self.assertEqual(ex2.return_clef("Zheng","Qi,e0109"),(zkey1,zkey2,zkey3,zkey4))
        conn.close()


    def test_verify(self):

        self.assertEqual(ex2.verify(),True)

        conn = sqlite3.connect('ex2.db')
        cur = conn.cursor()

        #Randomly generate keys
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(128)]
        key1 = ''.join(str_list)
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(128)]
        key2 = ''.join(str_list)
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(128)]
        key3 = ''.join(str_list)
        str_list = [random.choice(string.digits + string.ascii_letters) for i in range(128)]
        key4 = ''.join(str_list)
    

        # username shorter than 3
        cur.execute("INSERT INTO USERS (USERNAME, PASSWORD, SPUBLICKEY, SPRIVATEKEY, EPUBLICKEY, EPRIVATEKEY) \
                VALUES ('Zh', 'Qi,e0109', '" + key1 + "', '" + key2 + "', '" + key3 + "', '" + key4 + "')") 
        conn.commit()
        self.assertEqual(ex2.verify(),False)
        conn.execute("DELETE FROM USERS WHERE USERNAME IS 'Zh'")
        conn.commit()

        # username contains a special char
        cur.execute("INSERT INTO USERS (USERNAME, PASSWORD, SPUBLICKEY, SPRIVATEKEY, EPUBLICKEY, EPRIVATEKEY) \
                VALUES ('Zhen,', 'Qi,e0109', '" + key1 + "', '" + key2 + "', '" + key3 + "', '" + key4 + "')") 
        conn.commit()
        self.assertEqual(ex2.verify(),False)
        conn.execute("DELETE FROM USERS WHERE USERNAME IS 'Zhen,'")
        conn.commit()


        #password does not contain a uppercase letter
        cur.execute("INSERT INTO USERS (USERNAME, PASSWORD, SPUBLICKEY, SPRIVATEKEY, EPUBLICKEY, EPRIVATEKEY) \
                VALUES ('zheng', 'qi,e0109', '" + key1 + "', '" + key2 + "', '" + key3 + "', '" + key4 + "')") 
        conn.commit()
        self.assertEqual(ex2.verify(),False)
        conn.execute("DELETE FROM USERS WHERE USERNAME IS 'zheng'")
        conn.commit()

        #password does not contain number
        cur.execute("INSERT INTO USERS (USERNAME, PASSWORD, SPUBLICKEY, SPRIVATEKEY, EPUBLICKEY, EPRIVATEKEY) \
                VALUES ('zheng', 'Qi,exxxx', '" + key1 + "', '" + key2 + "', '" + key3 + "', '" + key4 + "')") 
        conn.commit()
        self.assertEqual(ex2.verify(),False)
        conn.execute("DELETE FROM USERS WHERE USERNAME IS 'zheng'")
        conn.commit()

        conn.close()



if __name__ == '__main__':
    unittest.main()

