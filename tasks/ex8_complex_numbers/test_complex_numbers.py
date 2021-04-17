import unittest

from tasks.ex8_complex_numbers.complex_numbers import ComplexNumbers as comp


class TestComplexNumbers(unittest.TestCase):

    def test_equality(self):
        self.assertTrue(comp(2, 2j) == comp(2, 2j))
    
    def test_inequality(self):
        self.assertFalse(comp(1, 1j) == comp(2, 2j))
    
    def test_equality_raise_exception(self):
        with self.assertRaises(TypeError):
            a = comp(1, 2j)
            b = "test123"
            r = a == b

    def test_sum_str_results(self):
        i = comp(2, 10j)
        k = comp(3, 5j)
        self.assertEqual(str(i+k), "(5+15j)")

    def test_sum(self):
        i = comp(2, 10j)
        k = comp(3, 5j)
        self.assertEqual(i+k, comp(5, 15j))
    
    def test_sum_with_negative_parameters(self):
        i = comp(-2, -1)
        k = comp(-3, -5j)
        self.assertEqual(str(i+k), "(-6-5j)")
    
    def test_sum_with_cero_parameters(self):
        i = comp(0, 1)
        k = comp(3, 0)
        self.assertEqual(str(i+k), "4")
    
    def test_sum_raise_exception(self):
        with self.assertRaises(TypeError):
            a = comp(1, 2j)
            b = "test123"
            r = a + b
    
    def test_sum_raise_exception_with_str_parameter(self):
        with self.assertRaises(ValueError):
            a = comp(1, 2j)
            b = comp(1, "2j")
            r = a + b
    
    def test_product_str_results(self):
        i = comp(2, 10j)
        k = comp(3, 5j)
        self.assertEqual(str(i*k), "(56+40j)")

    def test_product(self):
        i = comp(2, 10j)
        k = comp(3, 5j)
        self.assertEqual(i*k, comp(56, 40j))
    
    def test_product_with_negative_parameters(self):
        i = comp(-2, -1)
        k = comp(-3, -5j)
        self.assertEqual(str(i*k), "(9+5j)")
    
    def test_product_with_cero_parameters(self):
        i = comp(0, 1)
        k = comp(3, 0)
        self.assertEqual(str(i*k), "3")
    
    def test_product_raise_exception(self):
        with self.assertRaises(TypeError):
            a = comp(1, 2j)
            b = "test123"
            r = a * b
    
    def test_product_raise_exception_with_str_parameter(self):
        with self.assertRaises(ValueError):
            a = comp("1", 2j)
            b = comp(1, 2j)
            r = a * b


if __name__ == "__main__":
    unittest.main()
