-- Meu Dia - Etapa 02: modelagem do banco
-- Usa o database que já existe: agenda
-- Seguro para rodar mais de uma vez: não apaga nada.

USE agenda;

-- Tabela de usuários
CREATE TABLE IF NOT EXISTS usuarios (
    id          INT UNSIGNED NOT NULL AUTO_INCREMENT,
    nome        VARCHAR(100) NOT NULL,
    email       VARCHAR(150) NOT NULL,
    senha_hash  VARCHAR(255) NOT NULL,  -- nunca guardar a senha em texto puro
    criado_em   DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    UNIQUE KEY uq_usuarios_email (email)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Tabela de tarefas (cada tarefa pertence a um usuário)
CREATE TABLE IF NOT EXISTS tarefas (
    id                  INT UNSIGNED NOT NULL AUTO_INCREMENT,
    usuario_id          INT UNSIGNED NOT NULL,
    titulo              VARCHAR(150) NOT NULL,
    descricao           TEXT NULL,
    categoria           VARCHAR(50) NULL,
    prioridade          ENUM('baixa', 'media', 'alta') NOT NULL DEFAULT 'media',
    data_prevista       DATE NOT NULL,
    tempo_estimado_min  INT UNSIGNED NOT NULL DEFAULT 0,  -- em minutos
    status              ENUM('pendente', 'em_andamento', 'concluida') NOT NULL DEFAULT 'pendente',
    criado_em           DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    atualizado_em       DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (id),
    KEY idx_tarefas_usuario_data (usuario_id, data_prevista),
    CONSTRAINT fk_tarefas_usuario
        FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- Conferência
SHOW TABLES;
DESCRIBE usuarios;
DESCRIBE tarefas;
