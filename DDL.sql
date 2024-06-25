create database db_dadosRMI;
use db_dadosRMI;

create table tb_usuario (
	id_user INT NOT NULL auto_increment,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(50) NOT NULL,
    primary key (id_user)
);

create table tb_servidor_grupo (
	id_grupo int not null auto_increment,
    descricao varchar(1000) null,
    grupo_adm_user int not null,
    primary key (id_grupo),
    CONSTRAINT grupoAdm_user
		FOREIGN KEY ( grupo_adm_user )
		REFERENCES tb_usuario( id_user)
);

create table tb_grupo (
	servidor_id_grupo int not null,
    servidor_id_user int not null,
	CONSTRAINT servidorID_grupo
		FOREIGN KEY ( servidor_id_grupo )
		REFERENCES tb_servidor_grupo( id_grupo),
	CONSTRAINT servidorID_user
		FOREIGN KEY ( servidor_id_user )
		REFERENCES tb_usuario( id_user)
);

create table tb_servidor_privado (
	id_privado int not null auto_increment,
    servidor_id_user1 int not null,
    servidor_id_user2 int not null,
	primary key (id_privado),
	CONSTRAINT servidorID_user1
		FOREIGN KEY ( servidor_id_user1 )
		REFERENCES tb_usuario( id_user),
	CONSTRAINT servidorID_user2
		FOREIGN KEY ( servidor_id_user2 )
		REFERENCES tb_usuario( id_user)
);

DROP DATABASE db_dadosRMI;

