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
        sabor = sabor.upper()
        ingredientes = ingredientes.upper()
        tamanho = 'Seis'
        sql = "insert into seisPedacos(sabor, tamanho, valorProduto, ingredientes) values(%s, %s, %s, %s)"
        dados = (str(sabor), str(tamanho), valor, str(ingredientes))
        cursor.execute(sql, dados)
        banco10.commit()

        lista = []
        sql = "select * from broto"
        cursor.execute(sql)
        dados1 = cursor.fetchall()
        sql = "select * from seisPedacos"
        cursor.execute(sql)
        dados2 = cursor.fetchall()

        for j, k in zip(dados1, dados2):
            lista.append(j)
            lista.append(k)

        telaProduto.tableWidget_cadastro.setRowCount(len(lista))
        telaProduto.tableWidget_cadastro.setColumnCount(5)
        for i in range(0, len(lista)):
            for j in range(5):
                telaProduto.tableWidget_cadastro.setItem(i, j, QtWidgets.QTableWidgetItem(str(lista[i][j])))
        telaProduto.valor_cadastro.clear()

    except:
        telaErro.show()
        telaErro.label.setText("  Erro!Campos vazios ou invalidos")


