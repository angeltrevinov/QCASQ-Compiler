# QCASQ-Compiler

Angel Odiel Treviño Villanueva A01336559

Julia Margarita Jimenez Herrera A00821428

## Como ejecutar el codigo:
 - Instala la ```ply``` dentro del proyecto
 - corre el archivo ```main.py```
 - Insertar la ruta y el nombre del archivo ```.txt```

## Como utilizar QCASQ
[Video Tutorial](https://youtu.be/v7wLawZVGso)

Aqui puedes observar como se implementan algunos de los bloques de codigo,
si quieres ver ejemplos con mayor detalle, checa la carpeta ```TestCases```

### Estructura basica
```
program <nombre del programa>;

main() {
}
```

### Declaración de Variables
```
var x: int;
var arr[8]: float;
var matrix[3][4]; float;
var mensaje: string;

x = 8*7;
arr[8-3] = 9.32;
matrix[1][3] = false; // true
mensaje = "hola";
```

### Funciones
```
// funcion void
func fib() {

}

// funcion con return
func fib_while(n:int, x:int): int {
    return n;
}
```

### While
```
var n: int;
n = 0;
while(n < 9) {
    output(n);
    n = n + 1;
}
```

## Documentos
- [Diagrams](https://lucid.app/lucidchart/invitations/accept/ceed37c7-75ad-4741-bd13-869e665169f7?viewport_loc=-11%2C-11%2C2219%2C1108%2C0_0)
