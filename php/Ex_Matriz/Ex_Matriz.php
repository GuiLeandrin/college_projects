<?php

$array = [23,123,65,83,74,33,45,765,96,61,45,76,45,23,52,43,3,35,12,32,523,54,68,18,12];

//Exercício 1//
echo "Exercício 1:";
echo "<br>";
$comp = 0;
$indicematriz = 0;
for($i = 0; $i <= 4; $i++)
{
    if ($comp == 0) 
    {
        $comp = $comp + 4;
    } else 
        {
            $comp = $comp + 5;
        }
    for(; $indicematriz <= $comp; $indicematriz++)
    {
        echo "$array[$indicematriz] | ";
    }
    echo "<br>";
}
echo "<br>";

//Exercício 2//
echo "Exercício 2:";
echo "<br>";
$multiplicacao = $array[0];
$indicem = 6;
for($i = 0; $i <= 3; $i++)
{
    $multiplicacao = $multiplicacao * $array[$indicem];
    $indicem = $indicem + 6;
}
echo "A Multiplicação da diagonal da matriz ($array[0],$array[6],$array[12],$array[18],$array[24]) é: $multiplicacao <br><br>";

//Exercício 3//
echo "Exercício 3:";
echo "<br>";
$soma = $array[4];
$indices = 9;
for($i = 0; $i <= 3; $i++)
{
    $soma = $soma + $array[$indices];
    $indices= $indices + 5;
}
echo "A Soma da última coluna da matriz ($array[4],$array[9],$array[14],$array[19],$array[24]) é: $soma <br><br>";

//Exercício 4//
echo "Exercício 4:";
echo "<br>";
$indiced = 0;
$linha = 0;
for($i = 0; $i <=4; $i++)
{
    $coluna = 0;
    for($j = 0; $j <= 4; $j++)
    {
        if($array[$indiced] % 2 == 0) {
            echo "O Valor $array[$indiced] é PAR, está na Linha: $linha e Coluna: $coluna. <br>";
        } else {
            echo "O Valor $array[$indiced] é ÍMPAR, está na Linha: $linha e Coluna: $coluna. <br>";
        }
        $indiced = $indiced + 1;
        $coluna = $coluna + 1;
    }
    $linha = $linha + 1;
}

?>
