<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body class="container mt-5">
    <h2 class="mb-4">Exclusão de Alunos!</h2>
    <p class="mb-5">Para excluir um aluno, selecione qual o R.A. dele, confirme na tabela abaixo se é esse mesmo e clique em excluir no fim da página:</p>
    <form action="" method="POST">
    <div class="form-group d-flex align-items-center">
        <label for="ra" class="mb-0 pr-3">Digite o R.A. do aluno:</label>
        <input type="number" name="ra" id="ra" placeholder="R.A.:" class="form-control w-50 mr-3" >
        <input type="submit" value="Selecionar Aluno" class="btn btn-primary mr-3">
        <a href="aluno_novo.php" class="btn btn-secondary">Voltar para Cadastro</a>
    </div>
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
                $ra = $_POST['ra'] ?? "";

                $confirmarAluno = "SELECT * FROM alunos WHERE ra = '$ra';";
                $confirma = $conexao->query($confirmarAluno);
                foreach($confirma as $linha)
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
    <?php
    if (!empty($confirma) && $confirma->num_rows > 0) {
        echo"<form action='' method='POST'>
            <input type='hidden' name='ra' value='$ra'>
            <input type='submit' name='excluir' value='Excluir' class='btn btn-danger'>
        </form>
        ";
    }
    if (isset($_POST['excluir'])) {
        $ra = $_POST['ra'];
        $excluirAluno = "DELETE FROM alunos WHERE ra = '$ra';";
        $excluir = $conexao->query($excluirAluno);
    
        if ($excluir) {
            echo "
            <div class='bg-success mt-4 rounded text-center w-100 p-3 mt-5'>
                <p class='text-white m-0 d-flex justify-content-center align-items-center h-100'>Aluno Excluído com Sucesso!!</p>
            </div>
            ";
        } else {
            echo "
            <div class='bg-danger mt-4 rounded text-center w-100 p-3 mt-5'>
                <p class='text-white m-0 d-flex justify-content-center align-items-center h-100'>Erro na Exclusão, Tente Novamente!!</p>
            </div>
            ";
        }
    }
    ?>
</body>
</html>


