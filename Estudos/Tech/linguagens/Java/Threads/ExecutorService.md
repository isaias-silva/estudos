interface para gerenciamento de Threads, substitui a criação manual, devido a criação de Threads manualmente ser custosa[^1] para o sistema operacional.

- ExecutorService adiciona o conceito de **ThreadPool**.

### ThreadPool
o ExecutorService mantém um grupo de threads vivas e prontas para o trabalho, quando uma tarefa chega.
- Reuso de threads
- gerenciamento de fila
- controle de ciclo de vida


### Criação
para criar um executor Service é necessário usar  métodos do utilitário `Executors`:


| método                    | função                                                                                                                                               |
| ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| newFixedThreadPool(n)     | cria um ExecutorService com um ThreadPool de tamanho n                                                                                               |
| newCachedThreadPool()     | cria um ExecutorService com um ThreadPool capaz de criar novas threads conforme a necessidade e as descarta por inatividade(bom para tarefas curtas) |
| newSingleThreadExecutor() | apenas uma thread gerante que as tarefas sejam executadas em ordem                                                                                   |
| newScheduleThreadPool(n)  | permite agendar tarefas para o futuro ou de forma recorrente                                                                                         |


### Execução
existem duas maneiras de executar tarefas em ExecutorService existem 2 métodos.

`execute(Runnable)`: dispara a execução da tarefa não recebe retorno ou sabe se a tarefa acabou.

`submit`: retorna um objeto `Future<T>` . Com ele, é possível pegar resultados da tarefa e capturar exceções.

### Finalização
ao final da execução de todas as tarefas que o executor service faz no programa é necessário utilizar o método `shutdown`, caso contrário a [[JVM]] continua rodando.


### Exemplo:

```java
public static void main(String[] args) { 
	// 1. Criar o pool com 3 threads 
	ExecutorService executor = Executors.newFixedThreadPool(3); 
	// 2. Enviar tarefas 
	for (int i = 1; i <= 5; i++) { 
		int taskId = i; 
		executor.execute(()->System.out.println("hello task "+taskId)); 
	} 
	// 3. SEMPRE desligue o executor, senão a JVM continua rodando 
	executor.shutdown();
 }
```



[^1]: .Cada vez que você cria uma thread, o Java reserva um bloco fixo de memória para o **Stack** (pilha) dessa thread. Por padrão, esse valor costuma ser de **1 MB** (dependendo da [[JVM]] e do SO). Se você criar 1.000 threads, você acabou de consumir **1 GB de RAM** apenas com a estrutura básica delas, antes mesmo de executarem qualquer lógica de negócio.
