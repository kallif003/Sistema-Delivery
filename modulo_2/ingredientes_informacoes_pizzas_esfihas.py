def mostrar(tela1, tela2, cursor, QtWidgets):
    try:
        listaIngredientes = []
        id = 0
        lista = []
        listaId = []
        telaPrincipal = tela1
        tela_exibi_valores_pizzas = tela2
        listaEsfihas = []
        listaPizza = []

        cursor.execute("select ingredientes from broto")
        dados = cursor.fetchall()
        for i in dados:
            for j in i:
                listaIngredientes.append(j)

        cursor.execute("select id from broto")
        dados2 = cursor.fetchall()
        for i in dados2:
            for j in i:
                listaId.append(j)


        if telaPrincipal.checkBox1.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[0]))
            id = str(listaId[0])
            print(id)
        if telaPrincipal.checkBox2.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[1]))
            id = str(listaId[1])
        if telaPrincipal.checkBox3.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[2]))
            id = str(listaId[2])
        if telaPrincipal.checkBox4.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[3]))
            id = str(listaId[3])
        if telaPrincipal.checkBox5.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[4]))
            id = str(listaId[4])
        if telaPrincipal.checkBox6.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[5]))
            id = str(listaId[5])
        if telaPrincipal.checkBox7.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[6]))
            id = str(listaId[6])
        if telaPrincipal.checkBox8.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[7]))
            id = str(listaId[7])
        if telaPrincipal.checkBox9.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[8]))
            id = str(listaId[8])
        if telaPrincipal.checkBox10.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[9]))
            id = str(listaId[9])
        if telaPrincipal.checkBox11.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[10]))
            id = str(listaId[10])
        if telaPrincipal.checkBox12.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[11]))
            id = str(listaId[11])
        if telaPrincipal.checkBox13.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[12]))
            id = str(listaId[12])
        if telaPrincipal.checkBox14.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[13]))
            id = str(listaId[13])
        if telaPrincipal.checkBox15.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[14]))
            id = str(listaId[14])
        if telaPrincipal.checkBox16.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[15]))
            id = str(listaId[15])
        if telaPrincipal.checkBox17.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[16]))
            id = str(listaId[16])
        if telaPrincipal.checkBox18.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[17]))
            id = str(listaId[17])
        if telaPrincipal.checkBox19.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[18]))
            id = str(listaId[18])
        if telaPrincipal.checkBox20.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[19]))
            id = str(listaId[19])
        if telaPrincipal.checkBox21.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[20]))
            id = str(listaId[20])
        if telaPrincipal.checkBox22.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[21]))
            id = str(listaId[21])
        if telaPrincipal.checkBox23.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[22]))
            id = str(listaId[22])
        if telaPrincipal.checkBox24.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[23]))
            id = str(listaId[23])
        if telaPrincipal.checkBox25.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[24]))
            id = str(listaId[24])
        if telaPrincipal.checkBox26.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[25]))
            id = str(listaId[25])
        if telaPrincipal.checkBox27.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[26]))
            id = str(listaId[26])
        if telaPrincipal.checkBox28.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[27]))
            id = str(listaId[27])
        if telaPrincipal.checkBox29.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[28]))
            id = str(listaId[28])
        if telaPrincipal.checkBox30.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[29]))
            id = str(listaId[29])
        if telaPrincipal.checkBox31.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[30]))
            id = str(listaId[30])
        if telaPrincipal.checkBox32.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[31]))
            id = str(listaId[31])
        if telaPrincipal.checkBox33.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[32]))
            id = str(listaId[32])
        if telaPrincipal.checkBox34.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[33]))
            id = str(listaId[33])
        if telaPrincipal.checkBox35.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[34]))
            id = str(listaId[34])
        if telaPrincipal.checkBox36.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[35]))
            id = str(listaId[35])
        if telaPrincipal.checkBox37.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[36]))
            id = str(listaId[36])
        if telaPrincipal.checkBox38.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[37]))
            id = str(listaId[37])
        if telaPrincipal.checkBox39.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[38]))
            id = str(listaId[38])
        if telaPrincipal.checkBox40.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[39]))
            id = str(listaId[39])
        if telaPrincipal.checkBox41.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[40]))
            id = str(listaId[40])
        if telaPrincipal.checkBox42.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[41]))
            id = str(listaId[41])
        if telaPrincipal.checkBox43.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[42]))
            id = str(listaId[42])
        if telaPrincipal.checkBox44.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[43]))
            id = str(listaId[43])
        if telaPrincipal.checkBox45.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[44]))
            id = str(listaId[44])
        if telaPrincipal.checkBox46.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[45]))
            id = str(listaId[45])
        if telaPrincipal.checkBox47.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[46]))
            id = str(listaId[46])
        if telaPrincipal.checkBox48.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[47]))
            id = str(listaId[47])
        if telaPrincipal.checkBox49.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[48]))
            id = str(listaId[48])
        if telaPrincipal.checkBox50.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[49]))
            id = str(listaId[49])
        if telaPrincipal.checkBox51.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaIngredientes[50]))
            id = str(listaId[50])

        cursor.execute("select ingredientes from esfihas")
        dados2 = cursor.fetchall()
        for i in dados2:
            for j in i:
                listaEsfihas.append(j)

        cursor.execute("select id from esfihas")
        dados2 = cursor.fetchall()
        for i in dados2:
            for j in i:
                listaPizza.append(j)

        if telaPrincipal.esfihas_1.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[0]))
            id = str(listaPizza[0])
        if telaPrincipal.esfihas_2.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[1]))
            id = str(listaPizza[1])
        if telaPrincipal.esfihas_3.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[2]))
            id = str(listaPizza[2])
        if telaPrincipal.esfihas_4.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[3]))
            id = str(listaPizza[3])
        if telaPrincipal.esfihas_5.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[4]))
            id = str(listaPizza[4])
        if telaPrincipal.esfihas_6.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[5]))
            id = str(listaPizza[5])
        if telaPrincipal.esfihas_7.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[6]))
            id = str(listaPizza[6])
        if telaPrincipal.esfihas_8.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[7]))
            id = str(listaPizza[7])
        if telaPrincipal.esfihas_9.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[8]))
            id = str(listaPizza[8])
        if telaPrincipal.esfihas_10.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[9]))
            id = str(listaPizza[9])
        if telaPrincipal.esfihas_11.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[10]))
            id = str(listaPizza[10])
        if telaPrincipal.esfihas_12.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[11]))
            id = str(listaPizza[11])
        if telaPrincipal.esfihas_13.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[12]))
            id = str(listaPizza[12])
        if telaPrincipal.esfihas_14.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[13]))
            id = str(listaPizza[13])
        if telaPrincipal.esfihas_15.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[14]))
            id = str(listaPizza[17])
        if telaPrincipal.esfihas_16.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[15]))
            id = str(listaPizza[15])
        if telaPrincipal.esfihas_17.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[16]))
            id = str(listaPizza[16])
        if telaPrincipal.esfihas_18.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[17]))
            id = str(listaPizza[17])
        if telaPrincipal.esfihas_19.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[18]))
            id = str(listaPizza[18])
        if telaPrincipal.esfihas_20.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[19]))
            id = str(listaPizza[19])
        if telaPrincipal.esfihas_21.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[20]))
            id = str(listaPizza[20])
        if telaPrincipal.esfihas_22.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[21]))
            id = str(listaPizza[21])
        if telaPrincipal.esfihas_23.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[22]))
            id = str(listaPizza[22])
        if telaPrincipal.esfihas_24.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[23]))
            id = str(listaPizza[23])
        if telaPrincipal.esfihas_25.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[24]))
            id = str(listaPizza[24])
        if telaPrincipal.esfihas_26.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[25]))
            id = str(listaPizza[25])
        if telaPrincipal.esfihas_27.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[26]))
            id = str(listaPizza[26])
        if telaPrincipal.esfihas_28.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[27]))
            id = str(listaPizza[27])
        if telaPrincipal.esfihas_29.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[28]))
            id = str(listaPizza[28])
        if telaPrincipal.esfihas_30.isChecked():
            tela_exibi_valores_pizzas.label.setText(str(listaEsfihas[29]))
            id = str(listaPizza[29])

        cursor.execute("select tamanho, sabor, valorProduto from esfihas where id = %s" % id)
        esfihas = cursor.fetchall()

        cursor.execute("select tamanho, sabor, valorProduto from broto where id = %s" % id)
        broto = cursor.fetchall()

        cursor.execute("select tamanho, sabor, valorProduto from seisPedacos where id = %s" % id)
        seis = cursor.fetchall()

        cursor.execute("select tamanho, sabor, valorProduto from oitoPedacos where id = %s" % id)
        oito = cursor.fetchall()

        cursor.execute("select tamanho, sabor, valorProduto from dezPedacos where id = %s" % id)
        dez = cursor.fetchall()

        for a, b, c, d in zip(broto, seis, oito, dez):
            lista.append(a)
            lista.append(b)
            lista.append(c)
            lista.append(d)
        for e in esfihas:
            lista.append(e)
        print(lista)
        tela_exibi_valores_pizzas.tableWidget.setRowCount(len(lista))
        tela_exibi_valores_pizzas.tableWidget.setColumnCount(3)
        for i in range(0, len(lista)):
            for j in range(3):
                tela_exibi_valores_pizzas.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(lista[i][j])))

    except Exception as erro:
        print(erro.__class__)

