def gerar(*args):
    try:
        telaSecundaria = args[0]
        telaErro = args[1]
        cursor = args[2]
        datetime = args[3]
        os = args[4]
        data = args[5]

        semana = datetime.today().weekday()
        lista_dias_semana = ['Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sabado', 'Domingo']
        if semana == 2:
            dia_semana = lista_dias_semana[0]
        elif semana == 3:
            dia_semana = lista_dias_semana[1]
        elif semana == 4:
            dia_semana = lista_dias_semana[2]
        elif semana == 5:
            dia_semana = lista_dias_semana[3]
        else:
            dia_semana = lista_dias_semana[4]

        ano = data[4:8]
        mes = data[2:4]
        dia = data[0:2]
        data2 = str(dia + '/' + mes + '/' + ano)

        lista = []
        linha = telaSecundaria.tableWidget.currentRow()
        cursor.execute("select id from fechamento")
        dados = cursor.fetchall()
        id = dados[linha][0]
        x = str(id)
        sql = ("select * from fechamento where id = %s" % x)
        cursor.execute(sql)
        dados = cursor.fetchall()
        sql2 = ("select * from fechamento2 where id = %s" % x)
        cursor.execute(sql2)
        dados2 = cursor.fetchall()

        for i in dados:
            for j in i:
                lista.append(j)
        for i in dados2:
            for j in i:
                lista.append(j)

        arquivo = open('fechamento.txt', 'w')
        arquivo.write('FECHAMENTO DE CAIXA' + '\n')
        arquivo.write('-' * 32 + '\n')
        arquivo.write('Data:'+ str(data2) + ' ' + str(f'({dia_semana})') + '\n')
        arquivo.write('Inicio Caixa:' + str(lista[2]) + '\n')
        arquivo.write('Cartao:' + str(lista[6]) + '\n')
        arquivo.write('Retirada:' + str(lista[3]) + '\n')
        arquivo.write('Motoboy:' + str(lista[5]) + '\n')
        if lista[12] != '':
            arquivo.write(str(lista[12]) + ':' + str(lista[13]) + '\n')
        if lista[14] != '':
            arquivo.write(str(lista[14]) + ':' + str(lista[15]) + '\n')
        if lista[16] != '':
            arquivo.write(str(lista[16]) + ':' + str(lista[17]) + '\n')
        if lista[18] != '':
            arquivo.write(str(lista[18]) + ':' + str(lista[19]) + '\n')
        if lista[20] != '':
            arquivo.write(str(lista[20]) + ':' + str(lista[21]) + '\n')
        if lista[22] != '':
            arquivo.write(str(lista[22]) + ':' + str(lista[23]) + '\n')
        if lista[24] != '':
            arquivo.write(str(lista[24]) + ':' + str(lista[25]) + '\n')
        arquivo.write('Total pagamento:' + str(lista[34]) + '\n')
        arquivo.write('Total:' + str(lista[29]) + '\n')
        arquivo.write('Venda dia:' + str(lista[28]) + '\n')
        arquivo.write('-' * 32 + '\n')
        arquivo.write('Pagamento online Ifood:' + str(lista[10]) + '\n')
        arquivo.write('Pagamento dinheiro Ifood:' + str(lista[27]) + '\n')
        arquivo.write('Total Ifood:' + str(lista[11]) + '\n')
        arquivo.write('-' * 32 + '\n')
        arquivo.write('Pizzas:' + str(lista[9]) + '\n')
        arquivo.write('Esfihas:' + str(lista[8]) + '\n')
        arquivo.write('-' * 32 + '\n')
        arquivo.write('Subiu:' + str(lista[31]) + '\n')
        arquivo.write('Ficou:' + str(lista[30]) + '\n')
        arquivo.write('Faltou:' + str(lista[32]) + '\n')
        arquivo.write('Sobrou:' + str(lista[33]) + '\n')
        arquivo.write('Inicio proximo caixa:' + str(lista[4]) + '\n')
        arquivo.write('-' * 32 + '\n')
        arquivo.close()

        os.startfile("C:\\Users\\GRATONI\\Desktop\\dist\\sistemaDelivery\\fechamento.txt", "print")

    except:
        telaErro.show()
        telaErro.label.setText('  Erro, tente novamente!')