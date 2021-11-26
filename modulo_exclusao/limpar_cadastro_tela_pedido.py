def limpar(tela1, tela2):

    telaPrincipal = tela1
    telaConfirmacao = tela2

    lista = [telaPrincipal.numero, telaPrincipal.nome,
             telaPrincipal.cep, telaPrincipal.end,
             telaPrincipal.numero, telaPrincipal.bairro,
             telaPrincipal.ref, telaPrincipal.complemento, telaPrincipal.devendo, telaPrincipal.taxa_2]
    for i in lista:
        i.clear()

    telaConfirmacao.hide()
    telaPrincipal.label_cadastrado.hide()
    telaPrincipal.label_atualizado.hide()