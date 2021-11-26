def pizzas_esfihas(*args):

    telaProduto = args[0]
    telaAtualizarProdutos= args[1]
    cursor = args[2]
    QtWidgets = args[3]
    sql_pizza_adicionais = args[4]

    telaProduto.hide()
    telaAtualizarProdutos.frame_adc_atualizar.hide()
    telaAtualizarProdutos.show()

    sql_pizza_adicionais.sql_pizzas_esfihas(cursor, telaAtualizarProdutos, QtWidgets)