def info(tela1, tela2, cursor, QtWidgets, modulo1, modulo3, tela3):
    try:
        tela_exibi_valores_pizzas = tela1
        tela_exibi_valores_pizzas.show()

        telaErro = tela2
        telaPrincipal = tela3
        setar_checkBox_false = modulo1

        ingredientes_informacoes_pizzas = modulo3

        ingredientes_informacoes_pizzas.mostrar(telaPrincipal, tela_exibi_valores_pizzas, cursor, QtWidgets)


        setar_checkBox_false.checkBox_tela_pedidos_esfiha(telaPrincipal)
        setar_checkBox_false.checkBox_tela_pedidos_pizzas(telaPrincipal)
    except Exception as erro:
        print(erro.__class__)
    except IndexError:
        telaErro.show()
        telaErro.label.setText('       Erro! Selecione um sabor')
