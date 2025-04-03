<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
    <title>Resultado Pesquisa</title>
</head>
<body class="d-flex flex-column">
    <div class="d-flex justify-content-center align-items-center p-5 flex-grow-1">
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
                    $nome = $_GET['nome'];
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
    </div>
    <div class="d-flex justify-content-center mt-3 mb-5">
        <a href="index.html" class="btn btn-secondary">Voltar</a>
    </div>
    <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.3/dist/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"></script>
</body>
</html>