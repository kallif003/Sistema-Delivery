def calcular(tela, cursor, banco10):
    try:
        telaErro = tela

        subiu = 0
        ficou = 0
        faltou = 0
        sobrou = 0
        lista = []

        cursor.execute("select max(id) from fechamento")
        dados = cursor.fetchall()
        id = dados[0][0]
        x = id

        sql = ("select * from fechamento where id = %d" % x)
        cursor.execute(sql)
        dados = cursor.fetchall()

        for i in dados:
            for j in i:
                lista.append(j)

        if lista[2] > lista[4]:
            subiu = lista[2] - lista[4]
        elif lista[4] > lista[2]:
            ficou = lista[4] - lista[2]

        soma = lista[3] + lista[6] + lista[5] + lista[13] + lista[15] + lista[17] + lista[19] + lista[21] + lista[23] + \
               lista[25] + ficou - subiu
        total_pag = lista[13] + lista[15] + lista[17] + lista[19] + lista[21] + lista[23] + lista[25]

        if lista[11] <= 0:
            pag_din = lista[10] - lista[10]
        else:
            pag_din = lista[11] - lista[10]

        vendaDia = lista[7] + pag_din

        if soma < vendaDia:
            faltou = vendaDia - soma
        else:
            sobrou = soma - vendaDia

        sql = "insert into fechamento2 (Pag_dinheiro, venda_dia, total_dia, " \
              "ficou, subiu, faltou, sobrou, total_pagamento) " \
              "values (%s, %s, %s, %s, %s, %s, %s, %s)"
        dados = (str(pag_din), str(vendaDia),
                 str(soma), str(ficou),
                 str(subiu), str(faltou),
                 str(sobrou), str(total_pag))
        cursor.execute(sql, dados)
        banco10.commit()
    except:
        telaErro.show()
        telaErro.label.setText('  Erro, tente novamente!')