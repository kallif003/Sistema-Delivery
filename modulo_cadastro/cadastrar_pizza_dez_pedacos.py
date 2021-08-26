def cadastrar(tela1, tela2, cursor, banco10, QtWidgets):
    try:
        telaProduto = tela1
        telaErro = tela2

        sabor = telaProduto.produto_cadastro.text()
        valor = telaProduto.valor_cadastro.text()
        ingredientes = telaProduto.ingredientes.text()
        sabor = sabor.upper()
        ingredientes = ingredientes.upper()
        tamanho = 'Dez'
        sql = "insert into dezPedacos(sabor, tamanho, valorProduto, ingredientes) values(%s, %s, %s, %s)"
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
        sql = "select * from oitoPedacos"
        cursor.execute(sql)
        dados3 = cursor.fetchall()
        sql = "select * from dezPedacos"
        cursor.execute(sql)
        dados4 = cursor.fetchall()

        for j, k, l, m in zip(dados1, dados2, dados3, dados4):
            lista.append(j)
            lista.append(k)
            lista.append(l)
            lista.append(m)

        telaProduto.tableWidget_cadastro.setRowCount(len(lista))
        telaProduto.tableWidget_cadastro.setColumnCount(5)
        for i in range(0, len(lista)):
            for j in range(5):
                telaProduto.tableWidget_cadastro.setItem(i, j, QtWidgets.QTableWidgetItem(str(lista[i][j])))
        telaProduto.valor_cadastro.clear()
        telaProduto.produto_cadastro.clear()
        telaProduto.ingredientes.clear()
    except:
        telaErro.show()
        telaErro.label.setText("  Erro!Campos vazios ou invalidos")