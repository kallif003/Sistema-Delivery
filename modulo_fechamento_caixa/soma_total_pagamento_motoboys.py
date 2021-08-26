def somar(tela1, tela2):
    try:
        telaMotoboy = tela1
        telaErro = tela2

        motoboy = []
        for i in range(1):
            motoboy.append(float(telaMotoboy.lineBoy1.text() or 0))
            motoboy.append(float(telaMotoboy.lineBoy2.text() or 0))
            motoboy.append(float(telaMotoboy.lineBoy3.text() or 0))
            motoboy.append(float(telaMotoboy.lineBoy4.text() or 0))
            motoboy.append(float(telaMotoboy.lineBoy5.text() or 0))
            motoboy.append(float(telaMotoboy.lineBoy6.text() or 0))
            somaBoy = sum(motoboy)
        telaMotoboy.hide()
        return somaBoy
    except:
        telaErro.show()
        telaErro.label.setText('  Erro, tente novamente!')