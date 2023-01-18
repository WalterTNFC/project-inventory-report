from inventory_report.inventory.product import Product


def test_relatorio_produto():
    list = [
        "farinha",
        "Nature Coffees",
        "01/05/2021",
        "02/06/2023"
        "Armazenar ao abrigo de luz",
    ]

    product = Product(
        id=1,
        nome_do_produto=list[0],
        nome_da_empresa=list[1],
        data_de_fabricacao=list[2],
        data_de_validade=list[3],
        numero_de_serie='111111111',
        instrucoes_de_armazenamento=list[4],
    )

    assert product.__repr__() == (
        f"O produto {product['nome_do_produto']}"
        f" fabricado em {product['data_de_fabricacao']}"
        f" por {product['nome_da_empresa']} com validade"
        f" até {product['data_de_validade']}"
        f" precisa ser armazenado {product['instrucoes_de_armazenamento']}."
    )