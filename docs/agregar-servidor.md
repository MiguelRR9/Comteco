# Agregar un nuevo servidor

## Pasos
1. Identificar el tipo de servidor
   - mysql
   - linux
   - apache

2. Elegir la plantilla correspondiente

3. Editar:
   - nombre del servidor
   - ruta del log
   - IP y puerto de Kafka

4. Validar configuración
```bash
./filebeat test config -c filebeat.yml
./filebeat test output -c filebeat.yml

## Hacer correr el filebeat en el servidor


./filebeat -e -strict.perms=false -c filebeat.yml

##
