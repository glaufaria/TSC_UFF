<?php
Function listarImagens($saidaDoComando) {
    $linhas = (explode("\n",$saidaDoComando));
    $conteudo = separaLinhas($linhas);
    echo("<table border = 3>");
        $tableHeader = tableHeader($conteudo[0]);
        $tableHeader = tableBody($conteudo);
    echo("</table>");   
}  
function separaLinhas($linhas){
    for ($i=0;$i<=count($linhas)-1; $i++){
        $conteudo[$i] = (explode(";",$linhas[$i]));
    }
    return $conteudo;
}

function tableHeader($conteudo){
    echo("<tr>");
    for($i=0; $i <= count($conteudo)-1; $i++){
        echo("<th>".$conteudo[$i]."</th>");
    }
    echo("</tr>");
}

function tableBody($conteudo){
    for($i=1; $i <= count($conteudo)-1; $i++){
        echo("<tr>");
        for($j=0; $j <= count($conteudo[$i])-1; $j++){
        echo("<td>".$conteudo[$i][$j]."</td>");
        }
        echo("</tr>");
    }
}

 $quadro = ("REPOSITORY;TAG IMAGE ID;CREATED;SIZE
 mysql 5.7;b598110d0fff;6 weeks ago;435MB
 wordpress 5.3.2-php7.2-apache;6669a7a94d1b;2 months ago;539MB");

 ListarImagens($quadro);
 
 ?>