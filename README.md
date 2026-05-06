# Plataforma de Monitoreo y Análisis de Logs - Comteco

8. Resumen corto para decirlo de memoria

Puedes decir esto:

La Capa 1 recoge logs del servidor real con Filebeat y los manda a Kafka.
La Capa 2 usa Logstash para convertir esos logs en campos estructurados.
La Capa 3 los almacena en PostgreSQL mediante un ingestor en Python.
La Capa 4 será una API para que los encargados consulten los logs desde una app o panel.