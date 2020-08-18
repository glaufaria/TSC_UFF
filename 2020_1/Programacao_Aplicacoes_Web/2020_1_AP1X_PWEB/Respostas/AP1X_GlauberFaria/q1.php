<?php
function y($x){
    #Expressao Y
    return $y = pow($x,2);
}
function check_par($func_name){
    #valor ficticio para X
    $x=2;

    $par = $func_name($x) == $func_name (-$x);
    $impar = $func_name($x) == -$func_name (-$x);
    
    if ($par == true){
        echo "Par";
    }
    elseif($impar == true){
        echo "Impar";
    }
    else{
        echo "ERRO";
    }
}
check_par('y');
?>