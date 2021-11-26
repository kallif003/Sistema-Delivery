def venda_do_dia(*args):

    telaCaixa = args[0]
    cursor = args[1]
    data = args[2]
    QtWidgets = args[3]

    cursor.execute("select sum(qt_pizzas), sum(qt_esfihas), sum(qt_bebidas), sum(qt_outros), sum(total) from caixa where dataa = %s " % data)
    dados = cursor.fetchall()

    if dados == ((None, None, None, None, None),):
        dados = (('', '', '', '', ''),)

    telaCaixa.tableWidget.setRowCount(len(dados))
    telaCaixa.tableWidget.setColumnCount(5)
    for i in range(0, len(dados)):
        for j in range(5):
            telaCaixa.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))