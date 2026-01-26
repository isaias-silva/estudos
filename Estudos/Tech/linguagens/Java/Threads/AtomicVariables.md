Forma mais eficiente de lidar com concorrência quando é preciso atualizar valores simples(booleanos ou números) sem a necessidade de usar [[Lock]] ou synchronized.


- variáveis atômicas usam  CAS[^1]

### Principais classes atômicas:

| Classe              | uso                                                  |
| ------------------- | ---------------------------------------------------- |
| AtomicInteger       | inteiros                                             |
| AtomicLong          | números grandes                                      |
| AtomicBoolean       | booleanos                                            |
| AtomicReference< V> |  para qualquer objeto que precise mudar a referência |

#### Métodos das classes atômicas:
- **`get()`**: Lê o valor atual (garante visibilidade entre threads).

- **`set(newValue)`**: Define o novo valor.

- **`incrementAndGet()`**: Faz o `++i` de forma segura.

- **`getAndIncrement()`**: Faz o `i++` de forma segura.

- **`compareAndSet(expect, update)`**: A base de tudo. Só muda o valor se ele for igual ao esperado.

[^1]: a instrução CAS(Compare-And-Swap) faz com que as mudanças de valores sejam verificadas em um loop extremamente rápido, impedindo problemas como Race Condition.
