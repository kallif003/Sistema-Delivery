def cadastrar(tela1, tela2, cursor, banco10, QtWidgets):
    try:
        telaProduto = tela1
        telaErro = tela2

        sabor = telaProduto.produto_adc.text()
        valor = telaProduto.valor_adc.text()
        sabor = sabor.upper()
        tamanho = 'Broto'
        sql = "insert into adcBroto(tamanho,adicional, valor) values(%s, %s, %s)"
        dados = (str(tamanho), str(sabor), valor)
        cursor.execute(sql, dados)
        banco10.commit()

        sql2 = "select * from adcBroto"
        cursor.execute(sql2)
        dados = cursor.fetchall()
        telaProduto.tableWidget_cadastro_2.setRowCount(len(dados))
        telaProduto.tableWidget_cadastro_2.setColumnCount(4)
        for i in range(0, len(dados)):
            for j in range(4):
                telaProduto.tableWidget_cadastro_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))
    except:
        telaErro.show()
        telaErro.label.setText("  Erro!Campos vazios ou invalidos")