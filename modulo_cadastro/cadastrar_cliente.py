def cadastrar(*args):
    try:
        telaPrincipal = args[0]
        telaErro = args[1]
        cursor  = args[2]
        banco10 = args[3]
        date = args[4]
        pymysql = args[5]

        tel = telaPrincipal.telefone.text()
        taxa = int(telaPrincipal.taxa_2.text() or 0)
        nome = telaPrincipal.nome.text()
        cep = telaPrincipal.cep.text() or 0
        end = telaPrincipal.end.text() or ''
        numero = telaPrincipal.numero.text() or 0
        bairro = telaPrincipal.bairro.text() or ''
        ref = telaPrincipal.ref.text() or ''
        comple = telaPrincipal.complemento.text() or ''

        nome = nome.upper()
        end = end.upper()
        bairro = bairro.upper()
        ref = ref.upper()
        comple = comple.upper()

        data_atual = date.today()

        sql = "insert into cadastro_cliente (telefone, nome, cep, endereco, numero, bairro, referencia, complemento, taxaEntrega, data_inclusao)" \
              "values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
        dados = (
            str(tel), str(nome), str(cep), str(end), numero, str(bairro), str(ref), str(comple), str(taxa), data_atual)
        cursor.execute(sql, dados)
        banco10.commit()

        telaPrincipal.label_cadastrado.show()

    except(ValueError):
        telaErro.show()
        telaErro.label.setText('    Erro! Utilize numeros inteiros')
    except (pymysql.err.DataError):
        telaErro.show()
        telaErro.label.setText('Erro!Excesso de caracteres, abrevie ')