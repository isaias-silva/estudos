Palavras reservadas que servem para modificar como uma classe, método ou atributo java se comporta.


### Final:
utilizado para definir constantes e classes que não podem ter [[Herança]].
#### classes:

```java
public final class NotExtends{

//essa classe não pode ser herdada.

}


```


#### constantes

```java

final String name = "John"; // a String name não pode receber outro valor.

```


### Abstract:

utilizada para definir uma classe que use [[Abstração]] define comportamento geral de classes filhas assim como [[interfaces]] com a diferença de que uma classe abstrata pode possuir implementações de seus métodos dentro da própria classe. também ainda seguindo o principio é possível criar métodos abstratos que serão  herdados e sua implementação nas classes filhas será obrigatório com uso de uma das [[Annotations]] mais usadas: **<font color="#2DC26B">@override</font>**

```java
//classe pai
public abstract class Bot{


protected String getId(){
	return String.format("%s-%s-%s",id,type,serial);
}
public abstract void send(Message msg);

}

//classe filha
public class DiscordBot{

	@Override
	public void send(Message msg){
		LOG.info("{} sended message to {}", getId(), msg.to);
		discordSocket.send(msg.to, msg.body);
	}
}
```

