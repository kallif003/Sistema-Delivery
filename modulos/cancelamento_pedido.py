def cancelar(tela1, tela2, tela3, cursor, banco10, data, date,  QtWidgets):
    try:
        telaCancelar = tela1
        telaErro = tela2
        telaPedido = tela3

        id = telaCancelar.codigo.text()
        sql = ("select id from gerenciarPedido where id = %s and dataa = %s")
        values = (id, data)
        cursor.execute(sql, values)
        dados2 = cursor.fetchall()
        id2 = dados2[0][0]

        motivo = telaCancelar.motivo.text()

        cursor.execute("select st_pedido from status_pedido where id_pedido = %s" % id2)
        status = cursor.fetchall()
        status = status[0][0]

        if status == 'Cancelado':
            telaErro.show()
            telaErro.label.setText(' Erro! Esse pedido esta cancelado')
        elif status == 'Finalizado':
            telaErro.show()
            telaErro.label.setText('Erro! Esse pedido ja foi finalizado')
        else:
            sql = ("update status_pedido set st_pedido = %s , motivo = %s  where id_pedido = %s ")
            values = (str('Cancelado'), str(motivo), str(id2))
            cursor.execute(sql, values)
            banco10.commit()

        telaPedido.show()
        data = str(date.today().strftime('%d%m%Y'))

        sql = ("select gerenciarPedido.id,  gerenciarPedido.hora, nome, telefone, "
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

        telaCancelar.codigo.clear()
        telaCancelar.motivo.clear()
        telaCancelar.hide()
    except:
        telaErro.show()
        telaErro.label.setText('Codigo invalido, tente novamente!')