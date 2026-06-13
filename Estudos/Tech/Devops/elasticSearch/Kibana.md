Ferramenta da elasticStack responsável por garantir a visualização e análise de dados.

### Instalação:

Mais usual via docker:

```yaml
services:
	kibana: 
		image: docker.elastic.co/kibana/kibana:8.12.0 
		container_name: kibana ports: - "5601:5601"
		environment: - ELASTICSEARCH_HOSTS=http://elasticsearch:9200

```
