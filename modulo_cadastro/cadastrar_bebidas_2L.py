def cadastrar(tela1, tela2, cursor, banco10, QtWidgets):
    try:
        telaBebida = tela1
        telaErro = tela2

        bebida = telaBebida.produto_bebida.text()
        valor = telaBebida.valor_bebida.text()
        bebida = bebida.upper()
        tamanho = '2L'
        sql = "insert into doisLitros(bebida, tamanho, valor) values(%s, %s, %s)"
        dados = (str(bebida), str(tamanho), valor)
        cursor.execute(sql, dados)
        banco10.commit()

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

        telaBebida.tableWidget_cadastro_2.setRowCount(len(lista))
        telaBebida.tableWidget_cadastro_2.setColumnCount(4)
        for i in range(0, len(lista)):
            for j in range(4):
                telaBebida.tableWidget_cadastro_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(lista[i][j])))
    except:
        telaErro.show()
        telaErro.label.setText("  Erro!Campos vazios ou invalidos")