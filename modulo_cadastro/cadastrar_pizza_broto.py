def cadastrar(tela1, tela2, cursor, banco10, QtWidgets):
    try:
        telaProduto = tela1
        telaErro = tela2

        sabor = telaProduto.produto_cadastro.text()
        valor = telaProduto.valor_cadastro.text()
        ingredientes = telaProduto.ingredientes.text()

        sabor= sabor.upper()
        ingredientes = ingredientes.upper()
        tamanho = 'Broto'
        sql = "insert into broto(sabor, tamanho, valorProduto, ingredientes) values(%s, %s, %s, %s)"
        dados = (str(sabor), str(tamanho), valor, str(ingredientes))
        cursor.execute(sql, dados)
        banco10.commit()

        sql2 = "select * from broto"
        cursor.execute(sql2)
        dados = cursor.fetchall()
        telaProduto.tableWidget_cadastro.setRowCount(len(dados))
        telaProduto.tableWidget_cadastro.setColumnCount(5)
        for i in range(0, len(dados)):
            for j in range(5):
                telaProduto.tableWidget_cadastro.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))
        telaProduto.valor_cadastro.clear()
    except:
        telaErro.show()
        telaErro.label.setText("  Erro!Campos vazios ou invalidos")