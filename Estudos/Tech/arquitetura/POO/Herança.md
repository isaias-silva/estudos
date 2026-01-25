propriedades de uma classe podem ser herdadas por classes filhas.


```java
public class Animal{
	private int width;
	private int height;
	
	public int getWidth(){
		return width;
	}

	public void setWidth(int w){
		width=w;
	}
	...
}
```

a herança permite que métodos e propriedades não precisem ser reescritos.

```java 
public class Dog extends Animal{
	...
}

new Dog(30,25).getWidth();

```

