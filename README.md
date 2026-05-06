# Plataforma de Monitoreo y Análisis de Logs - Comteco

## Estado actual
Proyecto organizado por capas, iniciando por la Capa 1: Recolección.

## Capa 1
Objetivo: recolectar logs reales de servidores de Comteco y enviarlos a Kafka.

## Estructura actual
- infraestructura: docker-compose y servicios centrales
- agentes: plantillas de Filebeat por tipo de servidor
- docs: documentación operativa
- ejemplo: caso real de servidor MySQL

## Flujo actual
Servidor -> Filebeat -> Kafka

## Caso real trabajado
- servidor: becom-bd-01
- log: /var/log/mysqld.log
- agente: Filebeat
- destino: Kafka