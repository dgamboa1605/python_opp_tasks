import pytest

from tasks.ex8_complex_numbers.complex_numbers import ComplexNumbers as comp

a = comp(2, 10j)
b = comp(3, 5j)

c = comp(-2, -1)
d = comp(-3, -5j)

f = comp(0, 1)
g = comp(3, 0)

sum_positive_parameters = (a, b, "(5+15j)")
sum_negative_parameteres = (c, d, "(-6-5j)")
sum_zeros_parameters = (f, g, "4")

sum_parameters = [sum_positive_parameters, sum_negative_parameteres, sum_zeros_parameters]

prod_positive_parameters = (a, b, "(56+40j)")
prod_negative_parameteres = (c, d, "(9+5j)")
prod_zeros_parameters = (f, g, "3")

prod_parameters = [prod_positive_parameters, prod_negative_parameteres, prod_zeros_parameters]


class TestComplexNumbersTests:

    def test_equality(self):
        assert a == a
    
    def test_inequality(self):
        assert not a == b
    
    def test_equality_raise_exception(self):
        with pytest.raises(TypeError):
            b = "test123"
            r = a == b
    
    def test_sum(self):
        assert a + b == comp(5, 15j)

    @pytest.mark.parametrize("i, k, res", sum_parameters)
    def test_sum_str_results(self, i, k, res):
        assert str(i + k) == res
    
    def test_sum_raise_exception(self):
        with pytest.raises(TypeError):
            b = "test123"
            r = a + b
    
    def test_sum_raise_exception_with_str_parameter(self):
        with pytest.raises(ValueError):
            b = comp(1, "2j")
            r = a + b
    
    def test_product(self):
        assert a * b == comp(56, 40j)
    
    @pytest.mark.parametrize("i, k, res", prod_parameters)
    def test_product_str_results(self, i, k, res):
        assert str(i * k) ==  res
    
    def test_product_raise_exception(self):
        with pytest.raises(TypeError):
            b = "test123"
            r = a * b
    
    def test_product_raise_exception_with_str_parameter(self):
        with pytest.raises(ValueError):
            a = comp("1", 2j)
            r = a * b
