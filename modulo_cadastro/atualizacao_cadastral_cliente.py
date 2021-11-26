def atualizar(*args):
    try:
        telaPrincipal = args[0]
        telaErro = args[1]
        cursor = args[2]
        banco10 = args[3]
        pymysql = args[4]

        tel = telaPrincipal.telefone.text()
        taxa = telaPrincipal.taxa_2.text() or 0
        nome = telaPrincipal.nome.text()
        cep = telaPrincipal.cep.text() or 0
        end = telaPrincipal.end.text() or ''
        numero = telaPrincipal.numero.text() or 0
        bairro = telaPrincipal.bairro.text() or ''
        ref = telaPrincipal.ref.text() or ''
        comple = telaPrincipal.complemento.text() or ''
        devedor = telaPrincipal.devendo.text() or ''

        nome = nome.upper()
        end = end.upper()
        bairro = bairro.upper()
        ref = ref.upper()
        comple = comple.upper()

        sql = ("update cadastro_cliente set nome = %s, cep = %s, endereco = %s, numero = %s, bairro = %s, referencia = %s, complemento = %s, taxaEntrega = %s where telefone = %s")
        values = (str(nome), str(cep), str(end), str(numero), str(bairro), str(ref), str(comple), str(taxa), str(tel))
        cursor.execute(sql, values)
        banco10.commit()

        sql = ("update devedores set valor = %s where telefone = %s")
        values = (str(devedor), str(tel))
        cursor.execute(sql, values)
        banco10.commit()

        if devedor == '':
            cursor.execute("delete from devedores where telefone = %s" % tel)
            banco10.commit()

        telaPrincipal.label_atualizado.show()

    except (pymysql.err.DataError):
        telaErro.show()
        telaErro.label.setText('Erro!Excesso de caracteres, abrevie ')

    except(pymysql.err.DataError):
        telaErro.show()
        telaErro.label.setText('    Erro! Utilize numeros inteiros')

    except:
        telaErro.show()
        telaErro.label.setText('  Erro ao atualizar o cadastro!')