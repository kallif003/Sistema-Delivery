def remover(*args):
    try:
        telaPrincipal = args[0]
        telaAdicionais = args[1]
        telaErro = args[2]
        cursor = args[3]
        banco10 = args[4]
        pymysql = args[5]
        setar_checkBox_false = args[6]
        sql_tela_pedido = args[7]
        QtWidgets = args[8]
        data = args[9]

        listaAdc = []
        tel = telaPrincipal.telefone.text() or 1
        sql = ("select id from cadastro_cliente where telefone = %s" % tel)
        cursor.execute(sql)
        dados0 = cursor.fetchall()
        id_cliente = dados0[0][0]

        cursor.execute("select max(id) from temp_inteiro")
        dados1 = cursor.fetchall()
        if dados1 != ((None,),):
            id_inteiro = dados1[0][0]

        cursor.execute("select max(id) from temp_metade1")
        dados3 = cursor.fetchall()
        if dados3 != ((None,),):
            id_metade = dados3[0][0]

        cursor.execute("select max(id) from temp_terco1")
        dados4 = cursor.fetchall()
        if dados4 != ((None,),):
            id_terco = dados4[0][0]

        cursor.execute("select max(id) from temp_quarto1")
        dados5 = cursor.fetchall()
        if dados5 != ((None,),):
            id_quarto = dados5[0][0]

        sql5 = "select * from adcSem"
        cursor.execute(sql5)
        dados5 = cursor.fetchall()

        if telaAdicionais.c1.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[0])
                break
        if telaAdicionais.c2.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[1])
                break
        if telaAdicionais.c3.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[2])
                break
        if telaAdicionais.c4.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[3])
                break
        if telaAdicionais.c5.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[4])
                break
        if telaAdicionais.c6.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[5])
                break
        if telaAdicionais.c7.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[6])
                break
        if telaAdicionais.c8.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[7])
                break
        if telaAdicionais.c9.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[8])
                break
        if telaAdicionais.c10.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[9])
                break
        if telaAdicionais.c11.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[10])
                break
        if telaAdicionais.c12.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[11])
                break
        if telaAdicionais.c13.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[12])
                break
        if telaAdicionais.c14.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[13])
                break
        if telaAdicionais.c15.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[14])
                break
        if telaAdicionais.c16.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[15])
                break
        if telaAdicionais.c17.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[16])
                break
        if telaAdicionais.c18.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[17])
                break
        if telaAdicionais.c19.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[18])
                break
        if telaAdicionais.c20.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[19])
                break
        if telaAdicionais.c21.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[20])
                break
        if telaAdicionais.c22.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[21])
                break
        if telaAdicionais.c23.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[22])
                break
        if telaAdicionais.c24.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[23])
                break
        if telaAdicionais.c25.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[24])
                break
        if telaAdicionais.c26.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[25])
                break
        if telaAdicionais.c27.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[26])
                break
        if telaAdicionais.c28.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[27])
                break
        if telaAdicionais.c29.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[28])
                break
        if telaAdicionais.c30.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[29])
                break
        if telaAdicionais.c31.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[30])
                break
        if telaAdicionais.c32.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[31])
                break
        if telaAdicionais.c33.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[32])
                break
        if telaAdicionais.c34.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[33])
                break
        if telaAdicionais.c35.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[34])
                break
        if telaAdicionais.c36.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[35])
                break
        if telaAdicionais.c37.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[36])
                break
        if telaAdicionais.c38.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[37])
                break
        if telaAdicionais.c39.isChecked():
            for i in range(len(dados5)):
                listaAdc.append(dados5[38])
                break

        if telaAdicionais.umSabor.isChecked():
            sql6 = "insert into semAdc(tamanho, vazio1, adicional, valor, vazio2, vazio3, id_pizza, id_cliente, dataa) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert1 = (
            str(''), str(''), str(listaAdc[0][1]), str(''), str(''), str(''), str(id_inteiro), str(id_cliente), data)
            cursor.execute(sql6, insert1)
            banco10.commit()

        if telaAdicionais.doisSabores.isChecked():
            sql6 = "insert into semAdc(tamanho, vazio1, adicional, valor, vazio2, vazio3, id_pizza, id_cliente, dataa) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert1 = (
            str(''), str(''), str(listaAdc[0][1]), str(''), str(''), str(''), str(id_metade), str(id_cliente), data)
            cursor.execute(sql6, insert1)
            banco10.commit()

        if telaAdicionais.tresSabores.isChecked():
            sql6 = "insert into semAdc(tamanho, vazio1, adicional, valor, vazio2, vazio3, id_pizza, id_cliente, dataa) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert1 = (
            str(''), str(''), str(listaAdc[0][1]), str(''), str(''), str(''), str(id_terco), str(id_cliente), data)
            cursor.execute(sql6, insert1)
            banco10.commit()

        if telaAdicionais.quatroSabores.isChecked():
            sql6 = "insert into semAdc(tamanho, vazio1, adicional, valor, vazio2, vazio3, id_pizza, id_cliente, dataa) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert1 = (
            str(''), str(''), str(listaAdc[0][1]), str(''), str(''), str(''), str(id_quarto), str(id_cliente), data)
            cursor.execute(sql6, insert1)
            banco10.commit()

        telaPrincipal.tableWidget_cadastro.clear()
        sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
        setar_checkBox_false.checkBox_tela_adicionais_sem(telaAdicionais)

    except IndexError:
        telaErro.show()
        telaErro.label.setText(" Erro! Salve o contato do cliente")
    except pymysql.err.DataError:
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione uma pizza")
    except:
        telaErro.show()
        telaErro.label.setText("Erro! Escolha um item para remover")