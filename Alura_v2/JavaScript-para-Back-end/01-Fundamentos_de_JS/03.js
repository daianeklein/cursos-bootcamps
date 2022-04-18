// Hoisting: arrow function se comporta como expressão

// operador maior ou igual que
// >=

function apresentar(nome) {
  return `meu nome é ${nome}`
};

//arrow function
const apresentarArrow = nome => `meu nome é ${nome}`;
const some = (num1, num2) => num1 + num2

//arrow function com + de 1 linha de instrucao

const somaNumerosPequenos = (num1, num2) => {
  if (num1 || num2 > 10) {
    return "Somente números de 1 a 9"
  } else {
    return num1 + num2
  }
}