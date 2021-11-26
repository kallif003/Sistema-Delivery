def gerando_pedido(*args):
    try:
        gerar_pedido = args[0]
        cursor = args[1]
        banco10 = args[2]
        data = args[3]
        time = args[4]
        valorTotal = args[5]
        telaConfirmarPedido = args[6]
        telaPrincipal = args[7]
        telaErro = args[8]
        os = args[9]

        obs = telaConfirmarPedido.lineEdit.text() or ''
        obs = obs.upper()
        cartao = float(telaConfirmarPedido.cartao.text() or 0)
        voucher = float(telaConfirmarPedido.voucher.text() or 0)
        desc = float(telaPrincipal.desconto.text() or 0)
        din = float(telaConfirmarPedido.dinheiro.text() or 0)
        troco = float(telaConfirmarPedido.troco.text() or 0)
        pix = float(telaConfirmarPedido.pix.text() or 0)

        telaConfirmarPedido.hide()
        telaPrincipal.hide()

        ano = data[4:8]
        mes = data[2:4]
        dia = data[0:2]
        data2 = str(dia + '/' + mes + '/' + ano)

        a = time.ctime()
        a = a.split()
        hora = str(a[3])

        tel = telaPrincipal.telefone.text() or 1
        sql = ("select * from cadastro_cliente where telefone = %s" % tel)
        cursor.execute(sql)
        dados = cursor.fetchall()

        sql = "insert into gerenciarPedido(telefone, nome, cep, " \
              "endereco, numero, bairro, referencia, complemento, " \
              "taxaEntrega, dataa, hora, valorTotal) " \
              "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        insert = (str(dados[0][1]), str(dados[0][2]),
                  str(dados[0][3]), str(dados[0][4]),
                  str(dados[0][5]), str(dados[0][6]),
                  str(dados[0][7]), str(dados[0][8]),
                  str(dados[0][9]), data, str(hora),
                  valorTotal)
        cursor.execute(sql, insert)
        banco10.commit()

        cursor.execute("select max(id) from gerenciarPedido where telefone = %s" % tel)
        id_pedido = cursor.fetchall()

        sql2 = "insert into status_pedido(st_pedido, hora, motoboy, " \
               "hora_saida, hora_chegada, id_pedido) " \
               "values (%s, %s, %s, %s, %s, %s)"
        insert2 = (str('Em preparo'), str(hora), str(''), str(''), str(''), str(id_pedido[0][0]))
        cursor.execute(sql2, insert2)
        banco10.commit()

        gerar_pedido.pedido(cursor, banco10, id_pedido, data, data2, desc,
                            din, troco, cartao, voucher, pix, obs, valorTotal, dados, hora, os, telaConfirmarPedido, telaPrincipal)

    except(ValueError):
        telaErro.show()
        telaErro.label.setText('   Nao use virgula, utilize ponto!')
