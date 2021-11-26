def outros(*args):

    telaPrincipal = args[0]
    cursor = args[1]
    preenche_checkbox = args[2]

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