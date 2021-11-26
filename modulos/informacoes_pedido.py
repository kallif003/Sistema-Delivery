def inf_pedido(*args):
    try:
        telaInfoPedido = args[0]
        telaErro = args[1]
        cursor = args[2]
        data = args[3]
        sql_informacoes_pedidos = args[4]
        QtWidgets = args[5]

        id = telaInfoPedido.codigo.text()
        sql = ("select id from gerenciarPedido where id = %s and dataa = %s")
        values = (id, data)
        cursor.execute(sql, values)
        dados2 = cursor.fetchall()
        id2 = dados2[0][0]

        cursor.execute(
            "select telefone, nome, cep, endereco, numero, bairro, referencia, complemento, taxaEntrega, valorTotal from gerenciarPedido where id = %s" % id2)
        info_cliente = cursor.fetchall()

        cursor.execute("select motoboy from status_pedido where id_pedido = %s" % id2)
        motoboy = cursor.fetchall()

        telaInfoPedido.telefone.setText('Tel:' + ' ' + str(info_cliente[0][0]))
        telaInfoPedido.nome.setText('Nome:' + ' ' + str(info_cliente[0][1]))
        telaInfoPedido.cep.setText('Cep:' + ' ' + str(info_cliente[0][2]))
        telaInfoPedido.endereco.setText('End:' + ' ' + str(info_cliente[0][3]))
        telaInfoPedido.numero.setText('Numero:' + ' ' + str(info_cliente[0][4]))
        telaInfoPedido.bairro.setText('Bairro:' + ' ' + str(info_cliente[0][5]))
        telaInfoPedido.ref.setText('Ref:' + ' ' + str(info_cliente[0][6]))
        telaInfoPedido.complemento.setText('Compl:' + ' ' + str(info_cliente[0][7]))
        telaInfoPedido.taxa.setText('Taxa:' + ' ' + str(info_cliente[0][8]))
        telaInfoPedido.motoboy.setText('Motoboy:' + ' ' + str(motoboy[0][0]))

        sql = ("select * from pagamento where id_pagamento = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql, values)
        pagamento = cursor.fetchall()

        cursor.execute("select motivo from status_pedido where id_pedido = %s" % id2)
        motivo = cursor.fetchall()

        telaInfoPedido.cartao.setText('Cartao:' + ' ' + str(pagamento[0][1]))
        telaInfoPedido.voucher.setText('Voucher:' + ' ' + str(pagamento[0][2]))
        telaInfoPedido.dinheiro.setText('Dinheiro:' + ' ' + str(pagamento[0][3]))
        telaInfoPedido.troco.setText('Troco:' + ' ' + str(pagamento[0][4]))
        telaInfoPedido.desconto.setText('Desconto:' + ' ' + str(pagamento[0][5]))
        telaInfoPedido.label.setText(str(pagamento[0][6]))
        if motivo[0][0] != None:
            telaInfoPedido.label_2.setText(str(motivo[0][0]))

        sql_informacoes_pedidos.sql_info_pedido(id2, data, cursor, telaInfoPedido, QtWidgets)
        telaInfoPedido.valorTotal.setText(f'Total: {info_cliente[0][9]:.2f}')

    except:
        telaErro.show()
        telaErro.label.setText('Codigo invalido, tente novamente!')