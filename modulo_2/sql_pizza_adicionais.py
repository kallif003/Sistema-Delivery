def sql_pizzas_esfihas(cursor, tela, QtWidgets):
    telaAtualizarProdutos = tela
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
    sql = "select * from esfihas"
    cursor.execute(sql)
    dados5 = cursor.fetchall()

    for a, b, c, d in zip(dados1, dados2, dados3, dados4):
        lista.append(a)
        lista.append(b)
        lista.append(c)
        lista.append(d)

    for e in dados5:
        lista.append(e)

    telaAtualizarProdutos.tableWidget_cadastro_3.setRowCount(len(lista))
    telaAtualizarProdutos.tableWidget_cadastro_3.setColumnCount(5)
    for i in range(0, len(lista)):
        for j in range(5):
            telaAtualizarProdutos.tableWidget_cadastro_3.setItem(i, j, QtWidgets.QTableWidgetItem(str(lista[i][j])))

def sql_adicionais(cursor, tela, QtWidgets):
    telaAtualizarProdutos = tela

    listaAdc = []
    sql1 = ("select * from adcBroto")
    cursor.execute(sql1)
    dados1 = cursor.fetchall()
    sql2 = ("select * from adcSeis ")
    cursor.execute(sql2)
    dados2 = cursor.fetchall()
    sql3 = ("select * from adcOito")
    cursor.execute(sql3)
    dados3 = cursor.fetchall()
    sql4 = ("select * from adcDez")
    cursor.execute(sql4)
    dados4 = cursor.fetchall()
    slq5 = ("select * from adcSem")
    cursor.execute(slq5)
    dados5 = cursor.fetchall()

    for i, j, k, l in zip(dados1, dados2, dados3, dados4):
        listaAdc.append(i)
        listaAdc.append(j)
        listaAdc.append(k)
        listaAdc.append(l)

    for m in dados5:
        listaAdc.append(m)

    telaAtualizarProdutos.tableWidget_adc_atualizar.setRowCount(len(listaAdc))
    telaAtualizarProdutos.tableWidget_adc_atualizar.setColumnCount(4)
    for i in range(0, len(listaAdc)):
        for j in range(4):
            telaAtualizarProdutos.tableWidget_adc_atualizar.setItem(i, j,
            QtWidgets.QTableWidgetItem(str(listaAdc[i][j])))