from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        id=1,
        nome_do_produto="farinha",
        nome_da_empresa="Nature Coffees",
        data_de_fabricacao="2021-05-01",
        data_de_validade="2023-06-02",
        numero_de_serie="Farinini",
        instrucoes_de_armazenamento="ao abrigo de luz",
    )

    convert_to_string = str(product)
    assert (isinstance(convert_to_string, str)) is True
    assert (convert_to_string) == (
        "O produto farinha fabricado em 01-05-2021 por Farinini "
        "com validade até 02-06-2023 precisa ser armazenado "
        "ao abrigo de luz."
    )
