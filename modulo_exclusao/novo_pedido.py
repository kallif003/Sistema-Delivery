def pedido_novo(*args):

    telaPrincipal = args[0]
    sql_limpa_tableWidget = args[1]
    setar_checkBox_false = args[2]
    cursor = args[3]
    banco10 = args[4]

    lista1 = [telaPrincipal.telefone, telaPrincipal.nome,
              telaPrincipal.cep,
              telaPrincipal.end,
              telaPrincipal.numero,
              telaPrincipal.bairro,
              telaPrincipal.ref,
              telaPrincipal.complemento, telaPrincipal.tableWidget_cadastro, telaPrincipal.taxa_2, telaPrincipal.desconto, telaPrincipal.acrescimo, telaPrincipal.devendo]
    for i in lista1:
        i.clear()

    telaPrincipal.show()
    telaPrincipal.frame_esfiha.hide()
    telaPrincipal.valorTotal.setText("Valor Total:")
    telaPrincipal.label_cadastrado.hide()
    telaPrincipal.label_atualizado.hide()

    sql_limpa_tableWidget.limpar(cursor, banco10)
    setar_checkBox_false.checkBox_tela_pedidos_pizzas(telaPrincipal)
    setar_checkBox_false.checkBox_tela_pedidos_outros(telaPrincipal)
    setar_checkBox_false.checkBox_tela_pedidos_refrigerante(telaPrincipal)
    setar_checkBox_false.checkBox_tela_pedidos_esfiha(telaPrincipal)