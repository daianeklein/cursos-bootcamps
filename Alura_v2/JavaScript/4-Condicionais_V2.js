const idadeComprador = 17;
const estaAcompanhado = false
const temPassagemComprada = true

if (idadeComprador >= 18 || estaAcompanhado) {
    console.log("Boa viagem")
} else {
    console.log("Passagem não pode ser vendida")
};

console.log("Embarque \n");
if (idadeComprador >= 18 && temPassagemComprada) {
    console.log("Boa viagem");
} else {
    console.log("Não pode embarcar")
}