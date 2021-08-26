import os
import pycep_correios
import pymysql
from datetime import date, datetime
import time
from PyQt5 import uic, QtWidgets
import logo_rc, login_rc, login2_rc, pizza1_rc


from modulos import confirmacao_do_pedido, \
    total_diario_sistema, gerar_pedido_dois, \
    informacoes_pedido, cancelamento_pedido, \
    despacha_pedidos_prontos, finalizacao_pedido, \
    reimpressao_pedido, pagamentos, \
    funcao_gerar_pedido, total_mensal_sistema, \
    finalizacao_devedores, exibir_devedores, \
    declarar_cliente_como_devedor, atualizacao_adicionais, \
    remove_itens_produto, atualizacao_bebidas_outros, \
    atualizacao_pizzas_esfihas, busca_cep, \
    logar_sistema, informacao_adicionais

from modulo_2 import sql_informacoes_pedidos,\
    preenche_checkbox, pega_id_adicionais, \
    sql_tela_pedido, pega_id_pizzas_esfihas, \
    pega_id_bebidas, setar_checkBox_false, \
    sql_pizza_adicionais, ingredientes_informacoes, \
    ingredientes_informacoes_pizzas_esfihas, \
    chebox_isChecked_adicionais,checkBox_isChecked_esfiha, \
    checkBox_isChecked_bebidas, checkBox_isChecked_outros, \
    checkBox_isChecked_pizzas

from modulo_telas import tela_atualizacao_pizzas_esfihas, \
    tela_gerenciador_pedidos, tela_exibe_cadastro_bebidas, \
    tela_pedido_bebidas, tela_atualizacao_adicionais, \
    tela_exibidora_adicionais, tela_exibe_cadastro_outros, \
    tela_informacao_pedido, tela_caixa_sistema, \
    tela_exibe_cadastro_produtos, tela_pedido_esfihas, \
    tela_pedido_outros, tela_atualizacao_bebidas, \
    abre_tela_pedido, tela_carregamento_adicionais, \
    abre_tela_ultimo_pedido

from modulo_cadastro import cadastrar_adicionais_seis_pedacos, \
    cadastrar_esfihas, cadastrar_pizza_broto, \
    cadastrar_pizza_seis_pedacos, cadastrar_adicionais_oito_pedacos, \
    cadastrar_pizza_dez_pedacos, cadastrar_adicionais_broto, \
    cadastrar_pizza_oito_pedacos, cadastrar_adicionais_dez_pedacos,\
    cadastrar_bebidas_1L, cadastrar_bebidas_2L, \
    cadastrar_bebidas_1L_meio, cadastrar_bebidas_2L_meio,\
    cadastrar_bebidas_600, cadastrar_bebidas_lata, \
    cadastrar_outros, cadastrar_sem_adicionais,\
    atualizacao_cadastral_cliente, cadastrar_cliente, \
    verificacao_cadastro_cliente, cadastro_login_senha

from modulo_exclusao import excluir_outros, \
    excluir_bebidas, limpa_tableWidget_tela_pedido,\
    sql_limpa_tableWidget, novo_pedido, \
    excluir_pizzas_esfinhas_cadastradas,\
    excluir_adicionais_cadastrados, \
    limpar_cadastro_apos_sim, \
    limpar_cadastro_tela_pedido

from modulo_fechamento_caixa import inicio_termino_retirada_caixa, \
    soma_venda_maquinhas_cartoes,\
    soma_total_pagamento_motoboys, \
    soma_venda_terminais, \
    calcular_venda_ifood, \
    calcular_pagamentos_diarios,\
    somar_quantidade_pizzas_vendidas, \
    somar_quantidade_esfihas_vendidas, \
    calcular_venda_diaria, \
    consultar_fechamentos, \
    gerar_arquivo_txt, \
    excluir_fechamento


banco10 = pymysql.connect(
    host="localhost",
    user="root",
    password="2008",
    database="sistema_delivery"
)
cursor = banco10.cursor()

data = ''
valorTotal = 0

def tela_ultimo_pedido():
    abre_tela_ultimo_pedido.ultimo_pedido(telaUltimoPedido, telaPrincipal,
                                          telaErro, cursor, pymysql,
                                          QtWidgets)

def tela_bebidas_pedido():
    tela_pedido_bebidas.bebidas(telaPrincipal, cursor, preenche_checkbox)

def tela_outros_pedido():
    tela_pedido_outros.outros(telaPrincipal, cursor, preenche_checkbox)

def tela_esfihas_pedido():
    tela_pedido_esfihas.esfihas(telaPrincipal, cursor, preenche_checkbox)

def tela_caixa():
    tela_caixa_sistema.caixa(telaCaixa, data)

def voltar_tela_atualizar_produtos():
    telaAtualizarProdutos.frame_adc_atualizar.hide()

def tela_calendario():
    telaCalendario.show()

def tela_mensal():
    telaMensal.show()

def tela_periodo():
    telaPeriodo.show()

def pizzaTela():
    telaPrincipal.frame_esfiha.hide()
    telaPrincipal.frame_bebidas.hide()

def total_diario():
    total_diario_sistema.venda_do_dia(telaCaixa, cursor, data, QtWidgets)

def total_mensal():
    total_mensal_sistema.venda_mensal(telaCaixa, telaMensal, cursor, QtWidgets)

def telaConfirmacaoPedido():
    confirmacao_do_pedido.confirmando_pedido(telaPrincipal, telaErro, telaConfirmarPedido, cursor, pymysql, valorTotal)

def TelaGerenciarPedidos():
    tela_gerenciador_pedidos.gerenciador_pedidos(telaPedido, cursor, data, QtWidgets)

def tela_exibe_adicionais():
    tela_exibidora_adicionais.mostra_adicionais(telaProduto, cursor, QtWidgets)

def tela_atualizar_adicionais():
    tela_atualizacao_adicionais.atualiza_adicionais(telaAtualizarProdutos, cursor, QtWidgets, sql_pizza_adicionais)

def voltar_tela_produto():
    telaProduto.frame_adc.hide()

def Tela_Produtos():
    tela_exibe_cadastro_produtos.cadastrar_produtos(telaProduto, cursor, QtWidgets)

def tela_atualizar_bebidas():
    tela_atualizacao_bebidas.atualizar_bebidas(telaBebida, telaAtualizarBebidas, cursor, QtWidgets)

def tela_bebidas():
    tela_exibe_cadastro_bebidas.exibe_bebeidas(telaBebida, cursor, QtWidgets)

def telas_outros():
    tela_exibe_cadastro_outros.exibe_outros(telaBebida, cursor, QtWidgets)

def pagamento():
    pagamentos.formas_pagamento(telaConfirmarPedido, telaErro, valorTotal)

def gerar_pedido():
    funcao_gerar_pedido.gerando_pedido(gerar_pedido_dois, cursor, banco10, data,
                                       time, valorTotal, telaConfirmarPedido, telaPrincipal, telaErro)

def tela_imprimir():
    telaImprimir.show()
    telaImprimir.codigo.clear()

def imprimir_pedido():
    reimpressao_pedido.reimprimir(telaImprimir, data, cursor, os)

def tela_informacoes_pedido():
    tela_informacao_pedido.abre_informacao_pedido(telaInfoPedido)

def info_pedido():
    informacoes_pedido.inf_pedido(telaInfoPedido, telaErro, cursor, data, sql_informacoes_pedidos, QtWidgets)

def tela_despachar():
    telaDespachar.show()
    telaDespachar.codigo.clear()
    telaDespachar.motoboy.clear()

def despachar_pedido():
    despacha_pedidos_prontos.despachar(telaDespachar, telaErro, telaPedido, cursor, banco10, time, data, date, QtWidgets)

def tela_cancelar():
    telaCancelar.show()
    telaCancelar.codigo.clear()
    telaCancelar.motivo.clear()

def cancelar_pedido():
    cancelamento_pedido.cancelar(telaCancelar, telaErro, telaPedido, cursor, banco10, data, date, QtWidgets)

def tela_finalizar():
    telaFinalizar.show()
    telaFinalizar.codigo.clear()

def finalizar_pedido():
    finalizacao_pedido.finalizar(telaFinalizar, telaErro, telaPedido, date, time, data, cursor, banco10, QtWidgets)

def tela_devedores():
    telaDevedores.show()
    telaDevedores.codigo.clear()
    telaDevedores.motivo_dever.clear()

def pedidos_nao_pagos():
    declarar_cliente_como_devedor.devedor(telaDevedores, telaErro, cursor, banco10, data)

def tela_exibe_devedores():
    exibir_devedores.devendo(telaDevedores2, cursor, QtWidgets)

def tela_finalizar_devedores():
    telaFinalizarDeve.show()
    telaFinalizarDeve.codigo.clear()

def finalizar_devedores():
    finalizacao_devedores.finalizar(telaFinalizarDeve, telaDevedores2, telaErro, cursor, banco10, QtWidgets)

def remover_item():
    remove_itens_produto.remover(telaPrincipal, telaAdicionais, telaErro, cursor,
                                 banco10, pymysql, setar_checkBox_false, sql_tela_pedido, QtWidgets, data)

def id_bebidas_atualizar():
    pega_id_bebidas.pega_id(telaAtualizarBebidas, telaErro, cursor)

def bebidas_outros_atualizar():
    atualizacao_bebidas_outros.atualiza_bebidas_outros(telaAtualizarBebidas, telaErro, cursor,
                                                       banco10, QtWidgets, setar_checkBox_false)

def tela_atualizar_produtos():
    tela_atualizacao_pizzas_esfihas.pizzas_esfihas(telaProduto, telaAtualizarProdutos, cursor, QtWidgets,
                                                   sql_pizza_adicionais)

def id_adicionais_atualizar():
    pega_id_adicionais.pega_id(telaAtualizarProdutos, telaErro, cursor)

def id_pizza_esfiha_atualizar():
    pega_id_pizzas_esfihas.pega_id(telaAtualizarProdutos, telaErro, cursor)

def atualizar_adicionais():
    atualizacao_adicionais.atualiza_adicionais(telaAtualizarProdutos, telaErro, cursor,
                                               banco10, QtWidgets, setar_checkBox_false)

def atualizar_pizza_esfiha():
    atualizacao_pizzas_esfihas.atualiza_pizzas_esfihas(telaAtualizarProdutos, telaErro, cursor,
                                                       banco10, QtWidgets, setar_checkBox_false)

def cadastroEsfihas():
    cadastrar_esfihas.cadastrar(telaProduto, telaErro, cursor, banco10, QtWidgets)

def cadastroBroto():
    cadastrar_pizza_broto.cadastrar(telaProduto, telaErro, cursor, banco10, QtWidgets)

def cadastroSeis():
    cadastrar_pizza_seis_pedacos.cadastrar(telaProduto, telaErro, cursor, banco10, QtWidgets)

def cadastroOito():
    cadastrar_pizza_oito_pedacos.cadastrar(telaProduto, telaErro, cursor, banco10, QtWidgets)

def cadastroDez():
    cadastrar_pizza_dez_pedacos.cadastrar(telaProduto, telaErro, cursor, banco10, QtWidgets)

def cadastro_adicionais_broto():
    cadastrar_adicionais_broto.cadastrar(telaProduto, telaErro, cursor, banco10, QtWidgets)

def cadastro_adicionais_seis_pedacos():
    cadastrar_adicionais_seis_pedacos.cadastrar(telaProduto, telaErro, cursor, banco10, QtWidgets)

def cadastro_adicionais_oito_pedacos():
    cadastrar_adicionais_oito_pedacos.cadastrar(telaProduto, telaErro, cursor, banco10, QtWidgets)

def cadastro_adicionais_dez_pedacos():
    cadastrar_adicionais_dez_pedacos.cadastrar(telaProduto, telaErro, cursor, banco10, QtWidgets)

def cadastroLata():
    cadastrar_bebidas_lata.cadastrar(telaBebida, telaErro, cursor, banco10, QtWidgets)

def cadastro600():
    cadastrar_bebidas_600.cadastrar(telaBebida, telaErro, cursor, banco10, QtWidgets)

def cadastro1l():
    cadastrar_bebidas_1L.cadastrar(telaBebida, telaErro, cursor, banco10, QtWidgets)

def cadastro1meio():
    cadastrar_bebidas_1L_meio.cadastrar(telaBebida, telaErro, cursor, banco10, QtWidgets)

def cadastro2litro():
    cadastrar_bebidas_2L.cadastrar(telaBebida, telaErro, cursor, banco10, QtWidgets)

def cadastro2meio():
    cadastrar_bebidas_2L_meio.cadastrar(telaBebida, telaErro, cursor, banco10, QtWidgets)

def cadastrarOutros():
    cadastrar_outros.cadastrar(telaBebida, telaErro, cursor, banco10, QtWidgets)

