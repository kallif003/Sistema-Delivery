def caixa(*args):

    telaCaixa = args[0]
    data = args[1]

    ano = data[4:8]
    mes = data[2:4]
    dia = data[0:2]
    data2 = str(dia + '/' + mes + '/' + ano)
    telaCaixa.show()

    telaCaixa.label_data.setText('Data:' + ' ' + str(data2))
    telaCaixa.tableWidget.clear()