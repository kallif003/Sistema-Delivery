def venda_mensal(*args):

    telaCaixa = args[0]
    telaMensal = args[1]
    cursor = args[2]
    QtWidgets = args[3]

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