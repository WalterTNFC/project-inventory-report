from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
import csv
import json
import xmltodict


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

    def xml_file(path, type):
        with open(path) as file:
            # Referência 1
            data = xmltodict.parse(file.read())['dataset']['record']
            if type == 'simples':
                return SimpleReport.generate(data)
            elif type == 'completo':
                return CompleteReport.generate(data)

    @staticmethod
    def import_data(path, type):
        if 'csv' in path:
            return Inventory.csv_file(path, type)
        elif 'json' in path:
            return Inventory.json_file(path, type)
        elif 'xml' in path:
            return Inventory.xml_file(path, type)
        else:
            raise ValueError('Type Invalid')

# Referências:
# 1- https://stackabuse.com/reading-and-writing-xml-files-in-python/
