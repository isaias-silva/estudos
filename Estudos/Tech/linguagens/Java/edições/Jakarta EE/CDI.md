Contexts and Dependency Injection, tecnologia padrão de injeção de dependência e ciclos de vida.

- criar e gerenciar objetos de forma automática
- reduz acoplamento
- injetar dependências


O motor do CDI é o CDI container responsável por criar e gerenciar objetos.


## bean

um Bean é uma classe gerenciada pelo CDI.


```java

@ApplicationScoped
plublic class Bean {

}

```

**@ApplicationScoped** é uma notação que define um bean no escopo de aplicação.
para injetar um bean utiliza-se **@Inject**:

```java
public class useBean{
@Inject
Bean bean;
}

```

O CDI evita a necessidade de instanciar sempre um objeto dentro de outro.

#### Escopos
Definem por quanto tempo um Bean deve existir e em qual contexto ele é utilizado.

| @ApplicationScoped | dura durante toda a aplicação        |
| ------------------ | ------------------------------------ |
| @RequestScoped     | Dura durante uma requisição          |
| @SessionScoped     | dura durante uma sessão de usuário   |
| @Dependent         | acompanha o Bean onde ele é injetado |


#### Produces
por meio da anotação @Produces, transforma em bean objetos já existentes que não são por padrão.
