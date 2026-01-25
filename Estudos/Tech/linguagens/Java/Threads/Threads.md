 Recurso para executar tarefas de forma concorrente, para isso utiliza a classe <font color="#2DC26B">Thread</font> , a classe recebe uma implementação de uma das [[interfaces funcionais]] a <font color="#2DC26B">Runable</font>.

```java

Runnable process = ()->{System.out.println("hello process")}

Thread task = new Thread(process);

task.run();

```

### Synchronized
palavra reservada responsável por impedir a **Race Condition**, o bloco synchronized impede que duas threads executem uma ação especifica ao mesmo tempo(por exemplo um incremento, causando a perda de um ou mais).

```java

synchronized(this){
	count++
}
```

oque estiver entre parenteses no bloco synchronized é oque será trancado impedindo que outras threads acessem[^1], no caso do this, bloqueia-se o objeto onde aquele bloco é executado, mas pode-se bloquear qualquer outro objeto.


> [!INFO] 
> embora synchronized possa ser usado dentro de uma [[lambda]] o this apontaria para o monitor da classe principal por isso sendo aconselhável o uso de um Object como parâmetro do synchronized nesse caso.



### Threads de usuário
Threads principais, por padrão threads instanciadas são threads de usuários, enquanto houver threads de usuário em execução a [[JVM]] não pode encerrar. 
### Threads Daemon
Threads de segundo plano que não impedem a [[JVM]] de encerrar[^2] , ideal para monitoramento e loop, para definir uma Thread como Daemon basta:
```java 
thread.setDaemon(true);
```
uma thread tem que ser setada como daemon antes de startar, caso contrário o java lançara a exception **IllegalThreadStateException**.

### Estados de uma Thread:
as Threads em java possuem 6 possíveis estados:
  -  **NEW** : a thread foi instanciada porém ainda não iniciada(método start não foi chamado);
 
  - **RUNNABLE**: a thread está pronta para executar, ela pode estar executando ou esperando sua vez na fila do processador.
  
  - **BLOCKED**: a thread está travada esperando um lock que outra thread está segurando.
  
  - **WAITING**: a thread está esperando indefinidamente que outra thread realize uma ação especifica.

  -  **TIMED_WAITING:** a thread está esperando por um tempo determinado.

   - **TERMINATED:** a thread encerrou sua execução(o método run terminou ou houve uma exceção não tratada)


para consultar o estado da thread basta executar o método `.getState()` na instância da thread.

### Thread Join
método de instância que serve para fazer a thread atual(geralmente a main) esperar até que a  outra  thread chegue no status TERMINATED.

```java
tarefa.start();
tarefa.join(); //a thread atual tranca até a tarefa ser concluída
System.out.println("tarefa concluída")
```
### Thread Wait e Notify
Métodos  presentes em todo [[Objeto]]  java, instanciado de **Object**(classe base), ambos os métodos são executados dentro de um bloco synchronized.
#### Wait:
solta o monitor [^1] do objeto e a thread entra em estado **WAITING**, e libera o objeto(recurso) para que outra thread possa utilizar, pode-se adicionar um timeout.
#### Notify:
avisa a thread que deu wait e está esperando aquele recurso que já pode ser utilizado. recomenda-se utiliza **notifyAll** devido a notify selecionar uma thread aleatória.

```java
//Thread A
synchronized(resource){

//while no lugar de if evita Race condition, após o wait a thread entra em estado waiting

	while(resource.getStatus()!="listen"){
		resource.wait();
	}
	
	resource.save(this.data)

}

//Thread B
synchronized(resource){
	resource.load();
	resource.notifyAll();//o notify all acorda a thread que entrou em estado waiting
}


```

### Thread Sleep:

método estático presente na classe Thread utilizado para pausas. ao ser chamado ele faz com que a thread onde foi chamado mude seu estado de Running para Timed Waiting, e durante o tempo de sleep não há consumo de CPU.

```java

Thread.sleep(1000)//a thread atual irá pausar por 1 segundo

```


Hoje existem formas mais modernas de trabalhar com threads como:
 -  interface [[Lock]] com sua implementação ReentrantLock.
 -  [[ExecutorService]] para gerenciamento de threads.
 - [[AtomicVariables]] 
 - [[CompletableFuture]]
 - [[Virtual Threads]]
 




[^1]:  funcionamento de [[Lock]] no bloco synchronized:
	todo objeto possui um "monitor" intrínseco. Quando uma thread entra em um bloco sincronizado, ela **adquire a chave** desse monitor. Enquanto ela estiver lá dentro, nenhuma outra thread consegue entrar em qualquer bloco que dependa da mesma chave.


[^2]: o Garbage Collector, responsável por limpar lixo e liberar memória da JVM executa em uma thread Daemon.


