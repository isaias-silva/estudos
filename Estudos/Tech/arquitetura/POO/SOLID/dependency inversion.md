módulos de alto nível não devem depender de módulos de baixo nível e sim de [[Abstração]].

- Abstração sempre antes de implementação.
-  abstrações servem como ponde de comunicação.
-  caso haja uma mudança nos módulos de baixo nível, não deve ser necessário mudança nos módulos de alto nível que o utilizam.


> [!EXAMPLE] exemplo
>
Classe Carro com um atributo do tipo MotorV8, se trocar MotorV8 para MotorV10, será necessário modificar a classe Carro, agora se o atributo possuir o tipo Motor(que pode ser de [[interfaces]] ou uma classe abstrata) e MotorV8 e MotorV10 forem implementações deste, não haverá necessidade de modificar a classe Carro.
