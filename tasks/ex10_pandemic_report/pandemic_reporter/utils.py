import os


def get_csv_path():
    dir_path = os.path.dirname(__file__)
    path = os.path.join(dir_path, 'src/report.csv')
    return path
