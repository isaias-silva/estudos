permite que métodos herdados possuam comportamento diferente.

```java 
public class DiscordBot extends Bot{

@Override
public void sendMessage(Message msg){
	
	discordClient.post(generateRequest(msg));
}

}

```

