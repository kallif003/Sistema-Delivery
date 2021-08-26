def abre_informacao_pedido(tela):
    telaInfoPedido = tela

    telaInfoPedido.show()
    lista = [telaInfoPedido.codigo, telaInfoPedido.telefone, telaInfoPedido.nome, telaInfoPedido.cep,
             telaInfoPedido.endereco, telaInfoPedido.numero, telaInfoPedido.bairro, telaInfoPedido.ref,
             telaInfoPedido.complemento, telaInfoPedido.taxa, telaInfoPedido.motoboy, telaInfoPedido.tableWidget_2,
             telaInfoPedido.cartao, telaInfoPedido.voucher, telaInfoPedido.desconto,telaInfoPedido.dinheiro,telaInfoPedido.troco,
             telaInfoPedido.valorTotal, telaInfoPedido.label, telaInfoPedido.label_2]
    for i in lista:
        i.clear()