def devendo(*args):

    telaDevedores2 = args[0]
    cursor = args[1]
    QtWidgets = args[2]

    telaDevedores2.show()

    cursor.execute("select id, dataa, hora, nome, telefone, valor from devedores")
    dados = cursor.fetchall()

    telaDevedores2.tableWidget_2.setRowCount(len(dados))
    telaDevedores2.tableWidget_2.setColumnCount(6)
    for i in range(0, len(dados)):
        for j in range(6):
            telaDevedores2.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))