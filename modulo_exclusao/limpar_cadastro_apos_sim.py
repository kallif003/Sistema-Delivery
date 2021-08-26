def limpar(tela):
    telaPrincipal = tela

    lista = [telaPrincipal.telefone, telaPrincipal.nome,
             telaPrincipal.cep,
             telaPrincipal.end,
             telaPrincipal.numero,
             telaPrincipal.bairro,
             telaPrincipal.ref,
             telaPrincipal.complemento, telaPrincipal.devendo, telaPrincipal.taxa_2]
    for i in lista:
        i.clear()
    telaPrincipal.label_cadastrado.hide()
    telaPrincipal.label_atualizado.hide()