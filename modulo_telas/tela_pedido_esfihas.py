def esfihas(tela, cursor, modulo):
    try:
        telaPrincipal = tela
        preenche_checkbox = modulo

        telaPrincipal.frame_bebidas.hide()
        telaPrincipal.frame_esfiha.show()
        lista = []
        sql = ("select sabor from esfihas")
        cursor.execute(sql)
        dados = cursor.fetchall()
        for i in dados:
            for j in i:
                lista.append(j)

        preenche_checkbox.preenche_check_box_esfihas(telaPrincipal, lista)
    except Exception as erro:
        print(erro.__class__)


