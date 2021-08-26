def excluir(tela1, tela2, cursor, banco10, QtWidgets):
    try:
        telaBebida = tela1
        telaErro = tela2

        id = telaBebida.produto_2.text()
        cursor.execute("delete from outros where id = %s" % id)
        banco10.commit()
        telaErro.show()
        telaErro.label.setText('  Produto excluido com sucesso!')

        sql2 = "select * from outros"
        cursor.execute(sql2)
        dados = cursor.fetchall()
        telaBebida.tableWidget_cadastro_4.setRowCount(len(dados))
        telaBebida.tableWidget_cadastro_4.setColumnCount(4)
        for i in range(0, len(dados)):
            for j in range(4):
                telaBebida.tableWidget_cadastro_4.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))
        telaBebida.produto_2.clear()
    except:
        telaErro.show()
        telaErro.label.setText(" Codigo invalido, tente novamente")