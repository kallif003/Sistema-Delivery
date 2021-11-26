def cep(*args):
    try:
        telaPrincipal = args[0]
        telaErro = args[1]
        pycep_correios = args[2]

        cep = telaPrincipal.cep.text()
        end = pycep_correios.get_address_from_cep(cep)
        telaPrincipal.end.setText(end['logradouro'])
        telaPrincipal.bairro.setText(end['bairro'])
    except:
        telaErro.show()
        telaErro.label.setText("  CEP invalido, verifique por favor")