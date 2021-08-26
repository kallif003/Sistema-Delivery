create database sistema_delivery;
use sistema_delivery;

create table cadastro_cliente(
id int not null auto_increment primary key,
telefone varchar(15) not null,
nome varchar(50) not null,
cep varchar(9),
endereco varchar(50),
numero varchar(5),
bairro varchar(50),
referencia varchar(100),
complemento varchar(50),
taxaEntrega int(5),
data_inclusao date
);

create table cadastro_login(
login varchar(30),
senha varchar(8)
);

insert into cadastro_login(login, senha) values('GRATONI', '0901');
create table temp_inteiro(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade int(10),
subtotal decimal(10,2),
id_cliente int,
dataa varchar(12)
);

create table temp_metade1(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal varchar(5),
id_cliente int,
dataa varchar(12)
);

create table temp_metade2(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade int(10),
subtotal decimal(10,2)
);

create table temp_terco1(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal varchar(5),
id_cliente int,
dataa varchar(12)
);

create table temp_terco2(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal varchar(5)
);

create table temp_terco3(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade int(10),
subtotal decimal(10,2)
);

create table temp_outros(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal varchar(5),
id_cliente int,
dataa varchar(12)
);

create table temp_quarto1(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal varchar(5),
id_cliente int,
dataa varchar(12)
);

create table temp_quarto2(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal varchar(5)
);

create table temp_quarto3(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal varchar(5)
);

create table temp_quarto4(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade int(10),
subtotal decimal(10,2)
);

create table temp_adc(
id int not null auto_increment primary key,
tamanho varchar(10),
vazio1 varchar(5),
adicional varchar(50),
valor varchar(10),
vazio2 varchar(5),
vazio3 varchar(5),
id_pizza int,
id_cliente int,
dataa varchar(12)
);

create table semAdc(
id int not null auto_increment primary key,
tamanho varchar(10),
vazio1 varchar(5),
adicional varchar(50),
valor varchar(5),
vazio2 varchar(5),
vazio3 varchar(5),
id_pizza int,
id_cliente int,
dataa varchar(12)
);

create table temp_lata(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal decimal(10,2),
id_cliente int,
dataa varchar(12)
);

create table temp_600(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal decimal(10,2),
id_cliente int,
dataa varchar(12)
);

create table temp_1L(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal decimal(10,2),
id_cliente int,
dataa varchar(12)
);

create table temp_1Lmeio(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal decimal(10,2),
id_cliente int,
dataa varchar(12)
);

create table temp_2L(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal decimal(10,2),
id_cliente int,
dataa varchar(12)
);

create table temp_2Lmeio(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal decimal(10,2),
id_cliente int,
dataa varchar(12)
);

create table temp_esfihas(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal decimal(10,2),
id_cliente int,
dataa varchar(12)
);

#set foreign_key_checks = 1;

create table adcBroto(
id int not null auto_increment primary key,
adicional varchar(50),
tamanho varchar(10),
valor decimal(10,2)
);

create table adcSeis(
id int not null auto_increment primary key,
adicional varchar(50),
tamanho varchar(10),
valor decimal(10,2)
);

create table adcOito(
id int not null auto_increment primary key,
adicional varchar(50),
tamanho varchar(10),
valor decimal(10,2)
);

create table adcDez(
id int not null auto_increment primary key,
adicional varchar(50),
tamanho varchar(10),
valor decimal(10,2)
);

create table adcSem(
id int not null auto_increment primary key,
adicional varchar(50),
tamanho varchar(10),
vazio2 decimal(10,2)
);

create table broto(
id int not null auto_increment primary key,
sabor varchar(20),
tamanho varchar(20),
valorProduto decimal(10,2),
ingredientes varchar(200)
);

create table seisPedacos(
id int not null auto_increment primary key,
sabor varchar(20),
tamanho varchar(20),
valorProduto decimal(10,2),
ingredientes varchar(200)
);

create table oitoPedacos(
id int not null auto_increment primary key,
sabor varchar(20),
tamanho varchar(20),
valorProduto decimal(10,2),
ingredientes varchar(200)
);

create table dezPedacos(
id int not null auto_increment primary key,
sabor varchar(20),
tamanho varchar(20),
valorProduto decimal(10,2),
ingredientes varchar(200)
);

create table lata(
id int not null auto_increment primary key,
bebida varchar(20),
tamanho varchar(20),
valor decimal(10,2)
);

create table s600(
id int not null auto_increment primary key,
bebida varchar(20),
tamanho varchar(20),
valor decimal(10,2)
);

create table umLitro(
id int not null auto_increment primary key,
bebida varchar(20),
tamanho varchar(20),
valor decimal(10,2)
);

create table umEmeio(
id int not null auto_increment primary key,
bebida varchar(20),
tamanho varchar(20),
valor decimal(10,2)
);