def cadastro_sem_adicionais():
    cadastrar_sem_adicionais.cadastrar(telaProduto, telaErro, cursor, banco10, QtWidgets)

def exclui_outros():
    excluir_outros.excluir(telaBebida, telaErro, cursor, banco10, QtWidgets)

def tela_excluir_bebidas():
    telaExcluirBebidas.show()

def exclui_bebidas():
    excluir_bebidas.excluir(telaExcluirBebidas, telaErro, telaBebida, cursor,
                            banco10, QtWidgets, setar_checkBox_false)

def excluirTableWidget():
    global valorTotal
    valorTotal = 0
    limpa_tableWidget_tela_pedido.limpar(telaPrincipal, cursor, banco10, sql_limpa_tableWidget)

def NovoPedido():
    global valorTotal
    valorTotal = 0
    novo_pedido.pedido_novo(telaPrincipal, sql_limpa_tableWidget, setar_checkBox_false, cursor, banco10)

def excluir_cadastro_pizza():
    excluir_pizzas_esfinhas_cadastradas.excluir(telaAtualizarProdutos, telaErro, cursor,
                                                banco10, QtWidgets, sql_pizza_adicionais)

def excluir_cadastro_adicionais():
    excluir_adicionais_cadastrados.excluir(telaAtualizarProdutos, telaErro, cursor,
                                           banco10, QtWidgets, sql_pizza_adicionais)

def limpar_apos_sim():
    limpar_cadastro_apos_sim.limpar(telaPrincipal)

def limpa_dados_cadastrais():
    limpar_cadastro_tela_pedido.limpar(telaPrincipal, telaConfirmacao)

def exibe_cep():
    busca_cep.cep(telaPrincipal, telaErro, pycep_correios)

def atualizarCadastro():
    atualizacao_cadastral_cliente.atualizar(telaPrincipal, telaErro, cursor, banco10)

def cadastrar_Cliente():
    cadastrar_cliente.cadastrar(telaPrincipal, telaErro, cursor, banco10, date)

def verificar_cadastro_cliente():
    verificacao_cadastro_cliente.verificar(telaPrincipal,telaConfirmacao, cursor, banco10)

def tela_cadastrar_login():
    telaCadastroLogin.show()

def cadastrar_login():
    cadastro_login_senha.cadastrar(telaCadastroLogin, telaErro, cursor, banco10)

def login_sistema():
    logar_sistema.logar(telaLogin, telaCalendario2, telaErro, cursor)

def ingredientes():
    ingredientes_informacoes.info(tela_exibi_valores_pizzas, telaErro, cursor, QtWidgets, setar_checkBox_false,
                                  ingredientes_informacoes_pizzas_esfihas, telaPrincipal)

def telaDePedidos():
    global valorTotal
    valorTotal = 0
    abre_tela_pedido.tela_pedido(telaPrincipal, cursor, banco10, setar_checkBox_false, sql_tela_pedido)

def exibi_informacoes_adicionais():
    informacao_adicionais.informar(telaExibiPrecoAdicionais, telaAdicionais, cursor, QtWidgets, setar_checkBox_false)

def tela_carrega_adicionais():
    tela_carregamento_adicionais.carregar(telaAdicionais, cursor, setar_checkBox_false)

def calcular():
    calcular_venda_diaria.calcular(telaErro, cursor, banco10)

def tela_consulta():
    consultar_fechamentos.consultar(telaSecundaria, cursor, QtWidgets)

def gerar_arquivo():
    gerar_arquivo_txt.gerar(telaSecundaria, telaErro, cursor, datetime, os, data)

def excluir_dados():
    excluir_fechamento.excluir(telaSecundaria, telaErro, cursor, banco10)

def tela_caixa2():
    telaCaixa2.show()

def tela_cartao():
    telaCartao.show()

def tela_motoboy():
    telaMotoboy.show()

def tela_terminais():
    telaTerminais.show()

def tela_ifood():
    telaIfood.show()

def tela_pagamentos():
    telaPagamento.show()

def tela_pizza():
    telaPizza.show()

def tela_esfiha():
    telaEsfiha.show()

def tela_consulta():
    telaSecundaria.show()

def funcao_caixa():
    inicio_termino_retirada_caixa.caixa(telaCaixa2, telaErro)

def funcao_cartao():
    soma_venda_maquinhas_cartoes.somar(telaCartao, telaErro)

def funcao_motoboys():
    soma_total_pagamento_motoboys.somar(telaMotoboy, telaErro)

def funcao_venda():
    soma_venda_terminais.somar(telaTerminais, telaErro)

def funcao_ifood():
    calcular_venda_ifood.calcular(telaIfood, telaErro)

def funcao_pagamentos():
    calcular_pagamentos_diarios.calcular(telaPagamento, telaErro)

def funcao_pizza():
    somar_quantidade_pizzas_vendidas.somar(telaPizza, telaErro)

def funcao_esfiha():
    somar_quantidade_esfihas_vendidas.somar(telaEsfiha, telaErro)


def defini_data_sistema():
    global data
    data1 = str(telaCalendario2.calendarWidget2.selectedDate())

    ano = data1[19:23]

    if len(data1) <= 30:
        mes = data1[25]

    if len(data1) <= 31 and data1[28] != ' ' and data1[29] != ')':
        mes = data1[25]

    if len(data1) <=31 and data1[28] == ' ' and data1[29] != ' ':
        mes = data1[25:27]

    if len(data1) == 32:
        mes = data1[25:27]

    if len(data1) <= 30:
        dia = data1[28]

    if len(data1) == 31 and data1[25] != ' ' and data1[26] != ',':
        dia = data1[29]

    if len(data1) == 31 and data1[25] != ' ' and data1[26] == ',':
        dia = data1[28:30]

    if len(data1) == 32:
        dia = data1[29:31]

    if len(mes) < 2:
        mes = mes.zfill(2)
    if len(dia) < 2:
        dia = dia.zfill(2)

    data = str(dia + mes + ano)
    primeiraTela.show()
    telaCalendario2.hide()

def pegar_data():
    global data
    data1 = str(telaCalendario.calendarWidget.selectedDate())

    ano = data1[19:23]

    if len(data1) <= 30:
        mes = data1[25]

    if len(data1) <= 31 and data1[28] != ' ' and data1[29] != ')':
        mes = data1[25]

    if len(data1) <= 31 and data1[28] == ' ' and data1[29] != ' ':
        mes = data1[25:27]

    if len(data1) == 32:
        mes = data1[25:27]

    if len(data1) <= 30:
        dia = data1[28]

    if len(data1) == 31 and data1[25] != ' ' and data1[26] != ',':
        dia = data1[29]

    if len(data1) == 31 and data1[25] != ' ' and data1[26] == ',':
        dia = data1[28:30]

    if len(data1) == 32:
        dia = data1[29:31]

    if len(mes) < 2:
        mes = mes.zfill(2)
    if len(dia) < 2:
        dia = dia.zfill(2)

    data = str(dia + mes + ano)
    ano = data[4:8]
    mes = data[2:4]
    dia = data[0:2]
    data2 = str(dia + '/' + mes + '/' + ano)

    telaCaixa.label_data.setText('Data:' + ' ' + str(data2))
    telaCalendario.hide()

def taxaEntrega():
    try:
        global valorTotal

        tel = telaPrincipal.telefone.text() or 1
        cursor.execute("select taxaEntrega from cadastro_cliente where telefone = %s" % tel)
        dados = cursor.fetchall()
        taxa = float(dados[0][0])

        valorTotal = valorTotal + taxa
        telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')

    except IndexError:
        telaErro.show()
        telaErro.label.setText("Erro! Voce precisa salvar o contato")

def casa():
    try:
        global valorTotal
        valorTotal = valorTotal + 1
        telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')
    except Exception as erro:
        print(erro.__class__)

def excluir_item_pedido_id():
    try:
        global valorTotal
        desconto = float(telaPrincipal.desconto.text() or 0)
        id = telaPrincipal.codigo.text()

        cursor.execute("select subtotal from temp_inteiro where id = %s" % id)
        inteiro = cursor.fetchall()
        if inteiro != ():
            subInt = float(inteiro[0][0])
        else:
            subInt = 0

        cursor.execute(" delete from temp_inteiro where id = %s" % id)
        banco10.commit()

        cursor.execute("select subtotal from temp_metade2 where id = %s" % id)
        metade = cursor.fetchall()
        if metade != ():
            subMet = float(metade[0][0])
        else:
            subMet = 0

        cursor.execute(" delete from temp_metade1 where id = %s" % id)
        banco10.commit()

        cursor.execute("select subtotal from temp_terco3 where id = %s" % id)
        terco = cursor.fetchall()
        if terco != ():
            subTerco = float(terco[0][0])
        else:
            subTerco = 0

        cursor.execute(" delete from temp_terco1 where id = %s" % id)
        banco10.commit()

        cursor.execute("select subtotal from temp_quarto4 where id = %s" % id)
        quarto = cursor.fetchall()
        if quarto != ():
            subQt = float(quarto[0][0])
        else:
            subQt = 0

        cursor.execute(" delete from temp_quarto1 where id = %s" % id)
        banco10.commit()

        cursor.execute("select subtotal from temp_esfihas where id = %s" % id)
        esfihas = cursor.fetchall()
        if esfihas != ():
            subEsfihas = float(esfihas[0][0])
        else:
            subEsfihas = 0

        cursor.execute(" delete from temp_esfihas where id = %s" % id)
        banco10.commit()

        cursor.execute("select subtotal from temp_lata where id = %s" % id)
        lata = cursor.fetchall()
        if lata != ():
            subLata = float(lata[0][0])
        else:
            subLata = 0

        cursor.execute(" delete from temp_lata where id = %s" % id)
        banco10.commit()

        cursor.execute("select subtotal from temp_600 where id = %s" % id)
        s600 = cursor.fetchall()
        if s600 != ():
            sub600 = float(s600[0][0])
        else:
            sub600 = 0

        cursor.execute(" delete from temp_600 where id = %s" % id)
        banco10.commit()

        cursor.execute("select subtotal from temp_1L where id = %s" % id)
        umLitro = cursor.fetchall()
        if umLitro != ():
            sub1L = float(umLitro[0][0])
        else:
            sub1L = 0

        cursor.execute(" delete from temp_1L where id = %s" % id)
        banco10.commit()

        cursor.execute("select subtotal from temp_1Lmeio where id = %s" % id)
        umLmeio = cursor.fetchall()
        if umLmeio != ():
            sub1Lmeio = float(umLmeio[0][0])
        else:
            sub1Lmeio = 0

        cursor.execute(" delete from temp_1Lmeio where id = %s" % id)
        banco10.commit()

        cursor.execute("select subtotal from temp_2L where id = %s" % id)
        doisLitros = cursor.fetchall()
        if doisLitros != ():
            sub2L = float(doisLitros[0][0])
        else:
            sub2L = 0

        cursor.execute(" delete from temp_2L where id = %s" % id)
        banco10.commit()

        cursor.execute("select subtotal from temp_2Lmeio where id = %s" % id)
        doisLmeio = cursor.fetchall()
        if doisLmeio != ():
            sub2Lmeio = float(doisLmeio[0][0])
        else:
            sub2Lmeio = 0

        cursor.execute(" delete from temp_2Lmeio where id = %s" % id)
        banco10.commit()

        cursor.execute("select subtotal from temp_outros where id = %s" % id)
        outros = cursor.fetchall()
        if outros != ():
            subOutros = float(outros[0][0])
        else:
            subOutros = 0

        cursor.execute(" delete from temp_outros where id = %s" % id)
        banco10.commit()

        cursor.execute("select valor from temp_adc where id_pizza = %s" % id)
        adc = cursor.fetchall()
        if adc != ():
            subAdc = float(adc[0][0])
        else:
            subAdc = 0

        cursor.execute(" delete from temp_adc where id_pizza = %s" % id)
        banco10.commit()

        cursor.execute(" delete from semAdc where id_pizza = %s" % id)
        banco10.commit()

        sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)

        valorTotal = valorTotal - subInt - subMet - subTerco - subQt - subEsfihas - subLata - sub600 - sub1L - \
                     sub1Lmeio - sub2L - sub2Lmeio - subOutros - subAdc + desconto
        telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')

        telaPrincipal.codigo.clear()
    except:
        telaErro.show()
        telaErro.label.setText(" Codigo invalido, tente novamente")


