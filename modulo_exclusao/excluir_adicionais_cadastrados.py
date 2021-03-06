def excluir(*args):
    try:
        telaAtualizarProdutos = args[0]
        telaErro = args[1]
        cursor = args[2]
        banco10 = args[3]
        QtWidgets = args[4]
        sql_pizza_adicionais = args[5]

        id = telaAtualizarProdutos.cod_atualizar_2.text()

        if telaAtualizarProdutos.buttonBroto_atualizar.isChecked():
            cursor.execute("delete from adcBroto where id = %s" % id)
            banco10.commit()
            telaErro.show()
            telaErro.label.setText('Excluido com sucesso!')

        if telaAtualizarProdutos.ButtonSeis_atualizar.isChecked():
            cursor.execute("delete from adcSeis where id = %s" % id)
            banco10.commit()
            telaErro.show()
            telaErro.label.setText('Excluido com sucesso!')

        if telaAtualizarProdutos.ButtonOito_atualizar.isChecked():
            cursor.execute("delete from adcOito where id = %s" % id)
            banco10.commit()
            telaErro.show()
            telaErro.label.setText('Excluido com sucesso!')

        if telaAtualizarProdutos.ButtonDez_atualizar.isChecked():
            cursor.execute("delete from adcDez where id = %s" % id)
            banco10.commit()
            telaErro.show()
            telaErro.label.setText('Excluido com sucesso!')

        if telaAtualizarProdutos.sem_adc_atualizar_2.isChecked():
            cursor.execute("delete from adcSem where id = %s" % id)
            banco10.commit()
            telaErro.show()
            telaErro.label.setText('Excluido com sucesso!')

        sql_pizza_adicionais.sql_adicionais(cursor, telaAtualizarProdutos, QtWidgets)

    except Exception as erro:
        print(erro.__class__)

