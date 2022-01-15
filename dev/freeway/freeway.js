let imagemDaEstrada;
let imagemDoAtor;
let imagemCarro;

//variaveis do carro
xCarro = 420;

function preload(){
  imagemDaEstrada = loadImage("imagens/estrada.png");
}

function setup() {
  createCanvas(500, 400);
}

function draw() {
  background(imagemDaEstrada);
  image(imagemDoAtor, 100, 366, 30, 30);
  image(ImagemCarro, xCarro, 40 ,50, 40 );
}

function mostraAtor(){
  imagemDoAtor = loadImage("imagens/ator-1.png");
}

function mostraCarro(){
  ImagemCarro = loadImage("imagens/carro-1.png")
}