def adicionais_brotinho():
    try:
        global valorTotal

        tel = telaPrincipal.telefone.text() or 1
        sql = ("select id from cadastro_cliente where telefone = %s" % tel)
        cursor.execute(sql)
        dados0 = cursor.fetchall()
        id_cliente = dados0[0][0]

        cursor.execute("select max(id) from temp_inteiro")
        dados1 = cursor.fetchall()
        if dados1 != ((None,),):
            id_inteiro = dados1[0][0]

        cursor.execute("select max(id) from temp_metade1")
        dados3 = cursor.fetchall()

        if dados3 != ((None,),):
            id_metade = dados3[0][0]

        sql5 = "select * from adcBroto"
        cursor.execute(sql5)
        dados5 = cursor.fetchall()

        chebox_isChecked_adicionais.isChecked(telaAdicionais, dados5)
        listaAdc, listaValor = chebox_isChecked_adicionais.isChecked(telaAdicionais, dados5)

        valorAdc = sum(listaValor)
        valorTotal = valorTotal + valorAdc

        if telaAdicionais.umSabor.isChecked():
            sql6 = "insert into temp_adc(tamanho, vazio1, adicional, " \
                   "valor, vazio2, vazio3, id_pizza, id_cliente, " \
                   "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert1 = (str(''), str(''), str(listaAdc[0][1]), str(listaAdc[0][3]),
                       str(''), str(''), str(id_inteiro), str(id_cliente), data)
            cursor.execute(sql6, insert1)
            banco10.commit()
            telaPrincipal.tableWidget_cadastro.clear()

        if telaAdicionais.doisSabores.isChecked():
            sql6 = "insert into temp_adc(tamanho, vazio1, adicional, " \
                   "valor, vazio2, vazio3, id_pizza, id_cliente, " \
                   "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert1 = (str(''), str(''), str(listaAdc[0][1]), str(listaAdc[0][3]),
                       str(''), str(''), str(id_metade), str(id_cliente), data)
            cursor.execute(sql6, insert1)
            banco10.commit()

        sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
        telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')

        setar_checkBox_false.checkBox_tela_adicionais_com(telaAdicionais)

    except pymysql.err.DataError:
        valorTotal = valorTotal - valorAdc
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione uma pizza")
    except:
        valorTotal = valorTotal - valorAdc
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione um adicional")


def adicionais_pizza_seis_pedacos():
    try:
        global valorTotal

        tel = telaPrincipal.telefone.text() or 1
        sql = ("select id from cadastro_cliente where telefone = %s" % tel)
        cursor.execute(sql)
        dados0 = cursor.fetchall()
        id_cliente = dados0[0][0]

        cursor.execute("select max(id) from temp_inteiro")
        dados1 = cursor.fetchall()
        if dados1 != ((None,),):
            id_inteiro = dados1[0][0]

        cursor.execute("select max(id) from temp_metade1")
        dados3 = cursor.fetchall()

        if dados3 != ((None,),):
            id_metade = dados3[0][0]

        sql5 = "select * from adcSeis"
        cursor.execute(sql5)
        dados5 = cursor.fetchall()

        chebox_isChecked_adicionais.isChecked(telaAdicionais, dados5)
        listaAdc, listaValor = chebox_isChecked_adicionais.isChecked(telaAdicionais, dados5)

        valorAdc = sum(listaValor)
        valorTotal = valorTotal + valorAdc

        if telaAdicionais.umSabor.isChecked():
            sql6 = "insert into temp_adc(tamanho, vazio1, adicional, " \
                   "valor, vazio2, vazio3, id_pizza, id_cliente, " \
                   "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert1 = (str(''), str(''), str(listaAdc[0][1]), str(listaAdc[0][3]),
                       str(''), str(''), str(id_inteiro), str(id_cliente), data)
            cursor.execute(sql6, insert1)
            banco10.commit()
            telaPrincipal.tableWidget_cadastro.clear()

        if telaAdicionais.doisSabores.isChecked():
            sql6 = "insert into temp_adc(tamanho, vazio1, adicional, " \
                   "valor, vazio2, vazio3, id_pizza, id_cliente, " \
                   "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert1 = (str(''), str(''), str(listaAdc[0][1]), str(listaAdc[0][3]),
                       str(''), str(''), str(id_metade), str(id_cliente), data)
            cursor.execute(sql6, insert1)
            banco10.commit()

        sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
        telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')
        setar_checkBox_false.checkBox_tela_adicionais_com(telaAdicionais)

    except pymysql.err.DataError:
        valorTotal = valorTotal - valorAdc
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione uma pizza")
    except:
        valorTotal = valorTotal - valorAdc
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione um adicional")


def adicionais_pizza_oito_pedacos():
    try:
        global valorTotal

        tel = telaPrincipal.telefone.text() or 1
        sql = ("select id from cadastro_cliente where telefone = %s" % tel)
        cursor.execute(sql)
        dados0 = cursor.fetchall()
        id_cliente = dados0[0][0]

        cursor.execute("select max(id) from temp_inteiro")
        dados1 = cursor.fetchall()
        if dados1 != ((None,),):
            id_inteiro = dados1[0][0]

        cursor.execute("select max(id) from temp_metade1")
        dados3 = cursor.fetchall()
        if dados3 != ((None,),):
            id_metade = dados3[0][0]

        cursor.execute("select max(id) from temp_terco1")
        dados4 = cursor.fetchall()
        if dados4 != ((None,),):
            id_terco = dados4[0][0]

        sql5 = "select * from adcOito"
        cursor.execute(sql5)
        dados5 = cursor.fetchall()

        chebox_isChecked_adicionais.isChecked(telaAdicionais, dados5)
        listaAdc, listaValor = chebox_isChecked_adicionais.isChecked(telaAdicionais, dados5)

        valorAdc = sum(listaValor)
        valorTotal = valorTotal + valorAdc

        if telaAdicionais.umSabor.isChecked():
            sql6 = "insert into temp_adc(tamanho, vazio1, adicional, " \
                   "valor, vazio2, vazio3, id_pizza, id_cliente, " \
                   "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert1 = (str(''), str(''), str(listaAdc[0][1]), str(listaAdc[0][3]),
                       str(''), str(''), str(id_inteiro), str(id_cliente), data)
            cursor.execute(sql6, insert1)
            banco10.commit()

        if telaAdicionais.doisSabores.isChecked():
            sql6 = "insert into temp_adc(tamanho, vazio1, adicional, " \
                   "valor, vazio2, vazio3, id_pizza, id_cliente, " \
                   "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert1 = (str(''), str(''), str(listaAdc[0][1]), str(listaAdc[0][3]),
                       str(''), str(''), str(id_metade), str(id_cliente), data)
            cursor.execute(sql6, insert1)
            banco10.commit()

        if telaAdicionais.tresSabores.isChecked():
            sql6 = "insert into temp_adc(tamanho, vazio1, adicional, " \
                   "valor, vazio2, vazio3, id_pizza, id_cliente, " \
                   "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert1 = (str(''), str(''), str(listaAdc[0][1]), str(listaAdc[0][3]),
                       str(''), str(''), str(id_terco), str(id_cliente), data)
            cursor.execute(sql6, insert1)
            banco10.commit()

        telaPrincipal.tableWidget_cadastro.clear()

        sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
        telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')
        setar_checkBox_false.checkBox_tela_adicionais_com(telaAdicionais)

    except pymysql.err.DataError:
        valorTotal = valorTotal - valorAdc
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione uma pizza")
    except:
        valorTotal = valorTotal - valorAdc
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione um adicional")


def adicionais_pizza_dez_pedacos():
    try:
        global valorTotal

        tel = telaPrincipal.telefone.text() or 1
        sql = ("select id from cadastro_cliente where telefone = %s" % tel)
        cursor.execute(sql)
        dados0 = cursor.fetchall()
        id_cliente = dados0[0][0]

        cursor.execute("select max(id) from temp_inteiro")
        dados1 = cursor.fetchall()
        if dados1 != ((None,),):
            id_inteiro = dados1[0][0]

        cursor.execute("select max(id) from temp_metade1")
        dados3 = cursor.fetchall()
        if dados3 != ((None,),):
            id_metade = dados3[0][0]

        cursor.execute("select max(id) from temp_terco1")
        dados4 = cursor.fetchall()
        if dados4 != ((None,),):
            id_terco = dados4[0][0]

        cursor.execute("select max(id) from temp_quarto1")
        dados5 = cursor.fetchall()
        if dados5 != ((None,),):
            id_quarto = dados5[0][0]

        sql5 = "select * from adcDez"
        cursor.execute(sql5)
        dados5 = cursor.fetchall()

        chebox_isChecked_adicionais.isChecked(telaAdicionais, dados5)
        listaAdc, listaValor = chebox_isChecked_adicionais.isChecked(telaAdicionais, dados5)

        valorAdc = sum(listaValor)
        valorTotal = valorTotal + valorAdc

        if telaAdicionais.umSabor.isChecked():
            sql6 = "insert into temp_adc(tamanho, vazio1, adicional, " \
                   "valor, vazio2, vazio3, id_pizza, id_cliente, " \
                   "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert1 = (str(''), str(''), str(listaAdc[0][1]), str(listaAdc[0][3]),
                       str(''), str(''), str(id_inteiro), str(id_cliente), data)
            cursor.execute(sql6, insert1)
            banco10.commit()

        if telaAdicionais.doisSabores.isChecked():
            sql6 = "insert into temp_adc(tamanho, vazio1, adicional, " \
                   "valor, vazio2, vazio3, id_pizza, id_cliente, " \
                   "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert1 = (str(''), str(''), str(listaAdc[0][1]), str(listaAdc[0][3]),
                       str(''), str(''), str(id_metade), str(id_cliente), data)
            cursor.execute(sql6, insert1)
            banco10.commit()

        if telaAdicionais.tresSabores.isChecked():
            sql6 = "insert into temp_adc(tamanho, vazio1, adicional, " \
                   "valor, vazio2, vazio3, id_pizza, id_cliente, " \
                   "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert1 = (str(''), str(''), str(listaAdc[0][1]), str(listaAdc[0][3]),
                       str(''), str(''), str(id_terco), str(id_cliente), data)
            cursor.execute(sql6, insert1)
            banco10.commit()

        if telaAdicionais.quatroSabores.isChecked():
            sql6 = "insert into temp_adc(tamanho, vazio1, adicional, " \
                   "valor, vazio2, vazio3, id_pizza, id_cliente, " \
                   "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert1 = (str(''), str(''), str(listaAdc[0][1]), str(listaAdc[0][3]),
                       str(''), str(''), str(id_quarto), str(id_cliente), data)
            cursor.execute(sql6, insert1)
            banco10.commit()

        telaPrincipal.tableWidget_cadastro.clear()

        sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
        telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')
        setar_checkBox_false.checkBox_tela_adicionais_com(telaAdicionais)

    except pymysql.err.DataError:
        valorTotal = valorTotal - valorAdc
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione uma pizza")
    except:
        valorTotal = valorTotal - valorAdc
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione um adicional")


def esfihas():
    try:
        global valorTotal
        quantidade = int(telaPrincipal.spinBox_2.text())

        tel = telaPrincipal.telefone.text() or 1
        sql = ("select id from cadastro_cliente where telefone = %s" % tel)
        cursor.execute(sql)
        dados0 = cursor.fetchall()
        id = dados0[0][0]

        sql1 = "select sabor, tamanho, valorProduto from esfihas"
        cursor.execute(sql1)
        dados = cursor.fetchall()

        checkBox_isChecked_esfiha.isChecked(telaPrincipal, dados)
        listaTemp, valorProduto = checkBox_isChecked_esfiha.isChecked(telaPrincipal, dados)

        for i in valorProduto:
            valor = i

        soma = quantidade * float(valor)
        sql2 = "insert into temp_esfihas(tamanho, parte, sabor, valorProduto, " \
               "quantidade, subtotal, id_cliente, dataa) " \
               "values(%s, %s, %s, %s, %s, %s, %s, %s)"
        insert2 = (str(listaTemp[0][1]), str(''), str(listaTemp[0][0]),
                   str(listaTemp[0][2]), str(quantidade), str(soma), str(id), data)
        cursor.execute(sql2, insert2)
        banco10.commit()

        telaPrincipal.tableWidget_cadastro.clear()

        valorTotal = valorTotal + soma
        sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
        telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')
        setar_checkBox_false.checkBox_tela_pedidos_esfiha(telaPrincipal)

    except IndexError:
        telaErro.show()
        telaErro.label.setText("Erro! Voce precisa salvar o contato")
    except:
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione um produto")


