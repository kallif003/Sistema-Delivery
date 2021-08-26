def atualiza_pizzas_esfihas(tela1, tela2, cursor, banco10, QtWidgets, modulo):

    try:
        telaAtualizarProdutos= tela1
        telaErro = tela2
        setar_checkBox_false = modulo

        id = telaAtualizarProdutos.cod_atualizar.text()
        sabor = telaAtualizarProdutos.produto_atualizar.text()
        ingredientes = telaAtualizarProdutos.ingredientes_atualizar.text()
        valor = telaAtualizarProdutos.valor_atualizar.text()

        if telaAtualizarProdutos.broto_atualizar.isChecked():
            sql = ("update broto set sabor = %s , ingredientes = %s, valorProduto = %s where id = %s ")
            values = (str(sabor), str(ingredientes), str(valor), str(id))
            cursor.execute(sql, values)
            banco10.commit()

        if telaAtualizarProdutos.seis_atualizar.isChecked():
            sql = ("update seisPedacos set sabor = %s , ingredientes = %s, valorProduto = %s where id = %s ")
            values = (str(sabor), str(ingredientes), str(valor), str(id))
            cursor.execute(sql, values)
            banco10.commit()

        if telaAtualizarProdutos.oito_atualizar.isChecked():
            sql = ("update oitoPedacos set sabor = %s , ingredientes = %s, valorProduto = %s where id = %s ")
            values = (str(sabor), str(ingredientes), str(valor), str(id))
            cursor.execute(sql, values)
            banco10.commit()

        if telaAtualizarProdutos.dez_atualizar.isChecked():
            sql = ("update dezPedacos set sabor = %s , ingredientes = %s, valorProduto = %s where id = %s ")
            values = (str(sabor), str(ingredientes), str(valor), str(id))
            cursor.execute(sql, values)
            banco10.commit()

        if telaAtualizarProdutos.esfiha_atualizar.isChecked():
            sql = ("update esfihas set sabor = %s , ingredientes = %s, valorProduto = %s where id = %s ")
            values = (str(sabor), str(ingredientes), str(valor), str(id))
            cursor.execute(sql, values)
            banco10.commit()

        telaErro.show()
        telaErro.label.setText('  Produto atualizado com sucesso!')

        lista = []
        sql = "select * from broto"
        cursor.execute(sql)
        dados1 = cursor.fetchall()
        sql = "select * from seisPedacos"
        cursor.execute(sql)
        dados2 = cursor.fetchall()
        sql = "select * from oitoPedacos"
        cursor.execute(sql)
        dados3 = cursor.fetchall()
        sql = "select * from dezPedacos"
        cursor.execute(sql)
        dados4 = cursor.fetchall()
        sql = "select * from esfihas"
        cursor.execute(sql)
        dados5 = cursor.fetchall()

        for a, b, c, d in zip(dados1, dados2, dados3, dados4):
            lista.append(a)
            lista.append(b)
            lista.append(c)
            lista.append(d)
        for e in dados5:
            lista.append(e)

        telaAtualizarProdutos.tableWidget_cadastro_3.setRowCount(len(lista))
        telaAtualizarProdutos.tableWidget_cadastro_3.setColumnCount(5)
        for i in range(0, len(lista)):
            for j in range(5):
                telaAtualizarProdutos.tableWidget_cadastro_3.setItem(i, j, QtWidgets.QTableWidgetItem(str(lista[i][j])))

        telaAtualizarProdutos.produto_atualizar.clear()
        telaAtualizarProdutos.ingredientes_atualizar.clear()
        telaAtualizarProdutos.valor_atualizar.clear()
        setar_checkBox_false.checkBox_atualizacao_pizzas_esfihas(telaAtualizarProdutos)

    except Exception as erro:
        print(erro.__class__)
        print('cu')
    except:
        telaErro.show()
        telaErro.label.setText('  Erro, tente novamente!')
