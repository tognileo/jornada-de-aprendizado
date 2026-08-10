CREATE TABLE aluno (
id INT PRIMARY KEY NOT NULL auto_increment,
    nome varchar (44),
    genero varchar (45)
);
CREATE TABLE turma (
id INT PRIMARY KEY NOT NULL auto_increment,
    alunos_turma varchar (45),
    sala varchar (45),
    periodo varchar(45),
    aluno_id int,
    foreign key (aluno_id) references aluno(id)
);



select a.nome, a.genero as aluno,
t.alunos_turma, t.sala ,t.periodo

from turma t inner join aluno a

on t.aluno_id = a.id;



INSERT INTO aluno (nome, genero)
VALUES ('leo', 'sei_la');


INSERT INTO turma (alunos_turma, sala,periodo,aluno_id)
VALUES ('45', '203',"matutino",1);

