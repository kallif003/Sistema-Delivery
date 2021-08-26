def pizzas_esfihas(tela1, tela2, cursor, QtWidgets, modulo):
    telaProduto = tela1
    telaAtualizarProdutos= tela2
    sql_pizza_adicionais = modulo

    telaProduto.hide()
    telaAtualizarProdutos.frame_adc_atualizar.hide()
    telaAtualizarProdutos.show()

    sql_pizza_adicionais.sql_pizzas_esfihas(cursor, telaAtualizarProdutos, QtWidgets)