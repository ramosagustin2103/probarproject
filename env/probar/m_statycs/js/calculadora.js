var p = document.getElementById('peso');
var d = document.getElementById('distancia');
var boton = document.getElementById('boton');
boton.addEventListener("click", calcularCosto);
var boton1 = document.getElementById('boton1');
boton1.addEventListener("click", limpiar);
var a = document.getElementById('precio_x_km_1');
var b = document.getElementById('precio_x_km_2');
var c = document.getElementById('precio_x_km_3');
var x = document.getElementById('limite_1');
var y = document.getElementById('limite_2');
var z = document.getElementById('limite_3');
function calcularCosto()
{
var peso = parseInt(p.value);
var distancia = parseInt(d.value);
var precio_1 = parseInt(a.value);
var precio_2 = parseInt(b.value);
var precio_3 = parseInt(c.value);
var peso_1 = parseInt(x.value);
var peso_2 = parseInt(y.value);
var peso_3 = parseInt(z.value);
var costo;
if (peso < peso_1)
{
costo = (precio_1 * distancia);		
}
 else if (peso > peso_1, peso < peso_2) 
{
costo = (precio_2 * distancia);		
}
else if (peso > peso_2, peso < peso_3) 
{
costo = (precio_3 * distancia);
}
else 
{
costo = 10000000000000;
}
document.getElementById("content").value = costo;
document.getElementById("content1").value = peso;
document.getElementById("content2").value = distancia;		
}
function limpiar()
{
var nada = "";
document.getElementById("content").value = nada;
document.getElementById("content1").value = nada;
document.getElementById("content2").value = nada;
document.getElementById('peso').value = nada;
document.getElementById('distancia').value = nada;	
}