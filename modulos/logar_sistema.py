def logar(tela1, tela2, tela3, cursor):

    telaLogin = tela1
    telaCalendario2 = tela2
    telaErro = tela3

    login = telaLogin.login.text()
    senha = telaLogin.senha.text()

    sql = ("select login, senha from cadastro_login where login = %s and senha = %s")
    values = (str(login), str(senha))
    cursor.execute(sql, values)
    dados = cursor.fetchall()

    if dados != ():
        telaCalendario2.show()
        telaLogin.hide()
    else:
        telaErro.show()
        telaErro.label.setText('Login ou senha invalidos, tente novamente!')