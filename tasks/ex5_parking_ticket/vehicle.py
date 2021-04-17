class Vehicle:
    
    def __init__(self, license_plate, color, model):
        self.__license_plate = license_plate
        self.__color = color
        self.__model = model

    @property
    def license_plate(self):
        return self.__license_plate
    
    @license_plate.setter
    def license_plate(self, new_license_plate):
        self.__license_plate = new_license_plate
    
    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(self, new_color):
        self.__color = new_color
    
    @property
    def model(self):
        return self.__model
    
    @model.setter
    def model(self, new_model):
        self.__model = new_model
