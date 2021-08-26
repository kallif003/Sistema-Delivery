def somar(tela1, tela2):
    try:
        telaTerminais = tela1
        telaErro = tela2

        venda = []
        for i in range(1):
            venda.append(float(telaTerminais.terminal1.text() or 0))
            venda.append(float(telaTerminais.terminal2.text() or 0))
            venda.append(float(telaTerminais.terminal3.text() or 0))
            venda.append(float(telaTerminais.terminal4.text() or 0))
            somaVenda = sum(venda)
        telaTerminais.hide()
        return somaVenda
    except:
        telaErro.show()
        telaErro.label.setText('  Erro, tente novamente!')