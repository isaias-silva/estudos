Adicionada no <font color="#2DC26B">Java 8</font>, a API de streams serve para processar coleções de [[estruturas de dados]] (List, Sets ou Array) em vez de utilizar um for complexo com várias condicionais.

```java

list.stream()
.filter(v-> v.starsWith("Z"))
.map(v->v.toUpperCase())
.collect(Collector.toList());

```

- streams nunca alteram a fonte original, por isso o resultado de uma stream pode e deve ser coletado via Collector.

-  streams são processos Lazy, dependem de uma operação terminal para serem executadas(forEach ou collect), caso contrário o processo não inicia.

- uma vez executada a operação terminal, o Stream não pode ser mais executado.

### Operações


| Operação | tipo          | oque faz                                                            |
| -------- | ------------- | ------------------------------------------------------------------- |
| .filter  | intermédiária | Filtra elementos com base em uma condição verdadeira                |
| .map     | intermédiária | Transforma os elementos percorridos em outras coisas                |
| .sorted  | intermédiária | Ordena elementos                                                    |
| .forEach | terminal      | executa uma ação para cada elemento                                 |
| collect  | terminal      | transforma a stream de volta em uma coleção(Lista, Set)             |
| count    | terminal      | conta quantos elementos restaram após as outras operações do stream |

### Collectors:
Classe utilitária que possui varias implementações para a operação terminal .collect dos streams.