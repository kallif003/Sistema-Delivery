def finalizar(tela1, tela2, tela3, cursor, banco10, QtWidgets):
    try:
        telaFinalizarDeve = tela1
        telaDevedores2 = tela2
        telaErro = tela3

        id = telaFinalizarDeve.codigo.text()
        sql = ("select id from gerenciarPedido where id = %s" % id)
        cursor.execute(sql)
        dados2 = cursor.fetchall()
        id2 = dados2[0][0]

        cursor.execute("delete from devedores where id = %s" % id2)
        banco10.commit()
        telaDevedores2.show()

        cursor.execute("select id, dataa, hora, nome, telefone, valor from devedores")
        dados = cursor.fetchall()

        telaDevedores2.tableWidget_2.setRowCount(len(dados))
        telaDevedores2.tableWidget_2.setColumnCount(6)
        for i in range(0, len(dados)):
            for j in range(6):
                telaDevedores2.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))
    except:
        telaErro.show()
        telaErro.label.setText('Codigo invalido, tente novamente!')