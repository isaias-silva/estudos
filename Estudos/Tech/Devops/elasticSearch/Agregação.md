agregações permitem extração de métricas, estatísticas e resumos analíticos.  

POST http://localhost:9200/meu-indice/_search

##  agrupamentos
agrupam documentos com base em critérios, como termos.

```json
{ "size": 0, 
	"aggs": {
	 "agregação_por_status":
	 { "terms": {
	  "field": "status.keyword",
	   "size": 10 } 
	   }
	    }
	     }
```
