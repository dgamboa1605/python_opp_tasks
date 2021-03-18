from string_class import StringClass
from list_class import ListClass
from dictionary_class import DictionaryClass
from calculate_length import CalculateLength

s = StringClass("123345")
l = ListClass([1,2,3,4])
d = DictionaryClass({"1":1, "2":2})

print(CalculateLength.calculate(s))
print(CalculateLength.calculate(l))
print(CalculateLength.calculate(d))