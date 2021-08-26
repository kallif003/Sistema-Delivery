def ultimo_pedido(tela1, tela2, tela3, cursor, pymysql, QtWidgets):
    try:
        telaUltimoPedido = tela1
        telaPrincipal = tela2
        telaErro = tela3

        telaUltimoPedido.show()

        listaPedido = []

        tel = telaPrincipal.telefone.text()
        cursor.execute("select max(id) from gerenciarPedido where telefone = %s" % tel)
        dados = cursor.fetchall()
        id_pedido = dados[0][0]

        cursor.execute("select dataa from gerenciarPedido where id = %s" % id_pedido)
        dados = cursor.fetchall()
        data = dados[0][0]

        cursor.execute("select valorTotal from gerenciarPedido where id = %s" % id_pedido)
        dados = cursor.fetchall()
        valor = float(dados[0][0])

        ano = data[4:8]
        mes = data[2:4]
        dia = data[0:2]
        data2 = str(dia + '/' + mes + '/' + ano)
        telaUltimoPedido.ultimo_pedido_data.setText(str(data2))

        cursor.execute("select max(id) from per_inteiro where id_int = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_inteiro = dados[0][0]
        else:
            id_inteiro = 0

        cursor.execute(
            "select id_int, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_inteiro where id = %s" % id_inteiro)
        inteiro = cursor.fetchall()

        cursor.execute("select max(id) from per_met1 where id_met = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_met1 = dados[0][0]
        else:
            id_met1 = 0

        cursor.execute("select max(id) from per_met2 where id_met2 = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_met2 = dados[0][0]
        else:
            id_met2 = 0

        cursor.execute(
            "select id_met, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_met1 where id = %s" % id_met1)
        metade1 = cursor.fetchall()

        cursor.execute(
            "select id_met2, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_met2 where id = %s" % id_met2)
        metade2 = cursor.fetchall()

        cursor.execute("select max(id) from per_terco1 where id_terco = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_terco1 = dados[0][0]
        else:
            id_terco1 = 0

        cursor.execute("select max(id) from per_terco2 where id_terco2 = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_terco2 = dados[0][0]
        else:
            id_terco2 = 0

        cursor.execute("select max(id) from per_terco3 where id_terco3 = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_terco3 = dados[0][0]
        else:
            id_terco3 = 0

        cursor.execute(
            "select id_terco, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_terco1 where id = %s" % id_terco1)
        terco1 = cursor.fetchall()

        cursor.execute(
            "select id_terco2, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_terco2 where id = %s" % id_terco2)
        terco2 = cursor.fetchall()

        cursor.execute(
            "select id_terco3, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_terco3 where id = %s" % id_terco3)
        terco3 = cursor.fetchall()

        cursor.execute("select max(id) from per_quarto1 where id_Qt = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_quarto1 = dados[0][0]
        else:
            id_quarto1 = 0

        cursor.execute("select max(id) from per_quarto2 where id_Qt2 = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_quarto2 = dados[0][0]
        else:
            id_quarto2 = 0

        cursor.execute("select max(id) from per_quarto3 where id_Qt3 = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_quarto3 = dados[0][0]
        else:
            id_quarto3 = 0

        cursor.execute("select max(id) from per_quarto4 where id_Qt4 = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_quarto4 = dados[0][0]
        else:
            id_quarto4 = 0

        cursor.execute(
            "select id_Qt, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_quarto1 where id = %s" % id_quarto1)
        quarto1 = cursor.fetchall()

        cursor.execute(
            "select id_Qt2, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_quarto2 where id = %s" % id_quarto2)
        quarto2 = cursor.fetchall()

        cursor.execute(
            "select id_Qt3, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_quarto3 where id = %s" % id_quarto3)
        quarto3 = cursor.fetchall()

        cursor.execute(
            "select id_Qt4, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_quarto4 where id = %s" % id_quarto4)
        quarto4 = cursor.fetchall()

        cursor.execute("select max(id) from per_esfihas where id_esfiha = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_esfiha = dados[0][0]
        else:
            id_esfiha = 0

        cursor.execute(
            "select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_esfihas where id = %s" % id_esfiha)
        esfiha = cursor.fetchall()

        cursor.execute("select max(id) from per_lata where id_lata = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_lata = dados[0][0]
        else:
            id_lata = 0

        cursor.execute(
            "select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_lata where id = %s" % id_lata)
        lata = cursor.fetchall()

        cursor.execute("select max(id) from per_s600 where id_600 = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_600 = dados[0][0]
        else:
            id_600 = 0

        cursor.execute(
            "select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_s600 where id = %s" % id_600)
        s600 = cursor.fetchall()

        cursor.execute("select max(id) from per_1L where id_1L = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_1L = dados[0][0]
        else:
            id_1L = 0

        cursor.execute(
            "select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_1L where id = %s" % id_1L)
        umLitro = cursor.fetchall()

        cursor.execute("select max(id) from per_1Lmeio where id_1meio = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_1meio = dados[0][0]
        else:
            id_1meio = 0

        cursor.execute(
            "select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_1Lmeio where id = %s" % id_1meio)
        umLmeio = cursor.fetchall()

        cursor.execute("select max(id) from per_2L where id_2L = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_2L = dados[0][0]
        else:
            id_2L = 0

        cursor.execute(
            "select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_2L where id = %s" % id_2L)
        doisLitros = cursor.fetchall()

        cursor.execute("select max(id) from per_2Lmeio where id_2meio = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_2meio = dados[0][0]
        else:
            id_2meio = 0

        cursor.execute(
            "select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_2Lmeio where id = %s" % id_2meio)
        doisLmeio = cursor.fetchall()

        cursor.execute("select max(id) from per_outros where id_outros = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_outros = dados[0][0]
        else:
            id_outros = 0

        cursor.execute(
            "select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_outros where id = %s" % id_outros)
        outros = cursor.fetchall()

        cursor.execute("select max(id) from per_adc where id_adc = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_adc = dados[0][0]
        else:
            id_adc = 0

        cursor.execute(
            "select id_adc, tamanho, vazio1, adicional, valor, vazio2, vazio3 from per_adc where id = %s" % id_adc)
        adc2 = cursor.fetchall()

        cursor.execute("select max(id) from per_semAdc where id_semAdc = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_semAdc = dados[0][0]
        else:
            id_semAdc = 0

        cursor.execute(
            "select id_semAdc, tamanho, vazio1, adicional, valor, vazio2, vazio3 from per_semAdc where id = %s" % id_semAdc)
        adc = cursor.fetchall()

        if len(inteiro) > 0:
            for i in inteiro:
                listaPedido.append(i)
                for j in adc2:
                    if j[0] == i[0]:
                        listaPedido.append(j)
                for k in adc:
                    if k[0] == i[0]:
                        listaPedido.append(k)

        if len(metade1) and len(metade2) > 0:
            for j, k in zip(metade1, metade2):
                listaPedido.append(j)
                listaPedido.append(k)
                for c in adc2:
                    if c[0] == j[0]:
                        listaPedido.append(c)
                for d in adc:
                    if d[0] == j[0]:
                        listaPedido.append(d)

        if len(terco1) and len(terco2) and len(terco3) > 0:
            for l, m, n in zip(terco1, terco2, terco3):
                listaPedido.append(l)
                listaPedido.append(m)
                listaPedido.append(n)
                for c in adc2:
                    if c[0] == l[0]:
                        listaPedido.append(c)
                for d in adc:
                    if d[0] == l[0]:
                        listaPedido.append(d)

        if len(quarto1) and len(quarto2) and len(quarto3) and len(quarto4) > 0:
            for o, p, q, r in zip(quarto1, quarto2, quarto3, quarto4):
                listaPedido.append(o)
                listaPedido.append(p)
                listaPedido.append(q)
                listaPedido.append(r)
                for c in adc2:
                    if c[0] == o[0]:
                        listaPedido.append(c)
                for d in adc:
                    if d[0] == o[0]:
                        listaPedido.append(d)

        if len(esfiha) > 0:
            for u in esfiha:
                listaPedido.append(u)
        if len(lata) > 0:
            for v in lata:
                listaPedido.append(v)
        if len(s600) > 0:
            for w in s600:
                listaPedido.append(w)
        if len(umLitro) > 0:
            for x in umLitro:
                listaPedido.append(x)
        if len(umLmeio) > 0:
            for y in umLmeio:
                listaPedido.append(y)
        if len(doisLitros) > 0:
            for z in doisLitros:
                listaPedido.append(z)
        if len(doisLmeio) > 0:
            for a in doisLmeio:
                listaPedido.append(a)
        if len(outros) > 0:
            for b in outros:
                listaPedido.append(b)

        telaUltimoPedido.valorTotal.setText(f'Valor Total: {valor:.2f}')
        telaUltimoPedido.tableWidget.setRowCount(len(listaPedido))
        telaUltimoPedido.tableWidget.setColumnCount(7)
        for i in range(0, len(listaPedido)):
            for j in range(0, 7):
                telaUltimoPedido.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(listaPedido[i][j])))

    except pymysql.err.ProgrammingError:
        telaUltimoPedido.hide()
        telaErro.show()
        telaErro.label.setText('        Erro! Informe um telefone')
    except pymysql.err.OperationalError:
        telaUltimoPedido.hide()
        telaErro.show()
        telaErro.label.setText('           Erro! Nao ha registros ')