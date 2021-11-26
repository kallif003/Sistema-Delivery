def excluir(*args):
    try:
        telaAtualizarProdutos = args[0]
        telaErro = args[1]
        cursor = args[2]
        banco10 = args[3]
        QtWidgets = args[4]
        sql_pizza_adicionais = args[5]

        id = telaAtualizarProdutos.cod_atualizar.text()

        if telaAtualizarProdutos.broto_atualizar.isChecked():
            cursor.execute("delete from broto where id = %s" % id)
            banco10.commit()

        if telaAtualizarProdutos.esfiha_atualizar.isChecked():
            cursor.execute("delete from esfihas where id = %s" % id)
            banco10.commit()

        sql_pizza_adicionais.sql_pizzas_esfihas(cursor, telaAtualizarProdutos, QtWidgets)

        telaErro.show()
        telaErro.label.setText('Excluido com sucesso!')
    except Exception as erro:
        print(erro.__class__)
