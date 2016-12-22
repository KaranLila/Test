import unittest


def damage(n):
    return n * 2

def health_bar(x):
    return x + 3

def resources(k,p):
    return k == p

class testdamage(unittest.TestCase):

    def test_damage(self):

        self.assertEqual(damage(5 ), 10)
    def test_health_bar(self):
        self.assertEqual(health_bar(1),4)
    def test_resources(self):
        self.assertEqual(resources(10,5),False)

def main():
    unittest.main()




if __name__=='__main__':
    unittest.main()


