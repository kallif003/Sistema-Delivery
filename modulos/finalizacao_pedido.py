def finalizar(*args):
    try:

        telaFinalizar = args[0]
        telaErro = args[1]
        telaPedido = args[2]
        date = args[3]
        time = args[4]
        data = args[5]
        cursor = args[6]
        banco10 = args[7]
        QtWidgets = args[8]

        data2 = date.today()
        a = time.ctime()
        a = a.split()
        hora = str(a[3])

        id = telaFinalizar.codigo.text()
        sql = ("select id from gerenciarPedido where id = %s and dataa = %s")
        values = (id, data)
        cursor.execute(sql, values)
        dados2 = cursor.fetchall()
        id2 = dados2[0][0]

        sql = ("select valorTotal from gerenciarPedido where id = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql, values)
        total = cursor.fetchall()

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
            sql9 = ("select sum(quantidade) from per_inteiro where id_int = %s and dataa = %s")
            values = (id2, data)
            cursor.execute(sql9, values)
            inteiro = cursor.fetchall()

            if inteiro != ((None,),):
                qt_inteiro = inteiro[0][0]
            else:
                qt_inteiro = 0

            sql7 = ("select sum(quantidade) from per_met2 where id_met2 = %s and dataa = %s")
            values = (id2, data)
            cursor.execute(sql7, values)
            metade2 = cursor.fetchall()

            if metade2 != ((None,),):
                qt_met = metade2[0][0]
            else:
                qt_met = 0

            sql12 = ("select sum(quantidade) from per_terco3 where id_terco3 = %s and dataa = %s")
            values = (id2, data)
            cursor.execute(sql12, values)
            terco3 = cursor.fetchall()

            if terco3 != ((None,),):
                qt_terco = terco3[0][0]
            else:
                qt_terco = 0

            sql16 = ("select sum(quantidade) from per_quarto4 where id_Qt4 = %s and dataa = %s")
            values = (id2, data)
            cursor.execute(sql16, values)
            quarto4 = cursor.fetchall()

            if quarto4 != ((None,),):
                qt_quarto = quarto4[0][0]
            else:
                qt_quarto = 0

            sql19 = ("select sum(quantidade) from per_esfihas where id_esfiha = %s and dataa = %s")
            values = (id2, data)
            cursor.execute(sql19, values)
            esfiha = cursor.fetchall()

            if esfiha != ((None,),):
                qt_esfiha = esfiha[0][0]
            else:
                qt_esfiha = 0

            sql20 = ("select sum(quantidade) from per_lata where id_lata = %s and dataa = %s")
            values = (id2, data)
            cursor.execute(sql20, values)
            lata = cursor.fetchall()

            if lata != ((None,),):
                qt_lata = int(lata[0][0])
            else:
                qt_lata = 0

            sql21 = ("select sum(quantidade) from per_s600 where id_600 = %s and dataa = %s ")
            values = (id2, data)
            cursor.execute(sql21, values)
            s600 = cursor.fetchall()

            if s600 != ((None,),):
                qt_600 = int(s600[0][0])
            else:
                qt_600 = 0

            sql22 = ("select sum(quantidade) from per_1L where id_1L = %s and dataa = %s")
            values = (id2, data)
            cursor.execute(sql22, values)
            umLitro = cursor.fetchall()

            if umLitro != ((None,),):
                qt_1L = int(umLitro[0][0])
            else:
                qt_1L = 0

            sql23 = ("select sum(quantidade) from per_1Lmeio where id_1meio = %s and dataa = %s")
            values = (id2, data)
            cursor.execute(sql23, values)
            umLmeio = cursor.fetchall()

            if umLmeio != ((None,),):
                qt_1meio = int(umLmeio[0][0])
            else:
                qt_1meio = 0

            sql24 = ("select sum(quantidade) from per_2l where id_2L = %s and dataa = %s")
            values = (id2, data)
            cursor.execute(sql24, values)
            doisLitros = cursor.fetchall()

            if doisLitros != ((None,),):
                qt_2L = int(doisLitros[0][0])
            else:
                qt_2L = 0

            sql25 = ("select sum(quantidade) from per_2Lmeio where id_2meio = %s and dataa = %s")
            values = (id2, data)
            cursor.execute(sql25, values)
            doisLmeio = cursor.fetchall()

            if doisLmeio != ((None,),):
                qt_2meio = int(doisLmeio[0][0])
            else:
                qt_2meio = 0

            sql26 = ("select sum(quantidade) from per_outros where id_outros = %s and dataa = %s")
            values = (id2, data)
            cursor.execute(sql26, values)
            outros = cursor.fetchall()

            if outros != ((None,),):
                qt_outros = outros[0][0]
            else:
                qt_outros = 0

            sql = ("update status_pedido set st_pedido = %s , hora_chegada = %s where id_pedido = %s ")
            values = (str('Finalizado'), str(hora), str(id2))
            cursor.execute(sql, values)
            banco10.commit()
            qt_pizza = int(qt_inteiro + qt_met + qt_terco + qt_quarto)
            qt_bebidas = int(qt_lata + qt_600 + qt_1L + qt_1meio + qt_2L + qt_2meio)

            sql = "insert into caixa(qt_pizzas, qt_esfihas, qt_outros, qt_bebidas, total, dataa, data2) values (%s, %s, %s, %s, %s, %s, %s)"
            insert = (str(qt_pizza), str(qt_esfiha), str(qt_outros), str(qt_bebidas), str(total[0][0]), data, str(data2))
            cursor.execute(sql, insert)
            banco10.commit()

            telaPedido.show()

            sql = ("select gerenciarPedido.id, gerenciarPedido.hora, nome, telefone, valorTotal, st_pedido, motoboy, hora_saida, hora_chegada from gerenciarPedido join status_pedido on gerenciarPedido.id = status_pedido.id_pedido where dataa = %s" % data)
            cursor.execute(sql)
            dados = cursor.fetchall()

            telaPedido.tableWidget.setRowCount(len(dados))
            telaPedido.tableWidget.setColumnCount(9)
            for i in range(0, len(dados)):
                for j in range(9):
                    telaPedido.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(dados[i][j])))
            telaErro.show()
            telaErro.label.setText('  Pedido finalizado com sucesso!')
            telaFinalizar.codigo.clear()
    except:
        telaErro.show()
        telaErro.label.setText('Codigo invalido, tente novamente!')
