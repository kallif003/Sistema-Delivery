def despachar(*args):
    try:
        telaDespachar = args[0]
        telaErro = args[1]
        telaPedido = args[2]
        cursor = args[3]
        banco10 = args[4]
        time = args[5]
        data = args[6]
        date = args[7]
        QtWidgets = args[8]

        id = telaDespachar.codigo.text()
        sql = ("select id from gerenciarPedido where id = %s and dataa = %s")
        values = (id, data)
        cursor.execute(sql, values)
        dados2 = cursor.fetchall()
        id2 = dados2[0][0]

        a = time.ctime()
        a = a.split()
        hora = str(a[3])

        nome_boy = telaDespachar.motoboy.text()
        nome_boy = nome_boy.upper()

        cursor.execute("select st_pedido from status_pedido where id_pedido = %s" % id2)
        status = cursor.fetchall()
        status = status[0][0]

        if status == 'Cancelado':
            telaErro.show()
            telaErro.label.setText(' Erro! Esse pedido esta cancelado')
        elif status == 'Finalizado':
            telaErro.show()
            telaErro.label.setText('Erro! Esse pedido ja foi finalizado')
        elif status == 'A caminho':
            telaErro.show()
            telaErro.label.setText('Erro! Esse pedido ja foi despachado')
        else:
            sql = ("update status_pedido set st_pedido = %s , motoboy = %s, hora_saida = %s where id_pedido = %s ")
            values = (str('A caminho'), str(nome_boy), str(hora), str(id2))
            cursor.execute(sql, values)
            banco10.commit()

        telaPedido.show()
        data = str(date.today().strftime('%d%m%Y'))

        sql = ("select gerenciarPedido.id, gerenciarPedido.hora, nome, telefone, "
               "valorTotal, st_pedido, motoboy, hora_saida, hora_chegada "
               "from gerenciarPedido join status_pedido "
               "on gerenciarPedido.id = status_pedido.id_pedido where dataa = %s" % data)
        cursor.execute(sql)
        dados = cursor.fetchall()

        telaPedido.tableWidget.setRowCount(len(dados))
        telaPedido.tableWidget.setColumnCount(9)
        for i in range(0, len(dados)):
            for j in range(9):
                telaPedido.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))

        telaDespachar.codigo.clear()
        telaDespachar.motoboy.clear()
    except:
        telaErro.show()
        telaErro.label.setText('Codigo invalido, tente novamente!')