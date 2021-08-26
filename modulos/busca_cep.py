def cep(tela1, tela2, pycep_correios):
    try:
        telaPrincipal = tela1
        telaErro = tela2

        cep = telaPrincipal.cep.text()
        end = pycep_correios.get_address_from_cep(cep)
        telaPrincipal.end.setText(end['logradouro'])
        telaPrincipal.bairro.setText(end['bairro'])
    except:
        telaErro.show()
        telaErro.label.setText("  CEP invalido, verifique por favor")