listaDeDestinos = new Array (
    `São Paulo`,
    `Salvador`,
    `Rio de Janeiro`
);

idade = 18;
estaAcompanhada = true;
destino = "Salvador";
destinoExiste = (idade >=18 || estaAcompanhada);

for (let i = 0; i < 3; i++) {
    if(listaDeDestinos[i] == destino) {
        destinoExiste = true;
    }
}