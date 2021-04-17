import datetime


class ParkingTicket:

    def __init__(self, company_name, enter_date, leave_date, payment, license_plate):
        self.__company_name = company_name
        self.__enter_date = enter_date
        self.__leave_date = leave_date
        self.__payment = payment
        self.__license_plate = license_plate
    
    def get_date(self):
        return datetime.datetime.now()
    
    def print_ticket(self):
        print("==================================")
        print("========={}==========".format(self.__company_name))
        print("        CHECK FOR PARKING")
        print("           {}".format(self.get_date().strftime("%b %d %Y")))
        print("==================================")
        print("         CAR:  {}".format(self.__license_plate))
        print("FROM:  {}".format(self.__enter_date.strftime("%b %d %Y %H:%M:%S")))
        print("TO:    {}".format(self.__leave_date.strftime("%b %d %Y %H:%M:%S")))
        print("          Paid  : {}.00".format(self.__payment))
        print("==================================")
        print("    THANK YOU AND LUCKY ROAD!")
        print("==================================")