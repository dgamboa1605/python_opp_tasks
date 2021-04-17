import csv

from tasks.ex10_pandemic_report.pandemic_reporter.pandemic_report import constants
from tasks.ex10_pandemic_report.pandemic_reporter.pandemic_report.person import Person
from tasks.ex10_pandemic_report.pandemic_reporter.pandemic_report.data_collector import DataCollector
from tasks.ex10_pandemic_report.pandemic_reporter.utils import get_csv_path


class DataCollectorCsv(DataCollector):
    def __init__(self):
        self.__people = []
        self.__status_code = 200
        self.__load_data()

    def get_patients(self):
        status = constants.POSSIBLE_STATUS_CODES.get(self.__status_code)
        return self.__status_code, status.get("message"), self.__people

    def __load_data(self):
        try:
            with open(get_csv_path(), 'r') as file:
                reader = csv.reader(file)
                reader = list(reader)
                header = [h.lower() for h in reader[0]]
                for row in reader[1:]:
                    p_dict = dict(zip(header, row))
                    p = Person(p_dict["id"], p_dict["name"], p_dict["last name"], p_dict["age"], p_dict["gender"])
                    p.is_sick = constants.POSSIBLE_VALUES_SICK.get(p_dict["covid"].lower())
                    self.__people.append(p)
        except IOError:
            self.__status_code = 404
