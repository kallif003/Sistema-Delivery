def informar(tela1, tela2, cursor, QtWidgets, modulo):
    telaExibiPrecoAdicionais = tela1
    telaAdicionais = tela2
    setar_checkBox_false = modulo

    telaExibiPrecoAdicionais.show()
    listaAdc = []
    id = 0
    if (telaAdicionais.checkBox1.isChecked()):
        id = str(1)
    if (telaAdicionais.checkBox2.isChecked()):
        id = str(2)
    if (telaAdicionais.checkBox3.isChecked()):
        id = str(3)
    if (telaAdicionais.checkBox4.isChecked()):
        id = str(4)
    if (telaAdicionais.checkBox5.isChecked()):
        id = str(5)
    if (telaAdicionais.checkBox6.isChecked()):
        id = str(6)
    if (telaAdicionais.checkBox7.isChecked()):
        id = str(7)
    if (telaAdicionais.checkBox8.isChecked()):
        id = str(8)
    if (telaAdicionais.checkBox9.isChecked()):
        id = str(9)
    if (telaAdicionais.checkBox10.isChecked()):
        id = str(10)
    if (telaAdicionais.checkBox11.isChecked()):
        id = str(11)
    if (telaAdicionais.checkBox12.isChecked()):
        id = str(12)
    if (telaAdicionais.checkBox13.isChecked()):
        id = str(13)
    if (telaAdicionais.checkBox14.isChecked()):
        id = str(14)
    if (telaAdicionais.checkBox15.isChecked()):
        id = str(15)
    if (telaAdicionais.checkBox16.isChecked()):
        id = str(16)
    if (telaAdicionais.checkBox17.isChecked()):
        id = str(17)
    if (telaAdicionais.checkBox18.isChecked()):
        id = str(18)
    if (telaAdicionais.checkBox19.isChecked()):
        id = str(19)
    if (telaAdicionais.checkBox20.isChecked()):
        id = str(20)
    if (telaAdicionais.checkBox21.isChecked()):
        id = str(21)
    if (telaAdicionais.checkBox22.isChecked()):
        id = str(22)
    if (telaAdicionais.checkBox23.isChecked()):
        id = str(23)
    if (telaAdicionais.checkBox24.isChecked()):
        id = str(24)
    if (telaAdicionais.checkBox25.isChecked()):
        id = str(25)
    if (telaAdicionais.checkBox26.isChecked()):
        id = str(26)
    if (telaAdicionais.checkBox27.isChecked()):
        id = str(27)
    if (telaAdicionais.checkBox28.isChecked()):
        id = str(28)
    if (telaAdicionais.checkBox29.isChecked()):
        id = str(29)
    if (telaAdicionais.checkBox30.isChecked()):
        id = str(30)
    if (telaAdicionais.checkBox31.isChecked()):
        id = str(31)
    if (telaAdicionais.checkBox32.isChecked()):
        id = str(32)
    if (telaAdicionais.checkBox33.isChecked()):
        id = str(33)
    if (telaAdicionais.checkBox34.isChecked()):
        id = str(34)
    if (telaAdicionais.checkBox35.isChecked()):
        id = str(35)
    if (telaAdicionais.checkBox36.isChecked()):
        id = str(36)
    if (telaAdicionais.checkBox37.isChecked()):
        id = str(37)
    if (telaAdicionais.checkBox38.isChecked()):
        id = str(38)
    if (telaAdicionais.checkBox39.isChecked()):
        id = str(39)

    sql1 = ("select * from adcBroto where id = %s" % id)
    cursor.execute(sql1)
    dados1 = cursor.fetchall()
    sql2 = ("select * from adcSeis where id = %s" % id)
    cursor.execute(sql2)
    dados2 = cursor.fetchall()
    sql3 = ("select * from adcOito where id = %s" % id)
    cursor.execute(sql3)
    dados3 = cursor.fetchall()
    sql4 = ("select * from adcDez where id = %s" % id)
    cursor.execute(sql4)
    dados4 = cursor.fetchall()

    for i, j, k, l in zip(dados1, dados2, dados3, dados4):
        listaAdc.append(i)
        listaAdc.append(j)
        listaAdc.append(k)
        listaAdc.append(l)

    telaExibiPrecoAdicionais.tableWidget.setRowCount(len(listaAdc))
    telaExibiPrecoAdicionais.tableWidget.setColumnCount(4)
    for i in range(0, len(listaAdc)):
        for j in range(4):
            telaExibiPrecoAdicionais.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(listaAdc[i][j])))

    setar_checkBox_false.checkBox_tela_adicionais_com(telaAdicionais)
    setar_checkBox_false.checkBox_tela_adicionais_sem(telaAdicionais)