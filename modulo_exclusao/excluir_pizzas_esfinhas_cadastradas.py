def excluir(tela1, tela3, cursor, banco10, QtWidgets, modulo):
    try:
        telaAtualizarProdutos = tela1
        telaErro = tela3
        sql_pizza_adicionais = modulo

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
