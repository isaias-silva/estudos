Jakarta Restful web Services, padrão JakartaEE para criar **APIs REST**.[^1]
define:

- Como endpoints HTTP usando anotações de forma padronizada.
- Mapeia urls em métodos.
- Converte json(com Jackson/JSON-B).
- Trata headers, status http, parâmetros, queries.
  -  integra com [[CDI]], [[JPA]] e [[JTA]]
  
## Principais anotações:


| Anotação                   | Função                      |
| -------------------------- | --------------------------- |
| @Path                      | define rota http            |
| @GET, @POST, @PUT, @DELETE | define o método http        |
| @Produces                  | define o tipo de resposta   |
| @Consumes                  | define o tipo de entrada    |
| @PathParams                | define parâmetro na URL     |
| @QueryParams               | define parâmetros  de query |

## Implementações:

**RESTEasy:**

utilizada em [[Quarkus]] e WildFly

**SmallRye**:

  também utilizada em [[Quarkus]].


### Exemplo:

```java

@Path("/books")
@Produces("application/json")
@Consumes("application/json")
public class BookResource{
	@Inject
	BookService bookService
	
	
	@GET
	public List<BookDto> getBooks(){
	
	return bookService.getBooks();
	}

}



```




[^1]: Jax-RS é uma especificação assim como JPA, dependendo de implementações
