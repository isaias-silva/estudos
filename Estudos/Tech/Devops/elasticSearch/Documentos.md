no Elastic, um Documento é um dado que você procura, em formato JSON. todo documento tem um ID único.

### Criação de Documentos:

POST http://localhost:9200/products/_doc

```json

{"name": "Boné Águia de Fogo", "price": 300, "description": "Melhor produto de boné"}

```



> [!INFO] 
> É possível definir o id único do documento passando como parâmetro na url logo após o índice, caso contrário o elasticSearch define  um id 

### Atualização de documento
#### Parcial
POST http://localhost:9200/_update/id_doc
quando se quer adicionar apenas algum parâmetro
```json

{"doc":{
"status":"processado",
"atualizado_em":"2026-05-20T11:45"

}}

```

### Completa
PUT http://localhost:9200/my-index/_doc/id-doc
```json
{ "nome_projeto": "gear-roboto",
 "linguagem": "Node.js",
  "status": "ativo" }
```
### Exclusão de documento

DELETE http://localhost:9200/meu-indice/_doc/id_do_documento

### Operações em lote

PUT http://localhost:9200/_bulk
```
Content-Type: application/x-ndjson

{ "index" : { "_index" : "produtos", "_id" : "1" } }
{ "nome" : "Teclado Mecânico", "preco" : 350.00 }
{ "create" : { "_index" : "produtos", "_id" : "2" } }
{ "nome" : "Mouse Gamer", "preco" : 220.00 }
{ "update" : { "_id" : "1", "_index" : "produtos" } }
{ "doc" : {"preco" : 330.00} }
{ "delete" : { "_index" : "produtos", "_id" : "2" } }
```

- **index:** insere ou sobrescreve documento.
- **create:** insere documento caso não exista.
- **update:** atualiza parcialmente um documento.
- **delete:** remove um documento.

>[!INFO]
>falhas em  ____bulk__  não geram Rollback, caso a operação 500 falhe, em 1000, as outras 500 continuarão.

