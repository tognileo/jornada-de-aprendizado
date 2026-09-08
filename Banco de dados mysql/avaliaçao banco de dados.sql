CREATE TABLE cliente(
id INT PRIMARY KEY NOT NULL auto_increment,
    nome varchar (100),
   telefone varchar (100),
   email varchar (100),
   cidade varchar (80)
);




CREATE TABLE endereco (
id INT PRIMARY KEY NOT NULL auto_increment,
    id_cliente int,
   rua  varchar (150),
   numero varchar (10),
   bairro  varchar (80),
   foreign key (id_cliente) references cliente (id)
);

CREATE TABLE categoria (
id INT PRIMARY KEY NOT NULL auto_increment,
    nome varchar (80),
   descricao  varchar (200)
   
);




CREATE TABLE pizza (
id_pizza INT PRIMARY KEY NOT NULL auto_increment,
    id_categoria int   ,
   nome  varchar (100),
   sabor varchar (80),
   tamanho varchar (20),
   preco decimal (8,2),
   foreign key (id_categoria) references categoria (id)
);

CREATE TABLE pedido (
id INT PRIMARY KEY NOT NULL auto_increment,
    id_cliente int   ,
   id_pizza  int,
   data_pedido date,
   quantidade  int,
   status varchar(30),
   foreign key (id_cliente) references cliente (id),
   foreign key (id_pizza) references pizza (id_pizza)
   
);


insert into categoria (id,nome,descricao)
values
(1,"tradiconal","Pizzas clássicas do cardápio"),
(2,"Especial","Pizzas premium com ingredientes diferenciados"),
(3,"Doce","Pizzas com recheio doce");


insert into cliente (nome,telefone,email,cidade)
values
("Ana Souza","(49)9111-2233","ana@email.com","Videira"),
("Bruno Lima","(49)9444-5566","bruno@email.com","Caçador"),
("Carla Melo","(49)9777-8899","carla@email.com","Fraiburgo"),
("Diego Costa","(49)9777-8899","carla@email.com","Fraiburgo")
;





insert into endereco (id_cliente,rua,numero,bairro)
values
(1,"Rua das Flores","123","Centro"),
(2,"Av. Brasil","456","São Cristóvão"),
(3,"Rua XV de Novembro","789","Centro"),
(4,"Rua Tiradentes",565,"Vila Nova")
;



insert into pedido (id_cliente,id_pizza,data_pedido,quantidade,status)
values
(1,2,2024-10-01,1,"Entregue"),
(2,1,2024-10-03,2,"entregue"),
(3,3,2024-10-05,1,"Aguardando"),
(1,1,2024-10-07,3,"Em preparo"),
(4,4,2024-10-10,1,"Aguardando")

;



select *from cliente where  cidade = "Videira";



select c.nome ,e.rua,e.numero,e.bairro from cliente c 
inner join endereco e on e.id_cliente = c.id;





select count(*)as total_pedidos from pedido ;




create table log_pedidos (
id_log INT AUTO_INCREMENT PRIMARY KEY,
id_pedido INT,
data_hora DATETIME,
mensagem VARCHAR(100)
);



DELIMITER //
CREATE TRIGGER trg_log_pedido
AFTER INSERT ON pedido
FOR EACH ROW
BEGIN
INSERT INTO log_pedidos (id_pedido, data_hora, mensagem)
VALUES (NEW.id, NOW(), 'Novo pedido registrado');
END //
DELIMITER ;



create view vw_pizzas_cardapio as
select p.nome as pizza, p.sabor, p.tamanho,p.preco,c.nome as nome_categoria from 
pizza p inner join categoria c  on p.id_categoria = c.id;



select *from vw_pizzas_cardapio;









