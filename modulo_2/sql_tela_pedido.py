def sql(*args):

    telaPrincipal = args[0]
    cursor = args[1]
    QtWidgets = args[2]

    listaPedido = []
    sql9 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_inteiro")
    cursor.execute(sql9)
    inteiro = cursor.fetchall()

    sql6 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_metade1")
    cursor.execute(sql6)
    metade1 = cursor.fetchall()

    sql7 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_metade2")
    cursor.execute(sql7)
    metade2 = cursor.fetchall()

    sql10 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_terco1")
    cursor.execute(sql10)
    terco1 = cursor.fetchall()

    sql11 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_terco2")
    cursor.execute(sql11)
    terco2 = cursor.fetchall()

    sql12 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_terco3")
    cursor.execute(sql12)
    terco3 = cursor.fetchall()

    sql13 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_quarto1")
    cursor.execute(sql13)
    quarto1 = cursor.fetchall()

    sql14 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_quarto2")
    cursor.execute(sql14)
    quarto2 = cursor.fetchall()

    sql15 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_quarto3")
    cursor.execute(sql15)
    quarto3 = cursor.fetchall()

    sql16 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_quarto4")
    cursor.execute(sql16)
    quarto4 = cursor.fetchall()

    sql17 = ("select id_pizza, tamanho, vazio1, adicional, valor, vazio2, vazio3 from semAdc")
    cursor.execute(sql17)
    adc = cursor.fetchall()

    sql18 = ("select id_pizza, tamanho, vazio1, adicional, valor, vazio2, vazio3 from temp_adc")
    cursor.execute(sql18)
    adc2 = cursor.fetchall()

    sql19 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_esfihas ")
    cursor.execute(sql19)
    esfiha = cursor.fetchall()

    sql20 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_lata ")
    cursor.execute(sql20)
    lata = cursor.fetchall()

    sql21 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_600 ")
    cursor.execute(sql21)
    s600 = cursor.fetchall()

    sql22 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_1L ")
    cursor.execute(sql22)
    umLitro = cursor.fetchall()

    sql23 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_1Lmeio ")
    cursor.execute(sql23)
    umLmeio = cursor.fetchall()

    sql24 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_2l ")
    cursor.execute(sql24)
    doisLitros = cursor.fetchall()

    sql25 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_2Lmeio ")
    cursor.execute(sql25)
    doisLmeio = cursor.fetchall()

    sql26 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_outros ")
    cursor.execute(sql26)
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

    telaPrincipal.tableWidget_cadastro.setRowCount(len(listaPedido))
    telaPrincipal.tableWidget_cadastro.setColumnCount(7)
    for i in range(0, len(listaPedido)):
        for j in range(7):
            telaPrincipal.tableWidget_cadastro.setItem(i, j, QtWidgets.QTableWidgetItem(str(listaPedido[i][j])))

