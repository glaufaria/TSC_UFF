<?php
class Pessoa{
    private $nome;

    function __construct($nome)
    {
        $this->nome = $nome;
    }
    function getNome(){
        return $this->nome;
    }
}
class Paciente extends Pessoa{ }
class Medico extends Pessoa{ }

class ReceitaMedica{
    private $medico;
    private $paciente;
    private $receita = Array();

    function __construct($medico,$paciente)
    {
        $this->medico = $medico;
        $this->paciente = $paciente;
    }
    function __destruct()
    {
        echo("Médico: ".$this->medico->getNome() . "</br>");
        echo("Paciente: ".$this->paciente->getNome(). "</br>");

        echo ("<br/>RECEITA <br/>");
        for($i=0;$i<=count($this->receita)-1;$i+=2){
            print_r($this->receita[$i]->getNomeMedicamento()." ");
            print_r($this->receita[$i+1]->getQuantidade());
            print_r($this->receita[$i+1]->getUnidadeMedida()."<br/>");
        }
    }
    function adicionar($medicamento,$dosagem){
        array_push($this->receita,$medicamento,$dosagem);
    }


}
class Medicamento{
    private $nome;

    function __construct($medicacao)
    {
       $this->nome = $medicacao;
    }
    function getNomeMedicamento(){
        return $this->nome;
    }

}
class Dosagem{
    private $quantidade;
    private $unidadeMedida;

    function __construct($quantidade,$unidadeMedida)
    {
        $this->quantidade = $quantidade;
        $this->unidadeMedida = $unidadeMedida;
    }
    function getQuantidade(){
        return $this->quantidade;
    }
    function getUnidadeMedida(){
        return $this->unidadeMedida;
    }

}

$receitaMedica = new ReceitaMedica(new Medico("Flavio"),new Paciente("Silva"));
$receitaMedica-> adicionar(new Medicamento("Aspirina"),new Dosagem(20, "mg"));

?>