drop database if exists drinkAgile;
create database drinkAgile;
use drinkAgile;

CREATE TABLE funcionarios (
    id INT PRIMARY KEY auto_increment,
    nome VARCHAR(100),
    cargo VARCHAR(50),
    salario DECIMAL(10,2)
);

CREATE TABLE clientes (
    idcli INT PRIMARY KEY auto_increment,
    nomecli VARCHAR(100),
    email VARCHAR(100),
    telefone VARCHAR(15),
    estatus varchar(20)
);

CREATE TABLE produtos (
    idprod INT PRIMARY KEY auto_increment,
    nome VARCHAR(100),
    preco float,
    estoque INT
);

CREATE TABLE fornecedores (
    idforn INT PRIMARY KEY auto_increment,
    nomeforn VARCHAR(100),
    emailforn VARCHAR(100),
    telefoneforn varchar(100),
    idprod int,
    foreign key (idprod) references produtos(idprod));

create table historicovendas(
idvenda INT PRIMARY KEY,
idcli INT,
idfunc INT, 
valor_venda float,
FOREIGN KEY(idcli) REFERENCES Clientes(idcli),
FOREIGN KEY(idfunc) REFERENCES Funcionarios(id)
);
 -- inserts
insert into produtos(nome,preco,estoque)
values("cerveja","15.00","90");

insert into fornecedores(nomeforn,emailforn,telefoneforn,idprod)
values ("jorge","jorge@gmail.com","(17)988076220","1");

insert into funcionarios(nome,cargo,salario)
values("isaac","vendedor","3000");

insert into clientes(nomecli,email,telefone)
values("felipe","felipe016@gmail.com","(17)1899834");

 -- inserts
insert into produtos(nome,preco,estoque)
values("cerveja","15.00","90");

insert into fornecedores(nomeforn,emailforn,telefoneforn,idprod)
values ("jorge","jorge@gmail.com","(17)988076220","1");

insert into funcionarios(nome,cargo,salario)
values("isaac","vendedor","3000");

insert into clientes(nomecli,email,telefone, estatus)
values("felipe","felipe016@gmail.com","(17)1899834", "Ativo");


-- CLIENTES

CREATE TABLE HistoricoClientes (
    idHistorico INT AUTO_INCREMENT PRIMARY KEY,
    idClientes INT,
    nomeAntigo VARCHAR(100),
    emailAntigo VARCHAR(100),
    telefoneAntigo VARCHAR(15),
    estatusAntigo VARCHAR(20),
    nomeNovo VARCHAR(100),
    emailNovo VARCHAR(100),
    telefoneNovo VARCHAR(15),
    estatusNovo VARCHAR(20),
    dataAlteracao TIMESTAMP
);
DELIMITER //
CREATE TRIGGER trig_registro_historico_clientes AFTER UPDATE ON clientes
FOR EACH ROW
BEGIN
    INSERT INTO HistoricoClientes (idClientes, nomeAntigo, emailAntigo, telefoneAntigo, estatusAntigo, nomeNovo, emailNovo, telefoneNovo, estatusNovo, dataAlteracao)
    VALUES (OLD.idcli, OLD.nomecli, OLD.email, OLD.telefone, OLD.estatus, NEW.nomecli, NEW.email, NEW.telefone, NEW.estatus, NOW());
END//
DELIMITER ;

update clientes
set nomecli = 'Cleitin'
where idcli = 3;

select *from HistoricoClientes;


UPDATE clientes SET nomecli = 'Emanuelly', email = 'manujappin@gmail.com', telefone = '(17)9232323', estatus ="ativo" WHERE estatus = '';

UPDATE fornecedores SET nomeforn = 'Felipe', emailforn = 'felipin@gmail.com', telefoneforn = '(17)12345678' WHERE nomeforn = 'Juan';

UPDATE produtos SET nome = 'Pinga', preco = '2.00', estoque = '12' WHERE nome = 'Chopp';


ALTER TABLE clientes
ADD COLUMN Status VARCHAR(50);

UPDATE clientes
SET Status = "Ativo"
WHERE idcli > 0;

DELIMITER //
CREATE PROCEDURE procinativarCliente (
    IN p_idcli INT
)
BEGIN
    UPDATE clientes
    SET estatus = 'Inativo'
    WHERE idcli = p_idcli;
END //
DELIMITER ;


SELECT * FROM CLIENTES;


-- FUNCIONARIOS

CREATE TABLE HistoricoFuncionarios (
    idHistorico INT AUTO_INCREMENT PRIMARY KEY,
    idFuncionario INT,
    nomeAntigo VARCHAR(100),
    cargoAntigo VARCHAR(100),
    salarioAntigo DECIMAL(10, 2),
    nomeNovo VARCHAR(100),
    cargoNovo VARCHAR(100),
    salarioNovo DECIMAL(10, 2),
    dataAlteracao TIMESTAMP
);

DELIMITER //
CREATE TRIGGER trig_registro_historico_funcionario AFTER UPDATE ON funcionarios
FOR EACH ROW
BEGIN
    INSERT INTO HistoricoFuncionarios (idFuncionario, nomeAntigo, cargoAntigo, salarioAntigo, nomeNovo, cargoNovo, salarioNovo, dataAlteracao)
    VALUES (OLD.id, OLD.nome, OLD.cargo, OLD.salario, NEW.nome, NEW.cargo, NEW.salario, NOW());
END//
DELIMITER ;



-- FORNECEDOR

CREATE TABLE HistoricoFornecedor (
    idHistorico INT AUTO_INCREMENT PRIMARY KEY,
    idFornecedor INT,
    nomeAntigo VARCHAR(100),
    emailAntigo VARCHAR(100),
    telefoneAntigo VARCHAR(100),
    nomeNovo VARCHAR(100),
    emailNovo VARCHAR(100),
    telefoneNovo VARCHAR(100),
    dataAlteracao TIMESTAMP
);

DELIMITER //
CREATE TRIGGER trg_registro_historico_fornecedor AFTER UPDATE ON fornecedores
FOR EACH ROW
BEGIN
    INSERT INTO HistoricoFornecedor (idFornecedor, nomeAntigo, emailAntigo, telefoneAntigo, nomeNovo, emailNovo, telefoneNovo, dataAlteracao)
    VALUES (OLD.idforn, OLD.nomeforn, OLD.emailforn, OLD.telefoneforn, NEW.nomeforn, NEW.emailforn, NEW.telefoneforn, NOW());
END//
DELIMITER ;



-- PRODUTOS

CREATE TABLE historicoProdutos (
    idHistorico INT AUTO_INCREMENT PRIMARY KEY,
    NomeAntigo varchar(100),
    idProdAntigo INT,
    precoAntigo FLOAT,
    estoqueAntigo INT,
    NomeNovo varchar (100),
    idProdNovo INT,
    precoNovo FLOAT,
    estoqueNovo INT,
    dataAlteracao TIMESTAMP
);

DELIMITER //
CREATE TRIGGER trg_registro_historico_prod AFTER UPDATE ON produtos
FOR EACH ROW
BEGIN
    INSERT INTO historicoProdutos (NomeAntigo, NomeNovo, idProdAntigo, idProdNovo, precoAntigo, precoNovo, estoqueAntigo, estoqueNovo, dataAlteracao)
    VALUES (OLD.nome, NEW.nome, OLD.idprod, NEW.idprod, OLD.preco, NEW.preco, OLD.estoque, NEW.estoque, NOW());
END//
DELIMITER ;




