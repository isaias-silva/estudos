Jakarta transaction API, padrão do [[JavaEE]] para controle de transações.

- usa o modelo [[#2PC]]  two phase commit).

- garante que operações sejam feitas de forma atômica(ou tudo dá certo, ou é desfeito).

- garante consistência

```java


import jakarta.transaction.Transactional;

@Transactional
public void criarPedido(Pedido p) {
    pedidoRepo.persist(p);
    filaService.enviar(p);
}

```

>  se qualquer parte de `criarPedido` falhar, ocorre um **rollback** e tudo é desfeito.


### 2PC:
Two-Phase-Commit, modelo usado pelo JTA com duas principais fases:

 1 - *Prepare*
     todos os recursos checam se podem confirmar

2 - *Commit*
	Se todos os recursos confirmarem a transação é completa.
	 Se não: rollback.


#### Componentes:
**Transaction Manager**
    coordena as transações

**UserTransaction**
    API para o desenvolvedor controlar manualmente transações.

- **@Transactional**
     controle automático ([[CDI]])

