classes simples para transferência de dados e serialization, para ser considerada uma classe POJO é necessário ter apenas métodos de [[Encapsulamento]] (getters & setters).

### Exemplo:
```java

public class Book{

	private String title;
	private String resume;
	private final List<Page> pages;

	public Book(String title, String resume, List<Page> pages){
		this.title = title;
		this.resume = resume;
		this.pages = pages;
	}
	
	public String getTitle(){
		return this.title;
	}
	
	public void setTitle(String title){
		this.title = title;
	}
	...
}


```

