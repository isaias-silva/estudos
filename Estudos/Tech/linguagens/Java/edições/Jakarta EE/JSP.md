Java server pages, camada de visualização em aplicações web java.

basicamente combina HTML com a linguagem java.

```jsp

<html>
<body>
    <h1>Olá, mundo!</h1>
    <p>Hora no servidor: <%= new java.util.Date() %></p>
</body>
</html>


```


Funciona como camada view em aplicações  [[servlet]], onde a lógica é responsabilidade do servlet e a exibição de dados com o jsp.




> [!info]
> JSP é uma tecnologia legado, sendo preferível hoje uso de frontend separado.
