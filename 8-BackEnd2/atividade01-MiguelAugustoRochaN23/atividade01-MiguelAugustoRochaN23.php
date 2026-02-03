<?php
class Computador {
    public $marca;
    public $modelo;
    public $cor;
    public $RAM;
    public $armazenamento;
    
    public function Ligar() {
        return "O computador " . $this->marca . " " . $this->modelo . " está ligado.";
    }

    public function Desligar() {
        return "O computador " . $this->marca . " " . $this->modelo . " está desligado.";
    }

    public function Projetar() {
        return "O computador " . $this->marca . " " . $this->modelo . " está projetando.";
    }
}

class Celular {
    public $marca;
    public $modelo;
    public $cor;
    public $RAM;
    public $armazenamento;
    
    public function Ligar() {
        return "O celular " . $this->marca . " " . $this->modelo . " está ligado.";
    }

    public function Desligar() {
        return "O celular " . $this->marca . " " . $this->modelo . " está desligado.";
    }

    public function Fotografar() {
        return "O celular " . $this->marca . " " . $this->modelo . " tirou uma foto.";
    }
}

class Mesa {
    public $material;
    public $cor;
    public $formato;
    public $altura;
    public $largura;
    
    public function Apoiar() {
        return "A mesa de " . $this->material . " está apoiando objetos.";
    }

    public function Colocar() {
        return "A mesa de " . $this->material . " está colocada.";
    }

    public function Limpar() {
        return "A mesa de " . $this->material . " foi limpa.";
    }
}

class Caderno {
    public $marca;
    public $numeroDePaginas;
    public $cor;
    public $formato;
    public $tipoDeCapa;
    
    public function Abrir() {
        return "O caderno " . $this->marca . " está aberto.";
    }

    public function Escrever() {
        return "Escrevendo no caderno " . $this->marca . ".";
    }

    public function Fechar() {
        return "O caderno " . $this->marca . " está fechado.";
    }
}

class Mochila {
    public $marca;
    public $cor;
    public $capacidade;
    public $numeroDeCompartimentos;
    public $material;
    
    public function Abrir() {
        return "A mochila " . $this->marca . " está aberta.";
    }

    public function Guardar() {
        return "Guardando itens na mochila " . $this->marca . ".";
    }

    public function Fechar() {
        return "A mochila " . $this->marca . " está fechada.";
    }
}
?>