def cadastrar(tela1, tela2, cursor, banco10):
    telaCadastroLogin = tela1
    telaErro = tela2

    login = telaCadastroLogin.login_cadastro.text()
    senha = telaCadastroLogin.senha_cadastro.text()

    sql = "insert into cadastro_login(login, senha) values (%s, %s)"
    insert = (str(login), str(senha))
    cursor.execute(sql, insert)
    banco10.commit()
    telaErro.show()
    telaErro.label.setText('  Cadastro realizado com sucesso!')