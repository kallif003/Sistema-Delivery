def atualiza_bebidas_outros(*args):
    try:
        telaAtualizarBebidas = args[0]
        telaErro = args[1]
        cursor = args[2]
        banco10 = args[3]
        QtWidgets = args[4]
        setar_checkBox_false = args[5]

        id = telaAtualizarBebidas.id_atualizar_bebidas.text()
        produto = telaAtualizarBebidas.produto_atualizar.text()
        tipo = telaAtualizarBebidas.tipo_atualizar.text()
        valor = telaAtualizarBebidas.valor_atualizar.text()

        if telaAtualizarBebidas.lata_atualizar.isChecked():
            sql = ("update lata set bebida = %s, valor = %s where id = %s")
            values = (str(produto), str(valor), str(id))
            cursor.execute(sql, values)
            banco10.commit()

        if telaAtualizarBebidas.s600_atualizar.isChecked():
            sql = ("update s600 set bebida = %s, valor = %s where id = %s")
            values = (str(produto), str(valor), str(id))
            cursor.execute(sql, values)
            banco10.commit()

        if telaAtualizarBebidas.umLitro_atualizar.isChecked():
            sql = ("update umLitro set bebida = %s, valor = %s where id = %s")
            values = (str(produto), str(valor), str(id))
            cursor.execute(sql, values)
            banco10.commit()

        if telaAtualizarBebidas.umLmeio_atualizar.isChecked():
            sql = ("update umEmeio set bebida = %s, valor = %s where id = %s")
            values = (str(produto), str(valor), str(id))
            cursor.execute(sql, values)
            banco10.commit()

        if telaAtualizarBebidas.doisLitros_atualizar.isChecked():
            sql = ("update doisLitros set bebida = %s, valor = %s where id = %s")
            values = (str(produto), str(valor), str(id))
            cursor.execute(sql, values)
            banco10.commit()

        if telaAtualizarBebidas.doisLmeio_atualizar.isChecked():
            sql = ("update doisEmeio set bebida = %s, valor = %s where id = %s")
            values = (str(produto), str(valor), str(id))
            cursor.execute(sql, values)
            banco10.commit()

        if telaAtualizarBebidas.outros_atualizar.isChecked():
            sql = ("update outros set produto = %s, tipo = %s, valor = %s where id = %s")
            values = (str(produto), str(tipo), str(valor), str(id))
            cursor.execute(sql, values)
            banco10.commit()

        telaErro.show()
        telaErro.label.setText('  Produto atualizado com sucesso')

        lista = []
        sql = "select * from lata"
        cursor.execute(sql)
        dados1 = cursor.fetchall()
        sql = "select * from s600"
        cursor.execute(sql)
        dados2 = cursor.fetchall()
        sql = "select * from umLitro"
        cursor.execute(sql)
        dados3 = cursor.fetchall()
        sql = "select * from umEmeio"
        cursor.execute(sql)
        dados4 = cursor.fetchall()
        sql = "select * from doisLitros"
        cursor.execute(sql)
        dados5 = cursor.fetchall()
        sql = "select * from doisEmeio"
        cursor.execute(sql)
        dados6 = cursor.fetchall()
        sql = "select * from outros"
        cursor.execute(sql)
        dados7 = cursor.fetchall()

        for j in dados1:
            lista.append(j)
        for k in dados2:
            lista.append(k)
        for i in dados3:
            lista.append(i)
        for l in dados4:
            lista.append(l)
        for m in dados5:
            lista.append(m)
        for n in dados6:
            lista.append(n)
        for o in dados7:
            lista.append(o)

        telaAtualizarBebidas.tableWidget_cadastro_4.setRowCount(len(lista))
        telaAtualizarBebidas.tableWidget_cadastro_4.setColumnCount(4)
        for i in range(0, len(lista)):
            for j in range(4):
                telaAtualizarBebidas.tableWidget_cadastro_4.setItem(i, j, QtWidgets.QTableWidgetItem(str(lista[i][j])))

        telaAtualizarBebidas.produto_atualizar.clear()
        telaAtualizarBebidas.valor_atualizar.clear()
        telaAtualizarBebidas.tipo_atualizar.clear()

        setar_checkBox_false.checkBox_atualizacao_bebidas_outros(telaAtualizarBebidas)
    except:
        telaErro.show()
        telaErro.label.setText('  Erro, tente novamente!')