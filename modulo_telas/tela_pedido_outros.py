def outros(tela, cursor, modulo):

    telaPrincipal = tela
    preenche_checkbox = modulo

    telaPrincipal.frame_esfiha.show()
    telaPrincipal.frame_bebidas.show()
    telaPrincipal.frame_outros.show()

    lista = []
    sql = ("select produto from outros")
    cursor.execute(sql)
    dados = cursor.fetchall()
    for i in dados:
        for j in i:
            lista.append(j)

    preenche_checkbox.preenche_check_box_outros(telaPrincipal, lista)