def preenche_checkBox_tela_pedido(tela, cursor):
    lista = []
    telaPrincipal = tela
    sql = ("select sabor from broto")
    cursor.execute(sql)
    dados = cursor.fetchall()
    for i in dados:
        for j in i:
            lista.append(j)

    if len(lista) > 0:
        telaPrincipal.checkBox1.show()
        telaPrincipal.checkBox1.setText(str(lista[0]))
    if len(lista) > 1:
        telaPrincipal.checkBox2.show()
        telaPrincipal.checkBox2.setText(str(lista[1]))
    if len(lista) > 2:
        telaPrincipal.checkBox3.show()
        telaPrincipal.checkBox3.setText(str(lista[2]))
    if len(lista) > 3:
        telaPrincipal.checkBox4.show()
        telaPrincipal.checkBox4.setText(str(lista[3]))
    if len(lista) > 4:
        telaPrincipal.checkBox5.show()
        telaPrincipal.checkBox5.setText(str(lista[4]))
    if len(lista) > 5:
        telaPrincipal.checkBox6.show()
        telaPrincipal.checkBox6.setText(str(lista[5]))
    if len(lista) > 6:
        telaPrincipal.checkBox7.show()
        telaPrincipal.checkBox7.setText(str(lista[6]))
    if len(lista) > 7:
        telaPrincipal.checkBox8.show()
        telaPrincipal.checkBox8.setText(str(lista[7]))
    if len(lista) > 8:
        telaPrincipal.checkBox9.show()
        telaPrincipal.checkBox9.setText(str(lista[8]))
    if len(lista) > 9:
        telaPrincipal.checkBox10.show()
        telaPrincipal.checkBox10.setText(str(lista[9]))
    if len(lista) > 10:
        telaPrincipal.checkBox11.show()
        telaPrincipal.checkBox11.setText(str(lista[10]))
    if len(lista) > 11:
        telaPrincipal.checkBox12.show()
        telaPrincipal.checkBox12.setText(str(lista[11]))
    if len(lista) > 12:
        telaPrincipal.checkBox13.show()
        telaPrincipal.checkBox13.setText(str(lista[12]))
    if len(lista) > 13:
        telaPrincipal.checkBox14.show()
        telaPrincipal.checkBox14.setText(str(lista[13]))
    if len(lista) > 14:
        telaPrincipal.checkBox15.show()
        telaPrincipal.checkBox15.setText(str(lista[14]))
    if len(lista) > 15:
        telaPrincipal.checkBox16.show()
        telaPrincipal.checkBox16.setText(str(lista[15]))
    if len(lista) > 16:
        telaPrincipal.checkBox17.show()
        telaPrincipal.checkBox17.setText(str(lista[16]))
    if len(lista) > 17:
        telaPrincipal.checkBox18.show()
        telaPrincipal.checkBox18.setText(str(lista[17]))
    if len(lista) > 18:
        telaPrincipal.checkBox19.show()
        telaPrincipal.checkBox19.setText(str(lista[18]))
    if len(lista) > 19:
        telaPrincipal.checkBox20.show()
        telaPrincipal.checkBox20.setText(str(lista[19]))
    if len(lista) > 20:
        telaPrincipal.checkBox21.show()
        telaPrincipal.checkBox21.setText(str(lista[20]))
    if len(lista) > 21:
        telaPrincipal.checkBox22.show()
        telaPrincipal.checkBox22.setText(str(lista[21]))
    if len(lista) > 22:
        telaPrincipal.checkBox23.show()
        telaPrincipal.checkBox23.setText(str(lista[22]))
    if len(lista) > 23:
        telaPrincipal.checkBox24.show()
        telaPrincipal.checkBox24.setText(str(lista[23]))
    if len(lista) > 24:
        telaPrincipal.checkBox25.show()
        telaPrincipal.checkBox25.setText(str(lista[24]))
    if len(lista) > 25:
        telaPrincipal.checkBox26.show()
        telaPrincipal.checkBox26.setText(str(lista[25]))
    if len(lista) > 26:
        telaPrincipal.checkBox27.show()
        telaPrincipal.checkBox27.setText(str(lista[26]))
    if len(lista) > 27:
        telaPrincipal.checkBox28.show()
        telaPrincipal.checkBox28.setText(str(lista[27]))
    if len(lista) > 28:
        telaPrincipal.checkBox29.show()
        telaPrincipal.checkBox29.setText(str(lista[28]))
    if len(lista) > 29:
        telaPrincipal.checkBox30.show()
        telaPrincipal.checkBox30.setText(str(lista[29]))
    if len(lista) > 30:
        telaPrincipal.checkBox31.show()
        telaPrincipal.checkBox31.setText(str(lista[30]))
    if len(lista) > 31:
        telaPrincipal.checkBox32.show()
        telaPrincipal.checkBox32.setText(str(lista[31]))
    if len(lista) > 32:
        telaPrincipal.checkBox33.show()
        telaPrincipal.checkBox33.setText(str(lista[32]))
    if len(lista) > 33:
        telaPrincipal.checkBox34.show()
        telaPrincipal.checkBox34.setText(str(lista[33]))
    if len(lista) > 34:
        telaPrincipal.checkBox35.show()
        telaPrincipal.checkBox35.setText(str(lista[34]))
    if len(lista) > 35:
        telaPrincipal.checkBox36.show()
        telaPrincipal.checkBox36.setText(str(lista[35]))
    if len(lista) > 36:
        telaPrincipal.checkBox37.show()
        telaPrincipal.checkBox37.setText(str(lista[36]))
    if len(lista) > 37:
        telaPrincipal.checkBox38.show()
        telaPrincipal.checkBox38.setText(str(lista[37]))
    if len(lista) > 38:
        telaPrincipal.checkBox39.show()
        telaPrincipal.checkBox39.setText(str(lista[38]))
    if len(lista) > 39:
        telaPrincipal.checkBox40.show()
        telaPrincipal.checkBox40.setText(str(lista[39]))
    if len(lista) > 40:
        telaPrincipal.checkBox41.show()
        telaPrincipal.checkBox41.setText(str(lista[40]))
    if len(lista) > 41:
        telaPrincipal.checkBox42.show()
        telaPrincipal.checkBox42.setText(str(lista[41]))
    if len(lista) > 42:
        telaPrincipal.checkBox43.show()
        telaPrincipal.checkBox43.setText(str(lista[42]))
    if len(lista) > 43:
        telaPrincipal.checkBox44.show()
        telaPrincipal.checkBox44.setText(str(lista[43]))
    if len(lista) > 44:
        telaPrincipal.checkBox45.show()
        telaPrincipal.checkBox45.setText(str(lista[44]))
    if len(lista) > 45:
        telaPrincipal.checkBox46.show()
        telaPrincipal.checkBox46.setText(str(lista[45]))
    if len(lista) > 46:
        telaPrincipal.checkBox47.show()
        telaPrincipal.checkBox47.setText(str(lista[46]))
    if len(lista) > 47:
        telaPrincipal.checkBox48.show()
        telaPrincipal.checkBox48.setText(str(lista[47]))
    if len(lista) > 48:
        telaPrincipal.checkBox49.show()
        telaPrincipal.checkBox49.setText(str(lista[48]))
    if len(lista) > 49:
        telaPrincipal.checkBox50.show()
        telaPrincipal.checkBox50.setText(str(lista[49]))
    if len(lista) > 50:
        telaPrincipal.checkBox51.show()
        telaPrincipal.checkBox51.setText(str(lista[50]))