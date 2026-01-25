Uma interface com apenas um método, adicionadas a partir do <font color="#2DC26B">java 8</font> úteis para implementação de métodos anônimos e uso em [[Threads]].


### criação de interface funcional:
Para criar uma interface funcional pode se usar uma das [[Annotations]] chamada de <font color="#2DC26B">@FunctionalInterface</font> [^1]  e declarar a interface conforme ocorre nas [[interfaces]] habituais: 

```java

@FunctionalInterface
public interface Opertation{
	int run(String expression){}
}

```


### Interfaces funcionais padrão:

- **Runnable**:  função não recebe parâmetros e nem retorna valores, método <font color="#2DC26B">run()</font>.

- **Function<In, Out>**:  recebe parâmetro do tipo In e retorna parâmetro do tipo Out, método <font color="#2DC26B">apply(<font color="#ff9">value</font>)</font>.

- **BiFunction<In, In, Out>**:  recebe 2 parâmetros do tipo In que podem ser de tipos diferentes e retorna um valor do tipo Out, método <font color="#2DC26B">apply(<font color="#ff9">value</font>)</font>.

- **Supplier< Input>**:   não recebe nenhum parâmetro e retorna um valor do tipo Input, método<font color="#2DC26B">get()</font>;

- **Consumer< Input>**:  recebe um parâmetro e não retorna nenhum valor, método <font color="#2DC26B">accept(<font color="#f80">value</font>)</font>;

- **Predicate< Input>**:  recebe um parâmetro do tipo Input e retorna um booleano. método <font color="#2DC26B">test(<font color="#D2f">value</font>)</font>.





[^1]: o uso da annotation <font color="#2DC26B">@FunctionalInterface</font> é opcional visto que qualquer interface com apenas um método é considerada interface funcional.
