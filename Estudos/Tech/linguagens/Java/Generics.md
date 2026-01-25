Forma de escrever código genérico e seguro em tempo de execução.

```java
class Box<T>{//Box recebe elementos do tipo T
}

class Box<?>{//Box recebe qualquer tipo de elemento
}

class Box<? extends Paper>{//Box recebe Paper e seus filhos
}

class Box<? super Paper>{//Box recebe Paper e seus pais
}

```



###  Regra produce & consume:

**Producer**  --> apenas usa coisas (extends);
**Consumer** --> apenas adiciona coisas(super);