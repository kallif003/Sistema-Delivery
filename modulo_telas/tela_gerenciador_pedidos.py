def gerenciador_pedidos(*args):

    telaPedido = args[0]
    cursor = args[1]
    data  = args[2]
    QtWidgets = args[3]

    telaPedido.show()
    ano = data[4:8]
    mes = data[2:4]
    dia = data[0:2]
    data1 = str(dia + '/' + mes + '/' + ano)

    telaPedido.label_data.setText('Data:' + ' ' + str(data1))
    sql = ("select gerenciarPedido.id, gerenciarPedido.hora, nome, telefone, "
           "valorTotal, st_pedido, motoboy, hora_saida, hora_chegada "
           "from gerenciarPedido join status_pedido on "
           "gerenciarPedido.id = status_pedido.id_pedido "
           "where dataa = %s" % data)
    cursor.execute(sql)
    dados = cursor.fetchall()

    telaPedido.tableWidget.setRowCount(len(dados))
    telaPedido.tableWidget.setColumnCount(9)
    for i in range(0, len(dados)):
        for j in range(9):
            telaPedido.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))