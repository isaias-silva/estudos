
A linguagem java possui tipos primitivos e tipos de referencia, tipos definem valores de retorno de  métodos e de [^1]variáveis:

```java

int value = 1 //tipo primitivo
String texto = "olá tudo bem?" //tipo composto


```

### Tipos primitivos
Tipos básicos, **<font color="#2DC26B">guardam valor diretamente na memória</font>**.
- não são objetos
- não podem ser nulos
- consomem menos memória

| tipo    | uso                                                            |
| ------- | -------------------------------------------------------------- |
| byte    | ler arquivos binários, streams e buffers                       |
| short   | para valores pequenos quando int é desnecessário               |
| int     | padrão para números inteiros                                   |
| long    | padrão para números grandes, timestamps, IDs                   |
| float   | números flutuantes onde a precisão não é crítica               |
| double  | padrão para números decimais, calculo científico e estatístico |
| char    | padrão para caracteres unicode                                 |
| boolean | valor booleano(verdadeiro ou falso)                            |



### Tipos de referência:

São objetos, a variável guarda uma referência para um endereço de memória.



### Wrapper Classes
para cada tipo primitivo existe um tipo de referência equivalente que:

- são objetos
- podem ser nulos
- mais flexíveis

```java

Integer inteiroObj = 3; //wrapper class de int
int inteiroPrimitivo = 3;// int 

```


[^1]: variáveis, estruturas que armazenam um valor(em java podem ser objetos ou não)
