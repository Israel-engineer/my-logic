let dia = Number(prompt("Numero del dia de la semana 1 a 7"));
switch (dia) {
    case 1: document.write("Lunes"); break;
    case 2: document.write("Martes"); break;
    case 3: document.write("Miercoles"); break;
    case 4: document.write("Jueves"); break;
    case 5: document.write("Viernes"); break;
    case 6: document.write("Sabado"); break;
    case 7: document.write("Domingo"); break;
    default: document.write("Dia Invalido, Debes elegir entre 1 a 7 ")
        break;
    
}