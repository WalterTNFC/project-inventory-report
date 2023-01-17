from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json


class Inventory:
    @staticmethod
    def csv_file(path, type):
        with open(path, encoding="utf-8") as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
            if type == 'simples':
                return SimpleReport.generate(list(data))
            elif type == 'completo':
                return CompleteReport.generate(list(data))

    def json_file(path, type):
        with open(path, mode="r") as file:
            data = json.load(file)
            if type == 'simples':
                return SimpleReport.generate(data)
            elif type == 'completo':
                return CompleteReport.generate(data)

    @staticmethod
    def import_data(path, type):
        try:
            if 'csv' in path:
                return Inventory.csv_file(path, type)
            elif 'json' in path:
                return Inventory.json_file(path, type)
        except OSError:
            raise ValueError('Type invalid')
