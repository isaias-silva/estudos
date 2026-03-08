Operadores lógico , relacionais e matemáticos, símbolos especiais que servem para modificar valores e validar condições.

### operadores aritméticos

usados para operações básicas.

| operador | função                   |
| -------- | ------------------------ |
| +        | soma                     |
| -        | subtração                |
| *        | multiplicação            |
| /        | divisão                  |
| %        | módulo(resto de divisão) |


### operadores relacionais
usados para comparação, sempre retornam um booleano.


| operador | função                                  |
| -------- | --------------------------------------- |
| ==       | igual a                                 |
| !=       | diferente de                            |
| > e <    | maior que e menor que                   |
| >= e <=  | maior ou igual que e menor ou igual que |


### operadores lógicos:
operadores essenciais para [[Condicionais e loops]]  


| operador | função                                                      |
| -------- | ----------------------------------------------------------- |
| &&       | AND as condições da esquerda e da direita devem ser verdade |
| \|\|     | OR uma das condições deve ser verdadeira                    |
| !        | NOT inverte o valor booleano                                |

### operadores de atribuição
além de `=`  existem outros operadores que atribuem valor:


| operador | função               |
| -------- | -------------------- |
| +=       | soma e atribui       |
| -=       | subtrai e atribui    |
| *-=      | multiplica e atribui |
|          |                      |

### operadores de incremento e decremento
aumentam ou diminuem valores em 1.


| operador | função     |
| -------- | ---------- |
| ++       | incremento |
| --       | decremento |


### operador ternário:
forma compacta do if/else;

```java

String status= (idade>18)?"adulto":"criança";

```