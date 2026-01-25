estruturas importantes para a execução de um programa.


## Condicionais:
estruturas de controle de fluxo via condições verdadeiras ou falsas.

### If:
bloco executado se uma condição for verdadeira.
```java
if(condicao){
// se a condição for verdadeira essa parte do código é executada
}
```

### Else:
bloco executado se uma condição If for falsa:
```java 
if(condicao){

}else{
	//se a condição for falsa essa parte do código é executada
}

```

### Switch case:
baseia-se em possíveis valores para uma variável,

```java
switch(type){
	case "A":
		//bloco executado caso type seja igual a A
	break
	
	case "B":
		//bloco executado caso type seja igual a B
	break
	
	default:
		//bloco default caso type seja diferente de qualquer outro case
	break
}


```

switch case possui uma forma moderna a partir do java 12, focado no retorno do valor para uma variável:

```java

String status = switch(numStatus){
	case(404) -> "not found";
	case(400) -> "bad request";
	case(200) -> "sucess";
	case(304) -> "redirect";
	default -> "internal server error";
}

```


## Loops

estruturas de repetição controladas também via condição.

### while:
Repetição enquanto:
```java
while(condicao){
//enquanto a condição for verdadeira esse bloco será executado

}

```


### do while:
Repetição while mas com uma execução antes da verificação.
```java 
do{
//primeira execução não verificada, enquanto a condição for verdadeira esse bloco voltará a ser executado

}while(condicao);

```


### for:
Repetição mais robusta que funciona com incremento ou decremento;

#### for básico:
```java


for(int i=0; i<10; i++){  
        //bloco é executado enquanto i for menor que 10, a cada ciclo i é incrementado.  
}



```

#### for each
Percorre por uma array ou iterator.

```java

for(String name:names){

//percorre todos os itens da array names

}


```

