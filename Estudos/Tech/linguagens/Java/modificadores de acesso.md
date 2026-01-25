Definem a acessibilidade de propriedades e métodos de uma classe.


## Public
Acesso total, pode ser usado em qualquer lugar do programa.
```java 

public class PublicClass{

	public void publicMethod(){

	}
}


```

## Default
Acesso apenas no package onde a classe se encontra
-  apenas classes no exato mesmo pacote.
```java
class DefaultClass{

}
```


## Protected
Acesso apenas de classes que herdam a classe principal
```java

public class Bot{

	protected void loadConfig(){

	}
}


public class YoutubeBot extends Bot{
	//Youtube bot pode acessar dentro de seus métodos .loadConfig.

}
```

## Private

Acessível apenas para a própria classe 

```java 
public class Car{

private void changeGear(){
//changeGear só será usado dentro de Car.
}

}

```

