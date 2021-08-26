def confirmando_pedido(tela1, tela2,tela3, cursor, pymysql, valor):
    try:

        telaPrincipal = tela1
        telaErro = tela2
        telaConfirmarPedido = tela3
        valorTotal = valor

        tel = telaPrincipal.telefone.text() or 1
        cursor.execute("select telefone from cadastro_cliente where telefone = %s" % tel)
        dados = cursor.fetchall()

        if dados == ():
            telaErro.show()
            telaErro.label.setText('  Erro! Salve o cadastro do cliente')
        else:
            telaConfirmarPedido.show()
            lista = [telaConfirmarPedido.voucher, telaConfirmarPedido.cartao, telaConfirmarPedido.dinheiro,
                     telaConfirmarPedido.troco,
                     telaConfirmarPedido.resto, telaConfirmarPedido.lineEdit, telaConfirmarPedido.pix]
            for i in lista:
                i.clear()
            # telaConfirmarPedido.vemBuscar.setChecked(False)
            telaConfirmarPedido.valorTotal.setText(f'{valorTotal:.2f}')
    except pymysql.err.ProgrammingError:
        telaErro.show()
        telaErro.label.setText('Telefone invalido, tente novamente')
    except pymysql.err.OperationalError:
        telaErro.show()
        telaErro.label.setText('Telefone invalido, tente novamente')