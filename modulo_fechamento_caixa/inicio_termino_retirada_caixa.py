def caixa(tela1, tela2):
    try:
        telaCaixa2 = tela1
        telaErro = tela2

        inicioCx = telaCaixa2.inicioCx.text() or 0
        finalCx = telaCaixa2.terminoCx.text() or 0
        retirada = telaCaixa2.retirada.text() or 0
        x = inicioCx, finalCx, retirada
        telaCaixa2.hide()
        return x
    except:
        telaErro.show()
        telaErro.label.setText('    Erro, tente novamente!')