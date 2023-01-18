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

    mock_product = create_product()

    product = Product(
        mock_product['id'],
        mock_product['nome_do_produto'],
        mock_product['nome_da_empresa'],
        mock_product['data_de_fabricacao'],
        mock_product['data_de_validade'],
        mock_product['numero_de_serie'],
        mock_product['instrucoes_de_armazenamento'],
    )

    assert product.__repr__() == (
        f"O produto {mock_product['nome_do_produto']}"
        f" fabricado em {mock_product['data_de_fabricacao']}"
        f" por {mock_product['nome_da_empresa']} com validade"
        f" até {mock_product['data_de_validade']}"
        f" precisa ser armazenado {mock_product['instrucoes_de_armazenamento']}."
    )
