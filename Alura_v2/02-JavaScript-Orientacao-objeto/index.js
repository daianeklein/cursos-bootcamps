class Cliente {
    nome;
    cpf;
    agencia;
    #saldo;
}

class ContaCorrente {
    agencia;
    conta;
    #saldo = 0;

    //operacao
    sacar(valor) {
        if(this.#saldo >= valor) {
            this.#saldo -= valor;
        }
    }

    //parametros ou argumentos
    depositar(valor){
        if(valor > 0) {
            this.#saldo += valor;
        }
    }
}


const cliente1 = new Cliente();

cliente1.nome = "Ricardo";
cliente1.cpf = 12312312312;
cliente1.agencia = 1001;
cliente1.saldo = 0;

const contaCorrenteRicardo = new ContaCorrente();
//contaCorrenteRicardo.#saldo = 100;
contaCorrenteRicardo.agencia = 1001;

console.log(cliente1);
console.log(contaCorrenteRicardo);
contaCorrenteRicardo.sacar(50);
console.log(contaCorrenteRicardo);

contaCorrenteRicardo.sacar(200);
console.log(contaCorrenteRicardo);
