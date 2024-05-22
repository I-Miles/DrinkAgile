-- procedures cadastrar
delimiter //
create procedure insere_produto(
in p_nomeprod varchar(100),
in p_valorprod float,
in p_estoqueprod int
)
begin
insert into produtos( nome, preco, estoque )
values
( p_nomeprod, p_valorprod, p_estoqueprod);
end//
delimiter ;

DELIMITER //
CREATE PROCEDURE insere_func( 
IN p_nome VARCHAR(100),
IN p_cargo VARCHAR(50),
IN p_salario DECIMAL(10,2))
BEGIN
    INSERT INTO Funcionarios ( nome, cargo, salario) VALUES ( p_nome, p_cargo, p_salario);
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE insere_cli( 
IN p_nome VARCHAR(100),
IN p_email VARCHAR(50),
IN p_telefone int,
in p_estatus varchar(50))
BEGIN
    INSERT INTO clientes (nomecli,email,telefone,estatus) VALUES ( p_nome, p_email, p_telefone,p_estatus);
END //
DELIMITER ;

delimiter //
create procedure insere_fornecedor(
in p_nomeforn varchar(100),
in p_emailforn varchar(100),
in p_telefoneforn int,
in p_idprod int)
begin
if exists(select 1 from produtos where idprod = p_idprod) then insert into fornecedores( nomeforn,emailforn,telefoneforn,idprod)
values
( p_nomeforn, p_emailforn, p_telefoneforn, p_idprod);
select 'Fornecedor cadastrado  com sucesso' as mensagem;
else 
select 'Fornecedor não encontrado' as mensagem;
end if;
end//
delimiter ;

-- procedure procurar funcionario
delimiter //

create procedure buscarfuncionario (
in nomefunc int
)
begin
if exists (select 1 from funcionarios where nome = nomefunc) then
select id, nome, cargo, salario from funcionarios
where nome = nomefunc;
else
select 'funcionário não encontrado.' as mensagem;
end if;
end //
delimiter ;;

-- update
DELIMITER //
CREATE PROCEDURE procalterarfuncionario (
    IN id_funcionario INT,
    IN novo_nome VARCHAR(255),
    IN novo_cargo VARCHAR(255),
    IN novo_salario DECIMAL(10, 2)
)
BEGIN
    IF EXISTS (SELECT 1 FROM funcionarios WHERE id = id_funcionario) THEN
        UPDATE funcionarios
        SET nome = novo_nome, cargo = novo_cargo, salario = novo_salario
        WHERE id = id_funcionario;
       
        SELECT "Funcionário alterado com sucesso!" AS mensagem;
    ELSE
        SELECT "Funcionário não encontrado." AS mensagem;
    END IF;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE procalterarclientes (
    IN id_clientes INT,
    IN novo_nome VARCHAR(50),
    IN novo_email VARCHAR(255),
    IN novo_telefone VARCHAR(30)
)
BEGIN
    IF EXISTS (SELECT 1 FROM clientes WHERE idcli = id_clientes) THEN
        UPDATE clientes
        SET nomecli = novo_nome, email = novo_email, telefone = novo_telefone
        WHERE idcli = id_clientes;
       
        SELECT "Cliente alterado com sucesso!" AS mensagem;
    ELSE
        SELECT "Cliente não encontrado." AS mensagem;
    END IF;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE procalterarfornecedores(
    IN id_fornecedores INT,
    IN novo_nome VARCHAR(50),
    IN novo_email VARCHAR(255),
    IN novo_telefone VARCHAR(30),
    IN novo_idprodutos INT 
)
BEGIN
    IF EXISTS (SELECT 1 FROM fornecedores WHERE idforn = id_fornecedores) THEN
        UPDATE fornecedores
        SET nomeforn = novo_nome, emailforn = novo_email, telefoneforn = novo_telefone, idprod = novo_idprodutos
        WHERE idforn = id_fornecedores;
       
        SELECT "Fornecedor alterado com sucesso!" AS mensagem;
    ELSE
        SELECT "Fornecedor não encontrado." AS mensagem;
    END IF;
END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE procalterarprodutos(
	IN id_produtos INT,
    IN novo_nome VARCHAR(50),
    IN novo_preco VARCHAR(255),
    IN novo_estoque VARCHAR(30)
)
BEGIN
    IF EXISTS (SELECT 1 FROM produtos WHERE idprod = id_produtos) THEN
        UPDATE produtos
        SET nome = novo_nome, preco = novo_preco, estoque = novo_estoque
        WHERE idprod = id_produtos;
       
        SELECT "Produto alterado com sucesso!" AS mensagem;
    ELSE
        SELECT "Produto não encontrado." AS mensagem;
    END IF;
END //
DELIMITER ;

-- delete 
DELIMITER //
CREATE PROCEDURE procremovefuncionario( 
	IN p_id int
    )
    BEGIN
	DELETE from funcionarios
    where id = p_id;
    SELECT "Funcionário deletado com sucesso!" AS mensagem;

    END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE procremoveclientes( 
	IN p_id int
    )
    BEGIN
	DELETE from clientes
    where idcli = p_id;
    SELECT "Cliente deletado com sucesso!" AS mensagem;

    END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE procremovefornecedores( 
	IN p_id int
    )
    BEGIN
	DELETE from fornecedores
    where idforn = p_id;
    SELECT "fornecedor deletado com sucesso!" AS mensagem;

    END //
DELIMITER ;

DELIMITER //
CREATE PROCEDURE procremoveprodutos( 
	IN p_id int
    )
    BEGIN
	DELETE from produtos
    where idprod = p_id;
	SELECT "Produto deletado com sucesso!" AS mensagem;

    END //
DELIMITER ;

-- view consulta
delimiter //
create view consultar funcionario as 
select 
id as ID
nome as Nome
cargo AS Cargo
salario as Salario
from funcionarios
select * from funcionarios
delimiter ;;

delimiter //
create view consultar cliente as 
select 
idcli as ID
nomecli as Nome
email AS E-mail
telefone as Telefone
from clientes
select * from clientes
delimiter ;;

delimiter //
create view consultar produtos as 
select 
idprod as ID
nome as Nome
preco AS Preço
estoque as Estoque 
from produtos
select * from produtos
delimiter ;;

delimiter //
create view consultar fornecedores as 
select 
idforn as ID
nomeforn as Nome
emailforn AS E-mail
telefoneforn as Telefone
idprod as ID_Produto
from fornecedores
select * from fornecedores
delimiter ;;


-- View --

create view v_produtos_fornecedor as
select p.idprod, p.nomeprod, p.descprod, p.valorprod, p.estprod, p.idforn, f.nomeforn from produtos p
join fornecedores f on p.idforn = f.idforn;