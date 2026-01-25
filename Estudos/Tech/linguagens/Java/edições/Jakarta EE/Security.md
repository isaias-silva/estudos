módulo de segurança padrão do JakartaEE para cuidar de:

- autenticação(usuário)
- autorização(privilégios)

Security permite controlar o acesso e proteger recursos de :
- [[servlet]]
- [[JAX-RS]]

Além de integrar com:
- [[JPA]]
- [[CDI]]

## Autorização
Uso de Roles que definem que tipo de usuário pode acessar aquele recurso.

```java 
@RolesAllowed("ADMIN")
	public class AdminResource{
	
	...
	
	}



```


## Autenticação:
Uso do componente Authentication Mechanism que define como um usuário pode se autenticar.

#### @BasicAuthenticationMechanismDefinition
 
 Mechanism básico, usuário e senha no header da requisição.
 ```java 
 
 @BasicAuthenticationMechanismDefinition
 public class SecurityConfig{}
 
 ```


#### @FormAuthenticationMechanismDefinition
Mechanism que utiliza formulário(HTML)

```java 

@FormAuthenticationMechanismDefinition(loginToContinue = @LoginToContinue(
        loginPage = "/login.html",
        errorPage = "/erro.html"
    ))



```


#### @LoginConfig(jwt)

Muito usado em APIs modernas.
```java 

@LoginConfig(authMethod = "MP-JWT")
public class JwtConfig { }
```



> [!NOTE] 
> [[Quarkus]] utiliza security de forma evoluída e simplificada mas ainda utilizando Roles.
