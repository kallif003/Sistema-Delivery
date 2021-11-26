def info(*args):
    try:
        tela_exibi_valores_pizzas = args[0]
        telaErro = args[1]
        cursor = args[2]
        QtWidgets = args[3]
        setar_checkBox_false = args[4]
        ingredientes_informacoes_pizzas = args[5]
        telaPrincipal = args[6]

        tela_exibi_valores_pizzas.show()

        ingredientes_informacoes_pizzas.mostrar(telaPrincipal, tela_exibi_valores_pizzas, cursor, QtWidgets)
        setar_checkBox_false.checkBox_tela_pedidos_esfiha(telaPrincipal)
        setar_checkBox_false.checkBox_tela_pedidos_pizzas(telaPrincipal)

    except IndexError:
        telaErro.show()
        telaErro.label.setText('       Erro! Selecione um sabor')
