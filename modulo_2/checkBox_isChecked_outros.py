def isChecked(*args):

    telaPrincipal = args[0]
    dados = args[1]
    listaTemp = []
    valorProduto = []

    if (telaPrincipal.checkBox2_5.isChecked()):
        for i in range(len(dados)):
            listaTemp.append(dados[0])
            valorProduto.append(dados[0][2])
            break
    if (telaPrincipal.checkBox2_4.isChecked()):
        for i in range(len(dados)):
            listaTemp.append(dados[1])
            valorProduto.append(dados[1][2])
            break
    if (telaPrincipal.checkBox3_4.isChecked()):
        for i in range(len(dados)):
            listaTemp.append(dados[2])
            valorProduto.append(dados[2][2])
            break
    if (telaPrincipal.checkBox4_4.isChecked()):
        for i in range(len(dados)):
            listaTemp.append(dados[3])
            valorProduto.append(dados[3][2])
            break
    if (telaPrincipal.checkBox22_5.isChecked()):
        for i in range(len(dados)):
            listaTemp.append(dados[4])
            valorProduto.append(dados[4][2])
            break
    if (telaPrincipal.checkBox22_4.isChecked()):
        for i in range(len(dados)):
            listaTemp.append(dados[5])
            valorProduto.append(dados[5][2])
            break
    if (telaPrincipal.checkBox23_4.isChecked()):
        for i in range(len(dados)):
            listaTemp.append(dados[6])
            valorProduto.append(dados[6][2])
            break
    if (telaPrincipal.checkBox24_4.isChecked()):
        for i in range(len(dados)):
            listaTemp.append(dados[7])
            valorProduto.append(dados[7][2])
            break
    if (telaPrincipal.checkBox42_9.isChecked()):
        for i in range(len(dados)):
            listaTemp.append(dados[8])
            valorProduto.append(dados[8][2])
            break
    if (telaPrincipal.checkBox42_7.isChecked()):
        for i in range(len(dados)):
            listaTemp.append(dados[9])
            valorProduto.append(dados[9][2])
            break
    if (telaPrincipal.checkBox43_7.isChecked()):
        for i in range(len(dados)):
            listaTemp.append(dados[10])
            valorProduto.append(dados[10][2])
            break
    if (telaPrincipal.checkBox44_7.isChecked()):
        for i in range(len(dados)):
            listaTemp.append(dados[11])
            valorProduto.append(dados[11][2])
            break

    return listaTemp, valorProduto