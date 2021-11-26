def reimprimir(*args):
    try:

        telaImprimir = args[0]
        data = args[1]
        cursor = args[2]
        os = args[3]

        telaImprimir.hide()

        ano = data[4:8]
        mes = data[2:4]
        dia = data[0:2]
        data2 = str(dia + '/' + mes + '/' + ano)

        id = telaImprimir.codigo.text()
        sql = ("select id from gerenciarPedido where id = %s and dataa = %s")
        values = (id, data)
        cursor.execute(sql, values)
        dados2 = cursor.fetchall()
        id2 = dados2[0][0]

        cursor.execute("select dataa, hora, id, telefone, nome, cep, endereco, numero, bairro, referencia, complemento, taxaEntrega, valorTotal from gerenciarPedido where id = %s" % id2)
        dados = cursor.fetchall()

        sql9 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_inteiro where id_int = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql9, values)
        inteiro = cursor.fetchall()

        sql6 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_met1 where id_met = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql6, values)
        metade1 = cursor.fetchall()

        sql7 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_met2 where id_met2 = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql7, values)
        metade2 = cursor.fetchall()

        sql10 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_terco1 where id_terco = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql10, values)
        terco1 = cursor.fetchall()

        sql11 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_terco2 where id_terco2 = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql11, values)
        terco2 = cursor.fetchall()

        sql12 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_terco3 where id_terco3 = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql12, values)
        terco3 = cursor.fetchall()

        sql13 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_quarto1 where id_Qt = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql13, values)
        quarto1 = cursor.fetchall()

        sql14 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_quarto2 where id_Qt2 = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql14, values)
        quarto2 = cursor.fetchall()

        sql15 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_quarto3 where id_Qt3 = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql15, values)
        quarto3 = cursor.fetchall()

        sql16 = ("select id, tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_quarto4 where id_Qt4 = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql16, values)
        quarto4 = cursor.fetchall()

        sql18 = ("select tamanho, vazio1, adicional, vazio2, vazio3, id_pizza, valor from per_adc where id_adc = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql18, values)
        adc2 = cursor.fetchall()

        sql18 = ("select tamanho, vazio1, adicional, vazio2, vazio3, id_pizza, valor from per_semAdc where id_semAdc = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql18, values)
        adc = cursor.fetchall()

        sql19 = ("select tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_esfihas where id_esfiha = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql19, values)
        esfiha = cursor.fetchall()

        sql20 = ("select tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_lata where id_lata = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql20, values)
        lata = cursor.fetchall()

        sql21 = ("select tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_s600 where id_600 = %s and dataa = %s ")
        values = (id2, data)
        cursor.execute(sql21, values)
        s600 = cursor.fetchall()

        sql22 = ("select tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_1L where id_1L = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql22, values)
        umLitro = cursor.fetchall()

        sql23 = ("select tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_1Lmeio where id_1meio = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql23, values)
        umLmeio = cursor.fetchall()

        sql24 = ("select tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_2l where id_2L = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql24, values)
        doisLitros = cursor.fetchall()

        sql25 = ("select tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_2Lmeio where id_2meio = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql25, values)
        doisLmeio = cursor.fetchall()

        sql26 = ("select tamanho, parte, sabor, valorProduto, quantidade, subtotal from per_outros where id_outros = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql26, values)
        outros = cursor.fetchall()

        sql27 = ("select * from pagamento where id_pagamento = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql27, values)
        pagamento = cursor.fetchall()

        print(pagamento)
        arquivo = open('pedido.txt', 'w')
        arquivo.write('REIMPRESSAO' + '\n')
        arquivo.write('COMPUTADOR 2' + '\n')
        arquivo.write('-' * 33 + '\n')
        arquivo.write('PIZZARIA GRATONI' + '\n')
        arquivo.write(str(data2) + ' - ' + str(dados[0][1]) + '\n')
        arquivo.write('Pedido:' + ' ' + str(dados[0][2]) + '\n')
        arquivo.write('-' * 33 + '\n')
        arquivo.write('Cliente:' + ' ' + str(dados[0][4]) + '\n')
        arquivo.write('Telefone:' + ' ' + str(dados[0][3]) + '\n')
        arquivo.write('Endereco:' + ' ' + str(dados[0][6]) + '   ' + 'Numero:' + ' ' + str(dados[0][7]) + '\n')
        arquivo.write('Bairro:' + ' ' + str(dados[0][8]) + '\n')
        arquivo.write('CEP:' + ' ' + str(dados[0][5]) + '\n')
        arquivo.write('Ref:' + ' ' + str(dados[0][9]) + '\n')
        arquivo.write('Comple:' + ' ' + str(dados[0][10]) + '\n')
        arquivo.write('Taxa de Entrega:' + ' ' + str(dados[0][11]) + '\n')
        arquivo.write('-' * 33 + '\n')
        arquivo.write('      ------Pedido------' + '\n')

        # pizza de um sabor
        if inteiro != ():
            for i in range(len(inteiro)):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(inteiro[i][5]) + 'x' + ' ' + 'Pizza' + ' ' + str(inteiro[i][1]) + ' ' + 'Pedacos' + ' ' + 'R$:' + str(inteiro[i][6]) + '\n\n\n')
                arquivo.write('Sabor:' + '\n')
                arquivo.write('(1/1)' + str(inteiro[i][3]) + '\n')
                for j in adc2:
                    if j[5] == inteiro[i][0]:
                        arquivo.write(str(j[2]) + ' ' + str(j[6]) + '\n')
                for k in adc:
                    if k[5] == inteiro[i][0]:
                        arquivo.write(str(k[2]) + '\n')

        # pizza meio a meio
        if metade1 != ():
            for i, j in zip(metade1, metade2):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(j[5]) + 'x' + ' ' + 'Pizza' + ' ' + str(i[1]) + ' ' + 'Pedacos' + ' ' + 'R$:' + str(j[6]) + '\n\n\n')
                arquivo.write('Sabor:' + '\n')
                arquivo.write('(1/2)' + str(i[3]) + '\n')
                arquivo.write('(1/2)' + str(j[3]) + '\n')
                for c in adc2:
                    if i[0] == c[5]:
                        arquivo.write(str(c[2]) + ' ' + str(c[6]) + '\n')
                for k in adc:
                    if i[0] == k[5]:
                        arquivo.write(str(k[2]) + '\n')

        # pizza 3 sabores
        if terco1 != ():
            for i, j, k in zip(terco1, terco2, terco3):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(k[5]) + 'x' + ' ' + 'Pizza' + ' ' + str(i[1]) + ' ' + 'Pedacos' + ' ' + 'R$:' + str(k[6]) + '\n\n\n')
                arquivo.write('Sabor:' + '\n')
                arquivo.write('(1/3)' + str(i[3]) + '\n')
                arquivo.write('(1/3)' + str(j[3]) + '\n')
                arquivo.write('(1/3)' + str(k[3]) + '\n')
                for c in adc2:
                    if i[0] == c[5]:
                        arquivo.write(str(c[2]) + ' ' + str(c[6]) + '\n')
                for w in adc:
                    if i[0] == w[5]:
                        arquivo.write(str(w[2]) + '\n')

        # pizza de 4 sabores
        if quarto1 != ():
            for i, j, k, l in zip(quarto1, quarto2, quarto3, quarto4):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(l[5]) + 'x' + ' ' + 'Pizza' + ' ' + str(i[1]) + ' ' + 'Pedacos' + ' ' + 'R$:' + str(l[6]) + '\n\n\n')
                arquivo.write('Sabor:' + '\n')
                arquivo.write('(1/4)' + str(i[3]) + '\n')
                arquivo.write('(1/4)' + str(j[3]) + '\n')
                arquivo.write('(1/4)' + str(k[3]) + '\n')
                arquivo.write('(1/4)' + str(l[3]) + '\n')
                for c in adc2:
                    if i[0] == c[5]:
                        arquivo.write(str(c[2]) + ' ' + str(c[6]) + '\n')
                for w in adc:
                    if i[0] == w[5]:
                        arquivo.write(str(w[2]) + '\n')

        # esfihas
        if esfiha != ():
            for i in range(len(esfiha)):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(esfiha[i][4]) + 'x' + ' ' + 'Esfiha' + ' ' + 'R$:' + str(esfiha[i][5]) + '\n\n\n')
                arquivo.write('Sabor:' + ' ' + str(esfiha[i][2]) + '\n')

        # refrigerante lata
        if lata != ():
            for i in range(len(lata)):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(lata[i][4]) + 'x' + ' ' + 'Bebida' + ' ' + 'R$:' + str(lata[i][5]) + '\n\n\n')
                arquivo.write('Sabor:' + ' ' + str(lata[i][2]) + ' ' + str(lata[i][0]) +'\n')

        # refrigerante 600
        if s600 != ():
            for i in range(len(s600)):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(s600[i][4]) + 'x' + ' ' + 'Bebida' + ' ' + 'R$:' + str(s600[i][5]) + '\n\n\n')
                arquivo.write('Sabor:' + ' ' + str(s600[i][2]) + ' ' + str(s600[i][0]) + str('ml') + '\n')

        # refrigerante 1 litro
        if umLitro != ():
            for i in range(len(umLitro)):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(umLitro[i][4]) + 'x' + ' ' + 'Bebida' + ' ' + 'R$:' + str(umLitro[i][5]) + '\n\n\n')
                arquivo.write('Sabor:' + ' ' + str(umLitro[i][2]) + ' ' + str(umLitro[i][0]) + '\n')

        # refrigerante 1,5 litros
        if umLmeio != ():
            for i in range(len(umLmeio)):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(umLmeio[i][4]) + 'x' + ' ' + 'Bebida' + ' ' + 'R$:' + str(umLmeio[i][5]) + '\n\n\n')
                arquivo.write('Sabor:' + ' ' + str(umLmeio[i][2]) + ' ' + str(umLmeio[i][0]) + '\n')

        # refrigerante 2 litros
        if doisLitros != ():
            for i in range(len(doisLitros)):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(doisLitros[i][4]) + 'x' + ' ' + 'Bebida' + ' ' + 'R$:' + str(doisLitros[i][5]) + '\n\n\n')
                arquivo.write('Sabor:' + ' ' + str(doisLitros[i][2]) + ' ' + str(doisLitros[i][0]) +'\n')

        # refrigerante 2,5 litros
        if doisLmeio != ():
            for i in range(len(doisLmeio)):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(doisLmeio[i][4]) + 'x' + ' ' + 'Bebida' + ' ' + 'R$:' + str(doisLmeio[i][5]) + '\n\n\n')
                arquivo.write('Sabor:' + ' ' + str(doisLmeio[i][2]) + ' ' + str(doisLmeio[i][0]) +'\n')

        # outros produtos vendidos
        if outros != ():
            for i in range(len(outros)):
                arquivo.write('-' * 33 + '\n')
                arquivo.write(str(outros[i][4]) + 'x' + ' ' + str(outros[i][0]) + ' ' + 'R$:' + str(outros[i][5]) + '\n\n\n')
                arquivo.write('Item:' + ' ' + str(outros[i][2]) + '\n')

        arquivo.write('-' * 33 + '\n')
        arquivo.write('    ------Valor do Pedido------' + '\n')
        if pagamento[0][5] != 0:
            arquivo.write('Desconto:............:' + ' ' + f'{pagamento[0][5]:.2f}' + '\n')
        arquivo.write('Valor total:...........:' + ' ' + f'{dados[0][12]:.2f}' + '\n')
        arquivo.write('-' * 33 + '\n')
        arquivo.write('    ------Pagamento------' + '\n')
        if pagamento[0][3] != 0:
            arquivo.write('Dinheiro:...............:' + ' ' + f'{pagamento[0][3]:.2f}' + '\n')
        if pagamento[0][4] != 0:
            arquivo.write('Troco:..................:' + ' ' + f'{pagamento[0][4]:.2f}' + '\n')
        if pagamento[0][1] != 0:
            arquivo.write('Cartao:.................:' + ' ' + f'{pagamento[0][1]:.2f}' + '\n')
        if pagamento[0][2] != 0:
            arquivo.write('Voucher:................:' + ' ' + f'{pagamento[0][2]:.2f}' + '\n')
        if pagamento[0][6] != 0:
            arquivo.write('Pago via Pix:.........:' + ' ' + f'{pagamento[0][6]:.2f}' + '\n')
        if pagamento[0][7] != '':
            arquivo.write('    ------Observacoes------' + '\n\n')
            arquivo.write(str(pagamento[0][7]) + '\n')
            arquivo.write('-' * 33 + '\n')
        else:
            arquivo.write('-' * 33)
        arquivo.close()

        os.startfile("C:\\Users\\GRATONI\\Desktop\\dist\\sistemaDelivery\\pedido.txt", "print")
        telaImprimir.codigo.clear()

    except Exception as erro:
        print(erro.__class__)