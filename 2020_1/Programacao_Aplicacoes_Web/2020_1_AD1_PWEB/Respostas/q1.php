<?php
function convertint($string){
	$arrayString = separa($string);
	for ($i = 0; $i < count($arrayString); $i++) {

		$arrayString[$i] = intval($arrayString[$i]);
	}
	return $arrayString;
}	
function separa($string){
	$string =  explode( " ", $string);
	if (conta($string) == true){
		return $string;	
	}
}

function conta($string){
	if (count($string) > 32) {
		return false;
	}
	else{
		return true;
	}
}
function main($string){
	if (calculoDaParidadePar($string) == 0){
		echo 'Paridade Par = Bit de paridade 0';
	}
	else{
		echo 'Paridade Impar = Bit de paridade 1';
	}

}
function calculoDaParidadePar($string){
	$bloco = convertint($string);
	$count = 0;
	foreach ($bloco as $value) {
		if ($value == 1) {
			$count = $count+1;
		}
	}
	if ($count % 2 == 0){
		return 0;
	}
	else{
		return 1;
	}

}
#bloco de bits separados por espaços
$bytes = "1 0 1 0 1 1";
#Inicia a função main
$bytes = main($bytes);
?>
