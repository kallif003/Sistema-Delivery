def cadastrar(tela1, tela2, cursor, banco10, QtWidgets):
    try:
        telaProduto = tela1
        telaErro = tela2

        sabor = telaProduto.produto_adc.text()
        valor = telaProduto.valor_adc.text()
        sabor = sabor.upper()
        tamanho = 'Seis'
        sql = "insert into adcSeis(tamanho,adicional, valor) values(%s, %s, %s)"
        dados = (str(tamanho), str(sabor), valor)
        cursor.execute(sql, dados)
        banco10.commit()

        listaAdc = []
        sql1 = ("select * from adcBroto")
        cursor.execute(sql1)
        dados1 = cursor.fetchall()
        sql2 = ("select * from adcSeis ")
        cursor.execute(sql2)
        dados2 = cursor.fetchall()

        for i, j in zip(dados1, dados2):
            listaAdc.append(i)
            listaAdc.append(j)

        telaProduto.tableWidget_cadastro_2.setRowCount(len(listaAdc))
        telaProduto.tableWidget_cadastro_2.setColumnCount(4)
        for i in range(0, len(listaAdc)):
            for j in range(4):
                telaProduto.tableWidget_cadastro_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(listaAdc[i][j])))
    except:
        telaErro.show()
        telaErro.label.setText("  Erro!Campos vazios ou invalidos")