Alternativa ao bloco synchronized, permite uma forma mais flexível de  processamento linear entre threads concorrentes.

### ReentrantLock:
implementação mais comum da interface Lock.

```java
Lock locker = new ReentrantLock();

locker.lock();//bloqueia a thread
try{
...
}finally{
	locker.unlock();//libera a thread
}
```

### Condition:
diferente do synchronized, Lock não possui `wait` e `notify` , em vez disso ele usa um objeto que implementa a interface **Condition**, esse objeto substitui wait por **await** e notify por **signal**.

```java
//thread A
Condition freeResource = locker.newCondition();

locker.lock();
try{
while(resource.getStatus()!=Resource.LISTEN){
	freeResource.await();
}
...
}finally{
locker.unlock()
}

//thread B

locker.lock();
try{

...
freeResource.signal();
}finally{
locker.unlock();
}
```

### principais métodos:

### Lock

**.lock:**  adquire o bloqueio 

**.lockInterruptibly**:  adquire o bloqueio, mas permite que a thread seja interrompida enquanto espera.

.**tryLock:**  tenta adquirir o bloqueio  caso não consiga retorna false.

**.tryLock(Long tile, TImeUnit unit)**: tenta pegar bloqueio por um tempo determinado.

**.unlock**: libera a thread deve sempre ser chamado no bloco finally.

**.newCondition**: cria uma nova Condition.

### ReentrantLock:

- **`isLocked()`**: Verifica se o cadeado está ocupado por qualquer thread.
    
- **`isHeldByCurrentThread()`**: Verifica se **esta** thread específica é quem segura o cadeado.
    
- **`getHoldCount()`**: Retorna quantas vezes a thread atual "entrou" no cadeado (já que ele é reentrante).
    
- **`getQueueLength()`**: Estima quantas threads estão na fila esperando por esse cadeado.
    
- **`hasWaiters(Condition condition)`**: Pergunta se há alguém dormindo em uma sala específica.

### Condition

**.await**: faz a thread dormir e soltar lock  até ser sinalizada assim como *wait*

**.awaitUninterruptibly**:  Dorme e ignora interrupções até ser sinalizada.

.**awaitNanos(long nanos)** :  Dorme por um tempo máximo em nanosegundos.

**.await(long time, TimeUnit unit)**:   Dorme por um tempo determinado. Retorna `false` se o tempo acabou.

.**awaitUntil(Date deadline)**:   Dorme até uma data/hora específica.

**.signal()**:   Acorda **uma** thread que está nesta sala de espera (como o `notify()`).

.**signalAll()**:   Acorda **todas** as threads nesta sala de espera (como o `notifyAll()`).