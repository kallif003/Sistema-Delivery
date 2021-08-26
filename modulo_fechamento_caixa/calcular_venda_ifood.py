def calcular(tela1, tela2):
    try:
        telaIfood = tela1
        telaErro = tela2

        ifood1 = telaIfood.online.text() or 0
        ifood2 = telaIfood.total.text() or 0
        ifood = ifood1, ifood2
        telaIfood.hide()
        return ifood
    except:
        telaErro.show()
        telaErro.label.setText('  Erro, tente novamente!')