def exibe_outros(tela, cursor, QtWidgets):

    telaBebida = tela
    telaBebida.frame_outros.show()

    sql2 = "select * from outros"
    cursor.execute(sql2)
    dados = cursor.fetchall()
    telaBebida.tableWidget_cadastro_4.setRowCount(len(dados))
    telaBebida.tableWidget_cadastro_4.setColumnCount(4)
    for i in range(0, len(dados)):
        for j in range(4):
            telaBebida.tableWidget_cadastro_4.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))