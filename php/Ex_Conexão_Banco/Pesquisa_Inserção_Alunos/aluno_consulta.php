<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pesquisa Alunos</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body class="container mt-5">
    <a href="aluno_novo.php" class="btn btn-success">NOVO</a>
    <h2 class="mb-4">Pesquisa Alunos!</h2>
    <p class="mb-3">Para consultar os alunos que você deseja encontrar, selecione o nome no campo abaixo e clique em pesquisa:</p>
    <form action="" method="get">
        <div class="form-group">
            <label for="nome">Nome do Aluno</label>
            <input type="text" class="form-control" id="nome" placeholder="Digite o nome do aluno:" name="nome">
        </div>
        <button type="submit" class="btn btn-secondary">Pesquisar</button>
    </form>
    <br><br>
    <table class="table table-bordered table-striped">
        <thead>
            <tr>
                <th>R.A.:</th>
                <th>NOME:</th>
                <th>IDADE:</th>
                <th>CURSO:</th>
            </tr>
        </thead>
        <tbody>
            <?php
                $conexao = new mysqli("localhost", "root", "", "ite");
                $nome = "";
                if (isset($_GET['nome'])) {
                    $nome = $_GET['nome'];
                }
                $sql = "SELECT * FROM alunos WHERE nome like '%$nome%'";
                $pesquisa = $conexao->query($sql);
                foreach($pesquisa as $linha)
                {
                    echo "
                    <tr>
                        <td>" . $linha['ra'] . "</td>
                        <td>" . $linha['nome'] ."</td>
                        <td>" . $linha['idade'] ."</td>
                        <td>" . $linha['curso'] . "</td>
                    </tr>
                    ";
                }
            ?>
        </tbody>
    </table>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>