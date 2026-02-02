Estrutura que mantém a ordem de inserção e permite elementos duplicados.

### Implementações:
- **ArrayList:** funciona como um Array dinâmico mais comum, rápida para acessar elementos por índice, porém lenta para remover itens no meio.

- **LinkedList**: funciona como uma lista duplamente ligada, inserção rápida e busca mais lenta.

### métodos:
 - add(element): adiciona um elemento ao final lista.
 - add(index,  element): adiciona elemento no índice especifico e empurra os próximos itens para frente.
 - addAll(collection): adiciona uma coleção ao final da lista.
 - get(index): retorna o item da lista baseado no índice.
 - indexOf(element): retorna o índice do elemento passado, caso não encontre retorna -1.]
 - lastIndexOf(element): o mesmo do indexOf porém começa a procurar no final da lista.
 - clear(): limpa toda a lista.
 - size(): retorna o tamanho da lista.
 - isEmpty(): retorna booleano verdadeiro caso a lista esteja vazia.
 - contains(element): retorna booleano verdadeiro caso o elemento esteja na lista.
 - sublist(fromIndex, toIndex): retorna um pedaço da lista de fromIndex até toIndex.

-  List.of(element, element, element): cria uma lista imutável. 
### Exemplo:


criação de lista:
```java
List<String> students = new ArrayList();
```

criação de lista imutável:
```java
List<String> students = List.of("joe","marc", "gilbert");

```

captura de sublist:
```java
List<String> students= List.of("antom", "dexter", "joe", "michael", "aaron");
List<String> problematicStudents= students.sublist(0,2);
// um sublist de uma lista imutável será imutável também.
```


> [!INFO] Listas imutáveis
> ao tentar adicionar, remover ou alterar algum valor de uma lista imutável(criada a partir de List.of() ) obtém-se uma UnsupportedOperationException.
