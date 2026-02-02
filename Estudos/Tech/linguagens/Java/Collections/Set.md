Estrutura que não permite duplicatas.

### Implementações:
- **HashSet**:  uso de tabela hash para armazenar elementos, é ideal quando o assunto é performasse.

- **LinkedHashSet**:  variação que usa uma lista duplamente ligada, ideal quando o assunto é ordem de inserção.

-  **TreeSet**: elementos são armazenados em uma estrutura de árvore  os elementos são mantidos em ordem natural ou via Comparator(uma das [[interfaces funcionais]] especiais).

### Exemplos:
HashSet
```java
Set<String> hashSet = new HashSet<>();
hashSet.add("A");
hashSet.add("B");
hashSet.add("B");//duplicata
hashSet.add("C");
//O resultado será A,B e C

```

LinkedHashSet
```java
Set<String> hashSet = new LinkedHashSet<>();
hashSet.add("D");
hashSet.add("B");
hashSet.add("A");
hashSet.add("C");
//O resultado será D,B,A,C em ordem de inserção

```

TreeSet
```java
Set<String> hashSet = new HashSet<>();
hashSet.add("D");
hashSet.add("B");
hashSet.add("A");
hashSet.add("C");
//O resultado será A,B,C,D em ordem alfabética

```

TreeSet com Comparator
```java
Comparator<String> porTamanho = (s1, s2) -> { s1.length() > s2.length()};

 Set<String> tecnologia = new TreeSet<>(porTamanho);
 tecnologia.add("Java");
 tecnologia.add("Python"); 
 tecnologia.add("C");
 tecnologia.add("Go");

```