<!DOCTYPE html>
<html lang="pt-br">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cadastro</title>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
</head>
<body class="container mt-5">
    <h2 class="mb-4">Cadastro Alunos!</h2>
    <p class="mb-4">Para cadastrar novos alunos, preencha os dados abaixo, e clique em Cadastrar:</p>
    <form action="" method="POST">
        <div class="row">
            <div class="col-md-3 col-12 col-sm-12">
                <div class="form-group">
                    <label for="ra">R.A.: </label>
                    <input class="form-control" placeholder="Digite o R.A.:" type="number" id="ra" name="ra">
                </div>
            </div>
            <div class="col-md-3 col-12 col-sm-12">
                <div class="form-group">
                    <label for="nome">Nome: </label>
                    <input class="form-control" placeholder="Digite o Nome:" type="text" id="nome" name="nome">
                </div>
            </div>
            <div class="col-md-3 col-12 col-sm-12">
                <div class="form-group">
                    <label for="idade">Idade: </label>
                    <input class="form-control" placeholder="Digite a Idade:" type="number" id="idade" name="idade">
                </div>
            </div>
            <div class="col-md-3 col-12 col-sm-12">
                <div class="form-group">
                    <label for="curso">Curso: </label>
                    <input class="form-control" placeholder="Digite o Curso:" type="text" id="curso" name="curso">
                </div>
            </div>
        </div>  
        <div class="d-flex justify-content-between">
            <div>
                <button type="submit" name="cadastrar" class="btn btn-primary">Cadastrar</button>
                <a href="aluno_exclusao.php" class="btn btn-danger">Exclusão de Cadastro</a>
            </div>
            <a href="index.php" class="btn btn-secondary">Voltar para Pesquisa</a>
        </div>
    </form>
    <?php
    $conexao = new mysqli("localhost", "root", "", "ite");

    if (isset($_POST['cadastrar'])) {
        $ra = $_POST['ra'] ?? "";
        $nome = $_POST['nome'] ?? "";
        $idade = $_POST['idade'] ?? "";
        $curso = $_POST['curso'] ?? "";

        if (!empty($ra) && !empty($nome) && !empty($idade) && !empty($curso)) {
            $conferenciaAlunoNovo = "SELECT * FROM alunos WHERE ra = '$ra';";
            $conferir = $conexao->query($conferenciaAlunoNovo);
            $cadastro = false;
        
            if ($conferir->num_rows > 0) {
                echo "
                <div class='bg-danger mt-4 rounded text-center w-100 p-3 mt-5'>
                    <p class='text-white m-0 d-flex justify-content-center align-items-center h-100'>Esse R.A. já está cadastrado, digite novamente...</p>
                </div>
                ";
            } else {
                $cadastrarAluno = "INSERT INTO alunos (ra, nome, idade, curso) VALUES ('$ra', '$nome', '$idade', '$curso');";
                $cadastro = $conexao->query($cadastrarAluno);

                if($cadastro) {
                    echo "
                    <div class='bg-success mt-4 rounded text-center w-100 p-3 mt-5'>
                        <p class='text-white m-0 d-flex justify-content-center align-items-center h-100'>Cadastro Realizado com Sucesso!!</p>
                    </div>
                    ";
                } else {
                    echo "
                    <div class='bg-danger mt-4 rounded text-center w-100 p-3 mt-5'>
                        <p class='text-white m-0 d-flex justify-content-center align-items-center h-100'>Erro no Cadastro, Tente Novamente!!</p>
                    </div>
                    ";
                }
            }
        } else {
            echo "
            <div class='bg-warning mt-4 rounded text-center w-100 p-3 mt-5'>
                <p class='text-black m-0 d-flex justify-content-center align-items-center h-100'>Informações Incompletas</p>
            </div>
            ";
        }
    }
    ?>
</body>
</html>