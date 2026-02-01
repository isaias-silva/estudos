[[interfaces]] devem ser especificas e minimalistas, o objetivo desse principio é evitar a "interface gorda"



> [!EXAMPLE] Exemplo
> a interface Bot possui em seu contrato o método sendMessage, postPublication, porém caso essa interface implemente um Bot de uma rede social que não possui feed de publicação, não faz sentido o método postPublication, separando assim em duas interfaces, ChatBot e FeedBot por exemplo.
