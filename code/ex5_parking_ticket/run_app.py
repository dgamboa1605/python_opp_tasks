import time

from vehicle import Vehicle
from parking_lot import ParkingLot
from parking_ticket import ParkingTicket

company_name = "--zonePArking--"
print("======================================================")
print("Welcome to {}, please register your car.".format(company_name))
print("======================================================")
car_license_plate = input("[+] Enter license plate of car: ")
print("License plate registered: {}".format(car_license_plate))
car_color = input("[+] Enter color of car: ")
print("Color registered: {}".format(car_color))
car_model = input("[+] Enter model of car: ")
print("Model registered: {}".format(car_model))


car = Vehicle(car_license_plate, car_color, car_model)
parking = ParkingLot(company_name)
parking.vehicle_enters(car.license_plate)
time.sleep(5)
parking.vehicle_leaves(car.license_plate)
parking.calcule_earnings()
ticket = ParkingTicket(parking.name, parking.enter_date, parking.leave_date, parking.earnings, car.license_plate)
ticket.print_ticket()