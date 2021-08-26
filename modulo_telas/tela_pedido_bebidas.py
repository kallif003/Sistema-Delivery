def bebidas(tela, cursor, modulo):
    try:
        telaPrincipal = tela
        preenche_checkbox = modulo

        telaPrincipal.frame_esfiha.show()
        telaPrincipal.frame_outros.hide()
        telaPrincipal.frame_bebidas.show()

        lista = []
        sql = ("select bebida from lata")
        cursor.execute(sql)
        dados = cursor.fetchall()
        for i in dados:
            for j in i:
                lista.append(j)

        preenche_checkbox.preenche_checkBox_bebida(telaPrincipal, lista)

    except Exception as erro:
        print(erro.__class__)