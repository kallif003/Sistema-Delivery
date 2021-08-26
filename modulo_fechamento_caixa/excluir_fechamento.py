def excluir(tela1, tela2, cursor, banco10):
    try:
        telaSecundaria = tela1
        telaErro = tela2

        linha = telaSecundaria.tableWidget.currentRow()
        telaSecundaria.tableWidget.removeRow(linha)
        cursor.execute("select id from fechamento")
        dados = cursor.fetchall()
        id = dados[linha][0]
        x = str(id)

        cursor.execute("delete from fechamento where id = %s" % x)
        cursor.execute("delete from fechamento2 where id = %s" % x)
        banco10.commit()
    except:
        telaErro.show()
        telaErro.label.setText('  Erro, tente novamente!')