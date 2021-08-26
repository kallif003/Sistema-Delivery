def limpar(tela, cursor, banco10, modulo):
    telaPrincipal = tela
    sql_limpa_tableWidget = modulo

    telaPrincipal.valorTotal.setText("Valor Total:")
    telaPrincipal.tableWidget_cadastro.clear()
    telaPrincipal.desconto.clear()
    telaPrincipal.acrescimo.clear()

    sql_limpa_tableWidget.limpar(cursor, banco10)