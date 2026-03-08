Estrutura chave e valor(dicionário), onde as chaves sempre serão únicas mas os valores podem ser iguais.

### Implementações:

- HashMap: ordem aleatória
- LinkedHashMap: ordem de inserção
- ThreeMap: ordem natural das chaves


### métodos

- `put(K chave, V valor)`: Insere ou atualiza um par.

- `get(Object chave)`: Recupera o valor associado à chave.

- `containsKey(Object chave)`: Verifica se aquela chave existe.

- `remove(Object chave)`: Deleta o par correspondente à chave.

- `keySet()`: Retorna um `Set` com todas as chaves.

- `values()`: Retorna uma `Collection` com todos os valores.


### Exemplos:
```java
Map<String, Integer> estoque = new HashMap<>();

        estoque.put("Notebook", 10);
        estoque.put("Mouse", 50);
        estoque.put("Teclado", 20);
```

