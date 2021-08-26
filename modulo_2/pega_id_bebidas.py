def pega_id(tela1, tela2, cursor):
    try:
        telaAtualizarBebidas = tela1
        telaErro = tela2

        id = telaAtualizarBebidas.id_atualizar_bebidas.text()

        if telaAtualizarBebidas.lata_atualizar.isChecked():
            cursor.execute("select bebida, valor from lata where id = %s" % id)
            lata = cursor.fetchall()
            telaAtualizarBebidas.produto_atualizar.setText(str(lata[0][0]))
            telaAtualizarBebidas.valor_atualizar.setText(str(lata[0][1]))

        if telaAtualizarBebidas.s600_atualizar.isChecked():
            cursor.execute("select bebida, valor from s600 where id = %s" % id)
            s600 = cursor.fetchall()
            telaAtualizarBebidas.produto_atualizar.setText(str(s600[0][0]))
            telaAtualizarBebidas.valor_atualizar.setText(str(s600[0][1]))

        if telaAtualizarBebidas.umLitro_atualizar.isChecked():
            cursor.execute("select bebida, valor from umLitro where id = %s" % id)
            umLitro = cursor.fetchall()
            telaAtualizarBebidas.produto_atualizar.setText(str(umLitro[0][0]))
            telaAtualizarBebidas.valor_atualizar.setText(str(umLitro[0][1]))

        if telaAtualizarBebidas.umLmeio_atualizar.isChecked():
            cursor.execute("select bebida, valor from umEmeio where id = %s" % id)
            umEmeio = cursor.fetchall()
            telaAtualizarBebidas.produto_atualizar.setText(str(umEmeio[0][0]))
            telaAtualizarBebidas.valor_atualizar.setText(str(umEmeio[0][1]))

        if telaAtualizarBebidas.doisLitros_atualizar.isChecked():
            cursor.execute("select bebida, valor from doisLitros where id = %s" % id)
            doisLitros = cursor.fetchall()
            telaAtualizarBebidas.produto_atualizar.setText(str(doisLitros[0][0]))
            telaAtualizarBebidas.valor_atualizar.setText(str(doisLitros[0][1]))

        if telaAtualizarBebidas.doisLmeio_atualizar.isChecked():
            cursor.execute("select bebida, valor from doisEmeio where id = %s" % id)
            doisEmeio = cursor.fetchall()
            telaAtualizarBebidas.produto_atualizar.setText(str(doisEmeio[0][0]))
            telaAtualizarBebidas.valor_atualizar.setText(str(doisEmeio[0][1]))

        if telaAtualizarBebidas.outros_atualizar.isChecked():
            cursor.execute("select produto, tipo, valor from outros where id = %s" % id)
            outros = cursor.fetchall()
            telaAtualizarBebidas.produto_atualizar.setText(str(outros[0][0]))
            telaAtualizarBebidas.tipo_atualizar.setText(str(outros[0][1]))
            telaAtualizarBebidas.valor_atualizar.setText(str(outros[0][2]))
    except:
        telaErro.show()
        telaErro.label.setText('  Erro, tente novamente!')