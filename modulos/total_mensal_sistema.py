def venda_mensal(tela1, tela2, cursor, QtWidgets):

    telaCaixa = tela1
    telaMensal = tela2

    data1 = telaMensal.data_mensal.text()
    cursor.execute("select sum(qt_pizzas), sum(qt_esfihas), sum(qt_bebidas), sum(qt_outros), sum(total) from caixa where extract(year_month from data2) = %s " % data1)
    dados = cursor.fetchall()

    if dados == ((None, None, None, None, None),):
        dados = (('', '', '', '', ''),)

    telaCaixa.tableWidget.setRowCount(len(dados))
    telaCaixa.tableWidget.setColumnCount(5)
    for i in range(0, len(dados)):
        for j in range(5):
            telaCaixa.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))
    telaMensal.hide()