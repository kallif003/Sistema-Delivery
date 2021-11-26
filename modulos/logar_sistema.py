def logar(*args):

    telaLogin = args[0]
    telaCalendario2 = args[1]
    telaErro = args[2]
    cursor = args[3]

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