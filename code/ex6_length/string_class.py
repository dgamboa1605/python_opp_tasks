from base_class import BaseClass

class StringClass(BaseClass):

    def __init__(self, value) -> None:
        self.value = value
    
    def validate_input(self):
        if type(self.value) is not str:
            raise ValueError("input value must be of type string")

    def calculate_length(self):
        count = 0
        for i in self.value:
            count += 1
        
        return count