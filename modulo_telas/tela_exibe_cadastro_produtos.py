def cadastrar_produtos(*args):

    telaProduto = args[0]
    cursor = args[1]
    QtWidgets = args[2]

    telaProduto.show()
    telaProduto.frame_adc.hide()
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

    for j, k, l, m in zip(dados1, dados2, dados3, dados4):
        lista.append(j)
        lista.append(k)
        lista.append(l)
        lista.append(m)

    for i in dados5:
        lista.append(i)

    telaProduto.tableWidget_cadastro.setRowCount(len(lista))
    telaProduto.tableWidget_cadastro.setColumnCount(5)
    for i in range(0, len(lista)):
        for j in range(5):
            telaProduto.tableWidget_cadastro.setItem(i, j, QtWidgets.QTableWidgetItem(str(lista[i][j])))