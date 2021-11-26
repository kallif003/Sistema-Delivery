def esfihas(*args):
    try:
        telaPrincipal = args[0]
        cursor = args[1]
        preenche_checkbox = args[2]

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


