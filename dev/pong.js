//variaveis da bolinha
let xBolinha = 300;
let yBolinha = 200;
let diametro = 25;
let raio = diametro / 2;

//variaveis da velocidade da bolinha
let velocidadeXBolinha = 6;
let velocidadeYBolinha = 6;

//variaveis da raquete
let xRaquete = 5;
let yRaquete = 150;
let raqueteComprimento = 10;
let raqueteAltura = 90;

//variaveis do oponente
let xRaqueteOponente = 585;
let yRaqueteOponente = 150;
let velocidadeYOponente;

let atingiu = false; 

//placar do jogo
let meusPontos = 0
let pontosDoOponente = 0

function setup() { 
  createCanvas(600, 400);
}

function draw() {
  background(10);
  mostraBolinha();
  movimentaBolinha();
  verificacaoColisaoBorda();
  mostraRaquete(xRaquete, yRaquete);
  movimentaMinhaRaquete();
  //verificaColisaoRaquete();
  verificaColisaoRaquete(xRaquete, yRaquete);
  verificaColisaoRaquete(xRaqueteOponente, yRaqueteOponente);
  mostraRaqueteOponente(xRaqueteOponente, yRaqueteOponente);
  movimentaRaqueteOponente();
  incluiPlacar();
  marcaPonto();
  
}


function mostraBolinha() {
  circle(xBolinha, yBolinha, diametro);
}

function movimentaBolinha() {
  xBolinha += velocidadeXBolinha;
  yBolinha += velocidadeYBolinha;
}

function verificacaoColisaoBorda() {
  if (xBolinha + raio > width ||
    xBolinha - raio < 0) {
    velocidadeXBolinha *= -1;
  }
  if (yBolinha + raio > height ||
    yBolinha - raio < 0) {
    velocidadeYBolinha *= -1
  }
  }

function mostraRaquete(x, y) {
  rect(x, y, raqueteComprimento,raqueteAltura);
}

function mostraRaqueteOponente(x, y) {
  rect(x, y, raqueteComprimento,raqueteAltura);
}


function movimentaMinhaRaquete() {
  if (keyIsDown(UP_ARROW)) {
    yRaquete -= 10;
  }
  
  if (keyIsDown(DOWN_ARROW)) {
    yRaquete -= -10;
  }
  }
  
function verificaColisaoRaquete(){
  if (xBolinha - raio < xRaquete + raqueteComprimento
     && yBolinha - raio < yRaquete + raqueteAltura
     && yBolinha + raio > yRaquete){
    velocidadeXBolinha *= -1;
    
  }
}  

function verificaColisaoRaquete(x, y){
  colidiu = collideRectCircle(x, y, raqueteComprimento, raqueteAltura, xBolinha, yBolinha, raio);
  if (colidiu){
    velocidadeXBolinha *= -1;
  }
}


  
function movimentaRaqueteOponente(){
  velocidadeYOponente = yBolinha - yRaqueteOponente - raqueteComprimento /2 - 30;
  yRaqueteOponente += velocidadeYOponente
}

function incluiPlacar(){
  stroke(255);
  textAlign(CENTER);
  textSize(16);
  fill(color(255, 140, 0));
  rect(150, 10, 40, 20);
  fill(255)
  
  text(meusPontos, 170, 26)
  fill(color(255, 140, 0));
  rect(450, 10, 40, 20);
  fill(255);
  text(pontosDoOponente, 470, 26)
}

function marcaPonto(){
  if (xBolinha > 586){
    meusPontos += 1;
  }
  if (xBolinha < 5){
    pontosDoOponente += 1
  }
}
