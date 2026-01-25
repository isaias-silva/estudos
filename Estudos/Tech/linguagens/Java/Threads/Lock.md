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
**.lock:**  adquire o bloqueio 

**.lockInterruptibly**:  adquire o bloqueio, mas permite que a thread seja interrompida enquanto espera.

.**tryLock:**  tenta adquirir o bloqueio  caso não consiga retorna false.

**.tryLock(Long tile, TImeUnit unit)**: tenta pegar bloqueio por um tempo determinado.
