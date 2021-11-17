import Main
import unittest


class UnitTest(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(Main.calculate("5+5"),10)
        self.assertEqual(Main.calculate("-3+6"),3)
        self.assertEqual(Main.calculate("-6+-5"),-11)
    
    def test_sub(self):
        self.assertEqual(Main.calculate("5-5"),0)
        self.assertEqual(Main.calculate("-3-6"),-9)
        self.assertEqual(Main.calculate("-6--5"),-1)
    
    def test_div(self):
        self.assertEqual(Main.calculate("5/5"),1)
        self.assertEqual(Main.calculate("-3/6"),-0.5)
        self.assertEqual(Main.calculate("-6/-5"),1.2)

    def test_mul(self):
        self.assertEqual(Main.calculate("5*5"),25)
        self.assertEqual(Main.calculate("-3*6"),-18)
        self.assertEqual(Main.calculate("-6*-5"),30)

    # def test_zero(self):
    #     self.assertEqual(Main.calculate('1/0'), 0)
    
    # def test_wrongInput(self):
    #     self.assertEqual(Main.calculate('1+f'), 1)

    def test_zero(self):
        self.assertEqual(Main.calculate('1/0'), "Division By Zero")
    
    def test_wrongInput(self):
        self.assertEqual(Main.calculate('1+f'), "char not allowed")


if __name__=='__main__':
    unittest.main()