def refriLata():
    try:
        global valorTotal
        quantidade = int(telaPrincipal.spinBox_3.text())

        tel = telaPrincipal.telefone.text() or 1
        sql = ("select id from cadastro_cliente where telefone = %s" % tel)
        cursor.execute(sql)
        dados0 = cursor.fetchall()
        id = dados0[0][0]

        sql1 = "select bebida, tamanho, valor from lata"
        cursor.execute(sql1)
        dados = cursor.fetchall()

        checkBox_isChecked_bebidas.isChecked(telaPrincipal, dados)
        listaTemp, valorProduto = checkBox_isChecked_bebidas.isChecked(telaPrincipal, dados)

        for i in valorProduto:
            valor = i

        soma = quantidade * float(valor)
        sql2 = "insert into temp_lata(tamanho, parte, sabor, " \
               "valorProduto, quantidade, subtotal, id_cliente, " \
               "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s)"
        insert2 = (str(listaTemp[0][1]), str(''), str(listaTemp[0][0]),
                   str(listaTemp[0][2]), str(quantidade), str(soma),
                   str(id), data)
        cursor.execute(sql2, insert2)
        banco10.commit()

        telaPrincipal.tableWidget_cadastro.clear()
        valorTotal = valorTotal + soma
        sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
        telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')
        setar_checkBox_false.checkBox_tela_pedidos_refrigerante(telaPrincipal)

    except IndexError:
        telaErro.show()
        telaErro.label.setText("Erro! Voce precisa salvar o contato")
    except:
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione um produto")


def refri600():
    try:
        global valorTotal

        quantidade = int(telaPrincipal.spinBox_3.text())

        tel = telaPrincipal.telefone.text() or 1
        sql = ("select id from cadastro_cliente where telefone = %s" % tel)
        cursor.execute(sql)
        dados0 = cursor.fetchall()
        id = dados0[0][0]

        sql1 = "select bebida, tamanho, valor from s600"
        cursor.execute(sql1)
        dados = cursor.fetchall()

        checkBox_isChecked_bebidas.isChecked(telaPrincipal, dados)
        listaTemp, valorProduto = checkBox_isChecked_bebidas.isChecked(telaPrincipal, dados)

        for i in valorProduto:
            valor = i

        soma = quantidade * float(valor)
        sql2 = "insert into temp_600(tamanho, parte, sabor, " \
               "valorProduto, quantidade, subtotal, id_cliente, " \
               "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s)"
        insert2 = (str(listaTemp[0][1]), str(''), str(listaTemp[0][0]),
                   str(listaTemp[0][2]), str(quantidade), str(soma),
                   str(id), data)
        cursor.execute(sql2, insert2)
        banco10.commit()

        telaPrincipal.tableWidget_cadastro.clear()

        valorTotal = valorTotal + soma
        sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
        telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')
        setar_checkBox_false.checkBox_tela_pedidos_refrigerante(telaPrincipal)

    except IndexError:
        telaErro.show()
        telaErro.label.setText("Erro! Voce precisa salvar o contato")
    except:
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione um produto")


def refri1l():
    try:
        global valorTotal

        quantidade = int(telaPrincipal.spinBox_3.text())

        tel = telaPrincipal.telefone.text() or 1
        sql = ("select id from cadastro_cliente where telefone = %s" % tel)
        cursor.execute(sql)
        dados0 = cursor.fetchall()
        id = dados0[0][0]

        sql1 = "select bebida, tamanho, valor from umLitro"
        cursor.execute(sql1)
        dados = cursor.fetchall()

        checkBox_isChecked_bebidas.isChecked(telaPrincipal, dados)
        listaTemp, valorProduto = checkBox_isChecked_bebidas.isChecked(telaPrincipal, dados)

        for i in valorProduto:
            valor = i

        soma = quantidade * float(valor)
        sql2 = "insert into temp_1L(tamanho, parte, sabor, " \
               "valorProduto, quantidade, subtotal, id_cliente, " \
               "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s)"
        insert2 = (str(listaTemp[0][1]), str(''), str(listaTemp[0][0]),
                   str(listaTemp[0][2]), str(quantidade), str(soma),
                   str(id), data)
        cursor.execute(sql2, insert2)
        banco10.commit()

        telaPrincipal.tableWidget_cadastro.clear()
        valorTotal = valorTotal + soma
        sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
        telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')
        setar_checkBox_false.checkBox_tela_pedidos_refrigerante(telaPrincipal)

    except IndexError:
        telaErro.show()
        telaErro.label.setText("Erro! Voce precisa salvar o contato")
    except:
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione um produto")


def refri1meio():
    try:
        global valorTotal

        quantidade = int(telaPrincipal.spinBox_3.text())

        tel = telaPrincipal.telefone.text() or 1
        sql = ("select id from cadastro_cliente where telefone = %s" % tel)
        cursor.execute(sql)
        dados0 = cursor.fetchall()
        id = dados0[0][0]

        sql1 = "select bebida, tamanho, valor from umEmeio"
        cursor.execute(sql1)
        dados = cursor.fetchall()

        checkBox_isChecked_bebidas.isChecked(telaPrincipal, dados)
        listaTemp, valorProduto = checkBox_isChecked_bebidas.isChecked(telaPrincipal, dados)

        for i in valorProduto:
            valor = i

        soma = quantidade * float(valor)
        sql2 = "insert into temp_1Lmeio(tamanho, parte, sabor, " \
               "valorProduto, quantidade, subtotal, id_cliente, " \
               "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s)"
        insert2 = (str(listaTemp[0][1]), str(''), str(listaTemp[0][0]),
                   str(listaTemp[0][2]), str(quantidade), str(soma),
                   str(id), data)
        cursor.execute(sql2, insert2)
        banco10.commit()

        telaPrincipal.tableWidget_cadastro.clear()
        valorTotal = valorTotal + soma
        sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
        telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')
        setar_checkBox_false.checkBox_tela_pedidos_refrigerante(telaPrincipal)

    except IndexError:
        telaErro.show()
        telaErro.label.setText("Erro! Voce precisa salvar o contato")
    except:
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione um produto")


def refri2L():
    try:
        global valorTotal

        quantidade = int(telaPrincipal.spinBox_3.text())

        tel = telaPrincipal.telefone.text() or 1
        sql = ("select id from cadastro_cliente where telefone = %s" % tel)
        cursor.execute(sql)
        dados0 = cursor.fetchall()
        id = dados0[0][0]

        sql1 = "select bebida, tamanho, valor from doisLitros"
        cursor.execute(sql1)
        dados = cursor.fetchall()

        checkBox_isChecked_bebidas.isChecked(telaPrincipal, dados)
        listaTemp, valorProduto = checkBox_isChecked_bebidas.isChecked(telaPrincipal, dados)

        for i in valorProduto:
            valor = i

        soma = quantidade * float(valor)
        sql2 = "insert into temp_2L(tamanho, parte, sabor, " \
               "valorProduto, quantidade, subtotal, id_cliente, " \
               "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s)"
        insert2 = (str(listaTemp[0][1]), str(''), str(listaTemp[0][0]),
                   str(listaTemp[0][2]), str(quantidade), str(soma),
                   str(id), data)
        cursor.execute(sql2, insert2)
        banco10.commit()

        telaPrincipal.tableWidget_cadastro.clear()
        valorTotal = valorTotal + soma
        sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
        telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')
        setar_checkBox_false.checkBox_tela_pedidos_refrigerante(telaPrincipal)

    except IndexError:
        telaErro.show()
        telaErro.label.setText("Erro! Voce precisa salvar o contato")
    except:
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione um produto")


def refri2meio():
    try:
        global valorTotal

        quantidade = int(telaPrincipal.spinBox_3.text())

        tel = telaPrincipal.telefone.text() or 1
        sql = ("select id from cadastro_cliente where telefone = %s" % tel)
        cursor.execute(sql)
        dados0 = cursor.fetchall()
        id = dados0[0][0]

        sql1 = "select bebida, tamanho, valor from doisEmeio"
        cursor.execute(sql1)
        dados = cursor.fetchall()

        checkBox_isChecked_bebidas.isChecked(telaPrincipal, dados)
        listaTemp, valorProduto = checkBox_isChecked_bebidas.isChecked(telaPrincipal, dados)

        for i in valorProduto:
            valor = i

        soma = quantidade * float(valor)
        sql2 = "insert into temp_2Lmeio(tamanho, parte, sabor, " \
               "valorProduto, quantidade, subtotal, id_cliente, " \
               "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s)"
        insert2 = (str(listaTemp[0][1]), str(''), str(listaTemp[0][0]),
                   str(listaTemp[0][2]), str(quantidade), str(soma),
                   str(id), data)
        cursor.execute(sql2, insert2)
        banco10.commit()

        telaPrincipal.tableWidget_cadastro.clear()
        valorTotal = valorTotal + soma
        sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
        telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')
        setar_checkBox_false.checkBox_tela_pedidos_refrigerante(telaPrincipal)

    except IndexError:
        telaErro.show()
        telaErro.label.setText("Erro! Voce precisa salvar o contato")
    except:
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione um produto")


def outros():
    try:
        global valorTotal

        quantidade = int(telaPrincipal.spinBox_4.text())

        tel = telaPrincipal.telefone.text() or 1
        sql = ("select id from cadastro_cliente where telefone = %s" % tel)
        cursor.execute(sql)
        dados0 = cursor.fetchall()
        id = dados0[0][0]

        sql1 = "select produto, tipo, valor from outros"
        cursor.execute(sql1)
        dados = cursor.fetchall()

        checkBox_isChecked_outros.isChecked(telaPrincipal, dados)
        listaTemp, valorProduto = checkBox_isChecked_outros.isChecked(telaPrincipal, dados)

        for i in valorProduto:
            valor = i

        soma = quantidade * float(valor)
        sql2 = "insert into temp_outros(tamanho, parte, sabor, " \
               "valorProduto, quantidade, subtotal, id_cliente, " \
               "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s)"
        insert2 = (str(listaTemp[0][1]), str(''), str(listaTemp[0][0]),
                   str(listaTemp[0][2]), str(quantidade), str(soma),
                   str(id), data)
        cursor.execute(sql2, insert2)
        banco10.commit()

        telaPrincipal.tableWidget_cadastro.clear()

        valorTotal = valorTotal + soma
        sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
        telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')
        setar_checkBox_false.checkBox_tela_pedidos_outros(telaPrincipal)

    except IndexError:
        telaErro.show()
        telaErro.label.setText("Erro! Voce precisa salvar o contato")
    except:
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione um produto")


def pizzaOito():
    try:
        global valorTotal

        quantidade = int(telaPrincipal.spinBox.text())

        tel = telaPrincipal.telefone.text() or 1
        sql = ("select id from cadastro_cliente where telefone = %s" % tel)
        cursor.execute(sql)
        dados0 = cursor.fetchall()

        id = dados0[0][0]

        sql1 = "select sabor, tamanho, valorProduto from oitoPedacos"
        cursor.execute(sql1)
        dados = cursor.fetchall()

        checkBox_isChecked_pizzas.isChecked(telaPrincipal, dados)
        listaTemp, valorProduto = checkBox_isChecked_pizzas.isChecked(telaPrincipal, dados)

        valor = max(valorProduto)

        if len(listaTemp) == 1:
            partes = '1/1'
            soma = quantidade * float(valor)
            sql2 = "insert into temp_inteiro(tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal, id_cliente, " \
                   "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s)"
            insert2 = (str(listaTemp[0][1]), str(partes), str(listaTemp[0][0]),
                       str(listaTemp[0][2]), str(quantidade), str(soma),
                       str(id), data)
            cursor.execute(sql2, insert2)
            banco10.commit()

            telaPrincipal.tableWidget_cadastro.clear()

            valorTotal = valorTotal + soma

            sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)

            telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')

        elif len(listaTemp) == 2:
            partes = '1/2'
            soma = quantidade * float(valor)
            sql4 = "insert into temp_metade1(tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal, id_cliente, " \
                   "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s)"
            insert4 = (str(listaTemp[0][1]), str(partes), str(listaTemp[0][0]),
                       str(listaTemp[0][2]), str(''), str(''),
                       str(id), data)
            cursor.execute(sql4, insert4)
            banco10.commit()

            sql5 = "insert into temp_metade2(tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal) " \
                   "values (%s, %s, %s, %s, %s, %s)"
            insert5 = (str(''), str(partes), str(listaTemp[1][0]),
                       str(listaTemp[1][2]), str(quantidade), str(soma))
            cursor.execute(sql5, insert5)
            banco10.commit()

            telaPrincipal.tableWidget_cadastro.clear()
            valorTotal = valorTotal + soma

            sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)

            telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')

        else:
            partes = '1/3'
            soma = quantidade * float(valor)
            sql = "insert into temp_terco1(tamanho, parte, sabor, " \
                  "valorProduto, quantidade, subtotal, id_cliente, " \
                  "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s)"
            insert = (str(listaTemp[0][1]), str(partes), str(listaTemp[0][0]),
                      str(listaTemp[0][2]), str(''), str(''),
                      str(id), data)
            cursor.execute(sql, insert)

            sql2 = "insert into temp_terco2(tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal) " \
                   "values (%s, %s, %s, %s, %s, %s)"
            insert2 = (str('    '), str(partes), str(listaTemp[1][0]),
                       str(listaTemp[1][2]), str(''), str(''))
            cursor.execute(sql2, insert2)
            banco10.commit()

            sql3 = "insert into temp_terco3(tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal) " \
                   "values (%s, %s, %s, %s, %s, %s)"
            insert3 = (str('    '), str(partes), str(listaTemp[2][0]),
                       str(listaTemp[2][2]), str(quantidade), str(soma))
            cursor.execute(sql3, insert3)
            banco10.commit()

            telaPrincipal.tableWidget_cadastro.clear()
            valorTotal = valorTotal + soma
            sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
            telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')

        setar_checkBox_false.checkBox_tela_pedidos_pizzas(telaPrincipal)

    except IndexError:
        telaErro.show()
        telaErro.label.setText("Erro! Voce precisa salvar o contato")
    except:
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione um produto")


