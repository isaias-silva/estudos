introduzido no java 8 evolução do [[ExecutorService]] funciona como uma promessa de que o resultado chegará e permite que você diga oque deve acontecer depois sem que o programa trave.


> [!INFO] O Problema do `Future` comum
> 
Com um `Future` normal (do [[ExecutorService]]), para pegar o resultado, você precisa chamar `.get()`. O problema? O `.get()` é **bloqueante**. Se a tarefa demorar 10 segundos, sua thread principal fica parada ali esperando.
O `CompletableFuture` é **não-bloqueante**. Você registra um _callback_ (uma reação) e segue a vida.

#### Chaining - Programação fluente

Encadeamento de etapas, quando a tarefa A termina seu resultado vai para a tarefa B.
```java
CompletableFuture<String> pipeline = CompletableFuture.supplyAsync(()->"pão")
.thenApply((alimento)-> new Dish(alimento)).thenAccept(System.out::println);
```

#### Tratamento de erros
O try/catch tradicional não funciona bem em threads separadas, por isso existe o método `exceptionally` .

### principais métodos:

| método      | função                                          |
| ----------- | ----------------------------------------------- |
| supplyAsync | inicia uma tarefa que retorna um valor          |
| runAssync   | inicia uma tarefa que não retorna nada void     |
| thenApply   | transforma resultado retornado                  |
| thenCompose | quando se quer encadear dois CompletableFutures |
| allOf       | espera um grupo de várias tarefas terminarem    |

