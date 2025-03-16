<?php
error_reporting(0); //Tiro os erros pelo funcionamento de vários forms no mesmo arquivo
ini_set('display_errors', 0); //Tiro os erros pelo funcionamento de vários forms no mesmo arquivo

//Exercício 1
echo "Exercício 1 - Soma: <br><br>";

if ($_GET['sNumber1'] != null || $_GET['sNumber2'] != null) {
    $sNumber1 = $_GET['sNumber1'];
    $sNumber2 = $_GET['sNumber2'];

    $soma = $sNumber1 + $sNumber2; 
    echo "A soma de $sNumber1 + $sNumber2 é: $soma. <br><br><br>"; 
} else {
    echo"Você está fazendo outro exercício no momento! <br><br><br>";
}

//Exercício 2
echo "Exercício 2 - Apresentação: <br><br>";

if ($_POST['aNome'] != null || $_POST['aIdade'] != null) {
    $aNome = $_POST['aNome'];
    $aIdade = $_POST['aIdade'];

    echo"Olá, meu nome é $aNome, e tenho $aIdade anos. <br><br><br>";
} else {
    echo"Você está fazendo outro exercício no momento! <br><br><br>";
}

//Exercício 3
echo "Exercício 3 - Par ou ímpar: <br><br>";

if ($_GET['piNumber'] != null) {
    $piNumber = $_GET['piNumber'];

    if ($piNumber % 2 == 0) {
        echo "O valor $piNumber é PAR. <br><br><br>";
    } else {
        echo "O valor $piNumber é ÍMPAR. <br><br><br>";
    }
} else {
    echo"Você está fazendo outro exercício no momento! <br><br><br>";
}

//Exercício 4   
echo "Exercício 4 - Fahrenheit: <br><br>";

if ($_GET['fNumber'] != null) {
    $fNumber = $_GET['fNumber'];
    $celsius = ($fNumber - 32) * 5/9;

    echo "O valor de $fNumber em Graus Celsius é $celsius C°. <br><br><br>";
} else {
    echo"Você está fazendo outro exercício no momento! <br><br><br>";
}

//Exercício 5  
echo "Exercício 5 - Tabuada: <br><br>";

if ($_POST['tNumber'] != null) {
    $tNumber = $_POST['tNumber'];
    
    for($i = 1; $i <= 10; $i++) {
        $calculoMult = $tNumber * $i;
        echo "$tNumber x $i = $calculoMult <br>";
    }
    echo "<br><br><br>";
} else {
    echo"Você está fazendo outro exercício no momento! <br><br><br>";
}

//Exercício 6   
echo "Exercício 6 - Metros para Centímetros: <br><br>";

if ($_GET['mcNumber'] != null) {
    $mcNumber = $_GET['mcNumber'];
    $centimetros = $mcNumber * 100;

    echo "O valor em metros de $mcNumber m em centímetros é $centimetros cm. <br><br><br>";
} else {
    echo"Você está fazendo outro exercício no momento! <br><br><br>";
}

//Exercício 7  
echo "Exercício 7 - Real para Dólar: <br><br>";

if ($_POST['rdNumber'] != null) {
    $rdNumber = $_POST['rdNumber'];
    $dolar = $rdNumber / 5;

    echo "O valor de R$$rdNumber é $$dolar em dólares. <br><br><br>";
} else {
    echo"Você está fazendo outro exercício no momento! <br><br><br>";
}

//Exercício 8 
echo "Exercício 8 - Cálculo Área Triângulo: <br><br>";

if ($_GET['base'] != null || $_GET['altura'] != null) {
    $base = $_GET['base'];
    $altura = $_GET['altura'];
    $areat = ($base * $altura) / 2;

    echo "O valor da Área do Triângulo é $areat cm². <br><br><br>";
} else {
    echo"Você está fazendo outro exercício no momento! <br><br><br>";
}  

//Exercício 9 
echo "Exercício 9 - Cálculo Área Círculo: <br><br>";

if ($_POST['raio'] != null) {
    $raio = $_POST['raio'];
    $areac = 3.14 * ($raio ** 2);

    echo "O valor da Área do Círculo é $areac cm². <br><br><br>";
} else {
    echo"Você está fazendo outro exercício no momento! <br><br><br>";
}

//Exercício 10
echo "Exercício 10 - Verificação Número: <br><br>";

if ($_GET['vnNumber'] != null) {
    $vnNumber = $_GET['vnNumber'];
    if ($vnNumber == 0) {
        echo"O valor $vnNumber é 0. <br><br><br>";
    } elseif ($vnNumber < 0) {
        echo"O valor $vnNumber é NEGATIVO. <br><br><br>";
    } elseif ($vnNumber > 0) {
        echo"O valor $vnNumber é POSITIVO. <br><br><br>";
    }
    
} else {
    echo"Você está fazendo outro exercício no momento! <br><br><br>";
}  

//Exercício 11
echo "Exercício 11 - Desconto: <br><br>";

if ($_POST['preco'] != null) {
    $preco = $_POST['preco'];
    $qtdDesconto = 10;
    $desconto = ($preco / 100) * $qtdDesconto;
    $aplicacao = $preco - $desconto;

    echo "O valor do produto que custa R$$preco, com $qtdDesconto% de desconto resulta em: R$$aplicacao. <br><br><br>";
} else {
    echo"Você está fazendo outro exercício no momento! <br><br><br>";
}

//Exercício 12
echo "Exercício 12 - Verificação de Idade: <br><br>";

if ($_GET['vIdade'] != null) {
    $vIdade = $_GET['vIdade'];
    
    if ($vIdade < 18) {
        echo "Você tem $vIdade e é menor de idade. <br><br><br>";
    } else {
        echo "Você tem $vIdade e é maior de idade. <br><br><br>";
    }
    
} else {
    echo"Você está fazendo outro exercício no momento! <br><br><br>";
}  

//Exercício 13
echo "Exercício 13 - IMC: <br><br>";

if ($_POST['peso'] != null || $_POST['imcAltura'] != null) {
    $peso = $_POST['peso'];
    $imcAltura = $_POST['imcAltura'];
    $calculoImc = $peso / ($imcAltura ** 2);
    $imc = number_format($calculoImc, 2, ',', '');

    if($calculoImc < 18.5) {
        echo "Seu IMC é $imc e você está com Baixo Peso.";
    } elseif ($imc >= 18.5 && $imc <= 24.99) {
        echo "Seu IMC é $imc e você está com o peso Normal.";
    } elseif ($imc >= 25 && $imc <= 29.99) {
        echo "Seu IMC é $imc e você está com Sobre Peso.";
    } elseif ($imc >= 30) {
        echo "Seu IMC é $imc e você está com Obesidade.";
    }
} else {
    echo"Você está fazendo outro exercício no momento! <br><br><br>";
}

//Exercício 14
echo "Exercício 14 - Cálculo Idade: <br><br>";

if (!empty($_GET['data'])) {
    $data = $_GET['data'];
    $dataNasc = new DateTime($data);
    $dataAtual = new DateTime();
    $idade = $dataAtual->diff($dataNasc)->y;

    echo "Você possui $idade anos.";    
} else {
    echo"Você está fazendo outro exercício no momento! <br><br><br>";
}  



?>

