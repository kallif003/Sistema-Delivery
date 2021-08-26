def sql_info_pedido(id2, data, cursor, tela, QtWidgets):
    telaInfoPedido = tela

    listaPedido = []
    sql9 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, "
            "subtotal from per_inteiro where id_int = %s and dataa = %s")
    values = (id2, data)
    cursor.execute(sql9, values)
    inteiro = cursor.fetchall()

    sql6 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, "
            "subtotal from per_met1 where id_met = %s and dataa = %s")
    values = (id2, data)
    cursor.execute(sql6, values)
    metade1 = cursor.fetchall()

    sql7 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, "
            "subtotal from per_met2 where id_met2 = %s and dataa = %s")
    values = (id2, data)
    cursor.execute(sql7, values)
    metade2 = cursor.fetchall()

    sql10 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, "
             "subtotal from per_terco1 where id_terco = %s and dataa = %s")
    values = (id2, data)
    cursor.execute(sql10, values)
    terco1 = cursor.fetchall()

    sql11 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, "
             "subtotal from per_terco2 where id_terco2 = %s and dataa = %s")
    values = (id2, data)
    cursor.execute(sql11, values)
    terco2 = cursor.fetchall()

    sql12 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, "
             "subtotal from per_terco3 where id_terco3 = %s and dataa = %s")
    values = (id2, data)
    cursor.execute(sql12, values)
    terco3 = cursor.fetchall()

    sql13 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, "
             "subtotal from per_quarto1 where id_Qt = %s and dataa = %s")
    values = (id2, data)
    cursor.execute(sql13, values)
    quarto1 = cursor.fetchall()

    sql14 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, "
             "subtotal from per_quarto2 where id_Qt2 = %s and dataa = %s")
    values = (id2, data)
    cursor.execute(sql14, values)
    quarto2 = cursor.fetchall()

    sql15 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, "
             "subtotal from per_quarto3 where id_Qt3 = %s and dataa = %s")
    values = (id2, data)
    cursor.execute(sql15, values)
    quarto3 = cursor.fetchall()

    sql16 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, "
             "subtotal from per_quarto4 where id_Qt4 = %s and dataa = %s")
    values = (id2, data)
    cursor.execute(sql16, values)
    quarto4 = cursor.fetchall()

    sql17 = ("select id_pizza, tamanho, vazio1, adicional, valor, "
             "vazio2, vazio3 from per_semAdc where id_semAdc = %s and dataa = %s")
    values = (id2, data)
    cursor.execute(sql17, values)
    adc = cursor.fetchall()

    sql18 = ("select id_pizza, tamanho, vazio1, adicional, "
             "vazio2, vazio3, valor from per_adc where id_adc = %s and dataa = %s")
    values = (id2, data)
    cursor.execute(sql18, values)
    adc2 = cursor.fetchall()

    sql19 = ("select tamanho, parte, sabor, valorProduto, quantidade, "
             "subtotal from per_esfihas where id_esfiha = %s and dataa = %s")
    values = (id2, data)
    cursor.execute(sql19, values)
    esfiha = cursor.fetchall()

    sql20 = ("select tamanho, parte, sabor, valorProduto, quantidade, "
             "subtotal from per_lata where id_lata = %s and dataa = %s")
    values = (id2, data)
    cursor.execute(sql20, values)
    lata = cursor.fetchall()

    sql21 = ("select tamanho, parte, sabor, valorProduto, quantidade, "
            "subtotal from per_s600 where id_600 = %s and dataa = %s ")
    values = (id2, data)
    cursor.execute(sql21, values)
    s600 = cursor.fetchall()

    sql22 = ("select tamanho, parte, sabor, valorProduto, quantidade,"
             "subtotal from per_1L where id_1L = %s and dataa = %s")
    values = (id2, data)
    cursor.execute(sql22, values)
    umLitro = cursor.fetchall()

    sql23 = ("select tamanho, parte, sabor, valorProduto, quantidade, "
             "subtotal from per_1Lmeio where id_1meio = %s and dataa = %s")
    values = (id2, data)
    cursor.execute(sql23, values)
    umLmeio = cursor.fetchall()

    sql24 = ("select tamanho, parte, sabor, valorProduto, quantidade, "
             "subtotal from per_2l where id_2L = %s and dataa = %s")
    values = (id2, data)
    cursor.execute(sql24, values)
    doisLitros = cursor.fetchall()

    sql25 = ("select tamanho, parte, sabor, valorProduto, quantidade, "
             "subtotal from per_2Lmeio where id_2meio = %s and dataa = %s")
    values = (id2, data)
    cursor.execute(sql25, values)
    doisLmeio = cursor.fetchall()

    sql26 = ("select tamanho, parte, sabor, valorProduto, quantidade, "
             "subtotal from per_outros where id_outros = %s and dataa = %s")
    values = (id2, data)
    cursor.execute(sql26, values)
    outros = cursor.fetchall()

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

    telaInfoPedido.tableWidget_2.setRowCount(len(listaPedido))
    telaInfoPedido.tableWidget_2.setColumnCount(6)
    for i in range(0, len(listaPedido)):
        for j in range(6):
            telaInfoPedido.tableWidget_2.setItem(i, j, QtWidgets.QTableWidgetItem(str(listaPedido[i][j])))
