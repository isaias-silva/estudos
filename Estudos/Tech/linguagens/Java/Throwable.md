classe principal para erros em programas java, é dividida em 2 extensões:


### Erros:
problemas graves, em geral irrecuperáveis ou uma quebra no sistema.
Ex: OOM(OutOfMemoryError).

### Exceptions:
problemas que podem ser previsto e tratados que se dividem em mais 2 extensões:
- **Checked Exceptions**:  obrigatórias a ser tratadas, o código não compila caso não sejam tratadas(IOException).
- 
- **Unchecked Exceptions**: o compilador não obriga a tratar mas derrubam o app se ocorrem(NullPointerException)

## lançamento de exceções:
para lançar uma exception em um método é necessário usar a palavra reservada `throw` seguida  da instância de uma classe que estenda Throwable.

```java

throw new Exception("texto que será exibido na stacktrace");

```

o método onde o throw é chamado ou se algum método chamado por este tem algum lançamento de throw deve ter a declaração na assinatura do método:
```java
public void process(Data data) throws Exception{...}
```


## Tratamento de erro:

Erros podem ser tratados com os blocos `try` , `catch` e `finally`, onde try receberá o código perigoso que lançaram a exceção, catch tratará a exceção e finally será executado independente do erro ocorrer ou não, sempre ao final do bloco.

```java
try{
//danger code
}catch(Exception e){
//treat exception e.
}finally{
//end
}
```

### Exceções e erros mais populares:
| **Classe**                           | **Causa Comum**                                                                                                                                          |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **`NullPointerException`** (NPE)     | Tentar acessar um método ou atributo de um objeto que está `null`. É a "famosa" número 1.                                                                |
| **`ArrayIndexOutOfBoundsException`** | Tentar acessar um índice de um array que não existe (ex: acessar a posição 5 de um array de tamanho 3).                                                  |
| **`ArithmeticException`**            | Operações matemáticas impossíveis, como a divisão por zero.                                                                                              |
| **`ClassCastException`**             | Tentar converter (cast) um objeto para uma classe que ele não pertence (ex: tentar transformar um `String` em `Integer`).                                |
| **`IllegalArgumentException`**       | Quando um método recebe um argumento que é tecnicamente correto (tipo certo), mas inapropriado (ex: passar um número negativo onde se espera uma idade). |
| **`NumberFormatException`**          | Ocorre ao tentar converter uma String em número, mas a String contém letras ou caracteres inválidos.                                                     |
| **`IOException`**                    | Falha genérica em operações de entrada/saída (leitura de rede, teclado, etc).                                                                            |
| **`FileNotFoundException`**          | Tentativa de abrir um arquivo em um caminho que não existe no disco.                                                                                     |
| **`SQLException`**                   | Erros relacionados ao Banco de Dados (sintaxe SQL errada, conexão perdida, etc).                                                                         |
| **`ClassNotFoundException`**         | O Java tenta carregar uma classe pelo nome (via Reflection), mas não a encontra no Classpath.                                                            |
| `OutOfMemoryError`                   | A JVM ficou sem memória RAM para alocar novos objetos.                                                                                                   |
| `StackOverflowError`                 | Geralmente causado por uma recursão infinita (um método chamando a si mesmo sem parar até lotar a pilha).                                                |
