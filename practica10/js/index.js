var canvas;
var ctx;
var fps = 20;

var canvasX = 700;  
var canvasY = 700;  
var tileX, tileY;

var tablero;
var filas = 20;      
var columnas = 20;  

var amarillo ='#FCDF03';
var azul = '#07d7f7';
var rojo = '#f70707';
var negro = '#000000';
var blanco = '#FFFFFF';

var matriz = [
  [0,0,0,0,0,1,3,2,1,0,0,1,1,0,0,0,0,0,0,0],
  [0,0,0,0,0,1,0,0,1,0,1,0,0,1,0,0,0,0,0,0],
  [0,0,0,0,0,1,0,0,1,1,1,1,1,1,1,0,0,0,0,0],
  [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0],
  [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0],
  [0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0],
  [0,0,0,0,1,0,0,0,0,0,1,1,0,0,1,0,0,0,0,0],
  [0,0,0,0,0,1,0,0,0,1,0,0,1,1,0,0,0,0,0,0],
  [0,0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,1,0,0,0,0,0,1,1,1,0,0,0,0],
  [0,1,1,1,1,1,1,1,0,0,0,0,0,1,0,0,1,0,0,0],
  [1,0,0,0,1,0,0,0,,0,0,0,0,1,0,0,1,0,0,0],
  [1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0],
  [1,0,0,0,1,0,0,0,0,1,0,0,0,1,0,0,1,0,0,0],
  [1,1,1,0,1,1,1,1,1,1,0,0,0,0,1,1,0,0,0,0],
  [0,0,1,0,0,1,0,0,0,1,1,0,0,1,0,0,0,0,0,0],
  [0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0],
  [1,0,0,0,1,0,1,1,0,0,0,0,0,1,0,0,0,0,0,0],
  [1,1,1,1,0,1,0,0,1,1,1,1,1,1,0,0,0,0,0,0]

];

function creaArray2D(f,c){
  var obj = new Array(f);
  for(y=0; y<f; y++){
    obj[y]= new Array(c);
  }

  return obj;
}

var vacio = 0;
var cable = 1;
var cabeza = 2;
var cola = 3;

var Agente = function(x,y,estado){

  this.x = x;
  this.y = y;
  this.estado = estado;          
  this.estadoProx = this.estado;  

  this.vecinos = [];   
  this.addVecinos = function(){
    var xVecino;
    var yVecino;

    for(i=-1; i<2; i++){
      for(j=-1; j<2; j++){
        xVecino = (this.x + j + columnas) % columnas;
        yVecino = (this.y + i + filas) % filas;


        if(i!=0 || j!=0){
          this.vecinos.push(tablero[yVecino][xVecino]);
        }

      }
    }
  }



  this.dibuja = function(){

    var color;

    if(this.estado == 0){
      color = negro;
    }

    if(this.estado == 1){
      color = amarillo;
    }

    if(this.estado == 2){
      color = azul;
    }

    if(this.estado == 3){
      color = rojo;
    }

    ctx.fillStyle = color;
    ctx.fillRect(this.x*tileX, this.y*tileY, tileX, tileY);

  }
  this.nuevoCiclo = function(){
    if(this.estado == vacio)
      this.estadoProx = vacio;

    if(this.estado == cabeza)
      this.estadoProx = cola;

    if(this.estado == cola)
      this.estadoProx = cable;

    if(this.estado == cable){
      var cabezas = 0;

      for(i=0; i<this.vecinos.length; i++){
        if(this.vecinos[i].estado == cabeza){
          cabezas++;
        }
      }

      if(cabezas == 1 || cabezas == 2)
        this.estadoProx = cabeza;
      else
        this.estadoProx = cable;

    }



  }


  this.mutacion = function(){
    this.estado = this.estadoProx;
  }



}

function inicializaTablero(obj){

  var estado;

  for(y=0; y<filas; y++){
    for(x=0; x<columnas; x++){
      obj[y][x] = new Agente(x,y,matriz[y][x]);
    }
  }


  for(y=0; y<filas; y++){
    for(x=0; x<columnas; x++){
      obj[y][x].addVecinos();
    }
  }

}

function borraCanvas(){
  canvas.width=canvas.width;
  canvas.height=canvas.height;
}

function inicializa(){
  canvas = document.getElementById('pantalla');
  ctx = canvas.getContext('2d');

  canvas.width = canvasX;
  canvas.height = canvasY;

  tileX = Math.floor(canvasX/filas);
  tileY = Math.floor(canvasY/columnas);

  //creamos el tablero
  tablero = creaArray2D(filas,columnas);
  //Lo inicializamos
  inicializaTablero(tablero);

  setInterval(function(){principal();},1000/fps);

}


function dibujaTablero(obj){

  for(y=0; y<filas; y++){
    for(x=0; x<columnas; x++){
      obj[y][x].dibuja();
    }
  }

  for(y=0; y<filas;y++){
    for(x=0; x<columnas; x++){
      obj[y][x].nuevoCiclo();
    }
  }

  for(y=0; y<filas;y++){
    for(x=0; x<columnas; x++){
      obj[y][x].mutacion();
    }
  }

}

function principal(){
  borraCanvas();
  dibujaTablero(tablero);

}
