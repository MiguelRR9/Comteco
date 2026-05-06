CREATE TABLE IF NOT EXISTS servidores (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL UNIQUE,
    ip VARCHAR(50),
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS servicios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL UNIQUE,
    categoria VARCHAR(50),
    activo BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS logs_procesados (
    id BIGSERIAL PRIMARY KEY,
    log_fecha TIMESTAMP NULL,
    servidor_id INT REFERENCES servidores(id),
    servicio_id INT REFERENCES servicios(id),
    empresa VARCHAR(100),
    log_nivel VARCHAR(50),
    log_codigo VARCHAR(50),
    log_componente VARCHAR(100),
    log_detalle TEXT,
    message_original TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_logs_fecha ON logs_procesados(log_fecha);
CREATE INDEX IF NOT EXISTS idx_logs_servidor ON logs_procesados(servidor_id);
CREATE INDEX IF NOT EXISTS idx_logs_servicio ON logs_procesados(servicio_id);
CREATE INDEX IF NOT EXISTS idx_logs_nivel ON logs_procesados(log_nivel);
CREATE INDEX IF NOT EXISTS idx_logs_codigo ON logs_procesados(log_codigo);


INSERT INTO servicios (nombre, categoria)
VALUES ('mysql', 'base_de_datos')
ON CONFLICT (nombre) DO NOTHING;

INSERT INTO servidores (nombre, ip)
VALUES ('becom-bd-01', '192.9.200.159')
ON CONFLICT (nombre) DO NOTHING;