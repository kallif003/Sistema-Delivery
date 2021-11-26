def cadastrar(*args):
    try:
        telaProduto = args[0]
        telaErro = args[1]
        cursor = args[2]
        banco10 = args[3]
        QtWidgets = args[4]

        sabor = telaProduto.produto_cadastro.text()
        valor = telaProduto.valor_cadastro.text()
        ingredientes = telaProduto.ingredientes.text()
        tamanho = 'Padrao'
        sql = "insert into esfihas(sabor, tamanho, valorProduto, ingredientes) values(%s, %s, %s, %s)"
        dados = (str(sabor), str(tamanho), valor, str(ingredientes))
        cursor.execute(sql, dados)
        banco10.commit()

        sql2 = "select * from esfihas"
        cursor.execute(sql2)
        dados = cursor.fetchall()
        telaProduto.tableWidget_cadastro.setRowCount(len(dados))
        telaProduto.tableWidget_cadastro.setColumnCount(5)
        for i in range(0, len(dados)):
            for j in range(5):
                telaProduto.tableWidget_cadastro.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))
    except:
        telaErro.show()
        telaErro.label.setText("  Erro!Campos vazios ou invalidos")