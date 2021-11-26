def formas_pagamento(*args):
    try:
        telaConfirmarPedido = args[0]
        telaErro = args[1]
        valorTotal = args[2]

        cartao = float(telaConfirmarPedido.cartao.text() or 0)
        voucher = float(telaConfirmarPedido.voucher.text() or 0)
        din = float(telaConfirmarPedido.dinheiro.text() or 0)
        pix = float(telaConfirmarPedido.pix.text() or 0)

        if din > valorTotal:
            troco = din - valorTotal
            telaConfirmarPedido.troco.setText(f'{troco:.2f}')
        if din <= valorTotal:
            resto = din - valorTotal
            resto = abs(resto)
            telaConfirmarPedido.resto.setText(f'{resto:.2f}')
            telaConfirmarPedido.troco.clear()

        if cartao != 0:
            resto = cartao - float(valorTotal)
            resto = abs(resto)
            telaConfirmarPedido.resto.setText(f'{resto:.2f}')

        if voucher != 0:
            resto = voucher - float(valorTotal)
            resto = abs(resto)
            telaConfirmarPedido.resto.setText(f'{resto:.2f}')

        if pix != 0:
            resto = pix - float(valorTotal)
            resto = abs(resto)
            telaConfirmarPedido.resto.setText(f'{resto:.2f}')

        if din != 0 and cartao != 0:
            resto = cartao - float(valorTotal)
            trocado = din + resto
            telaConfirmarPedido.dinheiro.setText(f'{din:.2f}')
            telaConfirmarPedido.troco.setText(f'{trocado:.2f}')
            restante = 0.00
            telaConfirmarPedido.resto.setText(f'{restante:.2f}')

        if din != 0 and voucher != 0:
            resto = voucher - float(valorTotal)
            trocado = din + resto
            telaConfirmarPedido.dinheiro.setText(f'{din:.2f}')
            telaConfirmarPedido.troco.setText(f'{trocado:.2f}')
            restante = 0.00
            telaConfirmarPedido.resto.setText(f'{restante:.2f}')

        if din != 0 and pix != 0:
            resto = pix - float(valorTotal)
            trocado = din + resto
            telaConfirmarPedido.dinheiro.setText(f'{din:.2f}')
            telaConfirmarPedido.troco.setText(f'{trocado:.2f}')
            restante = 0.00
            telaConfirmarPedido.resto.setText(f'{restante:.2f}')

    except ValueError:
        telaErro.show()
        telaErro.label.setText('   Nao use virgula, utilize ponto!')