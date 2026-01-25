Funções anônimas adicionadas a partir do<font color="#2DC26B"> java 8</font>, implementações das [[interfaces funcionais]]


 ```java
 
 Runable action = ()->{
 System.out.println("execute action");
 }
 
 
 
 ```


Lambdas são utilizadas em vários casos como:

- For each:

```java
lista.forEach(v->System.out::println);
```

- [[Streams]]

```java 
lista.filter(v-> v > 10).forEach(v->System.out::println);
```

Lambdas garantem:

- código mais limpo: menos código repetitivo.
- facilita o uso de Streams.
- facilita paralelismo  com uso de [[Threads]].
