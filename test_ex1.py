import ex1
import unittest
list1 = [1,5,2,12,13,24,6]
list2 = [3,6,9,12,15,18]
list3 = [3,6,12,24,48,96]
list4 = [3,6,9,24,48,96]

class Test(unittest.TestCase):
    def test_min_int(self):
        self.assertEqual(ex1.min_int(0,2),0)
        self.assertEqual(ex1.min_int(-1,-5),-5)
        self.assertEqual(ex1.min_int(-1,2),-1)
        self.assertEqual(ex1.min_int(0,0),0)


    def test_mean_int(self):
        self.assertEqual(ex1.mean_int(list1),9)
        self.assertEqual(ex1.mean_int(list2),10.5)
        self.assertEqual(ex1.mean_int(list3),31.5)
        self.assertEqual(ex1.mean_int(list4),31)


    def test_median_int(self):
        self.assertEqual(ex1.median_int(list1),6)
        self.assertEqual(ex1.median_int(list2),10.5)
        self.assertEqual(ex1.median_int(list3),18)
        self.assertEqual(ex1.median_int(list4),16.5)


    def test_ecart_int(self):
        self.assertEqual(ex1.ecart_int(list1),7.45)
        self.assertEqual(ex1.ecart_int(list2),5.12)
        self.assertEqual(ex1.ecart_int(list3),32.48)
        self.assertEqual(ex1.ecart_int(list4),32.8)


    def test_geometrique(self):
        self.assertEqual(ex1.geometrique(list1),False)
        self.assertEqual(ex1.geometrique(list2),False)
        self.assertEqual(ex1.geometrique(list3),True)
        self.assertEqual(ex1.geometrique(list4),False)


    def test_arithmetique(self):
        self.assertEqual(ex1.arithmetique(list1),False)
        self.assertEqual(ex1.arithmetique(list2),True)
        self.assertEqual(ex1.arithmetique(list3),False)
        self.assertEqual(ex1.arithmetique(list4),False)


    def test_is_geometrique(self):
        self.assertEqual(ex1.is_geometrique(2,list2),False)
        self.assertEqual(ex1.is_geometrique(3,list3,),False)
        self.assertEqual(ex1.is_geometrique(2,list3),True)
        self.assertEqual(ex1.is_geometrique(2,list4),False)


    def test_is_arithmetique(self):
        self.assertEqual(ex1.is_arithmetique(2,list2),False)
        self.assertEqual(ex1.is_arithmetique(3,list2),True)
        self.assertEqual(ex1.is_arithmetique(3,list3),False)
        self.assertEqual(ex1.is_arithmetique(3,list4),False)


if __name__ == '__main__':
    unittest.main()
