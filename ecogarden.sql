CREATE DATABASE ecogarden;
USE ecogarden;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100),
    email VARCHAR(100)
);

CREATE TABLE dispositivos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT,
    nome_dispositivo VARCHAR(50),
    localizacao VARCHAR(100)
);

CREATE TABLE leituras (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dispositivo_id INT,
    nivel_umidade DECIMAL(5,2),
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE irrigacao (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dispositivo_id INT,
    modo VARCHAR(20),
    tempo_segundos INT,
    data_hora TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);