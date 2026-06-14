Classe introduzida no Java 8, funciona como um "container" para um objeto que pode ou não ser null.

- evita [NPE ](./Throwable)
- diminui tamanho e complexidade do código


```java

String role = Optional.ofNullable(UserService.getRole(id)).orElse("default-user");


```

### métodos

| método         | função                                                                                          | Exemplo                                                                |
| -------------- | ----------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| .empty()       | estático que retorna um Optional vazio                                                          | Optional.empty();                                                      |
| .of()          | estático que retorna um Optional com valor                                                      | Optional.of("dog");                                                    |
| ofNullable()   | estático que retorna um Optional com valor que pode ou não ser nulo                             | Optional.ofNullable(result);                                           |
| .orElse()      | método de instância que define um padrão no caso do valor ser nulo                              | Optional.ofNullable(result).orElse(Result.default());                  |
| .ifPresent()   | método de instância que recebe um [[lambda]] que é executado caso o valor não seja nulo         | optionalValue.ifPresent(value -> System.out.println("valor existe"));  |
| .orElseThrow() | lança uma exceção caso o valor seja nulo                                                        | Optional.ofNullable(result).orElseThrow(()-> new RuntimeException());  |
| .map()         | utiliza um método com retorno no proprio objeto dentro do Optional caso seu valor não seja nulo | Optional< String > email = optionalCliente.map(Cliente::getEmail);<br> |



