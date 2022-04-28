listaDeDestinos = new Array (
    `São Paulo`,
    `Salvador`,
    `Rio de Janeiro`
);

const idadeComprador = 18;
const estaAcompanhado = true;
let temPassagemComprada = true;
const destino = "Salvador"

const PodeComprar = idadeComprador >= 18 || estaAcompanhado == true;

let contador = 0;
while(contador <3){
    if (listaDeDestinos[contador] == destino){
        console.log("Destino existe")
} else {
    console.log("Destino não existe")
}
    contador += 1
}
