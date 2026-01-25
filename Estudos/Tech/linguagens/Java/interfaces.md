Definem o "contrato" de uma classe, em resumo, seu comportamento mas não a implementação do mesmo, uma forma de [[Abstração]].

```java

interface Robot{
public void sendMessage(Message msg);

}


```


### interface X classes abstratas:

Mesmo que ambas sejam formas de [[Abstração]], as interfaces possuem algumas diferenças em relação a classes abstratas:

- interfaces não possuem atributos
- interfaces não possuem construtor
- uma classe pode ter [[Herança]] de múltiplas interfaces.


