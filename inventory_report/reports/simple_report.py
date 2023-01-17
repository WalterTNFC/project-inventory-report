# Método estático
# Recebe uma lista
# Retorna uma string:
# Data de fabricação mais antiga: YYYY-MM-DD
# Data de validade mais próxima: YYYY-MM-DD
# Empresa com mais produtos: NOME DA EMPRESA

from datetime import date
from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(list):

        # Referência: 1
        # Data de referência
        ref = str(date.today())

        # Referência: 2
        oldest_date = min(list, key=lambda d: d["data_de_fabricacao"])
        expiration = [item for item in list if item["data_de_validade"] > ref]
        closest_exp = min(expiration, key=lambda d: d["data_de_validade"])

        # Referência: 3
        get_companies = [item["nome_da_empresa"] for item in list]
        verify_occurrence, _ = Counter(get_companies).most_common()[0]

        return_oldest = oldest_date['data_de_fabricacao']
        return_closest = closest_exp['data_de_validade']

        return (
            f"Data de fabricação mais antiga: {return_oldest}\n"
            f"Data de validade mais próxima: {return_closest}\n"
            f"Empresa com mais produtos: {verify_occurrence}"
        )


# Referências:
# 1- https://www.alura.com.br/artigos/lidando-com-datas-e-horarios-no-python
# 2- https://pt.stackoverflow.com/questions/482995
# 3- https://stackoverflow.com/questions/3594514
