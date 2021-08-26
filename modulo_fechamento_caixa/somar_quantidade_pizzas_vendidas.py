def somar(tela1, tela2):
    try:
        telaPizza = tela1
        telaErro = tela2

        pizza = []
        for i in range(1):
            pizza.append(int(telaPizza.pizza1.text() or 0))
            pizza.append(int(telaPizza.pizza2.text() or 0))
            pizza.append(int(telaPizza.pizza3.text() or 0))
            pizza.append(int(telaPizza.pizza4.text() or 0))
            pizza.append(int(telaPizza.pizzaIfood.text() or 0))
            somaPizza = sum(pizza)
        telaPizza.hide()
        return somaPizza
    except:
        telaErro.show()
        telaErro.label.setText('  Erro, tente novamente!')