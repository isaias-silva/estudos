controle de acesso a propriedades de um objeto.

```java


public class Machine{
	private int id;
	private String name;

	public int getId(){
		return id;
	}
	public void setId(int value){
		id=value;
	}
}
```

a propriedade nunca é acessada diretamente evitando acesso indevido e conservando o estado dentro do objeto.

