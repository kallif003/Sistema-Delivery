def excluir(*args):
    try:
        telaSecundaria = args[0]
        telaErro = args[1]
        cursor = args[2]
        banco10 = args[3]

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