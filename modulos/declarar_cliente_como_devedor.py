def devedor(tela1, tela2, cursor, banco10, data):
    try:
        telaDevedores = tela1
        telaErro = tela2

        id = telaDevedores.codigo.text()
        sql = ("select id from gerenciarPedido where id = %s and dataa = %s")
        values = (id, data)
        cursor.execute(sql, values)
        dados2 = cursor.fetchall()
        id2 = dados2[0][0]

        sql = ("select dataa, hora, nome, telefone, valorTotal from gerenciarPedido where id = %s and dataa = %s")
        values = (id2, data)
        cursor.execute(sql, values)
        inf_cliente = cursor.fetchall()

        motivo = telaDevedores.motivo_dever.text()

        sql = "insert into devedores(id, dataa, hora, nome, telefone, valor, motivo) values (%s, %s, %s, %s, %s, %s, %s)"
        insert = (str(id2), str(inf_cliente[0][0]), str(inf_cliente[0][1]),
                  str(inf_cliente[0][2]), str(inf_cliente[0][3]),
                  str(inf_cliente[0][4]), str(motivo))
        cursor.execute(sql, insert)
        banco10.commit()

        telaDevedores.hide()
    except:
        telaErro.show()
        telaErro.label.setText('Codigo invalido, tente novamente!')