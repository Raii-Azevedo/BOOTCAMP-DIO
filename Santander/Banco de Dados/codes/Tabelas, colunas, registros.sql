CREATE TABLE viagens (
  id INT,
  nome VARCHAR(255) NOT NULL COMMENT 'Nome do usuário',
  email VARCHAR(255) NOT NULL UNIQUE COMMENT 'Endereço de e-mail do usuário',
);

CREATE TABLE viagens.destinos (
	id INT,
    nome VARCHAR(255) NOT NULL UNIQUE COMMENT "Nome do Destino",
    descricao VARCHAR(300) NOT NULL COMMENT "Descrição do destino"
);

CREATE TABLE viagens.reservas (
	id INT COMMENT "Identificador único de reserva",
    id_usuario INT COMMENT "Referência ao ID do usuário que fez a reserva",
    id_destino INT COMMENT "Referência ao ID do destino da reserva",
    data DATE COMMENT "Data da reserva",
    status VARCHAR(255) DEFAULT 'pendente' COMMENT "Status da reserva (confirmada, pendente, cancelada, etc)"
);