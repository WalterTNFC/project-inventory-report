from inventory_report.inventory.product import Product

id = 0
nome_do_produto = "Teste do produto"
nome_da_empresa = "Teste da empresa"
data_de_fabricacao = "01/01/2000"
data_de_validade = "31/12/2000"
numero_de_serie = "111111"
instrucoes_de_armazenamento = "Teste de instrucoes"


def test_cria_produto():
    product = Product(
        id,
        nome_do_produto,
        nome_da_empresa,
        data_de_fabricacao,
        data_de_validade,
        numero_de_serie,
        instrucoes_de_armazenamento,
    )

    assert product.id == id
    assert product.nome_do_produto == nome_do_produto
    assert product.nome_da_empresa == nome_da_empresa
    assert product.data_de_fabricacao == data_de_fabricacao
    assert product.data_de_validade == data_de_validade
    assert product.numero_de_serie == numero_de_serie
    assert product.instrucoes_de_armazenamento == instrucoes_de_armazenamento
