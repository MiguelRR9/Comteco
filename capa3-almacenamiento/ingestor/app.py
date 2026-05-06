import json
import time
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable
import psycopg2


DB_CONFIG = {
    "host": "postgres",
    "database": "comteco_logs",    
    "user": "comteco",
    "password": "comteco123",
    "port": 5432,
}


def wait_for_postgres():
    while True:
        try:
            conn = psycopg2.connect(**DB_CONFIG)
            conn.close()
            print("PostgreSQL listo")
            break
        except Exception as e:
            print(f"Esperando PostgreSQL... {e}")
            time.sleep(5)


def wait_for_kafka():
    while True:
        try:
            consumer = KafkaConsumer(
                bootstrap_servers="kafka:9092",
                api_version_auto_timeout_ms=5000,
            )
            consumer.close()
            print("Kafka listo")
            break
        except NoBrokersAvailable as e:
            print(f"Esperando Kafka... {e}")
            time.sleep(5)


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def main():
    wait_for_postgres()
    wait_for_kafka()

    consumer = KafkaConsumer(
        "comteco-logs-procesados",
        bootstrap_servers="kafka:9092",
        auto_offset_reset="earliest",
        enable_auto_commit=True,
        group_id="ingestor-comteco",
        value_deserializer=lambda m: json.loads(m.decode("utf-8")),
    )

    conn = get_connection()
    cur = conn.cursor()

    print("Ingestor escuchando topic comteco-logs-procesados...")

    for msg in consumer:
        data = msg.value

        servidor = data.get("fields", {}).get("servidor")
        servicio = data.get("fields", {}).get("servicio")
        empresa = data.get("fields", {}).get("empresa")

        log_fecha = data.get("log_fecha")
        log_nivel = data.get("log_nivel")
        log_codigo = data.get("log_codigo")
        log_componente = data.get("log_componente")
        log_detalle = data.get("log_detalle")
        message_original = data.get("message")

        try:
            cur.execute(
                """
                INSERT INTO logs_procesados (
                    log_fecha,
                    servidor,
                    servicio,
                    empresa,
                    log_nivel,
                    log_codigo,
                    log_componente,
                    log_detalle,
                    message_original
                )
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                """,
                (
                    log_fecha,
                    servidor,
                    servicio,
                    empresa,
                    log_nivel,
                    log_codigo,
                    log_componente,
                    log_detalle,
                    message_original,
                ),
            )
            conn.commit()
            print(f"Guardado: {servidor} | {servicio} | {log_nivel} | {log_codigo}")
        except Exception as e:
            conn.rollback()
            print(f"Error insertando: {e}")


if __name__ == "__main__":
    main()