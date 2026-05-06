# Plataforma de Monitoreo y Análisis de Logs - Comteco

Capa 1 — Recolección
Aquí obtenemos los logs desde el servidor real de Comteco.
Qué usa


Filebeat


archivo de log real, por ejemplo:


/var/log/mysqld.log




Qué hace


lee el log del servidor


le agrega identidad:


servidor


servicio


empresa




lo envía a Kafka


Salida


topic: comteco-logs


Idea simple
Servidor → Filebeat → Kafka

Capa 2 — Procesamiento
Aquí agarramos el log crudo y lo ordenamos.
Qué usa


Logstash


Qué hace


consume desde comteco-logs


separa el mensaje en campos como:


log_fecha


log_nivel


log_codigo


log_componente


log_detalle




vuelve a enviarlo a Kafka ya estructurado


Salida


topic: comteco-logs-procesados


Idea simple
Kafka crudo → Logstash → Kafka procesado

Capa 3 — Almacenamiento
Aquí guardamos los logs procesados en base de datos.
Qué usa


PostgreSQL


Ingestor en Python


Qué hace


el ingestor escucha comteco-logs-procesados


recibe cada log procesado


lo inserta en PostgreSQL


Resultado
Los logs ya quedan guardados en la tabla.
Idea simple
Kafka procesado → Ingestor → PostgreSQL

Flujo completo actual
Así está funcionando hoy:
Servidor real → Filebeat → Kafka (comteco-logs) → Logstash → Kafka (comteco-logs-procesados) → Ingestor → PostgreSQL

Estado actual
Ya funcionando


Capa 1


Capa 2


Capa 3


Lo que sigue
Capa 4 — Backend / API
Será la capa que permita consultar la base desde una aplicación o panel.
Ahí haremos cosas como:


ver últimos logs


filtrar por servidor


filtrar por servicio


filtrar por nivel


buscar por código


ver eventos importantes


Capa 5 — Interfaz para los encargados
Sería la parte visual que usarán los encargados de Comteco.
Capa 6 — Alertas y reportes
Para notificaciones, correo, resumen de errores, etc.

