create table funcionarios(
id int primary key not null auto_increment,
nome varchar (45),
cargo varchar (45)
);
create table setores (
cod_setor int primary key not null auto_increment,
nome_setor varchar(45),
andar varchar(45),
id_funcionario int ,
foreign key (id_funcionario) references funcionarios(id)
);




select f.nome, f.cargo  as funcionarios, s.nome_setor, s.andar


from funcionarios f left  join setores s
								
on s.id_funcionario = f.id;






















