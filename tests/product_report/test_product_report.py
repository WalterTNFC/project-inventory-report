from inventory_report.inventory.product import Product


id = 0
nome_do_produto = "farinha",
nome_da_empresa = "Nature Coffees",
data_de_fabricacao = "01/05/2021"
data_de_validade = "02/06/2023"
numero_de_serie = "111111"
instrucoes_de_armazenamento = "ao abrigo de luz"


def test_relatorio_produto():
    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    for value in product:
        assert (value in product.__repr__()) is True
