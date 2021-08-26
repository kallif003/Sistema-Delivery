def carregar(tela, cursor, modulo):

    telaAdicionais = tela
    setar_checkBox_false = modulo

    telaAdicionais.show()
    lista = []
    listaSem = []
    sql = ("select adicional from adcBroto")
    cursor.execute(sql)
    dados = cursor.fetchall()
    for i in dados:
        for j in i:
            lista.append(j)

    if len(lista) > 0:
        telaAdicionais.checkBox1.setText(str(lista[0]))
    if len(lista) > 1:
        telaAdicionais.checkBox2.setText(str(lista[1]))
    if len(lista) > 2:
        telaAdicionais.checkBox3.setText(str(lista[2]))
    if len(lista) > 3:
        telaAdicionais.checkBox4.setText(str(lista[3]))
    if len(lista) > 4:
        telaAdicionais.checkBox5.setText(str(lista[4]))
    if len(lista) > 5:
        telaAdicionais.checkBox6.setText(str(lista[5]))
    if len(lista) > 6:
        telaAdicionais.checkBox7.setText(str(lista[6]))
    if len(lista) > 7:
        telaAdicionais.checkBox8.setText(str(lista[7]))
    if len(lista) > 8:
        telaAdicionais.checkBox9.setText(str(lista[8]))
    if len(lista) > 9:
        telaAdicionais.checkBox10.setText(str(lista[9]))
    if len(lista) > 10:
        telaAdicionais.checkBox11.setText(str(lista[10]))
    if len(lista) > 11:
        telaAdicionais.checkBox12.setText(str(lista[11]))
    if len(lista) > 12:
        telaAdicionais.checkBox13.setText(str(lista[12]))
    if len(lista) > 13:
        telaAdicionais.checkBox14.setText(str(lista[13]))
    if len(lista) > 14:
        telaAdicionais.checkBox15.setText(str(lista[14]))
    if len(lista) > 15:
        telaAdicionais.checkBox16.setText(str(lista[15]))
    if len(lista) > 16:
        telaAdicionais.checkBox17.setText(str(lista[16]))
    if len(lista) > 17:
        telaAdicionais.checkBox18.setText(str(lista[17]))
    if len(lista) > 18:
        telaAdicionais.checkBox19.setText(str(lista[18]))
    if len(lista) > 19:
        telaAdicionais.checkBox20.setText(str(lista[19]))
    if len(lista) > 20:
        telaAdicionais.checkBox21.setText(str(lista[20]))
    if len(lista) > 21:
        telaAdicionais.checkBox22.setText(str(lista[21]))
    if len(lista) > 22:
        telaAdicionais.checkBox23.setText(str(lista[22]))
    if len(lista) > 23:
        telaAdicionais.checkBox24.setText(str(lista[23]))
    if len(lista) > 24:
        telaAdicionais.checkBox25.setText(str(lista[24]))
    if len(lista) > 25:
        telaAdicionais.checkBox26.setText(str(lista[25]))
    if len(lista) > 26:
        telaAdicionais.checkBox27.setText(str(lista[26]))
    if len(lista) > 27:
        telaAdicionais.checkBox28.setText(str(lista[27]))
    if len(lista) > 28:
        telaAdicionais.checkBox29.setText(str(lista[28]))
    if len(lista) > 29:
        telaAdicionais.checkBox30.setText(str(lista[29]))
    if len(lista) > 30:
        telaAdicionais.checkBox31.setText(str(lista[30]))
    if len(lista) > 31:
        telaAdicionais.checkBox32.setText(str(lista[31]))
    if len(lista) > 32:
        telaAdicionais.checkBox33.setText(str(lista[32]))
    if len(lista) > 33:
        telaAdicionais.checkBox34.setText(str(lista[33]))
    if len(lista) > 34:
        telaAdicionais.checkBox35.setText(str(lista[34]))
    if len(lista) > 35:
        telaAdicionais.checkBox36.setText(str(lista[35]))
    if len(lista) > 36:
        telaAdicionais.checkBox37.setText(str(lista[36]))
    if len(lista) > 37:
        telaAdicionais.checkBox38.setText(str(lista[37]))
    if len(lista) > 38:
        telaAdicionais.checkBox39.setText(str(lista[38]))

    sql = ("select adicional from adcSem")
    cursor.execute(sql)
    dados1 = cursor.fetchall()
    for i in dados1:
        for j in i:
            listaSem.append(j)

    if len(listaSem) > 0:
        telaAdicionais.c1.setText(str(listaSem[0]))
    if len(listaSem) > 1:
        telaAdicionais.c2.setText(str(listaSem[1]))
    if len(listaSem) > 2:
        telaAdicionais.c3.setText(str(listaSem[2]))
    if len(listaSem) > 3:
        telaAdicionais.c4.setText(str(listaSem[3]))
    if len(listaSem) > 4:
        telaAdicionais.c5.setText(str(listaSem[4]))
    if len(listaSem) > 5:
        telaAdicionais.c6.setText(str(listaSem[5]))
    if len(listaSem) > 6:
        telaAdicionais.c7.setText(str(listaSem[6]))
    if len(listaSem) > 7:
        telaAdicionais.c8.setText(str(listaSem[7]))
    if len(listaSem) > 8:
        telaAdicionais.c9.setText(str(listaSem[8]))
    if len(listaSem) > 9:
        telaAdicionais.c10.setText(str(listaSem[9]))
    if len(listaSem) > 10:
        telaAdicionais.c11.setText(str(listaSem[10]))
    if len(listaSem) > 11:
        telaAdicionais.c12.setText(str(listaSem[11]))
    if len(listaSem) > 12:
        telaAdicionais.c13.setText(str(listaSem[12]))
    if len(listaSem) > 13:
        telaAdicionais.c14.setText(str(listaSem[13]))
    if len(listaSem) > 14:
        telaAdicionais.c15.setText(str(listaSem[14]))
    if len(listaSem) > 15:
        telaAdicionais.c16.setText(str(listaSem[15]))
    if len(listaSem) > 16:
        telaAdicionais.c17.setText(str(listaSem[16]))
    if len(listaSem) > 17:
        telaAdicionais.c18.setText(str(listaSem[17]))
    if len(listaSem) > 18:
        telaAdicionais.c19.setText(str(listaSem[18]))
    if len(listaSem) > 19:
        telaAdicionais.c20.setText(str(listaSem[19]))
    if len(listaSem) > 20:
        telaAdicionais.c21.setText(str(listaSem[20]))
    if len(listaSem) > 21:
        telaAdicionais.c22.setText(str(listaSem[21]))
    if len(listaSem) > 22:
        telaAdicionais.c23.setText(str(listaSem[22]))
    if len(listaSem) > 23:
        telaAdicionais.c24.setText(str(listaSem[23]))
    if len(listaSem) > 24:
        telaAdicionais.c25.setText(str(listaSem[24]))
    if len(listaSem) > 25:
        telaAdicionais.c26.setText(str(listaSem[25]))
    if len(listaSem) > 26:
        telaAdicionais.c27.setText(str(listaSem[26]))
    if len(listaSem) > 27:
        telaAdicionais.c28.setText(str(listaSem[27]))
    if len(listaSem) > 28:
        telaAdicionais.c29.setText(str(listaSem[28]))
    if len(listaSem) > 29:
        telaAdicionais.c30.setText(str(listaSem[29]))
    if len(listaSem) > 30:
        telaAdicionais.c31.setText(str(listaSem[30]))
    if len(listaSem) > 31:
        telaAdicionais.c32.setText(str(listaSem[31]))
    if len(listaSem) > 32:
        telaAdicionais.c33.setText(str(listaSem[32]))
    if len(listaSem) > 33:
        telaAdicionais.c34.setText(str(listaSem[33]))
    if len(listaSem) > 34:
        telaAdicionais.c35.setText(str(listaSem[34]))
    if len(listaSem) > 35:
        telaAdicionais.c36.setText(str(listaSem[35]))
    if len(listaSem) > 36:
        telaAdicionais.c37.setText(str(listaSem[36]))
    if len(listaSem) > 37:
        telaAdicionais.c38.setText(str(listaSem[37]))
    if len(listaSem) > 38:
        telaAdicionais.c39.setText(str(listaSem[38]))

    setar_checkBox_false.checkBox_tela_adicionais_com(telaAdicionais)
    setar_checkBox_false.checkBox_tela_adicionais_sem(telaAdicionais)
