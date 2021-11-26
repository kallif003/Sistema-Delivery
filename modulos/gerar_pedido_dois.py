def pedido(*args):

    try:
        cursor = args[0]
        banco10 = args[1]
        id_pedido = args[2]
        data = args[3]
        data2 = args[4]
        desc = args[5]
        din = args[6]
        troco = args[7]
        cartao = args[8]
        voucher = args[9]
        pix = args[10]
        obs = args[11]
        valorTotal = args[12]
        dados = args[13]
        hora = args[14]
        os = args[15]
        telaConfirmarPedido = args[16]
        telaPrincipal = args[17]

        tel = telaPrincipal.telefone.text() or 1

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

        sql17 = ("select id, tamanho, vazio1, adicional, valor, vazio2, vazio3, id_pizza, id_cliente from semAdc")
        cursor.execute(sql17)
        adc = cursor.fetchall()

        sql18 = ("select id, tamanho, vazio1, adicional,valor, vazio2, vazio3, id_pizza, id_cliente  from temp_adc")
        cursor.execute(sql18)
        adc2 = cursor.fetchall()

        sql19 = ("select tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_esfihas ")
        cursor.execute(sql19)
        esfiha = cursor.fetchall()

        sql20 = ("select tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_lata ")
        cursor.execute(sql20)
        lata = cursor.fetchall()

        sql21 = ("select tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_600 ")
        cursor.execute(sql21)
        s600 = cursor.fetchall()

        sql22 = ("select tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_1L ")
        cursor.execute(sql22)
        umLitro = cursor.fetchall()

        sql23 = ("select tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_1Lmeio ")
        cursor.execute(sql23)
        umLmeio = cursor.fetchall()

        sql24 = ("select tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_2l ")
        cursor.execute(sql24)
        doisLitros = cursor.fetchall()

        sql25 = ("select tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_2Lmeio ")
        cursor.execute(sql25)
        doisLmeio = cursor.fetchall()

        sql26 = ("select tamanho, parte, sabor, valorProduto, quantidade, subtotal from temp_outros ")
        cursor.execute(sql26)
        outros = cursor.fetchall()

        if inteiro != ():
            for i in range(len(inteiro)):
                sql = "insert into per_inteiro(id, tamanho, parte, sabor, valorProduto, quantidade, subtotal, id_int, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                insert = (
                    str(inteiro[i][0]), str(inteiro[i][1]), str(inteiro[i][2]), str(inteiro[i][3]), str(inteiro[i][4]),
                    str(inteiro[i][5]),
                    str(inteiro[i][6]), str(id_pedido[0][0]), data)
                cursor.execute(sql, insert)
                banco10.commit()

        if metade1 != ():
            for i in range(len(metade1)):
                sql = "insert into per_met1(id, tamanho, parte, sabor, valorProduto, quantidade, subtotal, id_met, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                insert = (
                    str(metade1[i][0]), str(metade1[i][1]), str(metade1[i][2]), str(metade1[i][3]), str(metade1[i][4]),
                    str(metade1[i][5]), str(metade1[i][6]), str(id_pedido[0][0]), data)
                cursor.execute(sql, insert)
                banco10.commit()

            for j in range(len(metade2)):
                sql2 = "insert into per_met2(id, tamanho, parte, sabor, valorProduto, quantidade, subtotal, id_met2, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                insert = (
                    str(metade2[j][0]), str(metade2[j][1]), str(metade2[j][2]), str(metade2[j][3]), str(metade2[j][4]),
                    str(metade2[j][5]), str(metade2[j][6]), str(id_pedido[0][0]), str(data))
                cursor.execute(sql2, insert)
                banco10.commit()

        if terco1 != ():
            for i in range(len(terco1)):
                sql = "insert into per_terco1(id, tamanho, parte, sabor, valorProduto, quantidade, subtotal, id_terco, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                insert = (str(terco1[i][0]), str(terco1[i][1]), str(terco1[i][2]), str(terco1[i][3]), str(terco1[i][4]),
                          str(terco1[i][5]), str(terco1[i][6]), str(id_pedido[0][0]), data)
                cursor.execute(sql, insert)
                banco10.commit()
            for j in range(len(terco2)):
                sql2 = "insert into per_terco2(id, tamanho, parte, sabor, valorProduto, quantidade, subtotal, id_terco2, dataa) values (%s,%s, %s, %s, %s, %s, %s, %s, %s)"
                insert = (str(terco2[j][0]), str(terco2[j][1]), str(terco3[j][2]), str(terco2[j][3]), str(terco2[j][4]),
                          str(terco2[j][5]), str(terco2[j][6]), str(id_pedido[0][0]), data)
                cursor.execute(sql2, insert)
                banco10.commit()
            for k in range(len(terco3)):
                sql3 = "insert into per_terco3(id, tamanho, parte, sabor, valorProduto, quantidade, subtotal, id_terco3, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                insert = (str(terco3[k][0]), str(terco3[k][1]), str(terco3[k][2]), str(terco3[k][3]), str(terco3[k][4]),
                          str(terco3[k][5]), str(terco3[k][6]), str(id_pedido[0][0]), data)
                cursor.execute(sql3, insert)
                banco10.commit()

        if quarto1 != ():
            for i in range(len(quarto1)):
                sql = "insert into per_quarto1(id, tamanho, parte, sabor, valorProduto, quantidade, subtotal, id_Qt, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                insert = (
                    str(quarto1[i][0]), str(quarto1[i][1]), str(quarto1[i][2]), str(quarto1[i][3]), str(quarto1[i][4]),
                    str(quarto1[i][5]), str(quarto1[i][6]), str(id_pedido[0][0]), data)
                cursor.execute(sql, insert)
                banco10.commit()

            for j in range(len(quarto2)):
                sql2 = "insert into per_quarto2(id, tamanho, parte, sabor, valorProduto, quantidade, subtotal, id_Qt2, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                insert = (
                    str(quarto2[j][0]), str(quarto2[j][1]), str(quarto2[j][2]), str(quarto2[j][3]), str(quarto2[j][4]),
                    str(quarto2[j][5]), str(quarto2[j][6]), str(id_pedido[0][0]), data)
                cursor.execute(sql2, insert)
                banco10.commit()

            for k in range(len(quarto3)):
                sql3 = "insert into per_quarto3(id, tamanho, parte, sabor, valorProduto, quantidade, subtotal, id_Qt3, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                insert = (
                    str(quarto3[k][0]), str(quarto3[k][1]), str(quarto3[k][2]), str(quarto3[k][3]), str(quarto3[k][4]),
                    str(quarto3[k][5]), str(quarto3[k][6]), str(id_pedido[0][0]), data)
                cursor.execute(sql3, insert)
                banco10.commit()

            for l in range(len(quarto4)):
                sql4 = "insert into per_quarto4(id, tamanho, parte, sabor, valorProduto, quantidade, subtotal, id_Qt4, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                insert = (
                    str(quarto4[l][0]), str(quarto4[l][1]), str(quarto4[l][2]), str(quarto4[l][3]), str(quarto4[l][4]),
                    str(quarto4[l][5]), str(quarto4[l][6]), str(id_pedido[0][0]), data)
                cursor.execute(sql4, insert)
                banco10.commit()

        if adc2 != ():
            for i in range(len(adc2)):
                sql = "insert into per_adc(tamanho, vazio1, adicional, valor, vazio2, vazio3, id_pizza, id_adc, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                insert = (
                    str(adc2[i][1]), str(adc2[i][2]), str(adc2[i][3]), str(adc2[i][4]), str(adc2[i][5]),
                    str(adc2[i][6]),
                    str(adc2[i][7]), str(id_pedido[0][0]), data)
                cursor.execute(sql, insert)
                banco10.commit()

        if adc != ():
            for i in range(len(adc)):
                sql = "insert into per_semAdc(tamanho, vazio1, adicional, valor, vazio2, vazio3, id_pizza, id_semAdc, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                insert = (
                str(adc[i][1]), str(adc[i][2]), str(adc[i][3]), str(adc[i][4]), str(adc[i][5]), str(adc[i][6]),
                str(adc[i][7]), str(id_pedido[0][0]), data)
                cursor.execute(sql, insert)
                banco10.commit()

        if esfiha != ():
            for i in range(len(esfiha)):
                sql = "insert into per_esfihas(tamanho, parte, sabor, valorProduto, quantidade, subtotal, id_esfiha, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s) "
                insert = (str(esfiha[i][0]), str(esfiha[i][1]), str(esfiha[i][2]), str(esfiha[i][3]), str(esfiha[i][4]),
                          str(esfiha[i][5]), str(id_pedido[0][0]), data)
                cursor.execute(sql, insert)
                banco10.commit()

        if lata != ():
            for i in range(len(lata)):
                sql = "insert into per_lata(tamanho, parte, sabor, valorProduto, quantidade, subtotal, id_lata, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s)  "
                insert = (
                    str(lata[i][0]), str(lata[i][1]), str(lata[i][2]), str(lata[i][3]), str(lata[i][4]),
                    str(lata[i][5]),
                    str(id_pedido[0][0]), data)
                cursor.execute(sql, insert)
                banco10.commit()

        if s600 != ():
            for i in range(len(s600)):
                sql = "insert into per_s600(tamanho, parte, sabor, valorProduto, quantidade, subtotal, id_600, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s) "
                insert = (
                    str(s600[i][0]), str(s600[i][1]), str(s600[i][2]), str(s600[i][3]), str(s600[i][4]),
                    str(s600[i][5]),
                    str(id_pedido[0][0]), data)
                cursor.execute(sql, insert)
                banco10.commit()

        if umLitro != ():
            for i in range(len(umLitro)):
                sql = "insert into per_1L(tamanho, parte, sabor, valorProduto, quantidade, subtotal, id_1L, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s)"
                insert = (
                    str(umLitro[i][0]), str(umLitro[i][1]), str(umLitro[i][2]), str(umLitro[i][3]), str(umLitro[i][4]),
                    str(umLitro[i][5]), str(id_pedido[0][0]), data)
                cursor.execute(sql, insert)
                banco10.commit()

        if umLmeio != ():
            for i in range(len(umLmeio)):
                sql = "insert into per_1Lmeio(tamanho, parte, sabor, valorProduto, quantidade, subtotal, id_1meio, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s)"
                insert = (
                    str(umLmeio[i][0]), str(umLmeio[i][1]), str(umLmeio[i][2]), str(umLmeio[i][3]), str(umLmeio[i][4]),
                    str(umLmeio[i][5]), str(id_pedido[0][0]), data)
                cursor.execute(sql, insert)
                banco10.commit()

        if doisLitros != ():
            for i in range(len(doisLitros)):
                sql = "insert into per_2L(tamanho, parte, sabor, valorProduto, quantidade, subtotal, id_2L, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s)"
                insert = (str(doisLitros[i][0]), str(doisLitros[i][1]), str(doisLitros[i][2]), str(doisLitros[i][3]),
                          str(doisLitros[i][4]), str(doisLitros[i][5]), str(id_pedido[0][0]), data)
                cursor.execute(sql, insert)
                banco10.commit()

        if doisLmeio != ():
            for i in range(len(doisLmeio)):
                sql = "insert into per_2Lmeio(tamanho, parte, sabor, valorProduto, quantidade, subtotal, id_2meio, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s)"
                insert = (str(doisLmeio[i][0]), str(doisLmeio[i][1]), str(doisLmeio[i][2]), str(doisLmeio[i][3]),
                          str(doisLmeio[i][4]), str(doisLmeio[i][5]), str(id_pedido[0][0]), data)
                cursor.execute(sql, insert)
                banco10.commit()

        if outros != ():
            for i in range(len(outros)):
                sql = "insert into per_outros(tamanho, parte, sabor, valorProduto, quantidade, subtotal, id_outros, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s)"
                insert = (str(outros[i][0]), str(outros[i][1]), str(outros[i][2]), str(outros[i][3]), str(outros[i][4]),
                          str(outros[i][5]), str(id_pedido[0][0]), data)
                cursor.execute(sql, insert)
                banco10.commit()

        sql = "insert into pagamento(cartao, voucher, dinheiro, troco, desconto, pix, observacao, id_pagamento, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        insert = (
            str(cartao), str(voucher), str(din), str(troco), str(desc), str(pix), str(obs), str(id_pedido[0][0]), data)
        cursor.execute(sql, insert)
        banco10.commit()

        arquivo = open('pedido.txt', 'w')
        arquivo.write('COMPUTADOR 1' + '\n')
        arquivo.write('-' * 33 + '\n')
        arquivo.write('PIZZARIA GRATONI' + '\n')
        arquivo.write(str(data2) + ' - ' + str(hora) + '\n')
        arquivo.write('Pedido:' + ' ' + str(id_pedido[0][0]) + '\n')
        arquivo.write('-' * 33 + '\n')
        arquivo.write('Cliente:' + ' ' + str(dados[0][2]) + '\n')
        arquivo.write('Telefone:' + ' ' + str(dados[0][1]) + '\n')
        arquivo.write('Endereco:' + ' ' + str(dados[0][4]) + '\n')
        arquivo.write('Numero:' + ' ' + str(dados[0][5]) + '\n')
        arquivo.write('Bairro:' + ' ' + str(dados[0][6]) + '\n')
        arquivo.write('CEP:' + ' ' + str(dados[0][3]) + '\n')
        arquivo.write('Ref:' + ' ' + str(dados[0][7]) + '\n')
        arquivo.write('Comple:' + ' ' + str(dados[0][8]) + '\n')
        arquivo.write('Taxa de Entrega:' + ' ' + str(dados[0][9]) + '\n')
        arquivo.write('-' * 33 + '\n')
        arquivo.write('       ------Pedido------' + '\n')

        # pizza de um sabor
        if inteiro != ():
            for i in range(len(inteiro)):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(inteiro[i][5]) + 'x' + ' ' + 'Pizza' + ' ' + str(
                    inteiro[i][1]) + ' ' + 'Pedacos' + ' ' + 'R$:' + str(inteiro[i][6]) + '\n\n')
                arquivo.write('Sabor:' + '\n')
                arquivo.write('(1/1)' + str(inteiro[i][3]) + '\n')
                for j in adc2:
                    if j[7] == inteiro[i][0]:
                        arquivo.write(str(j[3]) + ' ' + str(j[4]) + '\n')
                for k in adc:
                    if k[7] == inteiro[i][0]:
                        arquivo.write(str(k[3]) + '\n')

        # pizza meio a meio
        if metade1 != ():
            for i, j in zip(metade1, metade2):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(j[5]) + 'x' + ' ' + 'Pizza' + ' ' + str(i[1])
                              + ' ' + 'Pedacos' + ' ' + 'R$:' + str(j[6]) + '\n\n')
                arquivo.write('Sabor:' + '\n')
                arquivo.write('(1/2)' + str(i[3]) + '\n')
                arquivo.write('(1/2)' + str(j[3]) + '\n')
                for c in adc2:
                    if i[0] == c[7]:
                        arquivo.write(str(c[3]) + ' ' + str(c[4]) + '\n')
                for k in adc:
                    if i[0] == k[7]:
                        arquivo.write(str(k[3]) + '\n')

        # pizza 3 sabores
        if terco1 != ():
            for i, j, k in zip(terco1, terco2, terco3):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(k[5]) + 'x' + ' ' + 'Pizza' + ' ' + str(i[1])
                              + ' ' + 'Pedacos' + ' ' + 'R$:' + str(k[6]) + '\n\n')
                arquivo.write('Sabor:' + '\n')
                arquivo.write('(1/3)' + str(i[3]) + '\n')
                arquivo.write('(1/3)' + str(j[3]) + '\n')
                arquivo.write('(1/3)' + str(k[3]) + '\n')
                for c in adc2:
                    if i[0] == c[7]:
                        arquivo.write(str(c[3]) + ' ' + str(c[4]) + '\n')
                for k in adc:
                    if i[0] == k[7]:
                        arquivo.write(str(k[3]) + '\n')

        # pizza de 4 sabores
        if quarto1 != ():
            for i, j, k, l in zip(quarto1, quarto2, quarto3, quarto4):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(l[5]) + 'x' + ' ' + 'Pizza' + ' ' + str(i[1]) + ' '
                              + 'Pedacos' + ' ' + 'R$:' + str(l[6]) + '\n\n')
                arquivo.write('Sabor:' + '\n')
                arquivo.write('(1/4)' + str(i[3]) + '\n')
                arquivo.write('(1/4)' + str(j[3]) + '\n')
                arquivo.write('(1/4)' + str(k[3]) + '\n')
                arquivo.write('(1/4)' + str(l[3]) + '\n')
                for c in adc2:
                    if i[0] == c[7]:
                        arquivo.write(str(c[3]) + ' ' + str(c[4]) + '\n')
                for k in adc:
                    if i[0] == k[7]:
                        arquivo.write(str(k[3]) + '\n')

        # esfihas
        if esfiha != ():
            for i in range(len(esfiha)):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(esfiha[i][4]) + 'x' + ' ' + 'Esfiha'
                              + ' ' + 'R$:' + str(esfiha[i][5]) + '\n\n')
                arquivo.write('Sabor:' + ' ' + str(esfiha[i][2]) + '\n')

        # refrigerante lata
        if lata != ():
            print(lata)
            for i in range(len(lata)):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(lata[i][4]) + 'x' + ' ' + 'Bebida'
                              + ' ' + 'R$:' + str(lata[i][5]) + '\n\n')
                arquivo.write('Sabor:' + ' ' + str(lata[i][2]) + ' ' + str(lata[i][0]) + '\n')

        # refrigerante 600
        if s600 != ():
            for i in range(len(s600)):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(s600[i][4]) + 'x' + ' ' + 'Bebida'
                              + ' ' + 'R$:' + str(s600[i][5]) + '\n\n')
                arquivo.write('Sabor:' + ' ' + str(s600[i][2]) + ' ' + str(s600[i][0]) + str('ml') + '\n')

        # refrigerante 1 litro
        if umLitro != ():
            for i in range(len(umLitro)):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(umLitro[i][4]) + 'x' + ' ' + 'Bebida'
                              + ' ' + 'R$:' + str(umLitro[i][5]) + '\n\n')
                arquivo.write('Sabor:' + ' ' + str(umLitro[i][2]) + ' ' + str(umLitro[i][0]) + '\n')

        # refrigerante 1,5 litros
        if umLmeio != ():
            for i in range(len(umLmeio)):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(umLmeio[i][4]) + 'x' + ' ' + 'Bebida'
                              + ' ' + 'R$:' + str(umLmeio[i][5]) + '\n\n')
                arquivo.write('Sabor:' + ' ' + str(umLmeio[i][2]) + ' ' + str(umLmeio[i][0]) + '\n')

        # refrigerante 2 litros
        if doisLitros != ():
            for i in range(len(doisLitros)):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(doisLitros[i][4]) + 'x' + ' ' + 'Bebida'
                              + ' ' + 'R$:' + str(doisLitros[i][5]) + '\n\n')
                arquivo.write('Sabor:' + ' ' + str(doisLitros[i][2]) + ' ' + str(doisLitros[i][0]) + '\n')

        # refrigerante 2,5 litros
        if doisLmeio != ():
            for i in range(len(doisLmeio)):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(doisLmeio[i][4]) + 'x' + ' ' + 'Bebida'
                              + ' ' + 'R$:' + str(doisLmeio[i][5]) + '\n\n')
                arquivo.write('Sabor:' + ' ' + str(doisLmeio[i][2]) + ' ' + str(doisLmeio[i][0]) + '\n')

        # outros produtos vendidos
        if outros != ():
            for i in range(len(outros)):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(
                    str(outros[i][4]) + 'x' + ' ' + str(outros[i][0]) + ' '
                    + 'R$:' + str(outros[i][5]) + '\n\n')
                arquivo.write('Item:' + ' ' + str(outros[i][2]) + '\n')

        arquivo.write('-' * 33 + '\n')
        arquivo.write('    ------Valor do Pedido------' + '\n')
        if desc != 0:
            arquivo.write('Desconto:.................:' + ' ' + f'{desc:.2f}' + '\n')
        arquivo.write('Valor total:...........:' + ' ' + f'{valorTotal:.2f}' + '\n')
        arquivo.write('-' * 33 + '\n')
        arquivo.write('    ------Pagamento------' + '\n')
        if din != 0:
            arquivo.write('Dinheiro:..............:' + ' ' + f'{din:.2f}' + '\n')
        if troco != 0:
            arquivo.write('Troco:..............:' + ' ' + f'{troco:.2f}' + '\n')
        if cartao != 0:
            arquivo.write('Cartao:............:' + ' ' + f'{cartao:.2f}' + '\n')
        if voucher != 0:
            arquivo.write('Voucher:..............:' + ' ' + f'{voucher:.2f}' + '\n')
        if pix != 0:
            arquivo.write('Pago via Pix:.........:' + ' ' + f'{pix:.2f}' + '\n')
        if obs != '':
            arquivo.write('    ------Observacoes------' + '\n\n')
            arquivo.write(str(obs) + '\n')
            arquivo.write('-' * 33 + '\n')
        else:
            arquivo.write('-' * 33 + '\n')
        arquivo.close()

        '''if tel != 1 and telaConfirmarPedido.vemBuscar.isChecked():
            os.startfile("C:\\Users\\GRATONI\\Desktop\\dist\\sistemaDelivery\\pedido.txt", "print")
        elif tel != 1:
            for i in range(2):
                os.startfile("C:\\Users\\GRATONI\\Desktop\\dist\\sistemaDelivery\\pedido.txt", "print")
        else:
            os.startfile("C:\\Users\\GRATONI\\Desktop\\dist\\sistemaDelivery\\pedido.txt", "print")

        os.startfile("C:\\Users\\GRATONI\\Desktop\\dist\\sistemaDelivery\\pedido.txt", "print")'''

        os.startfile("C:\\Users\\kalli\\Desktop\\sistemaDelivery\\pedido.txt", "print")

    except Exception as erro:
        print(f'{erro.__class__}')


