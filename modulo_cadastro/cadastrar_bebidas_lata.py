def cadastrar(tela1, tela2, cursor, banco10, QtWidgets):
    try:
        telaBebida = tela1
        telaErro = tela2

        bebida = telaBebida.produto_bebida.text()
        valor = telaBebida.valor_bebida.text()
        bebida = bebida.upper()
        tamanho = 'Lata'
        sql = "insert into lata(bebida, tamanho, valor) values(%s, %s, %s)"
        dados = (str(bebida), str(tamanho), valor)
        cursor.execute(sql, dados)
        banco10.commit()

        sql2 = "select * from lata"
        cursor.execute(sql2)
        dados = cursor.fetchall()
        telaBebida.tableWidget_cadastro_2.setRowCount(len(dados))
        telaBebida.tableWidget_cadastro_2.setColumnCount(4)
        for i in range(0, len(dados)):
            for j in range(4):
                telaBebida.tableWidget_cadastro_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))
    except:
        telaErro.show()
        telaErro.label.setText("  Erro!Campos vazios ou invalidos")