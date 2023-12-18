<?php
// Conecte ao banco de dados SQLite3
$bancoDados = new SQLite3('nome-do-banco-de-dados.db');

// Crie a tabela se não existir
$bancoDados->exec('
    CREATE TABLE IF NOT EXISTS agendamentos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT NOT NULL,
        email TEXT NOT NULL,
        data TEXT NOT NULL,
        horario TEXT NOT NULL,
        servico TEXT NOT NULL,
        comentario TEXT
    )
');

// Receba os dados do formulário
$nome = $_POST['nome'];
$telefone = $_POST['telefone'];
$email = $_POST['email'];
$data = $_POST['data'];
$horario = $_POST['horario'];
$servico = $_POST['servico'];
$comentario = $_POST['comentario'];

// Insira os dados na tabela
$bancoDados->exec("
    INSERT INTO agendamentos (nome, telefone, email, data, horario, servico, comentario)
    VALUES ('$nome', '$telefone', '$email', '$data', '$horario', '$servico', '$comentario')
");

// Feche a conexão com o banco de dados
$bancoDados->close();

// Redirecione de volta à página principal ou faça qualquer outra coisa necessária
header('Location: index.html');
?>
