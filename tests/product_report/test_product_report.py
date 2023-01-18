from inventory_report.inventory.product import Product


def create_product():
    return {
        "id": 1,
        "nome_do_produto": "farinha",
        "nome_da_empresa": "Nature Coffees",
        "data_de_fabricacao": "01/05/2021",
        "data_de_validade": "02/06/2023",
        "numero_de_serie": "111111111",
        "instrucoes_de_armazenamento": "Armazenar ao abrigo de luz",
    }


def test_relatorio_produto():
    # list = [
    #     "farinha",
    #     "Nature Coffees",
    #     "01/05/2021",
    #     "02/06/2023"
    #     "Armazenar ao abrigo de luz",
    # ]

    mock = create_product()

    product = Product(
        mock['id'],
        mock['nome_do_produto'],
        mock['nome_da_empresa'],
        mock['data_de_fabricacao'],
        mock['data_de_validade'],
        mock['numero_de_serie'],
        mock['instrucoes_de_armazenamento'],
    )

    assert product.__repr__() == (
        f"O produto {mock['nome_do_produto']}"
        f" fabricado em {mock['data_de_fabricacao']}"
        f" por {mock['nome_da_empresa']} com validade"
        f" até {mock['data_de_validade']}"
        f" precisa ser armazenado {mock['instrucoes_de_armazenamento']}."
    )
