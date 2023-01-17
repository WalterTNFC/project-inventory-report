# Metodo generate
# CompleteReport herda a classe SimpleReport
# Sobrescrever o metodo generate


from inventory_report.reports.simple_report import SimpleReport


class CompleteReport:
    @staticmethod
    def generate(list):

        simple_report = SimpleReport.generate(list)
        print(simple_report)

        # Referência 1
        counter = {}
        for value in list:
            if value['nome_da_empresa'] in counter:
                counter[value['nome_da_empresa']] += 1
            else:
                counter[value['nome_da_empresa']] = 1

        # Referência 2:
        full_list = ''
        for key, value in counter.items():
            full_list += f"- {key}: {value}\n"

        return (
            f"{simple_report}\n"
            f"Produtos estocados por empresa:\n"
            f"{full_list}"
        )

# Referência:
# 1- https://pt.stackoverflow.com/a/407428
# 2- https://pt.stackoverflow.com/a/341176
