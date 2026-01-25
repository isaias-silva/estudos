Jakarta API for **XML** Web services, padrão JakartaEE para web services SOAP.


### Implementações:
- Metro
- Apache CXF

### Exemplos:

```java
import jakarta.jws.WebService;

@WebService
public class CalculadoraService {

    public int somar(int a, int b) {
        return a + b;
    }
}


```



> [!info] 
> JAX-WS é mais popular em aplicações legado.


