from tasks.ex10_pandemic_report.pandemic_reporter.pandemic_report import data_collector


class DataCollectorFactory(object):
    @staticmethod
    def get_data_collector_instance(collector_type):
        instance = None
        subclasses = data_collector.DataCollector.__subclasses__()
        for cls in subclasses:
            if cls.__name__ == collector_type:
                instance = cls()

        return instance
