estruturas funcionais dentro de uma classe.
a estrutura padrão de um método dentro de uma classe é:

```java
acesso retorno nomeDoMetodo(TipoDeParametro parametro){

}

```


podem ser instanciáveis ou não, dependendo dos [[modificadores de comportamento]] utilizados.
### método instanciado:
só pode ser chamado por um [[Objeto]] da classe instanciada;

```java

public Carro{

public void correr(){
//correr só pode ser chamado se Carro for instanciado new Carro();

}

}


```

### método estático
é chamado diretamente da classe, não necessitando de instância;

```java

public Math{

public static int sum(int a, int b){
return a+b; // sum é chamado diretamente pela classe Math, com Math.sum(1,2), sem depender de instanciação.
}

} 

```




quando a lógica não depende de estado de objeto utilizamos métodos estáticos, quando o estado é importante para a lógica, usamos os métodos de instância.