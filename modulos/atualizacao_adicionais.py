def atualiza_adicionais(*args):
    try:

        telaAtualizarProdutos = args[0]
        telaErro = args[1]
        cursor = args[2]
        banco10 = args[3]
        QtWidgets = args[4]
        setar_checkBox_false = args[5]

        id = telaAtualizarProdutos.cod_atualizar_2.text()
        adicional = telaAtualizarProdutos.produto_adc_atualizar.text()
        valor = telaAtualizarProdutos.valor_adc_atualizar.text()

        if telaAtualizarProdutos.buttonBroto_atualizar.isChecked():
            sql = ("update adcBroto set adicional = %s, valor = %s where id = %s")
            values = (str(adicional), str(valor), str(id))
            cursor.execute(sql, values)
            banco10.commit()

        if telaAtualizarProdutos.ButtonSeis_atualizar.isChecked():
            sql = ("update adcSeis set adicional = %s, valor = %s where id = %s")
            values = (str(adicional), str(valor), str(id))
            cursor.execute(sql, values)
            banco10.commit()

        if telaAtualizarProdutos.ButtonOito_atualizar.isChecked():
            sql = ("update adcOito set adicional = %s, valor = %s where id = %s")
            values = (str(adicional), str(valor), str(id))
            cursor.execute(sql, values)
            banco10.commit()

        if telaAtualizarProdutos.ButtonDez_atualizar.isChecked():
            sql = ("update adcDez set adicional = %s, valor = %s where id = %s")
            values = (str(adicional), str(valor), str(id))
            cursor.execute(sql, values)
            banco10.commit()

        if telaAtualizarProdutos.sem_adc_atualizar_2.isChecked():
            sql = ("update adcSem set adicional = %s where id = %s")
            values = (str(adicional), str(id))
            cursor.execute(sql, values)
            banco10.commit()

        telaErro.show()
        telaErro.label.setText('  Produto atualizado com sucesso!')

        listaAdc = []
        sql1 = ("select * from adcBroto")
        cursor.execute(sql1)
        dados1 = cursor.fetchall()
        sql2 = ("select * from adcSeis ")
        cursor.execute(sql2)
        dados2 = cursor.fetchall()
        sql3 = ("select * from adcOito")
        cursor.execute(sql3)
        dados3 = cursor.fetchall()
        sql4 = ("select * from adcDez")
        cursor.execute(sql4)
        dados4 = cursor.fetchall()
        slq5 = ("select * from adcSem")
        cursor.execute(slq5)
        dados5 = cursor.fetchall()

        for i, j, k, l, m in zip(dados1, dados2, dados3, dados4, dados5):
            listaAdc.append(i)
            listaAdc.append(j)
            listaAdc.append(k)
            listaAdc.append(l)
            listaAdc.append(m)

        telaAtualizarProdutos.tableWidget_adc_atualizar.setRowCount(len(listaAdc))
        telaAtualizarProdutos.tableWidget_adc_atualizar.setColumnCount(4)
        for i in range(0, len(listaAdc)):
            for j in range(4):
                telaAtualizarProdutos.tableWidget_adc_atualizar.setItem(i, j,
                QtWidgets.QTableWidgetItem(str(listaAdc[i][j])))

        telaAtualizarProdutos.produto_adc_atualizar.clear()
        telaAtualizarProdutos.valor_adc_atualizar.clear()
        setar_checkBox_false.checkBox_atualizacao_adicionais(telaAtualizarProdutos)

    except:
        telaErro.show()
        telaErro.label.setText('  Erro, tente novamente!')
