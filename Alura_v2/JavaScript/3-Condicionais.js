//console.log("Trabalhando com condicionais");
const listaDeDestinos = new Array(
    `Rio de Janeiro`,
    `Salvador`,
    `São Paulo`
);

//Declarando a idade do comprador
const idadeComprador = 15;
const estaAcompanhada = true;

if (idadeComprador >= 18) {
    console.log('Comprador maior de idade')

} else if (estaAcompanhada) {
    console.log('Pessoa menor de idade, mas acompanhada');
} else {
    console.log('Pessoa menor de idade e não acompanhada');
}
console.log('Comprador menor de idade');


//console.log(listaDeDestinos);