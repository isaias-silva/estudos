A partir do java 16 uma forma simplificada de [[Pojos]] foi adicionada ao java, uma forma mais simples e ao mesmo tempo organizada.


### Exemplo:

```java
public record Book(String name, String description, List<Page> pages){}
```


em resumo records:

- tem todas suas propriedades como imutáveis.
-  não podem extender ou herdar de outra classe.

