/*
PHP
$funcionario = new Funcionario();
$funcionario->setNome('Fulano);
$funcionario->setHorasExtras(10);
$funcionario->setValorDaHora(20);

echo $funcionario->getSalarioEfetivo();
*/

import {Funcionario} from "./Funcionario.js";

const funcionario1 = new Funcionario();

funcionario1.nome = "Juliana";
funcionario1.salarioBase = 8000;
funcionario1.horasExtras = 20;
funcionario1.valorDaHora = 100;

console.log(funcionario1.salarioEfetivo());
