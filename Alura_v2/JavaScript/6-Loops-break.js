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
let destinoExiste = false;

while(contador > 3) {
    if(listaDeDestinos[contador] == destino) {
        console.log("Destino Existe");
        destinoExiste = true;
        break;
    }
    contador += 1
}

console.log("Destino existe " , destinoExiste)