create table doisLitros(
id int not null auto_increment primary key,
bebida varchar(20),
tamanho varchar(20),
valor decimal(10,2)
);

create table doisEmeio(
id int not null auto_increment primary key,
bebida varchar(20),
tamanho varchar(20),
valor decimal(10,2)
);

create table esfihas(
id int not null auto_increment primary key,
sabor varchar(20),
tamanho varchar(20),
valorProduto decimal(10,2),
ingredientes varchar(200)
);

create table outros(
id int not null auto_increment primary key,
produto varchar(20),
tipo varchar(20),
valor decimal(10,2)
);

create table per_inteiro(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade int(5),
subtotal decimal(10,2),
id_int int,
dataa varchar(12)
);

create table per_met1(
id int not null primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal varchar(5),
id_met int,
dataa varchar(12)
);

create table per_met2(
id int not null primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade int(10),
subtotal decimal(10,2),
id_met2 int,
dataa varchar(12)
);

create table per_terco1(
id int not null primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal varchar(5),
id_terco int,
dataa varchar(12)
);

create table per_terco2(
id int not null primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal varchar(5),
id_terco2 int,
dataa varchar(12)
);

create table per_terco3(
id int not null primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade int(10),
subtotal decimal(10,2),
id_terco3 int,
dataa varchar(12)
);

create table per_quarto1(
id int not null primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal varchar(5),
id_Qt int,
dataa varchar(12)
);

create table per_quarto2(
id int not null primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal varchar(5),
id_Qt2 int,
dataa varchar(12)
);

create table per_quarto3(
id int not null primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal varchar(5),
id_Qt3 int,
dataa varchar(12)
);

create table per_quarto4(
id int not null primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade int(10),
subtotal decimal(10,2),
id_Qt4 int,
dataa varchar(12)
);

create table per_adc(
id int not null auto_increment primary key,
tamanho varchar(10),
vazio1 varchar(5),
adicional varchar(50),
valor decimal(10,2),
vazio2 varchar(5),
vazio3 varchar(5),
id_pizza int,
id_adc int,
dataa varchar(12)
);

create table per_semAdc(
id int not null auto_increment primary key,
tamanho varchar(10),
vazio1 varchar(5),
adicional varchar(50),
valor varchar(5),
vazio2 varchar(5),
vazio3 varchar(5),
id_pizza int,
id_semAdc int,
dataa varchar(12)
);

create table per_esfihas(
id int not null auto_increment key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal decimal(10,2),
id_esfiha int,
dataa varchar(12)
);

create table per_lata(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal decimal(10,2),
id_lata int,
dataa varchar(12)
);

create table per_s600(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal decimal(10,2),
id_600 int,
dataa varchar(12)
);

create table per_1L(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal decimal(10,2),
id_1L int,
dataa varchar(12)
);

create table per_1Lmeio(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal decimal(10,2),
id_1meio int,
dataa varchar(12)
);

create table per_2L(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal decimal(10,2),
id_2L int,
dataa varchar(12)
);

create table per_2Lmeio(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal decimal(10,2),
id_2meio int,
dataa varchar(12)
);

create table per_outros(
id int not null auto_increment primary key,
tamanho varchar(10),
parte varchar(5),
sabor varchar(30),
valorProduto decimal(10,2),
quantidade varchar(5),
subtotal decimal(10,2),
id_outros int,
dataa varchar(12)
);

create table gerenciarPedido(
id int not null auto_increment primary key,
telefone varchar(15) not null,
nome varchar(50) not null,
cep int(9),
endereco varchar(50),
numero int(5),
bairro varchar(50),
referencia varchar(100),
complemento varchar(50),
taxaEntrega decimal(10,2),
dataa varchar(12),
hora varchar(12),
valorTotal decimal(10,2),
id_cliente int
);

create table status_pedido(
id int not null auto_increment primary key,
st_pedido varchar(50),
hora varchar(12),
motoboy varchar(30),
hora_saida varchar(10),
hora_chegada varchar(10),
motivo varchar(100),
id_pedido int
);

create table pagamento(
id int not null auto_increment primary key,
cartao decimal(10,2),
voucher decimal(10,2),
dinheiro decimal(10,2),
troco decimal(10,2),
desconto decimal(10,2),
observacao varchar(200),
id_pagamento int,
dataa varchar(12)
);

alter table pagamento add pix decimal(10,2) after desconto;

create table caixa(
id int not null auto_increment primary key,
total decimal(10,2),
pizzas varchar(30),
qt_pizzas int(10),
esfihas varchar(30),
qt_esfihas int(10),
bebidas varchar(30),
qt_bebidas int(10),
outros varchar(30),
qt_outros int(10),
dataa varchar(12),
data2 date
);

create table devedores(
id int not null primary key,
dataa varchar(12),
hora varchar(12),
telefone varchar(15) not null,
nome varchar(50) not null,
motivo varchar(100), 
valor decimal(10,2)
);

