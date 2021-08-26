def cadastrar(tela1, tela2, cursor, banco10, QtWidgets):
    try:
        telaBebida = tela1
        telaErro = tela2

        produto = telaBebida.produto_2.text()
        valor = telaBebida.valor_2.text()
        tipo = telaBebida.tipo.text()
        sql = "insert into outros(produto, tipo, valor) values(%s, %s, %s)"
        dados = (str(produto), str(tipo), valor)
        cursor.execute(sql, dados)
        banco10.commit()

        sql2 = "select * from outros"
        cursor.execute(sql2)
        dados = cursor.fetchall()
        telaBebida.tableWidget_cadastro_4.setRowCount(len(dados))
        telaBebida.tableWidget_cadastro_4.setColumnCount(4)
        for i in range(0, len(dados)):
            for j in range(4):
                telaBebida.tableWidget_cadastro_4.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))
        telaBebida.produto_2.clear()
        telaBebida.valor_2.clear()
        telaBebida.tipo.clear()
    except:
        telaErro.show()
        telaErro.label.setText("  Erro!Campos vazios ou invalidos")