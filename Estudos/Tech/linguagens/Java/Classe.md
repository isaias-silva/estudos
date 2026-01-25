Estrutura base no Java, com [[Métodos]] e atributos, uma classe definem o comportamento de um [[Objeto]], e pode ter sua acessibilidade e comportamento alterados por [[modificadores de acesso]] e [[modificadores de comportamento]]. 

## Declaração de classe:

```java

public class TheClass{


}

```

após criada uma classe é usada para instanciar um objeto:

```java

TheClass theObject = new TheClass();

```


## Construtor

método especial chamado quando uma classe instancia um objeto.

```java

public class TheClass{

final String propertie;

	public Thecclass(String propertie){
		this.propertie = propertie;
	}

}


```

em classes com [[Herança]] utilizamos a palavra reservada <font color="#2DC26B" style="text-style: bold">super</font> que pode receber os parâmetros do construtor da classe pai.
uma classe pode ter vários construtores desde que eles não sejam idênticos.


### This:
variável de referência que aponta diretamente para o objeto atual, pode ser usada para chamar um construtor especifico dentro de outro construtor.

```java

public Engine(String key){

		this(key, "default-mode");
}

public Engine(String key, String mode){
//construtor que será chamado no de cima.
}

```

