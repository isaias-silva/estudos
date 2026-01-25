Tipo especial de [[Classe]] que possui valores já conhecidos.
```java
public enum BotTypes{
	WA("whatsapp"),
	TEL("telegram"),
	X("x/twitter"),
	DS("discord");
	
	private String name;
	
	 BotType(String name){
		 this.name = name;
	 }

	public String getName(){
		return this.name;
	}
}


```

- Enums são ótimos para uso de switch/case.  