def calcular(tela1, tela2):
    try:
        telaPagamento = tela1
        telaErro = tela2

        pag = []
        for i in range(1):
            pag.append(telaPagamento.pagamento1.text() or '')
            pag.append(telaPagamento.pagamento2.text() or '')
            pag.append(telaPagamento.pagamento3.text() or '')
            pag.append(telaPagamento.pagamento4.text() or '')
            pag.append(telaPagamento.pagamento5.text() or '')
            pag.append(telaPagamento.pagamento6.text() or '')
            pag.append(telaPagamento.pagamento7.text() or '')
        valor = []
        for j in range(1):
            valor.append(float(telaPagamento.Fuvalor1.text() or 0))
            valor.append(float(telaPagamento.Fuvalor2.text() or 0))
            valor.append(float(telaPagamento.Fuvalor3.text() or 0))
            valor.append(float(telaPagamento.Fuvalor4.text() or 0))
            valor.append(float(telaPagamento.Fuvalor5.text() or 0))
            valor.append(float(telaPagamento.Fuvalor6.text() or 0))
            valor.append(float(telaPagamento.Fuvalor7.text() or 0))
        telaPagamento.hide()
        return pag, valor
    except:
        telaErro.show()
        telaErro.label.setText('  Erro, tente novamente!')