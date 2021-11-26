def verificar(*args):
    try:
        telaPrincipal = args[0]
        telaConfirmacao = args[1]
        cursor = args[2]
        banco10 = args[3]

        lista2 = []
        lista = []

        global valorTotal
        tel = telaPrincipal.telefone.text() or 1

        sql = ("select id from cadastro_cliente where telefone = %s" % tel)
        cursor.execute(sql)
        dados = cursor.fetchall()
        id = dados[0][0]

        cursor.execute("select id_cliente from temp_inteiro")
        inteiro = cursor.fetchall()
        for a in inteiro:
            id1 = a
        cursor.execute("select id_cliente from temp_metade1")
        metade = cursor.fetchall()
        for b in metade:
            id2 = b
        cursor.execute("select id_cliente from temp_terco1")
        terco = cursor.fetchall()
        for c in terco:
            id3 = c
        cursor.execute("select id_cliente from temp_quarto1")
        quarto = cursor.fetchall()
        for d in quarto:
            id4 = d
        cursor.execute("select id_cliente from temp_adc")
        adc = cursor.fetchall()
        for e in adc:
            id5 = e
        cursor.execute("select id_cliente from semAdc")
        adc2 = cursor.fetchall()
        for f in adc2:
            id6 = f
        cursor.execute("select id_cliente from temp_esfihas")
        esfiha = cursor.fetchall()
        for g in esfiha:
            id7 = g
        cursor.execute("select id_cliente from temp_lata")
        lata = cursor.fetchall()
        for h in lata:
            id8 = h
        cursor.execute("select id_cliente from temp_600")
        s600 = cursor.fetchall()
        for i in s600:
            id9 = i
        cursor.execute("select id_cliente from temp_1L")
        umLitro = cursor.fetchall()
        for j in umLitro:
            id10 = j
        cursor.execute("select id_cliente from temp_1Lmeio")
        umLmeio = cursor.fetchall()
        for k in umLmeio:
            id11 = k
        cursor.execute("select id_cliente from temp_2L")
        doisLitros = cursor.fetchall()
        for l in doisLitros:
            id12 = l
        cursor.execute("select id_cliente from temp_2Lmeio")
        doisLmeio = cursor.fetchall()
        for m in doisLmeio:
            id13 = m
        cursor.execute("select id_cliente from temp_outros")
        outros = cursor.fetchall()
        for n in outros:
            id14 = n

        if len(inteiro) > 0:
            sql = ("update temp_inteiro set id_cliente = %s where id_cliente = %s")
            values = (id, id1)
            cursor.execute(sql, values)
            banco10.commit()

        if len(metade) > 0:
            sql = ("update temp_metade1 set id_cliente = %s where id_cliente = %s" )
            values = (id, id2)
            cursor.execute(sql, values)
            banco10.commit()

        if len(terco) > 0:
            sql = ("update temp_terco1 set id_cliente = %s where id_cliente = %s")
            values = (id, id3)
            cursor.execute(sql, values)
            banco10.commit()

        if len(quarto) > 0:
            sql = ("update temp_quarto1 set id_cliente = %s where id_cliente = %s")
            values = (id, id4)
            cursor.execute(sql, values)
            banco10.commit()

        if len(adc) > 0:
            sql = ("update temp_adc set id_cliente = %s where id_cliente = %s")
            values = (id, id5)
            cursor.execute(sql, values)
            banco10.commit()

        if len(adc2) > 0:
            sql =("update semAdc set id_cliente = %s where id_cliente = %s")
            values = (id, id6)
            cursor.execute(sql, values)
            banco10.commit()

        if len(esfiha) > 0:
            sql = ("update temp_esfihas set id_cliente = %s where id_cliente = %s")
            values = (id, id7)
            cursor.execute(sql, values)
            banco10.commit()

        if len(lata) > 0:
            sql = ("update temp_lata set id_cliente = %s where id_cliente = %s")
            values = (id, id8)
            cursor.execute(sql, values)
            banco10.commit()

        if len(s600) > 0:
            sql = ("update temp_600 set id_cliente = %s where id_cliente = %s")
            values = (id, id9)
            cursor.execute(sql, values)
            banco10.commit()

        if len(umLitro) > 0:
            sql = ("update temp_1L set id_cliente = %s where id_cliente = %s")
            values = (id, id10)
            cursor.execute(sql, values)
            banco10.commit()

        if len(umLmeio) > 0:
            sql = ("update temp_1Lmeio set id_cliente = %s where id_cliente = %s")
            values = (id, id11)
            cursor.execute(sql, values)
            banco10.commit()

        if len(doisLitros) > 0:
            sql = ("update temp_2L set id_cliente = %s where id_cliente = %s")
            values = (id, id12)
            cursor.execute(sql, values)
            banco10.commit()

        if len(doisLmeio) > 0:
            sql = ("update temp_2Lmeio set id_cliente = %s where id_cliente = %s")
            values = (id, id13)
            cursor.execute(sql, values)
            banco10.commit()

        if len(outros) > 0:
            sql = ("update temp_outros set id_cliente = %s where id_cliente = %s")
            values = (id, id14)
            cursor.execute(sql, values)
            banco10.commit()

        sql = ("select telefone from cadastro_cliente")
        cursor.execute(sql)
        dados1 = cursor.fetchall()
        for i in dados1:
            for j in i:
                lista.append(j)

        for i in lista:
            if tel == i:
                sql1 = ("select * from cadastro_cliente where telefone = %s" % tel)
                cursor.execute(sql1)
                dados = cursor.fetchall()
                for l in dados:
                    for j in l:
                        lista2.append(j)
        telaPrincipal.nome.setText(str(lista2[2]))
        telaPrincipal.cep.setText(str(lista2[3]))
        telaPrincipal.end.setText(str(lista2[4]))
        telaPrincipal.numero.setText(str(lista2[5]))
        telaPrincipal.bairro.setText(str(lista2[6]))
        telaPrincipal.ref.setText(str(lista2[7]))
        telaPrincipal.complemento.setText(str(lista2[8]))
        telaPrincipal.taxa_2.setText(str(lista2[9]))

        cursor.execute("select sum(valor) from devedores where telefone = %s" % tel)
        devedor = cursor.fetchall()

        if devedor != ((None,),):
            telaPrincipal.devendo.setText(str(devedor[0][0]))

        telaPrincipal.label_cadastrado.hide()
        telaPrincipal.label_atualizado.hide()
    except:
        telaConfirmacao.show()