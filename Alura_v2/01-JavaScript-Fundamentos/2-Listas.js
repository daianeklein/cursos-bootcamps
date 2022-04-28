//criando lista
const ListaDestinos = new Array(
   `Salvador`,
    `São Paulo`,
    `Rio de Janeiro`
);

console.log(ListaDestinos)

//adicionando novo elemento
ListaDestinos.push(`Curitiba`);
console.log(ListaDestinos)

//removendo elemento
ListaDestinos.splice(1, 1)
console.log(ListaDestinos)

console.log(ListaDestinos[1]) //mostrando apenas RJ