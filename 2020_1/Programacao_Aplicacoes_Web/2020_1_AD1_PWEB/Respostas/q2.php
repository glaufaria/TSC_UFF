<?php
function ocultaEmail($entrada){
	$arrayfrase = explode(" ", $entrada);

	for ($i = 0; $i < count($arrayfrase) ; $i++) {
		if (strstr($arrayfrase[$i], '@')){
			if ($i == count($arrayfrase)-1){
				$arrayfrase[$i] = "xxx.";
			}
			else{
				$arrayfrase[$i] = "xxx,";
			}

		}
		$fraseFinal[] = $arrayfrase[$i] . " ";
	}
	#return $fraseFinal;
	imprime ($fraseFinal);
}
function imprime($entrada){
	$frase = '';
	foreach ($entrada as $value) {
		$frase = $frase . $value;
	}
	$frase = $frase;
	echo $frase;
}

$frase = "Eu, Flávio fseixas@ic.uff.br, gostaria
de solicitar o cadastro de Beltrano beltrano@hotmail.com e
Sicrano sicrano@uol.com.br";

ocultaEmail($frase);
?>
