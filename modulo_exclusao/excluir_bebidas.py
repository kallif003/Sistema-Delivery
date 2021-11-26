def excluir(*args):
    try:
        telaExcluirBebidas = args[0]
        telaErro = args[1]
        telaBebida = args[2]
        cursor = args[3]
        banco10 = args[4]
        QtWidgets = args[5]
        setar_checkBox_false = args[6]

        id = telaExcluirBebidas.id_excluir_bebidas.text()

        if telaExcluirBebidas.lata.isChecked():
            cursor.execute("delete from lata where id = %s" % id)
            banco10.commit()

        if telaExcluirBebidas.s600.isChecked():
            cursor.execute("delete from s600 where id = %s" % id)
            banco10.commit()

        if telaExcluirBebidas.umLitro.isChecked():
            cursor.execute("delete from umLitro where id = %s" % id)
            banco10.commit()

        if telaExcluirBebidas.umLmeio.isChecked():
            cursor.execute("delete from umEmeio where id = %s" % id)
            banco10.commit()

        if telaExcluirBebidas.doisLitros.isChecked():
            cursor.execute("delete from doisLitros where id = %s" % id)
            banco10.commit()

        if telaExcluirBebidas.doisLmeio.isChecked():
            cursor.execute("delete from doisEmeio where id = %s" % id)
            banco10.commit()

        telaErro.show()
        telaErro.label.setText('  Produto excluido com sucesso!')

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

        telaBebida.tableWidget_cadastro_2.setRowCount(len(lista))
        telaBebida.tableWidget_cadastro_2.setColumnCount(4)
        for i in range(0, len(lista)):
            for j in range(4):
                telaBebida.tableWidget_cadastro_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(lista[i][j])))

        setar_checkBox_false.checkBox_excluir_bebidas(telaExcluirBebidas)
    except:
        telaErro.show()
        telaErro.label.setText(" Codigo invalido, tente novamente")