interface de Collection que segue o padrão FIFO(First in, First out).

### Implementações:

 -  LinkedList: funciona como uma fila padrão e é eficiente para inputs e removes.
 
 -  PriorityQueue:  Não segue estritamente o FIFO, ordena por prioridade natural ou por um Comparator.

-  ArrayDeque: fila baseada em array, geralmente mais rápida que LinkedList, mas não permite elementos nulos.

### métodos:
#### inserção 
- add: adiciona um item a Queue porém pode retornar uma Exceção
- offer: tenta adicionar um item a fila e retorna null ou false caso não consiga.

#### remoção
- remove: retorna uma exceção caso falhe
- pool: retorna null ou false caso falhe

#### consulta 
  - element: retorna o próximo item da fila, causa um throw caso falhe
  - peek: retorna o próximo item da fila, retorna null ou false caso falhe


#### Exemplos:

```java



import java.util.LinkedList;
import java.util.Queue;

public class ExemploQueue {
    public static void main(String[] args) {
        Queue<String> fila = new LinkedList<>();

        fila.add("João");
        fila.add("Maria");
        fila.add("José");

       
        System.out.println("Próximo a ser atendido: " + fila.peek());//joao
        String atendido = fila.poll();
        System.out.println("Atendido agora: " + atendido);//maria

        
        System.out.println("Fila restante: " + fila);
    }
}
```

