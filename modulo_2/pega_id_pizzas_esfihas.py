def pega_id(*args):
    try:
        telaAtualizarProdutos = args[0]
        telaErro = args[1]
        cursor = args[2]

        id = telaAtualizarProdutos.cod_atualizar.text()

        if telaAtualizarProdutos.broto_atualizar.isChecked():
            cursor.execute("select * from broto where id = %s" % id)
            pizza = cursor.fetchall()
            telaAtualizarProdutos.produto_atualizar.setText(str(pizza[0][1]))
            telaAtualizarProdutos.ingredientes_atualizar.setText(str(pizza[0][4]))
            telaAtualizarProdutos.valor_atualizar.setText(str(pizza[0][3]))

        if telaAtualizarProdutos.seis_atualizar.isChecked():
            cursor.execute("select * from seisPedacos where id = %s" % id)
            pizza = cursor.fetchall()
            telaAtualizarProdutos.produto_atualizar.setText(str(pizza[0][1]))
            telaAtualizarProdutos.ingredientes_atualizar.setText(str(pizza[0][4]))
            telaAtualizarProdutos.valor_atualizar.setText(str(pizza[0][3]))

        if telaAtualizarProdutos.oito_atualizar.isChecked():
            cursor.execute("select * from oitoPedacos where id = %s" % id)
            pizza = cursor.fetchall()
            telaAtualizarProdutos.produto_atualizar.setText(str(pizza[0][1]))
            telaAtualizarProdutos.ingredientes_atualizar.setText(str(pizza[0][4]))
            telaAtualizarProdutos.valor_atualizar.setText(str(pizza[0][3]))

        if telaAtualizarProdutos.dez_atualizar.isChecked():
            cursor.execute("select * from dezPedacos where id = %s" % id)
            pizza = cursor.fetchall()
            telaAtualizarProdutos.produto_atualizar.setText(str(pizza[0][1]))
            telaAtualizarProdutos.ingredientes_atualizar.setText(str(pizza[0][4]))
            telaAtualizarProdutos.valor_atualizar.setText(str(pizza[0][3]))

        if telaAtualizarProdutos.esfiha_atualizar.isChecked():
            cursor.execute("select * from esfihas where id = %s" % id)
            pizza = cursor.fetchall()
            telaAtualizarProdutos.produto_atualizar.setText(str(pizza[0][1]))
            telaAtualizarProdutos.ingredientes_atualizar.setText(str(pizza[0][4]))
            telaAtualizarProdutos.valor_atualizar.setText(str(pizza[0][3]))
    except:
        telaErro.show()
        telaErro.label.setText('  Erro, tente novamente!')