def pizzaDez():
    try:
        global valorTotal

        tel = telaPrincipal.telefone.text() or 1
        sql = ("select id from cadastro_cliente where telefone = %s" % tel)
        cursor.execute(sql)
        dados0 = cursor.fetchall()
        id = dados0[0][0]

        quantidade = int(telaPrincipal.spinBox.text())
        sql = "select sabor, tamanho, valorProduto from dezPedacos"
        cursor.execute(sql)
        dados = cursor.fetchall()

        checkBox_isChecked_pizzas.isChecked(telaPrincipal, dados)
        listaTemp, valorProduto = checkBox_isChecked_pizzas.isChecked(telaPrincipal, dados)

        valor = max(valorProduto)

        if len(listaTemp) == 1:
            partes = '1/1'
            soma = quantidade * float(valor)
            sql2 = "insert into temp_inteiro(tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal, id_cliente, " \
                   "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s)"
            insert2 = (str(listaTemp[0][1]), str(partes), str(listaTemp[0][0]),
                       str(listaTemp[0][2]), str(quantidade),
                       str(soma), str(id), data)
            cursor.execute(sql2, insert2)
            banco10.commit()

            telaPrincipal.tableWidget_cadastro.clear()
            valorTotal = valorTotal + soma
            sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
            telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')

        elif len(listaTemp) == 2:
            partes = '1/2'
            soma = quantidade * float(valor)
            sql4 = "insert into temp_metade1(tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal, id_cliente, " \
                   "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s)"
            insert4 = (str(listaTemp[0][1]), str(partes), str(listaTemp[0][0]),
                       str(listaTemp[0][2]), str(''), str(''), str(id), data)
            cursor.execute(sql4, insert4)
            banco10.commit()

            sql5 = "insert into temp_metade2(tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal) " \
                   "values (%s, %s, %s, %s, %s, %s)"
            insert5 = (str('   '), str(partes), str(listaTemp[1][0]),
                       str(listaTemp[1][2]), str(quantidade), str(soma))
            cursor.execute(sql5, insert5)
            banco10.commit()

            telaPrincipal.tableWidget_cadastro.clear()
            valorTotal = valorTotal + soma
            sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
            telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')

        elif len(listaTemp) == 3:
            partes = '1/3'
            soma = quantidade * float(valor)
            sql = "insert into temp_terco1(tamanho, parte, sabor, " \
                  "valorProduto, quantidade, subtotal, id_cliente, " \
                  "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s)"
            insert = (str(listaTemp[0][1]), str(partes), str(listaTemp[0][0]),
                      str(listaTemp[0][2]), str(''),
                      str(''), str(id), data)
            cursor.execute(sql, insert)

            sql2 = "insert into temp_terco2(tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal) " \
                   "values (%s, %s, %s, %s, %s, %s)"
            insert2 = (str('   '), str(partes), str(listaTemp[1][0]),
                       str(listaTemp[1][2]), str(''), str(''))
            cursor.execute(sql2, insert2)
            banco10.commit()

            sql3 = "insert into temp_terco3(tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal) " \
                   "values (%s, %s, %s, %s, %s, %s)"
            insert3 = (str('   '), str(partes), str(listaTemp[2][0]),
                       str(listaTemp[2][2]), str(quantidade), str(soma))
            cursor.execute(sql3, insert3)
            banco10.commit()

            telaPrincipal.tableWidget_cadastro.clear()
            valorTotal = valorTotal + soma
            sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
            telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')

        else:
            partes = '1/4'
            soma = quantidade * float(valor)

            sql = "insert into temp_quarto1(tamanho, parte, sabor, " \
                  "valorProduto, quantidade, subtotal, id_cliente, " \
                  "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s)"
            insert = (str(listaTemp[0][1]), str(partes), str(listaTemp[0][0]),
                      str(listaTemp[0][2]), str(''), str(''), str(id), data)
            cursor.execute(sql, insert)

            sql2 = "insert into temp_quarto2(tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal) " \
                   "values (%s, %s, %s, %s, %s, %s)"
            insert2 = (str('   '), str(partes), str(listaTemp[1][0]),
                       str(listaTemp[1][2]), str(''), str(''))
            cursor.execute(sql2, insert2)
            banco10.commit()

            sql3 = "insert into temp_quarto3(tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal) " \
                   "values (%s, %s, %s, %s, %s, %s)"
            insert3 = (str('   '), str(partes), str(listaTemp[2][0]),
                       str(listaTemp[2][2]), str(''), str(''))
            cursor.execute(sql3, insert3)
            banco10.commit()

            sql4 = "insert into temp_quarto4(tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal) " \
                   "values (%s, %s, %s, %s, %s, %s)"
            insert4 = (str('   '), str(partes), str(listaTemp[3][0]),
                       str(listaTemp[3][2]), str(quantidade), str(soma))
            cursor.execute(sql4, insert4)
            banco10.commit()

            telaPrincipal.tableWidget_cadastro.clear()

            valorTotal = valorTotal + soma
            sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
            telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')

        setar_checkBox_false.checkBox_tela_pedidos_pizzas(telaPrincipal)
    except IndexError:
        telaErro.show()
        telaErro.label.setText("Erro! Voce precisa salvar o contato")
    except:
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione um produto")


def pizzaSeis():
    try:
        quantidade = int(telaPrincipal.spinBox.text())
        global valorTotal

        tel = telaPrincipal.telefone.text() or 1
        sql = ("select id from cadastro_cliente where telefone = %s" % tel)
        cursor.execute(sql)
        dados0 = cursor.fetchall()
        id = dados0[0][0]

        sql1 = "select sabor, tamanho, valorProduto from seisPedacos"
        cursor.execute(sql1)
        dados = cursor.fetchall()

        checkBox_isChecked_pizzas.isChecked(telaPrincipal, dados)
        listaTemp, valorProduto = checkBox_isChecked_pizzas.isChecked(telaPrincipal, dados)

        valor = max(valorProduto)

        if len(listaTemp) == 1:
            partes = '1/1'
            soma = quantidade * float(valor)
            sql2 = "insert into temp_inteiro(tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal, id_cliente, " \
                   "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s)"
            insert2 = (str(listaTemp[0][1]), str(partes), str(listaTemp[0][0]),
                       str(listaTemp[0][2]), str(quantidade),
                       str(soma), str(id), data)
            cursor.execute(sql2, insert2)
            banco10.commit()

            telaPrincipal.tableWidget_cadastro.clear()
            valorTotal = valorTotal + soma
            sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
            telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')

        else:
            partes = '1/2'
            soma = quantidade * float(valor)
            sql4 = "insert into temp_metade1(tamanho, parte, sabor, valorProduto, " \
                   "quantidade, subtotal, id_cliente, dataa) " \
                   "values(%s, %s, %s, %s, %s, %s, %s, %s)"
            insert4 = (str(listaTemp[0][1]), str(partes), str(listaTemp[0][0]),
                       str(listaTemp[0][2]), str(''), str(''),
                       str(id), data)
            cursor.execute(sql4, insert4)
            banco10.commit()

            sql5 = "insert into temp_metade2(tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal) " \
                   "values (%s, %s, %s, %s, %s, %s)"
            insert5 = (str('    '), str(partes), str(listaTemp[1][0]),
                       str(listaTemp[1][2]), str(quantidade), str(soma))
            cursor.execute(sql5, insert5)
            banco10.commit()

            telaPrincipal.tableWidget_cadastro.clear()
            valorTotal = valorTotal + soma
            sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
            telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')

        setar_checkBox_false.checkBox_tela_pedidos_pizzas(telaPrincipal)

    except IndexError:
        telaErro.show()
        telaErro.label.setText("Erro! Voce precisa salvar o contato")
    except:
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione um produto")


def pizzaBroto():
    try:
        global valorTotal

        tel = telaPrincipal.telefone.text() or 1
        sql0 = ("select id from cadastro_cliente where telefone = %s" % tel)
        cursor.execute(sql0)
        dados0 = cursor.fetchall()
        id = dados0[0][0]

        quantidade = int(telaPrincipal.spinBox.text())
        sql1 = "select sabor, tamanho, valorProduto from broto"
        cursor.execute(sql1)
        dados = cursor.fetchall()

        checkBox_isChecked_pizzas.isChecked(telaPrincipal, dados)
        listaTemp, valorProduto = checkBox_isChecked_pizzas.isChecked(telaPrincipal, dados)

        valor = max(valorProduto)

        if len(listaTemp) == 1:
            partes = '1/1'
            soma = quantidade * float(valor)
            sql2 = "insert into temp_inteiro(tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal, id_cliente, " \
                   "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s)"
            insert2 = (str('Quatro'), str(partes), str(listaTemp[0][0]),
                       str(listaTemp[0][2]), str(quantidade),
                       str(soma), str(id), data)
            cursor.execute(sql2, insert2)
            banco10.commit()

            telaPrincipal.tableWidget_cadastro.clear()
            valorTotal = valorTotal + soma
            sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
            telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')

        else:
            partes = '1/2'
            soma = quantidade * float(valor)
            sql4 = "insert into temp_metade1(tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal, id_cliente, " \
                   "dataa) values(%s, %s, %s, %s, %s, %s, %s, %s)"
            insert4 = (str('Quatro'), str(partes), str(listaTemp[0][0]),
                       str(listaTemp[0][2]), str(''), str(''),
                       str(id), data)
            cursor.execute(sql4, insert4)
            banco10.commit()

            sql5 = "insert into temp_metade2(tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal) " \
                   "values (%s, %s, %s, %s, %s, %s)"
            insert5 = (str('     '), str(partes), str(listaTemp[1][0]),
                       str(listaTemp[1][2]), str(quantidade), str(soma))
            cursor.execute(sql5, insert5)
            banco10.commit()

            telaPrincipal.tableWidget_cadastro.clear()
            valorTotal = valorTotal + soma
            sql_tela_pedido.sql(telaPrincipal, cursor, QtWidgets)
            telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')

        setar_checkBox_false.checkBox_tela_pedidos_pizzas(telaPrincipal)

    except IndexError:
        telaErro.show()
        telaErro.label.setText("Erro! Voce precisa salvar o contato")
    except:
        telaErro.show()
        telaErro.label.setText("      Erro! Selecione um produto")

def encerrar_sistema():
    lista = [primeiraTela, telaPrincipal, telaProduto, telaPedido, telaConfirmacao,
             telaLogin, telaPizza, telaConfirmarPedido, telaAdicionais,
             telaBebida, telaErro, telaInfoPedido, telaDespachar, telaCancelar, telaImprimir,
             telaFinalizar, telaDevedores, telaDevedores2, telaFinalizarDeve, telaAtualizarProdutos,
             telaExcluirBebidas,
             telaAtualizarBebidas, telaCaixa, telaCalendario, telaCalendario2, telaPeriodo, telaMensal,
             telafechamento,
             telaSecundaria]
    for i in lista:
        i.hide()

def funcao_desconto():
    try:
        global valorTotal

        desconto = float(telaPrincipal.desconto.text())

        valorTotal = valorTotal - desconto

        telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')

    except:
        telaErro.show()
        telaErro.label.setText('          Erro, tente novamente!')

def funcao_acrescimo():
    try:
        global valorTotal

        acrescimo = float(telaPrincipal.acrescimo.text())

        valorTotal = valorTotal + acrescimo

        telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')

    except:
        telaErro.show()
        telaErro.label.setText('          Erro, tente novamente!')

