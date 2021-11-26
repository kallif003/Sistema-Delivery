def atualiza_adicionais(*args):

    telaAtualizarProdutos = args[0]
    cursor = args[1]
    QtWidgets = args[2]
    sql_pizza_adicionais = args[3]

    telaAtualizarProdutos.frame_adc_atualizar.show()

    sql_pizza_adicionais.sql_adicionais(cursor, telaAtualizarProdutos, QtWidgets)