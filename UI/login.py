import acesso_BD
import arquivos_ui

telaLogin = arquivos_ui.telaLogin
cursor = acesso_BD.cursor
telaCalendario2 = arquivos_ui.telaCalendario2
telaErro = arquivos_ui.telaErro

def login_sistema():
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