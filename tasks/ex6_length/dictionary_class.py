from tasks.ex6_length.base_class import BaseClass


class DictionaryClass(BaseClass):
    
    def __init__(self, value) -> None:
        self.value = value
    
    def validate_input(self):
        if type(self.value) is not dict:
            raise ValueError("input value must be of type dictionary")
    
    def calculate_length(self):
        count = 0
        for i in self.value:
            count += 1
        
        return count
