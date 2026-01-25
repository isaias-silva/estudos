Java Message Service, padrão Java para mensageria,
**comunicação assíncrona**, desacoplada e confiável entre sistemas.


Basicamente define como o java se comunica com serviços de messageria.

### Modelos de comunicação:

#### Point to Point:

Producer --> Queue --> Consumer

uma mensagem um consumidor.

#### Publish/Subscribe

Producer----> Topic ----> ...Consumers

1 mensagem vários consumidores.


### Exemplos:

**Envio**:
```java

@Inject
JMSContext ctx;


@Resource(lookup = "jms/queue")
Queue queue

public void send(){

context.createProducer().send(queue, "hello world");

}


```

**Recebimento**:

```java
@MessageDriven
public MessageListener(){

public void onMessage(Message msg){
	System.println("new message");
}
}


```


### Implementações:

- ActiveMQ
- ActiveMQ Artemis
- IBM MQ
- WebLogic JMS
- OpenMQ
- TIBCO EMS


> [!info] 
> Atualmente JMS é mais utilizado em sistemas legados

