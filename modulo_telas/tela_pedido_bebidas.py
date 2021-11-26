def bebidas(*args):
    try:
        telaPrincipal = args[0]
        cursor = args[1]
        preenche_checkbox = args[2]

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