def tela_limpa_campos_preenchidos():
    telafechamento.show()
    lista = [telaCaixa2.inicioCx, telaCaixa2.terminoCx,
             telaCaixa2.retirada, telaCartao.lineCartao1,
             telaCartao.lineCartao2,telaCartao.lineCartao3,
             telaCartao.lineCartao4, telaCartao.lineCartao5,
             telaCartao.lineCartao6,telaCartao.lineCartao7,
             telaCartao.lineCartao8, telaMotoboy.lineBoy1,
             telaMotoboy.lineBoy2, telaMotoboy.lineBoy3,
             telaMotoboy.lineBoy4,telaMotoboy.lineBoy5,
             telaMotoboy.lineBoy6, telaTerminais.terminal1,
             telaTerminais.terminal2, telaTerminais.terminal3,
             telaTerminais.terminal4, telaIfood.online,
             telaIfood.total, telaPagamento.pagamento1,
             telaPagamento.pagamento2,telaPagamento.pagamento3,
             telaPagamento.pagamento4, telaPagamento.pagamento5,
             telaPagamento.pagamento6,telaPagamento.pagamento7,
             telaPagamento.Fuvalor1, telaPagamento.Fuvalor2,
             telaPagamento.Fuvalor3, telaPagamento.Fuvalor4,
             telaPagamento.Fuvalor5,telaPagamento.Fuvalor6,
             telaPagamento.Fuvalor7, telaPizza.pizza1,
             telaPizza.pizza2, telaPizza.pizza3,
             telaPizza.pizza4,telaPizza.pizzaIfood,
             telaEsfiha.esfiha1, telaEsfiha.esfiha2,
             telaEsfiha.esfiha3, telaEsfiha.esfiha4]
    for i in lista:
        i.clear()

def funcao_salvar_fechamento():
    try:
        global data
        caixa, finalCx, retirada = inicio_termino_retirada_caixa.caixa(telaCaixa2, telaErro) or 0
        cartao = soma_venda_maquinhas_cartoes.somar(telaCartao, telaErro) or 0
        motoboy = soma_total_pagamento_motoboys.somar(telaMotoboy, telaErro) or 0

        terminal = soma_venda_terminais.somar(telaTerminais, telaErro) or 0

        ifoodOnline, ifoodTotal = calcular_venda_ifood.calcular(telaIfood, telaErro) or 0
        esfiha = somar_quantidade_esfihas_vendidas.somar(telaEsfiha, telaErro) or 0
        pizza = somar_quantidade_pizzas_vendidas.somar(telaPizza, telaErro) or 0
        pag, valor = calcular_pagamentos_diarios.calcular(telaPagamento, telaErro) or 0

        comando_sql1 = " insert into fechamento (dataVenda, inicio_caixa, retirada, " \
                       "final_caixa, motoboys, cartao, total_terminal, Ifood_online, " \
                       "total_Ifood, esfihas, pizzas, recebedor1, valor1, recebedor2, " \
                       "valor2, recebedor3, valor3, recebedor4, valor4, recebedor5, " \
                       "valor5, recebedor6, valor6, recebedor7, valor7) " \
                       "values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
                       "%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"

        dados1 = (data, str(caixa), str(retirada), str(finalCx),
                  str(motoboy), str(cartao), str(terminal), str(ifoodOnline),
                  str(ifoodTotal), str(esfiha), str(pizza), pag[0], str(valor[0]),
                  pag[1], str(valor[1]), pag[2], str(valor[2]), pag[3], str(valor[3]),
                  pag[4], str(valor[4]), pag[5], str(valor[5]), pag[6], str(valor[6]))

        cursor.execute(comando_sql1, dados1)
        banco10.commit()
    except:
        telaErro.show()
        telaErro.label.setText('  Erro, tente novamente!')

