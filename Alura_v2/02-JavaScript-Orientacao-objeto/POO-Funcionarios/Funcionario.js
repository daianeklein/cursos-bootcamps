/*export class Cliente{
    nome;
    _cpf;

    get cpf(){
        return this._cpf;
    }

    constructor(nome, cpf){
        this.nome = nome;
        this._cpf = cpf;
    }
}*/

export class Funcionario {
    nome;
    salarioBase;
    horasExtras;
    valorDaHora;

    get nome(){
        return this.nome;
    }

    salarioEfetivo(){
        return this.salarioBase + (this.horasExtras * this.valorDaHora)
    }        
}
