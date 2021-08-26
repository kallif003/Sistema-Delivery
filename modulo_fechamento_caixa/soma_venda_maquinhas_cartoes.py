def somar(tela1, tela2):
    try:
        telaCartao = tela1
        telaErro = tela2

        cartao = []
        for i in range(1):
            cartao.append(float(telaCartao.lineCartao1.text() or 0))
            cartao.append(float(telaCartao.lineCartao2.text() or 0))
            cartao.append(float(telaCartao.lineCartao3.text() or 0))
            cartao.append(float(telaCartao.lineCartao4.text() or 0))
            cartao.append(float(telaCartao.lineCartao5.text() or 0))
            cartao.append(float(telaCartao.lineCartao6.text() or 0))
            cartao.append(float(telaCartao.lineCartao7.text() or 0))
            cartao.append(float(telaCartao.lineCartao8.text() or 0))
            somaCartao = sum(cartao)
        telaCartao.hide()
        return somaCartao
    except:
        telaErro.show()
        telaErro.label.setText('  Erro, tente novamente!')