from code.ex6_length.base_class import BaseClass


class ListClass(BaseClass):
    
    def __init__(self, value) -> None:
        self.value = value
    
    def validate_input(self):
        if type(self.value) is not list:
            raise ValueError("input value must be of type list")
    
    def calculate_length(self):
        count = 0
        for i in self.value:
            count += 1
        
        return count
