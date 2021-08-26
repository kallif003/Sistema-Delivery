def atualiza_adicionais(tela, cursor, QtWidgets, modulo):
    telaAtualizarProdutos = tela
    sql_pizza_adicionais = modulo
    telaAtualizarProdutos.frame_adc_atualizar.show()

    sql_pizza_adicionais.sql_adicionais(cursor, telaAtualizarProdutos, QtWidgets)