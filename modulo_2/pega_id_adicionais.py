def pega_id(*args):
    try:
        telaAtualizarProdutos = args[0]
        telaErro = args[1]
        cursor = args[2]

        id = telaAtualizarProdutos.cod_atualizar_2.text()

        if telaAtualizarProdutos.buttonBroto_atualizar.isChecked():
            cursor.execute("select * from adcBroto where id = %s" % id)
            adicionais = cursor.fetchall()
            telaAtualizarProdutos.produto_adc_atualizar.setText(str(adicionais[0][1]))
            telaAtualizarProdutos.valor_adc_atualizar.setText(str(adicionais[0][3]))

        if telaAtualizarProdutos.ButtonSeis_atualizar.isChecked():
            cursor.execute("select * from adcSeis where id = %s" % id)
            adicionais = cursor.fetchall()
            telaAtualizarProdutos.produto_adc_atualizar.setText(str(adicionais[0][1]))
            telaAtualizarProdutos.valor_adc_atualizar.setText(str(adicionais[0][3]))

        if telaAtualizarProdutos.ButtonOito_atualizar.isChecked():
            cursor.execute("select * from adcOito where id = %s" % id)
            adicionais = cursor.fetchall()
            telaAtualizarProdutos.produto_adc_atualizar.setText(str(adicionais[0][1]))
            telaAtualizarProdutos.valor_adc_atualizar.setText(str(adicionais[0][3]))

        if telaAtualizarProdutos.ButtonDez_atualizar.isChecked():
            cursor.execute("select * from adcDez where id = %s" % id)
            adicionais = cursor.fetchall()
            telaAtualizarProdutos.produto_adc_atualizar.setText(str(adicionais[0][1]))
            telaAtualizarProdutos.valor_adc_atualizar.setText(str(adicionais[0][3]))

        if telaAtualizarProdutos.sem_adc_atualizar_2.isChecked():
            cursor.execute("select * from adcSem where id = %s" % id)
            adicionais = cursor.fetchall()
            telaAtualizarProdutos.produto_adc_atualizar.setText(str(adicionais[0][1]))
            telaAtualizarProdutos.valor_adc_atualizar.clear()
    except:
        telaErro.show()
        telaErro.label.setText('  Erro, tente novamente!')