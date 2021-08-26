def mostra_adicionais(tela, cursor, QtWidgets):

    telaProduto = tela

    telaProduto.frame_adc.show()
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

    telaProduto.tableWidget_cadastro_2.setRowCount(len(listaAdc))
    telaProduto.tableWidget_cadastro_2.setColumnCount(4)
    for i in range(0, len(listaAdc)):
        for j in range(4):
            telaProduto.tableWidget_cadastro_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(listaAdc[i][j])))