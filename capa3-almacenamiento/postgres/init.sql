CREATE TABLE IF NOT EXISTS logs_procesados (
    id BIGSERIAL PRIMARY KEY,
    log_fecha TIMESTAMP NULL,
    servidor VARCHAR(100),
    servicio VARCHAR(50),
    empresa VARCHAR(100),
    log_nivel VARCHAR(50),
    log_codigo VARCHAR(50),
    log_componente VARCHAR(100),
    log_detalle TEXT,
    message_original TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);