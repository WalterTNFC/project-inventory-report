from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv


class Inventory:
    @staticmethod
    def import_data(path, type):
        try:
            with open(path, encoding="utf-8") as file:
                data = csv.DictReader(file, delimiter=",", quotechar='"')
                if type == 'simples':
                    return SimpleReport.generate(data)
                elif type == 'completo':
                    return CompleteReport.generate(data)
        except OSError:
            raise ValueError('Type invalid')
