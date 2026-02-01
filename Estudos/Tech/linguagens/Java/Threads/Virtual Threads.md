implementado no Java 21, as Threads virtuais servem para resolver o problema do custo de criação de [[Threads]] normais[^1].

Diferente das Threads de Plataforma (Platform Threads), que são mapeadas 1:1 para threads do Sistema Operacional, as Virtual Threads são **Threads gerenciadas pela [[JVM]].

- **Platform Thread:** 1 Thread Java = 1 Thread do SO (cara, pesada).
- **Virtual Thread:** N Threads Virtuais = 1 Thread do SO (barata, leve).
-  Por serem extremamente leves, não precisam de pool como ocorre no [[ExecutorService]] clássico.


A JVM agora tem seu próprio "agendador" interno. Quando uma Virtual Thread tenta fazer algo que bloquearia o código (como ler um banco de dados ou chamar uma API), a JVM a "estaciona" e coloca outra Virtual Thread para rodar naquela mesma thread do SO.

#### Exemplo
```java 

// Este executor cria uma nova Virtual Thread para cada tarefa submetida
try (var executor = Executors.newVirtualThreadPerTaskExecutor()) {
    executor.submit(() -> {
        // Simula uma operação pesada de IO (banco, api, arquivo)
        Thread.sleep(Duration.ofSeconds(1));
        System.out.println("Executado por uma Virtual Thread!");
        return "Sucesso";
    });
} // O try-with-resources fecha o executor automaticamente

```

### Quando NÃO usar Virtual Threads?


- **Tarefas de CPU intensiva:** Se você está calculando decimais de Pi ou processando vídeo, as Virtual Threads não ajudam. Elas brilham em tarefas de **IO** (espera).

- **Thread Local pesada:** Se você guarda muita informação no `ThreadLocal`, ter milhões de threads virtuais pode estourar sua memória.

- **Bibliotecas Antigas (Pinning):** Se uma biblioteca usa muito código `synchronized` nativo, ela pode "prender" a Virtual Thread à thread do SO, perdendo a vantagem da agilidade.


[^1]: o custo para criar uma Thread clássica no java chega a 1 MB, 1000 dessas já consumiria um alto recurso do SO.
