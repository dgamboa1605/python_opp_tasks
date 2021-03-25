import unittest

from complex_numbers import ComplexNumbers as comp

class TestComplexNumers(unittest.TestCase):

    def test_equality(self):
        self.assertTrue(comp(2, 2j) == comp(2, 2j))
    
    def test_inequality(self):
        self.assertFalse(comp(1, 1j) == comp(2, 2j))
    
    def test_equality_raise_exception(self):
        with self.assertRaises(TypeError):
            a = comp(1, 2j)
            b = "test123"
            r = a == b

    def test_str_sum_results(self):
        i = comp(2, 10j)
        k = comp(3, 5j)
        self.assertEqual(str(i+k), "(5+15j)")

    def test_sum(self):
        i = comp(2, 10j)
        k = comp(3, 5j)
        self.assertEqual(i+k, comp(5, 15j))
    
    def test_sum_raise_exception(self):
        with self.assertRaises(TypeError):
            a = comp(1, 2j)
            b = "test123"
            r = a + b
    
    def test_str_product_results(self):
        i = comp(2, 10j)
        k = comp(3, 5j)
        self.assertEqual(str(i*k), "(56+40j)")

    def test_product(self):
        i = comp(2, 10j)
        k = comp(3, 5j)
        self.assertEqual(i*k, comp(56, 40j))
    
    def test_product_raise_exception(self):
        with self.assertRaises(TypeError):
            a = comp(1, 2j)
            b = "test123"
            r = a * b


if __name__ == "__main__":
    unittest.main()
