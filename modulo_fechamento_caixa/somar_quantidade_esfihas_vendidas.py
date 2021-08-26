def somar(tela1, tela2):
    try:
        telaEsfiha = tela1
        telaErro = tela2

        esfiha = []
        for i in range(1):
            esfiha.append(int(telaEsfiha.esfiha1.text() or 0))
            esfiha.append(int(telaEsfiha.esfiha2.text() or 0))
            esfiha.append(int(telaEsfiha.esfiha3.text() or 0))
            esfiha.append(int(telaEsfiha.esfiha4.text() or 0))
            somaEsfiha = sum(esfiha)
        telaEsfiha.hide()
        return somaEsfiha
    except:
        telaErro.show()
        telaErro.label.setText('  Erro, tente novamente!')