Elasticsearch é um motor de busca e análise de dados, foi projetado para trabalhar com grandes volumes de dados de forma rápida.

ideal para:

- logs
- análise de sistemas
- buscas
-  suporta dados estruturados
- foi projetado especialmente para pesquisa:
- [[índice#índice invertido]]: palavra vira o índice.
- full text search(texto é tratado antes): remoção de palavras inúteis, quebra frases em palavras.
- diferente do banco, o trabalho ocorre na hora de salvar, a busca é apenas consulta do índice. 
- score organiza peso de cada documento de acordo com a pesquisa.
-  comunicação via API rest, possível usar com qualquer linguagem

## ELK

Elastic Stack é uma plataforma de código aberto composta pelo ElasticSearch, [[Kibana]], [[Beats]] e [[Logstash]]. 

## Conceitos lógicos:
- [[Documentos]]
- [[índice]]
- [[cluster]]

![[index-cluster-doc.png]]

## Elasticsearch 7

- descontinuou o tipo de documento
- suporte a SQL 
-  Java "bundle"
- Replicação cross-cluster.
- Index Life-cycle.
- HLRC: cliente java Rest

### tópicos:

[[indexing e mapping]]
[[busca e consulta]]