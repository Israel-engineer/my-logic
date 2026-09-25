let zona = Number(prompt("Zona 1, 2 o 3"));
let hora = Number(prompt("Hora del viaje 0 a 23"));

let valor; 
switch (zona) {
    case 1: valor = 4000; break;
    case 2: valor = 6000; break;
    case 3: valor = 9000; break;
    
    default: 
        valor = 0; 
        document.write("Zona invalida");
        break;
}

if (valor > 0 && hora >= 20) {
    valor = valor * 1.20;
    document.write("Se aplica recargo nocturno");
}

if ( valor > 0) {
    document.write('Valor a pagar: $${valor}')
}