def utilizar_ultimo_pedido():
    try:
        listaPedido = []
        global data
        global valorTotal

        tel = telaPrincipal.telefone.text() or 1
        cursor.execute("select id from cadastro_cliente where telefone = %s" % tel)
        dados = cursor.fetchall()
        id = dados[0][0]

        cursor.execute("select max(id) from gerenciarPedido where telefone = %s" % tel)
        dados = cursor.fetchall()
        id_pedido = dados[0][0]

        cursor.execute("select valorTotal from gerenciarPedido where id = %s" % id_pedido)
        dados = cursor.fetchall()
        valor = float(dados[0][0])
        valorTotal = valorTotal + valor

        cursor.execute("select max(id) from per_inteiro where id_int = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_inteiro = dados[0][0]
        else:
            id_inteiro = 0

        cursor.execute("select id_int, tamanho, parte, sabor, "
                       "valorProduto, quantidade, subtotal "
                       "from per_inteiro where id = %s" % id_inteiro)
        inteiro = cursor.fetchall()

        if inteiro != ():
            sql = "insert into temp_inteiro(id, tamanho, parte, " \
                  "sabor, valorProduto, quantidade, subtotal, " \
                  "id_cliente, dataa) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert = (str(inteiro[0][0]), str(inteiro[0][1]),
                      str(inteiro[0][2]), str(inteiro[0][3]),
                      str(inteiro[0][4]), str(inteiro[0][5]),
                      str(inteiro[0][6]), str(id), str(data))
            cursor.execute(sql, insert)
            banco10.commit()

        cursor.execute("select max(id) from per_met1 where id_met = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_met1 = dados[0][0]
        else:
            id_met1 = 0

        cursor.execute("select max(id) from per_met2 where id_met2 = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_met2 = dados[0][0]
        else:
            id_met2 = 0

        cursor.execute("select id_met, tamanho, parte, sabor, "
                       "valorProduto, quantidade, subtotal "
                       "from per_met1 where id = %s" % id_met1)
        metade1 = cursor.fetchall()

        cursor.execute("select id_met2, tamanho, parte, sabor,"
                       "valorProduto, quantidade, subtotal "
                       "from per_met2 where id = %s" % id_met2)
        metade2 = cursor.fetchall()

        if metade1 != ():
            sql = "insert into temp_metade1(id, tamanho, parte, sabor, " \
                  "valorProduto, quantidade, subtotal, id_cliente, " \
                  "dataa) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert = (str(metade1[0][0]), str(metade1[0][1]),
                      str(metade1[0][2]), str(metade1[0][3]),
                      str(metade1[0][4]), str(metade1[0][5]),
                      str(metade1[0][6]), str(id), data)
            cursor.execute(sql, insert)
            banco10.commit()

            sql2 = "insert into temp_metade2(id, tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal) " \
                   "values (%s, %s, %s, %s, %s, %s, %s)"
            insert2 = (str(metade2[0][0]), str(metade2[0][1]),
                       str(metade2[0][2]), str(metade2[0][3]),
                       str(metade2[0][4]), str(metade2[0][5]),
                       str(metade2[0][6]))
            cursor.execute(sql2, insert2)
            banco10.commit()

        cursor.execute("select max(id) from per_terco1 where id_terco = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_terco1 = dados[0][0]
        else:
            id_terco1 = 0

        cursor.execute("select max(id) from per_terco2 where id_terco2 = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_terco2 = dados[0][0]
        else:
            id_terco2 = 0

        cursor.execute("select max(id) from per_terco3 where id_terco3 = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_terco3 = dados[0][0]
        else:
            id_terco3 = 0

        cursor.execute("select id_terco, tamanho, parte, sabor, "
                       "valorProduto, quantidade, subtotal "
                       "from per_terco1 where id = %s" % id_terco1)
        terco1 = cursor.fetchall()

        cursor.execute("select id_terco2, tamanho, parte, sabor, "
                       "valorProduto, quantidade, subtotal "
                       "from per_terco2 where id = %s" % id_terco2)
        terco2 = cursor.fetchall()

        cursor.execute("select id_terco3, tamanho, parte, sabor, "
                       "valorProduto, quantidade, subtotal "
                       "from per_terco3 where id = %s" % id_terco3)
        terco3 = cursor.fetchall()

        if terco1 != ():
            sql = "insert into temp_terco1(id, tamanho, parte, sabor, " \
                  "valorProduto, quantidade, subtotal, id_cliente, " \
                  "dataa) values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert = (str(terco1[0][0]), str(terco1[0][1]),
                      str(terco1[0][2]), str(terco1[0][3]),
                      str(terco1[0][4]), str(terco1[0][5]),
                      str(terco1[0][6]), str(id), data)
            cursor.execute(sql, insert)
            banco10.commit()

            sql2 = "insert into temp_terco2(id, tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal) " \
                   "values (%s, %s, %s, %s, %s, %s, %s)"
            insert2 = (str(terco2[0][0]), str(terco2[0][1]),
                       str(terco2[0][2]), str(terco2[0][3]),
                       str(terco2[0][4]), str(terco2[0][5]),
                       str(terco2[0][6]))
            cursor.execute(sql2, insert2)
            banco10.commit()

            sql3 = "insert into temp_terco3(id, tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal) " \
                   "values (%s, %s, %s, %s, %s, %s, %s)"
            insert3 = (str(terco3[0][0]), str(terco3[0][1]),
                       str(terco3[0][2]), str(terco3[0][3]),
                       str(terco3[0][4]), str(terco3[0][5]),
                       str(terco3[0][6]))
            cursor.execute(sql3, insert3)
            banco10.commit()

        cursor.execute("select max(id) from per_quarto1 where id_Qt = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_quarto1 = dados[0][0]
        else:
            id_quarto1 = 0

        cursor.execute("select max(id) from per_quarto2 where id_Qt2 = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_quarto2 = dados[0][0]
        else:
            id_quarto2 = 0

        cursor.execute("select max(id) from per_quarto3 where id_Qt3 = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_quarto3 = dados[0][0]
        else:
            id_quarto3 = 0

        cursor.execute("select max(id) from per_quarto4 where id_Qt4 = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_quarto4 = dados[0][0]
        else:
            id_quarto4 = 0

        cursor.execute("select id_Qt, tamanho, parte, sabor, "
                       "valorProduto, quantidade, subtotal "
                       "from per_quarto1 where id = %s" % id_quarto1)
        quarto1 = cursor.fetchall()

        cursor.execute("select id_Qt2, tamanho, parte, sabor, "
                       "valorProduto, quantidade, subtotal "
                       "from per_quarto2 where id = %s" % id_quarto2)
        quarto2 = cursor.fetchall()

        cursor.execute("select id_Qt3, tamanho, parte, sabor, "
                       "valorProduto, quantidade, subtotal "
                       "from per_quarto3 where id = %s" % id_quarto3)
        quarto3 = cursor.fetchall()

        cursor.execute("select id_Qt4, tamanho, parte, sabor, "
                       "valorProduto, quantidade, "
                       "subtotal from per_quarto4 "
                       "where id = %s" % id_quarto4)
        quarto4 = cursor.fetchall()

        if quarto1 != ():
            sql = "insert into temp_quarto1(id, tamanho, parte, sabor, " \
                  "valorProduto, quantidade, subtotal, " \
                  "id_cliente, dataa) " \
                  "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert = (str(quarto1[0][0]), str(quarto1[0][1]),
                      str(quarto1[0][2]), str(quarto1[0][3]),
                      str(quarto1[0][4]), str(quarto1[0][5]),
                      str(quarto1[0][6]), str(id), data)
            cursor.execute(sql, insert)
            banco10.commit()

            sql2 = "insert into temp_quarto2(id, tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal) " \
                   "values (%s, %s, %s, %s, %s, %s, %s)"
            insert2 = (str(quarto2[0][0]), str(quarto2[0][1]),
                       str(quarto2[0][2]), str(quarto2[0][3]),
                       str(quarto2[0][4]), str(quarto2[0][5]),
                       str(quarto2[0][6]))
            cursor.execute(sql2, insert2)
            banco10.commit()

            sql3 = "insert into temp_quarto3(id, tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal) " \
                   "values (%s, %s, %s, %s, %s, %s, %s)"
            insert3 = (str(quarto3[0][0]), str(quarto3[0][1]),
                       str(quarto3[0][2]), str(quarto3[0][3]),
                       str(quarto3[0][4]), str(quarto3[0][5]),
                       str(quarto3[0][6]))
            cursor.execute(sql3, insert3)
            banco10.commit()

            sql3 = "insert into temp_quarto4(id, tamanho, parte, sabor, " \
                   "valorProduto, quantidade, subtotal) " \
                   "values (%s, %s, %s, %s, %s, %s, %s)"
            insert3 = (str(quarto4[0][0]), str(quarto4[0][1]),
                       str(quarto4[0][2]), str(quarto4[0][3]),
                       str(quarto4[0][4]), str(quarto4[0][5]),
                       str(quarto4[0][6]))
            cursor.execute(sql3, insert3)
            banco10.commit()

        cursor.execute("select max(id) from per_esfihas where id_esfiha = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_esfiha = dados[0][0]
        else:
            id_esfiha = 0

        cursor.execute("select id_esfiha, tamanho, parte, sabor, "
                       "valorProduto, quantidade, subtotal "
                       "from per_esfihas where id = %s" % id_esfiha)
        esfihas = cursor.fetchall()

        if esfihas != ():
            sql = "insert into temp_esfihas(id, tamanho, parte, sabor, " \
                  "valorProduto, quantidade, subtotal, " \
                  "id_cliente, dataa) " \
                  "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert = (str(esfihas[0][0]), str(esfihas[0][1]),
                      str(esfihas[0][2]), str(esfihas[0][3]),
                      str(esfihas[0][4]), str(esfihas[0][5]),
                      str(esfihas[0][6]), str(id), data)
            cursor.execute(sql, insert)
            banco10.commit()

        cursor.execute("select max(id) from per_lata where id_lata = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_lata = dados[0][0]
        else:
            id_lata = 0

        cursor.execute("select id_lata, tamanho, parte, sabor, "
                       "valorProduto, quantidade, "
                       "subtotal from per_lata "
                       "where id = %s" % id_lata)
        lata = cursor.fetchall()

        if lata != ():
            sql = "insert into temp_lata(id, tamanho, parte, sabor, " \
                  "valorProduto, quantidade, subtotal, " \
                  "id_cliente, dataa) " \
                  "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert = (str(lata[0][0]), str(lata[0][1]),
                      str(lata[0][2]), str(lata[0][3]),
                      str(lata[0][4]), str(lata[0][5]),
                      str(lata[0][6]), str(id), data)
            cursor.execute(sql, insert)
            banco10.commit()

        cursor.execute("select max(id) from per_s600 where id_600 = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_600 = dados[0][0]
        else:
            id_600 = 0

        cursor.execute("select id_600, tamanho, parte, sabor, "
                       "valorProduto, quantidade, "
                       "subtotal from per_s600 "
                       "where id = %s" % id_600)
        s600 = cursor.fetchall()

        if s600 != ():
            sql = "insert into temp_600(id, tamanho, parte, sabor, " \
                  "valorProduto, quantidade, subtotal, " \
                  "id_cliente, dataa) " \
                  "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert = (str(s600[0][0]), str(s600[0][1]),
                      str(s600[0][2]), str(s600[0][3]),
                      str(s600[0][4]), str(s600[0][5]),
                      str(s600[0][6]), str(id), data)
            cursor.execute(sql, insert)
            banco10.commit()

        cursor.execute("select max(id) from per_1L where id_1L = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_1L = dados[0][0]
        else:
            id_1L = 0

        cursor.execute("select id_1L, tamanho, parte, sabor, "
                       "valorProduto, quantidade, "
                       "subtotal from per_1L "
                       "where id = %s" % id_1L)
        umLitro = cursor.fetchall()

        if umLitro != ():
            sql = "insert into temp_1L(id, tamanho, parte, sabor, " \
                  "valorProduto, quantidade, subtotal, " \
                  "id_cliente, dataa) " \
                  "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert = (str(umLitro[0][0]), str(umLitro[0][1]),
                      str(umLitro[0][2]), str(umLitro[0][3]),
                      str(umLitro[0][4]), str(umLitro[0][5]),
                      str(umLitro[0][6]), str(id), data)
            cursor.execute(sql, insert)
            banco10.commit()

        cursor.execute("select max(id) from per_1Lmeio where id_1meio = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_1meio = dados[0][0]
        else:
            id_1meio = 0

        cursor.execute("select id_1meio, tamanho, parte, sabor, "
                       "valorProduto, quantidade, subtotal "
                       "from per_1Lmeio "
                       "where id = %s" % id_1meio)
        umLmeio = cursor.fetchall()

        if umLmeio != ():
            sql = "insert into temp_1Lmeio(id, tamanho, parte, sabor, " \
                  "valorProduto, quantidade, subtotal, " \
                  "id_cliente, dataa) " \
                  "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert = (str(umLmeio[0][0]), str(umLmeio[0][1]),
                      str(umLmeio[0][2]), str(umLmeio[0][3]),
                      str(umLmeio[0][4]),str(umLmeio[0][5]),
                      str(umLmeio[0][6]), str(id), data)
            cursor.execute(sql, insert)
            banco10.commit()

        cursor.execute("select max(id) from per_2L where id_2L = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_2L = dados[0][0]
        else:
            id_2L = 0

        cursor.execute("select id_2L, tamanho, parte, sabor, "
                       "valorProduto, quantidade, "
                       "subtotal from per_2L "
                       "where id = %s" % id_2L)
        doisLitros = cursor.fetchall()

        if doisLitros != ():
            sql = "insert into temp_2L(id, tamanho, parte, sabor, " \
                  "valorProduto, quantidade, subtotal, " \
                  "id_cliente, dataa) " \
                  "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert = (str(doisLitros[0][0]), str(doisLitros[0][1]),
                      str(doisLitros[0][2]), str(doisLitros[0][3]),
                      str(doisLitros[0][4]), str(doisLitros[0][5]),
                      str(doisLitros[0][6]), str(id), data)
            cursor.execute(sql, insert)
            banco10.commit()

        cursor.execute("select max(id) from per_2Lmeio where id_2meio = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_2meio = dados[0][0]
        else:
            id_2meio = 0

        cursor.execute("select id_2meio, tamanho, parte, sabor, "
                       "valorProduto, quantidade, "
                       "subtotal from per_2Lmeio "
                       "where id = %s" % id_2meio)
        doisLmeio = cursor.fetchall()

        if doisLmeio != ():
            sql = "insert into temp_2Lmeio(id, tamanho, parte, sabor, " \
                  "valorProduto, quantidade, subtotal, " \
                  "id_cliente, dataa) " \
                  "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert = (str(doisLmeio[0][0]), str(doisLmeio[0][1]),
                      str(doisLmeio[0][2]), str(doisLmeio[0][3]),
                      str(doisLmeio[0][4]),str(doisLmeio[0][5]),
                      str(doisLmeio[0][6]), str(id), data)
            cursor.execute(sql, insert)
            banco10.commit()

        cursor.execute("select max(id) from per_outros where id_outros = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_outros = dados[0][0]
        else:
            id_outros = 0

        cursor.execute("select id_outros, tamanho, parte, sabor, "
                       "valorProduto, quantidade,"
                       "subtotal from per_outros "
                       "where id = %s" % id_outros)
        outros = cursor.fetchall()

        if outros != ():
            sql = "insert into temp_outros(id, tamanho, parte, sabor, " \
                  "valorProduto, quantidade, subtotal, " \
                  "id_cliente, dataa) " \
                  "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert = (str(outros[0][0]), str(outros[0][1]),
                      str(outros[0][2]), str(outros[0][3]),
                      str(outros[0][4]), str(outros[0][5]),
                      str(outros[0][6]), str(id), data)
            cursor.execute(sql, insert)
            banco10.commit()

            cursor.execute("delete from rascunho_outros where id_cliente = %s" % id)
            banco10.commit()

        cursor.execute("select max(id) from per_adc where id_adc = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_adc = dados[0][0]
        else:
            id_adc = 0

        cursor.execute("select id_adc, tamanho, vazio1, "
                       "adicional, valor, vazio2, "
                       "vazio3 from per_adc "
                       "where id = %s" % id_adc)
        adc = cursor.fetchall()

        if adc != ():
            sql = "insert into temp_adc(tamanho, vazio1, adicional, " \
                  "valor, vazio2, vazio3, id_pizza, " \
                  "id_cliente, dataa) " \
                  "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert = (str(adc[0][1]), str(adc[0][2]),
                      str(adc[0][3]), str(adc[0][4]),
                      str(adc[0][5]),str(adc[0][6]),
                      str(adc[0][0]), str(id), data)
            cursor.execute(sql, insert)
            banco10.commit()

        cursor.execute("select max(id) from per_semAdc where id_semAdc = %s" % id_pedido)
        dados = cursor.fetchall()
        if dados != ((None,),):
            id_semAdc = dados[0][0]
        else:
            id_semAdc = 0

        cursor.execute("select id_semAdc, tamanho, vazio1, "
                       "adicional, valor, vazio2, vazio3 "
                       "from per_semAdc "
                       "where id = %s" % id_semAdc)
        semAdc = cursor.fetchall()

        if semAdc != ():
            sql = "insert into semAdc(tamanho, vazio1, adicional, " \
                  "valor, vazio2, vazio3, id_pizza, " \
                  "id_cliente, dataa) " \
                  "values (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
            insert = (str(semAdc[0][1]), str(semAdc[0][2]),
                      str(semAdc[0][3]), str(semAdc[0][4]),
                      str(semAdc[0][5]), str(semAdc[0][6]),
                      str(semAdc[0][0]), str(id), data)
            cursor.execute(sql, insert)
            banco10.commit()

        if len(inteiro) > 0:
            for i in inteiro:
                listaPedido.append(i)
                for j in adc:
                    if j[0] == i[0]:
                        listaPedido.append(j)
                for k in semAdc:
                    if k[0] == i[0]:
                        listaPedido.append(k)

        if len(metade1) and len(metade2) > 0:
            for j, k in zip(metade1, metade2):
                listaPedido.append(j)
                listaPedido.append(k)
                for c in adc:
                    if c[0] == j[0]:
                        listaPedido.append(c)
                for d in semAdc:
                    if d[0] == j[0]:
                        listaPedido.append(d)

        if len(terco1) and len(terco2) and len(terco3) > 0:
            for l, m, n in zip(terco1, terco2, terco3):
                listaPedido.append(l)
                listaPedido.append(m)
                listaPedido.append(n)
                for c in adc:
                    if c[0] == l[0]:
                        listaPedido.append(c)
                for d in semAdc:
                    if d[0] == l[0]:
                        listaPedido.append(d)

        if len(quarto1) and len(quarto2) and len(quarto3) and len(quarto4) > 0:
            for o, p, q, r in zip(quarto1, quarto2, quarto3, quarto4):
                listaPedido.append(o)
                listaPedido.append(p)
                listaPedido.append(q)
                listaPedido.append(r)
                for c in adc:
                    if c[0] == o[0]:
                        listaPedido.append(c)
                for d in semAdc:
                    if d[0] == o[0]:
                        listaPedido.append(d)

        if len(esfihas) > 0:
            for u in esfihas:
                listaPedido.append(u)
        if len(lata) > 0:
            for v in lata:
                listaPedido.append(v)
        if len(s600) > 0:
            for w in s600:
                listaPedido.append(w)
        if len(umLitro) > 0:
            for x in umLitro:
                listaPedido.append(x)
        if len(umLmeio) > 0:
            for y in umLmeio:
                listaPedido.append(y)
        if len(doisLitros) > 0:
            for z in doisLitros:
                listaPedido.append(z)
        if len(doisLmeio) > 0:
            for a in doisLmeio:
                listaPedido.append(a)
        if len(outros) > 0:
            for b in outros:
                listaPedido.append(b)

        telaPrincipal.valorTotal.setText(f'Valor Total: {valorTotal:.2f}')
        telaPrincipal.tableWidget_cadastro.setRowCount(len(listaPedido))
        telaPrincipal.tableWidget_cadastro.setColumnCount(7)
        for i in range(0, len(listaPedido)):
            for j in range(0, 7):
                telaPrincipal.tableWidget_cadastro.setItem(i, j, QtWidgets.QTableWidgetItem(str(listaPedido[i][j])))

        telaUltimoPedido.hide()
    except Exception as erro:
        print(erro.__class__)

# Arquivos ui ---------------------------------------------------------------
app = QtWidgets.QApplication([])
telaExibiPrecoAdicionais = uic.loadUi("tela_exibir_preco_adicionais.ui")
telafechamento = uic.loadUi("fechamento.ui")
telaSecundaria = uic.loadUi("telaSecundaria.ui")
telaEsfiha = uic.loadUi("telaEsfiha.ui")
telaPizza = uic.loadUi("telaPizza.ui")
telaPagamento = uic.loadUi("telaFuncionario.ui")
telaIfood = uic.loadUi("telaIfood.ui")
telaTerminais = uic.loadUi("telaTerminal.ui")
telaMotoboy = uic.loadUi("telamotoboy.ui")
telaCaixa2 = uic.loadUi("telaCaixa2.ui")
telaCartao = uic.loadUi("telaCartao.ui")
primeiraTela = uic.loadUi("primeiraTela.ui")
telaPrincipal = uic.loadUi("telaPrincipal2.ui")
telaProduto = uic.loadUi("telaCadastroProdutos.ui")
telaPedido = uic.loadUi("telaGerenciarPedidos.ui")
telaConfirmacao = uic.loadUi("perguntaCadastro.ui")
telaUltimoPedido = uic.loadUi("telaUltimoPedido.ui")
tela_exibi_valores_pizzas = uic.loadUi("tela_exibi_valores_pizza.ui")
telaLogin = uic.loadUi("telaLogin.ui")
telaPizza = uic.loadUi("telaPizza.ui")
telaConfirmarPedido = uic.loadUi("telaConfimacaoPedido.ui")
telaAdicionais = uic.loadUi("telaAdicionais.ui")
telaBebida = uic.loadUi("telaBebidas.ui")
telaErro = uic.loadUi("telaErro.ui")
telaInfoPedido = uic.loadUi("telaInfoPedido.ui")
telaDespachar = uic.loadUi("telaDespachar.ui")
telaCancelar = uic.loadUi("telaCancelar.ui")
telaImprimir = uic.loadUi("telaImprimir.ui")
telaFinalizar = uic.loadUi("telaFinalizar.ui")
telaDevedores = uic.loadUi("telaDevedores.ui")
telaDevedores2 = uic.loadUi("telaDevedores2.ui")
telaFinalizarDeve = uic.loadUi("telaFinalizarDeve.ui")
telaAtualizarProdutos = uic.loadUi("telaAtualizarProdutos.ui")
telaExcluirBebidas = uic.loadUi("telaExcluirBebidas.ui")
telaAtualizarBebidas = uic.loadUi("telaAtualizarbebidas.ui")
telaCaixa = uic.loadUi("telaCaixa.ui")
telaCalendario = uic.loadUi("telaCalendario.ui")
telaCalendario2 = uic.loadUi("telaCalendario2.ui")
telaPeriodo = uic.loadUi("telaPeriodo.ui")
telaMensal = uic.loadUi("telaMensal.ui")
telaCadastroLogin = uic.loadUi("telaCadastroLogin.ui")
#--------------------------------------------------------------------------------------

# Outros botoes ---------------------------------------------------------------
telaUltimoPedido.utilizar.clicked.connect(utilizar_ultimo_pedido)
telaLogin.entrar.clicked.connect(login_sistema)
telaCadastroLogin.cadastrar_login.clicked.connect(cadastrar_login)
telaCalendario.abrir_2.clicked.connect(pegar_data)
telaCalendario2.abrir.clicked.connect(defini_data_sistema)
telaMensal.ok_mensal.clicked.connect(total_mensal)
telaConfirmacao.sim.clicked.connect(limpa_dados_cadastrais)
telaConfirmacao.nao.clicked.connect(lambda: telaConfirmacao.hide())
telaConfirmarPedido.confirmar.clicked.connect(pagamento)
telaConfirmarPedido.imprimir.clicked.connect(gerar_pedido)
telaAtualizarBebidas.atualizar_bebidas.clicked.connect(bebidas_outros_atualizar)
telaAtualizarBebidas.ok_atualizar.clicked.connect(id_bebidas_atualizar)
telaExcluirBebidas.ok.clicked.connect(exclui_bebidas)
#----------------------------------------------------------------------------------

# Botoes da tela de fechamento do caixa --------------------------------
telafechamento.consultar.clicked.connect(tela_consulta)
telafechamento.calcular.clicked.connect(calcular)
telafechamento.salvar.clicked.connect(funcao_salvar_fechamento)
telafechamento.esfihas.clicked.connect(tela_esfiha)
telafechamento.pagamentos.clicked.connect(tela_pagamentos)
telafechamento.ifood.clicked.connect(tela_ifood)
telafechamento.vendas.clicked.connect(tela_terminais)
telafechamento.cartao.clicked.connect(tela_cartao)
telafechamento.motoboys.clicked.connect(tela_motoboy)
telafechamento.caixa.clicked.connect(tela_caixa2)
#------------------------------------------------------------------------

# Botoes que fazem parte do fechamento de caixa -------------------------
telaEsfiha.salvarEsfiha.clicked.connect(funcao_esfiha)
telaPizza.salvarPizza.clicked.connect(funcao_pizza)
telaPagamento.salvarFuncionario.clicked.connect(funcao_pagamentos)
telaIfood.salvarIfood.clicked.connect(funcao_ifood)
telaTerminais.salvarTerminal.clicked.connect(funcao_venda)
telaMotoboy.salvarMotoboy.clicked.connect(funcao_motoboys)
telaCartao.salvarCartao.clicked.connect(funcao_cartao)
telaCaixa2.salvarCx.clicked.connect(funcao_caixa)
telaSecundaria.excluir.clicked.connect(excluir_dados)
telaSecundaria.arquivo.clicked.connect(gerar_arquivo)
#--------------------------------------------------------------------------

# Botoes da tela de adicionais --------------------------------------------
telaAdicionais.exibi_adc.clicked.connect(exibi_informacoes_adicionais)
telaAdicionais.broto_adc.clicked.connect(adicionais_brotinho)
telaAdicionais.seis_adc.clicked.connect(adicionais_pizza_seis_pedacos)
telaAdicionais.oito_adc.clicked.connect(adicionais_pizza_oito_pedacos)
telaAdicionais.dez_adc.clicked.connect(adicionais_pizza_dez_pedacos)
telaAdicionais.sem_adc.clicked.connect(remover_item)
#---------------------------------------------------------------------------

# Botoes da tela de gereciamento de pedidos --------------------------------
telaPedido.cancelamento.clicked.connect(tela_cancelar)
telaPedido.impressao.clicked.connect(tela_imprimir)
telaPedido.consultar.clicked.connect(tela_informacoes_pedido)
telaPedido.despache.clicked.connect(tela_despachar)
telaPedido.finalizacao.clicked.connect(tela_finalizar)
telaPedido.devendo.clicked.connect(tela_devedores)
#----------------------------------------------------------------------------

telaCancelar.cancelar.clicked.connect(cancelar_pedido)
telaImprimir.imprimir.clicked.connect(imprimir_pedido)
telaFinalizar.finalizar.clicked.connect(finalizar_pedido)
telaFinalizarDeve.finalizar_2.clicked.connect(finalizar_devedores)
telaDespachar.despachar.clicked.connect(despachar_pedido)
telaInfoPedido.consultar_pedido.clicked.connect(info_pedido)

# Botoes da tela principal do sistema----------------------------------------
primeiraTela.gerenciar_devedores.clicked.connect(tela_exibe_devedores)
primeiraTela.caixa.clicked.connect(tela_caixa)
primeiraTela.gerenciar.clicked.connect(TelaGerenciarPedidos)
primeiraTela.cadastrar_produtos_2.clicked.connect(tela_bebidas)
primeiraTela.cadastrar_produtos.clicked.connect(Tela_Produtos)
primeiraTela.pedidos.clicked.connect(telaDePedidos)
#----------------------------------------------------------------------------

# Botoes da tela de clientes que devem---------------------------------------
telaDevedores.enviar.clicked.connect(pedidos_nao_pagos)
telaDevedores2.consultar_2.clicked.connect(tela_informacoes_pedido)
telaDevedores2.impressao_2.clicked.connect(tela_imprimir)
telaDevedores2.atualizar_2.clicked.connect(tela_exibe_devedores)
telaDevedores2.finalizacao_2.clicked.connect(tela_finalizar_devedores)
#----------------------------------------------------------------------------

# Botoes da tela caixa ------------------------------------------------------
telaCaixa.total_mensal.clicked.connect(tela_mensal)
telaCaixa.calendario.clicked.connect(tela_calendario)
telaCaixa.cadastrar_login.clicked.connect(tela_cadastrar_login)
telaCaixa.encerrar.clicked.connect(encerrar_sistema)
telaCaixa.fechamento.clicked.connect(tela_limpa_campos_preenchidos)
telaCaixa.total_diario.clicked.connect(total_diario)
#----------------------------------------------------------------------------

# Botoes da tela de fazer pedidos ---------------
telaPrincipal.enviar_cadastro.clicked.connect(verificar_cadastro_cliente)
telaPrincipal.salvar.clicked.connect(cadastrar_Cliente)
telaPrincipal.atualizar.clicked.connect(atualizarCadastro)
telaPrincipal.limpar_2.clicked.connect(NovoPedido)
telaPrincipal.limpar.clicked.connect(limpar_apos_sim)
telaPrincipal.radioButton.clicked.connect(exibe_cep)
telaPrincipal.ultimo_pedido.clicked.connect(tela_ultimo_pedido)
telaPrincipal.aplicar_2.clicked.connect(funcao_acrescimo)
telaPrincipal.aplicar.clicked.connect(funcao_desconto)
telaPrincipal.taxa.clicked.connect(taxaEntrega)
telaPrincipal.casa.clicked.connect(casa)
telaPrincipal.bebidas_1.clicked.connect(refriLata)
telaPrincipal.bebidas_2.clicked.connect(refri600)
telaPrincipal.bebidas_3.clicked.connect(refri1l)
telaPrincipal.bebidas_4.clicked.connect(refri1meio)
telaPrincipal.bebidas_5.clicked.connect(refri2L)
telaPrincipal.bebidas_6.clicked.connect(refri2meio)
telaPrincipal.confirmar_4.clicked.connect(outros)
telaPrincipal.excluir_produto.clicked.connect(excluirTableWidget)
telaPrincipal.outros.clicked.connect(tela_outros_pedido)
telaPrincipal.bebidas_7.clicked.connect(tela_bebidas_pedido)
telaPrincipal.esfiha.clicked.connect(tela_esfihas_pedido)
telaPrincipal.pizza.clicked.connect(pizzaTela)
telaPrincipal.broto.clicked.connect(pizzaBroto)
telaPrincipal.seis.clicked.connect(pizzaSeis)
telaPrincipal.oito.clicked.connect(pizzaOito)
telaPrincipal.dez.clicked.connect(pizzaDez)
telaPrincipal.confirmar_3.clicked.connect(telaConfirmacaoPedido)
telaPrincipal.excluir_produto_2.clicked.connect(excluir_item_pedido_id)
telaPrincipal.ingredientes.clicked.connect(ingredientes)
telaPrincipal.confirmar_2.clicked.connect(esfihas)
telaPrincipal.ingredientes_2.clicked.connect(ingredientes)
telaPrincipal.adicionais.clicked.connect(tela_carrega_adicionais)
#----------------------------------------------------------------------

# Botoes da tela de cadastrar produtos --------------------------------
telaProduto.radioButton_4.clicked.connect(cadastroDez)
telaProduto.radioButton.clicked.connect(cadastroBroto)
telaProduto.radioButton_2.clicked.connect(cadastroSeis)
telaProduto.radioButton_3.clicked.connect(cadastroOito)
telaProduto.radioButton_6.clicked.connect(cadastroEsfihas)
telaProduto.adicionais.clicked.connect(tela_exibe_adicionais)
telaProduto.buttonBroto.clicked.connect(cadastro_adicionais_broto)
telaProduto.ButtonSeis.clicked.connect(cadastro_adicionais_seis_pedacos)
telaProduto.ButtonOito.clicked.connect(cadastro_adicionais_oito_pedacos)
telaProduto.ButtonDez.clicked.connect(cadastro_adicionais_dez_pedacos)
telaProduto.sem_adc.clicked.connect(cadastro_sem_adicionais)
telaProduto.voltar_adc.clicked.connect(voltar_tela_produto)
telaProduto.atualiza_tela.clicked.connect(tela_atualizar_produtos)
#------------------------------------------------------------------------

# Botoes da tela de cadastrar bebidas e outros --------------------------
telaBebida.excluir_bebidas.clicked.connect(tela_excluir_bebidas)
telaBebida.excluir_2.clicked.connect(exclui_outros)
telaBebida.atualizar_bebidas.clicked.connect(tela_atualizar_bebidas)
telaBebida.atualizar_outros.clicked.connect(tela_atualizar_bebidas)
telaBebida.bebida_cdt_1.clicked.connect(cadastroLata)
telaBebida.bebida_cdt_2.clicked.connect(cadastro600)
telaBebida.bebida_cdt_3.clicked.connect(cadastro1l)
telaBebida.bebida_cdt_4.clicked.connect(cadastro1meio)
telaBebida.bebida_cdt_5.clicked.connect(cadastro2litro)
telaBebida.bebida_cdt_6.clicked.connect(cadastro2meio)
telaBebida.confirmar_outros.clicked.connect(cadastrarOutros)
telaBebida.atualizar_bebidas.clicked.connect(tela_bebidas)
telaBebida.outros_2.clicked.connect(tela_bebidas)
telaBebida.outros.clicked.connect(telas_outros)
#------------------------------------------------------------------------

# Botoes da tela de atualizacao dos produtos ----------------------------------------------
telaAtualizarProdutos.id_pizza_esfiha_atualizar.clicked.connect(id_pizza_esfiha_atualizar)
telaAtualizarProdutos.atualizar_3.clicked.connect(tela_atualizar_adicionais)
telaAtualizarProdutos.atualizar_4.clicked.connect(atualizar_pizza_esfiha)
telaAtualizarProdutos.voltar_adc_atualizar.clicked.connect(voltar_tela_atualizar_produtos)
telaAtualizarProdutos.id_adc_atualizar.clicked.connect(id_adicionais_atualizar)
telaAtualizarProdutos.atualizar_6.clicked.connect(atualizar_adicionais)
telaAtualizarProdutos.excluir_adc.clicked.connect(excluir_cadastro_adicionais)
telaAtualizarProdutos.excluir_produto_2.clicked.connect(excluir_cadastro_pizza)
#-------------------------------------------------------------------------------------------

telaLogin.show()
telaLogin.login.setText('GRATONI')
app.exec()
