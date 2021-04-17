from tasks.ex6_length.string_class import StringClass
from tasks.ex6_length.list_class import ListClass
from tasks.ex6_length.dictionary_class import DictionaryClass
from tasks.ex6_length.calculate_length import calculate_length

s = StringClass("123345")
l = ListClass([1, 2, 3, 4])
d = DictionaryClass({"1": 1, "2": 2})

print(calculate_length(s))
print(calculate_length(l))
print(calculate_length(d))
