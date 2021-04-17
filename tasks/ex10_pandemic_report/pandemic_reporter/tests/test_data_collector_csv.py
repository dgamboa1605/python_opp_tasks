from tasks.ex10_pandemic_report.pandemic_reporter.pandemic_report.data_collector_csv import DataCollectorCsv
from tasks.ex10_pandemic_report.pandemic_reporter.pandemic_report.person import Person
from textwrap import dedent
from unittest.mock import patch, mock_open


DATA = dedent("""
        id,name,last name,age,gender,covid,,,
        1,name1,Last Name1,45,Male,Positive,,,
        """).strip()

DATA_EMPTY = dedent("""
        id,name,last name,age,gender,covid,,,
        """).strip()


@patch("builtins.open", mock_open(read_data=DATA_EMPTY))
def test_get_empty_patients():
    data_collector_csv = DataCollectorCsv()
    result = data_collector_csv.get_patients()
    assert result == (200, "OK", [])


@patch("builtins.open", mock_open(read_data=DATA))
def test_get_patients():
    data_collector_csv = DataCollectorCsv()
    result = data_collector_csv.get_patients()
    p = Person('1', "name1", "Last Name1", "45", "Male")
    p.is_sick = True
    assert result == (200, "OK", [p])


def test_get_patients_bad_request():
    with patch("builtins.open", mock_open()) as mock_file:
        mock_file.side_effect = IOError()
        data_collector_csv = DataCollectorCsv()
        result = data_collector_csv.get_patients()
        assert result == (404, "Not Found", [])
