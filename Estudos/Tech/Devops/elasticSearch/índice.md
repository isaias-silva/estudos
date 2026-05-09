Coleção de [[Documentos]] que possuem características semelhantes e são armazenados juntos.

## índice invertido 
em vez de indexar o documento, o elastic cria um índice e que aponta para os documentos que contenham a palavra, permitindo que a busca seja feita de forma mais rápida.

- o índice invertido pode armazenar informações como frequência de termos e a posição em que aparecem nos documentos.

TF-IDF = Term Frequency * Inverse Document Frequency

Term Frequency: frequência com que uma palavra aparece em um documento.
Document Frequency : é a frequência em que um termo aparece em todos os documentos.

Relevância = Term Frequency / Document Frequency


- Um Índice está divido em [[shards]]. 