import datetime


class ParkingLot:

  def __init__(self, name, capacity = 1, rate = 1):

    self.__name = name
    self.__capacity = capacity
    self.__rate = rate
    self.__earnings = 0
    self.__enter_date = ""
    self.__leave_date = ""
    
    self.__cars_enter_time = {}
  
  @property
  def name(self):
    return self.__name
  
  @property
  def enter_date(self):
    return self.__enter_date
  
  @property
  def leave_date(self):
    return self.__leave_date
  
  @property
  def earnings(self):
    return self.__earnings

  def get_time(self):
    return datetime.datetime.now()
  
  def vehicle_enters(self, vehicle):
    
    if self.__capacity == 0:
      raise Exception("Error: Parking lot full!")
    
    self.__enter_date = self.get_time()
    self.__cars_enter_time[vehicle] = self.__enter_date
    self.__capacity -= 1


  def vehicle_leaves(self, vehicle):
    self.__leave_date = self.get_time()
    del self.__cars_enter_time[vehicle]
    self.__capacity += 1

  def calcule_earnings(self):
    seconds_diff = self.__leave_date - self.__enter_date
    self.__earnings += self.__rate * seconds_diff.seconds
