def cadastrar(*args):

    telaCadastroLogin = args[0]
    telaErro = args[1]
    cursor = args[2]
    banco10 = args[3]

    login = telaCadastroLogin.login_cadastro.text()
    senha = telaCadastroLogin.senha_cadastro.text()

    sql = "insert into cadastro_login(login, senha) values (%s, %s)"
    insert = (str(login), str(senha))
    cursor.execute(sql, insert)
    banco10.commit()
    telaErro.show()
    telaErro.label.setText('  Cadastro realizado com sucesso!')