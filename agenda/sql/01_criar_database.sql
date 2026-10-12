-- Meu Dia - cria o database `agenda` caso ele ainda não exista no computador.
-- Seguro para rodar mais de uma vez: não apaga nada.

CREATE DATABASE IF NOT EXISTS agenda
  CHARACTER SET utf8mb4
  COLLATE utf8mb4_unicode_ci;

USE agenda;

SELECT DATABASE() AS banco_atual;
SHOW TABLES;
