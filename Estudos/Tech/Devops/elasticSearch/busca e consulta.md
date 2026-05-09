feito pelo endpoint POST https://localhost:9200/index/_search
Toda interação de pesquisa no Elasticsearch acontece em um desses dois "contextos",

## Contexto de Filtro:
uma pergunta binária, se o documento atende ou não ao critério.
### busca por termo exato:
quando se quer algo binário, como buscar ID ou categoria exata:

```json

"query":{
"term":{ "category.keyword":"acessorio"}
}

```

```json
"query":{
"range": { "preco": { "gte": 100 } }
}
```
``
```json
"query":{
"exists": { "field": "desconto" }}
```



## Contexto de Query
tipo de busca onde o conteúdo é analisado e recebe uma nota(``_score``) que diz o quanto aquele documento combinou com a busca.
### busca em campos específicos:
campos específicos dos documentos são utilizados para a busca 

```json
"query":{
"multi_match":{

"query":"boné",
"fields":["name", "description"]

}

}
```

### Match query 
quando se quer que erros de digitação e variações sejam consideradas na busca:

```json
"query": { "match": { "description": "confortável" } }

```



## Consultas complexas
uma consulta complexa utiliza a chave "bool", importante para conectivos lógicos como E, OU, NÃO.

### clausulas:
- **must:** o documento precisa a atender aos critérios dentro do bloco, contribui para a nota de relevância(score)

- **filter:** o documento precisa atender aos critérios,  não afeta a nota de relevância e é mais rápido(devido a ser uma pergunta binária(sim/não) e usar cache)

- **should:**  o documento não é obrigado a ter os critérios do bloco, mas se tiver sobe no score

- **must_not:** se o documento possuir esse critério ele é removido dos resultados.

### exemplos:

```json
{"query":{

"bool":{
"must":[{
"match":{"titulo":"queijo"}}],

"filter":[
{"term":{"disponível":true}}
],

"should":[
{"term":{"categoria.keyword":"paes"}}
], 

"must_not":[
{"term":{"categoria.keyword":"apimentado"}}
]
}
}}
```