CREATE TABLE fechamento (
  id int NOT NULL AUTO_INCREMENT,
  dataVenda varchar(20) DEFAULT NULL,
  inicio_caixa decimal(10,2) DEFAULT NULL,
  retirada decimal(10,2) DEFAULT NULL,
  final_caixa decimal(10,2) DEFAULT NULL,
  motoboys decimal(10,2) DEFAULT NULL,
  cartao decimal(10,2) DEFAULT NULL,
  total_terminal decimal(10,2) DEFAULT NULL,
  esfihas int DEFAULT NULL,
  pizzas int DEFAULT NULL,
  Ifood_online decimal(10,2) DEFAULT NULL,
  total_Ifood decimal(10,2) DEFAULT NULL,
  recebedor1 varchar(50) DEFAULT NULL,
  valor1 decimal(10,2) DEFAULT NULL,
   recebedor2 varchar(50) DEFAULT NULL,
  valor2 decimal(10,2) DEFAULT NULL,
   recebedor3 varchar(50) DEFAULT NULL,
  valor3 decimal(10,2) DEFAULT NULL,
   recebedor4 varchar(50) DEFAULT NULL,
  valor4 decimal(10,2) DEFAULT NULL,
   recebedor5 varchar(50) DEFAULT NULL,
  valor5 decimal(10,2) DEFAULT NULL,
   recebedor6 varchar(50) DEFAULT NULL,
  valor6 decimal(10,2) DEFAULT NULL,
   recebedor7 varchar(50) DEFAULT NULL,
  valor7 decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (id)
  );
 
 create table fechamento2(
 id int NOT NULL AUTO_INCREMENT,
Pag_dinheiro decimal(10,2) DEFAULT NULL,
 venda_dia decimal(10,2) DEFAULT NULL,
  total_dia decimal(10,2) DEFAULT NULL,
   ficou decimal(10,2) DEFAULT NULL,
  subiu decimal(10,2) DEFAULT NULL,
  faltou decimal(10,2) DEFAULT NULL,
  sobrou decimal(10,2) DEFAULT NULL,
  total_pagamento decimal(10,2),
   PRIMARY KEY (id)
  );
  
Alter Table status_pedido Add Constraint FK_pedido1 Foreign Key (id_pedido) references
gerenciarPedido (id) on delete cascade on update cascade; 

Alter Table temp_inteiro Add Constraint FK_int Foreign Key (id_cliente) references
cadastro_cliente (id) on delete cascade on update cascade;

Alter Table temp_metade1 Add Constraint FK_met1 Foreign Key (id_cliente) references
cadastro_cliente (id) on delete cascade on update cascade;

Alter Table temp_terco1 Add Constraint FK_tempTer Foreign Key (id_cliente) references
cadastro_cliente (id) on delete cascade on update cascade;

Alter Table temp_quarto1 Add Constraint FK_qt Foreign Key (id_cliente) references
cadastro_cliente (id) on delete cascade on update cascade;


Alter Table temp_metade2 Add Constraint FK_Meio Foreign Key (id) references
temp_metade1 (id) on delete cascade on update cascade;

Alter Table temp_terco3 Add Constraint FK_tempter3 Foreign Key (id) references
temp_terco1 (id) on delete cascade on update cascade;

Alter Table temp_terco2 Add Constraint FK_tempTer2 Foreign Key (id) references
temp_terco1 (id) on delete cascade on update cascade;

Alter Table temp_quarto4 Add Constraint FK_Qt4 Foreign Key (id) references
temp_quarto1 (id) on delete cascade on update cascade;

Alter Table temp_quarto3 Add Constraint FK_tempQt3 Foreign Key (id) references
temp_quarto1 (id) on delete cascade on update cascade;

Alter Table temp_quarto2 Add Constraint FK_tempQt2 Foreign Key (id) references
temp_quarto1 (id) on delete cascade on update cascade;

Alter Table seisPedacos Add Constraint FK_seis Foreign Key (id) references
broto(id) on delete cascade ;
Alter Table oitoPedacos Add Constraint FK_oito Foreign Key (id) references
broto(id) on delete cascade ;

Alter Table dezPedacos Add Constraint FK_dez Foreign Key (id) references
broto(id) on delete cascade ;

Alter Table adcSeis Add Constraint FK_adc_seis Foreign Key (id) references
adcBroto(id) on delete cascade ;
Alter Table adcOito Add Constraint FK_adc_oito Foreign Key (id) references
adcBroto(id) on delete cascade ;
Alter Table adcDez Add Constraint FK_adc_dez Foreign Key (id) references
adcBroto(id) on delete cascade ;

Alter Table fechamento2 Add Constraint FK_CLIENTES Foreign Key (id) references
fechamento (id) on delete cascade on update cascade;
