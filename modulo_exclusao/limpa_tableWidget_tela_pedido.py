def limpar(*args):

    telaPrincipal = args[0]
    cursor = args[1]
    banco10 = args[2]
    sql_limpa_tableWidget = args[3]

    telaPrincipal.valorTotal.setText("Valor Total:")
    telaPrincipal.tableWidget_cadastro.clear()
    telaPrincipal.desconto.clear()
    telaPrincipal.acrescimo.clear()

    sql_limpa_tableWidget.limpar(cursor, banco10)