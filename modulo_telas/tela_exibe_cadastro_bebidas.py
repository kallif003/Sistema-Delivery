def exibe_bebeidas(*args):
    try:

        telaBebida = args[0]
        cursor = args[1]
        QtWidgets = args[2]

        telaBebida.show()
        telaBebida.frame_outros.hide()
        lista = []
        sql = "select * from lata"
        cursor.execute(sql)
        dados1 = cursor.fetchall()
        sql = "select * from s600"
        cursor.execute(sql)
        dados2 = cursor.fetchall()
        sql = "select * from umLitro"
        cursor.execute(sql)
        dados3 = cursor.fetchall()
        sql = "select * from umEmeio"
        cursor.execute(sql)
        dados4 = cursor.fetchall()
        sql = "select * from doisLitros"
        cursor.execute(sql)
        dados5 = cursor.fetchall()

        sql = "select * from doisEmeio"
        cursor.execute(sql)
        dados6 = cursor.fetchall()

        for j in dados1:
            lista.append(j)
        for k in dados2:
            lista.append(k)
        for i in dados3:
            lista.append(i)
        for l in dados4:
            lista.append(l)
        for m in dados5:
            lista.append(m)
        for n in dados6:
            lista.append(n)

        telaBebida.tableWidget_cadastro_2.setRowCount(len(lista))
        telaBebida.tableWidget_cadastro_2.setColumnCount(4)
        for i in range(0, len(lista)):
            for j in range(4):
                telaBebida.tableWidget_cadastro_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(lista[i][j])))
    except Exception as erro:
        print(erro.__class__)