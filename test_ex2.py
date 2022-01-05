import ex2
import sqlite3
import unittest

class Test(unittest.TestCase):

    def test_insert_user(self):
        self.assertEqual(ex2.insert_user("Chen","X1mk.fioe"),True)
        self.assertEqual(ex2.insert_user("Zheng","Qi,e0109"),True)



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

        # username shorter than 3
        ex2.insert_user("ff","ji3O8h.T") 
        self.assertEqual(ex2.verify(),False)
        conn.execute("DELETE FROM USERS WHERE USERNAME IS 'ff'")
        conn.commit()

        # username contains a special char
        ex2.insert_user("ff:f","ji3O8h.T") 
        self.assertEqual(ex2.verify(),False)
        conn.execute("DELETE FROM USERS WHERE USERNAME IS 'ff:f'")
        conn.commit()


        #password does not contain a uppercase letter
        ex2.insert_user("kkk","ji3e8h.t") 
        self.assertEqual(ex2.verify(),False)
        conn.execute("DELETE FROM USERS WHERE USERNAME IS 'kkk'")
        conn.commit()

        #password does not contain number
        ex2.insert_user("kkk","jiReBh.t") 
        self.assertEqual(ex2.verify(),False)
        conn.execute("DELETE FROM USERS WHERE USERNAME IS 'kkk'")
        conn.commit()

        conn.close()



if __name__ == '__main__':
    unittest.main()

