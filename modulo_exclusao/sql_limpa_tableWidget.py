def limpar(cursor, banco10):

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
        cursor.execute("delete from temp_inteiro where id_cliente = %s" % id1)
        banco10.commit()
    if len(metade) > 0:
        cursor.execute("delete from temp_metade1 where id_cliente = %s" % id2)
        banco10.commit()
    if len(terco) > 0:
        cursor.execute("delete from temp_terco1 where id_cliente = %s" % id3)
        banco10.commit()
    if len(quarto) > 0:
        cursor.execute("delete from temp_quarto1 where id_cliente = %s" % id4)
        banco10.commit()
    if len(adc) > 0:
        cursor.execute("delete from temp_adc where id_cliente = %s" % id5)
        banco10.commit()
    if len(adc2) > 0:
        cursor.execute("delete from semAdc where id_cliente = %s" % id6)
        banco10.commit()
    if len(esfiha) > 0:
        cursor.execute("delete from temp_esfihas where id_cliente = %s" % id7)
        banco10.commit()
    if len(lata) > 0:
        cursor.execute("delete from temp_lata where id_cliente = %s" % id8)
        banco10.commit()
    if len(s600) > 0:
        cursor.execute("delete from temp_600 where id_cliente = %s" % id9)
        banco10.commit()
    if len(umLitro) > 0:
        cursor.execute("delete from temp_1L where id_cliente = %s" % id10)
        banco10.commit()
    if len(umLmeio) > 0:
        cursor.execute("delete from temp_1Lmeio where id_cliente = %s" % id11)
        banco10.commit()
    if len(doisLitros) > 0:
        cursor.execute("delete from temp_2L where id_cliente = %s" % id12)
        banco10.commit()
    if len(doisLmeio) > 0:
        cursor.execute("delete from temp_2Lmeio where id_cliente = %s" % id13)
        banco10.commit()
    if len(outros) > 0:
        cursor.execute("delete from temp_outros where id_cliente = %s" % id14)
        banco10.commit()