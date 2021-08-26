def consultar(tela, cursor, QtWidgets):
    telaSecundaria = tela

    telaSecundaria.show()
    sql = "select fechamento.*, fechamento2.* from fechamento join fechamento2 on fechamento.id = fechamento2.id"
    cursor.execute(sql)
    dados = cursor.fetchall()

    telaSecundaria.tableWidget.setRowCount(len(dados))
    telaSecundaria.tableWidget.setColumnCount(35)
    for i in range(0, len(dados)):
        for j in range(0, 35):
            telaSecundaria.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))