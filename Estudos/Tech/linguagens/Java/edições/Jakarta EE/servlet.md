Base das aplicações web java, responsável por receber requisições http e retornar respostas.
Diferente de [[Frameworks]] que já implementam "container de servidor" o servelet puro depende de servidores externos para executar uma aplicação.

### exemplo

```java
import jakarta.servlet.http.HttpServlet

@WebServlet("/hello")

public class HelloServlet extends HttpServlet{
	@Override 
	protected void doGet(HttpServletRequest req, HttpServletResponse res) throws IOException {
	
		res.getWriter().println("hello world");
	}

}


```

para executar uma aplicação com servlet puro é necessário um servidor(Tomcat, Jetty etc), e se estiver utilizando maven configurar o packing para `.war`, em seguida adicionar o arquivo compilado .war no servidor(no caso  do tomcat em `tomcat/webapps/`)
