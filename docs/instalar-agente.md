# Instalar agente Filebeat

## Pasos
1. Conectarse al servidor
2. Descargar Filebeat
3. Descomprimir Filebeat
4. Copiar la plantilla correspondiente
5. Editar:
   - nombre del servidor
   - ruta del log
   - IP y puerto de Kafka
6. Validar configuración
7. Ejecutar Filebeat

## Validación
```bash
./filebeat test config -c filebeat.yml
./filebeat test output -c filebeat.yml

## La ejecucion es con este comando

./filebeat -e -strict.perms=false -c filebeat.yml


###