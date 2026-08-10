-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 08-Abr-2026 às 03:03
-- Versão do servidor: 10.4.32-MariaDB
-- versão do PHP: 8.2.12





sudo timedatectl set-ntp true





timedatectl status









SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `sistema_de_aeroporto`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `historicosdepassageiros`
--

CREATE TABLE `historicosdepassageiros` (
  `id_do_passageiro` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `idade` int(11) DEFAULT NULL,
  `classe` varchar(45) DEFAULT NULL,
  `nessecidadeDAcessibilidade` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `historicosdepassageiros`
--

INSERT INTO `historicosdepassageiros` (`id_do_passageiro`, `nome`, `idade`, `classe`, `nessecidadeDAcessibilidade`) VALUES
(1, 'pedro', 5, 'primeira classe', 'cadeirante'),
(2, 'maria', 32, 'economica', 'nenhuma'),
(3, 'joao', 45, 'executiva', 'baixa visao'),
(4, 'ana', 28, 'economica', 'nenhuma'),
(5, 'carlos', 60, 'primeira classe', 'idoso'),
(6, 'juliana', 14, 'economica', 'menor desacompanhado'),
(7, 'roberto', 50, 'executiva', 'auditiva'),
(8, 'fernanda', 37, 'economica', 'nenhuma'),
(9, 'lucas', 22, 'economica', 'nenhuma'),
(10, 'patricia', 70, 'primeira classe', 'cadeirante');

-- --------------------------------------------------------

--
-- Estrutura da tabela `hitorico_de_funcionarios`
--

CREATE TABLE `hitorico_de_funcionarios` (
  `id_do_funcionario` int(11) NOT NULL,
  `nome` varchar(45) NOT NULL,
  `salario` int(100) DEFAULT NULL,
  `cargo` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `hitorico_de_funcionarios`
--

INSERT INTO `hitorico_de_funcionarios` (`id_do_funcionario`, `nome`, `salario`, `cargo`) VALUES
(1, 'Carlos Silva', 3500, 'Atendente'),
(2, 'Mariana Souza', 7200, 'Gerente'),
(3, 'João Pereira', 2800, 'Auxiliar Administrativo'),
(4, 'Fernanda Lima', 5000, 'Supervisora'),
(5, 'Ricardo Alves', 9000, 'Diretor'),
(6, 'Patrícia Gomes', 4100, 'Analista'),
(7, 'Lucas Rocha', 3000, 'Técnico'),
(8, 'Juliana Martins', 6500, 'Coordenadora'),
(9, 'Bruno Fernandes', 2700, 'Estagiário'),
(10, 'Aline Barbosa', 4800, 'Recursos Humanos');

-- --------------------------------------------------------

--
-- Estrutura da tabela `registro_de_compras`
--

CREATE TABLE `registro_de_compras` (
  `id_da_passagem` int(11) NOT NULL,
  `quantidade_de_passagens_vendidas` varchar(45) NOT NULL,
  `passagens_canceladas` varchar(45) DEFAULT NULL,
  `vagas_de_passagens` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `registro_de_compras`
--

INSERT INTO `registro_de_compras` (`id_da_passagem`, `quantidade_de_passagens_vendidas`, `passagens_canceladas`, `vagas_de_passagens`) VALUES
(1, '120', '5', '180'),
(2, '95', '2', '150'),
(3, '200', '10', '220'),
(4, '75', '3', '100'),
(5, '160', '8', '200'),
(6, '110', '4', '140'),
(7, '180', '6', '210'),
(8, '90', '1', '120'),
(9, '140', '7', '170'),
(10, '130', '5', '160');

-- --------------------------------------------------------

--
-- Estrutura da tabela `rendadosvoos`
--

CREATE TABLE `rendadosvoos` (
  `idDoVoo` int(11) NOT NULL,
  `quantidade_de_pasageiros` int(11) NOT NULL,
  `valor_total_do_voo` int(11) DEFAULT NULL,
  `porsentagem_de_lucro_por_voos` int(11) DEFAULT NULL,
  `porcentagem_de_gastos` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `rendadosvoos`
--

INSERT INTO `rendadosvoos` (`idDoVoo`, `quantidade_de_pasageiros`, `valor_total_do_voo`, `porsentagem_de_lucro_por_voos`, `porcentagem_de_gastos`) VALUES
(1, 120, 50000, 25, 75),
(2, 85, 32000, 20, 80),
(3, 200, 95000, 30, 70),
(4, 60, 21000, 18, 82),
(5, 150, 67000, 27, 73),
(6, 95, 40000, 22, 78),
(7, 180, 88000, 28, 72),
(8, 70, 25000, 19, 81),
(9, 140, 60000, 26, 74),
(10, 110, 47000, 24, 76);

-- --------------------------------------------------------

--
-- Estrutura da tabela `rotas`
--

CREATE TABLE `rotas` (
  `id_da_rota` int(11) NOT NULL,
  `nome_do_aviao` varchar(45) NOT NULL,
  `destino` varchar(45) DEFAULT NULL,
  `horario_de_saida` time DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Extraindo dados da tabela `rotas`
--

INSERT INTO `rotas` (`id_da_rota`, `nome_do_aviao`, `destino`, `horario_de_saida`) VALUES
(1, 'Boein 737', 'Sao Paulo', '08:30:00'),
(2, 'Airbu A320', 'Rio de Janeiro', '10:15:00'),
(3, 'Boing 777', 'Lisboa', '22:00:00'),
(4, 'Airbs A330', 'Buenos Aires', '14:45:00'),
(5, 'Embrer E195', 'Curitiba', '06:20:00'),
(6, 'Being 787', 'Nova York', '23:55:00'),
(7, 'Airus A321', 'Brasilia', '12:10:00'),
(8, 'Ebraer E175', 'Florianopolis', '09:40:00'),
(9, 'Boeing 767', 'Miami', '21:30:00'),
(10, 'Arbus A350', 'Paris', '19:00:00');

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `historicosdepassageiros`
--
ALTER TABLE `historicosdepassageiros`
  ADD PRIMARY KEY (`id_do_passageiro`);

--
-- Índices para tabela `hitorico_de_funcionarios`
--
ALTER TABLE `hitorico_de_funcionarios`
  ADD PRIMARY KEY (`id_do_funcionario`);

--
-- Índices para tabela `registro_de_compras`
--
ALTER TABLE `registro_de_compras`
  ADD PRIMARY KEY (`id_da_passagem`);

--
-- Índices para tabela `rendadosvoos`
--
ALTER TABLE `rendadosvoos`
  ADD PRIMARY KEY (`idDoVoo`);

--
-- Índices para tabela `rotas`
--
ALTER TABLE `rotas`
  ADD PRIMARY KEY (`id_da_rota`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `historicosdepassageiros`
--
ALTER TABLE `historicosdepassageiros`
  MODIFY `id_do_passageiro` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `hitorico_de_funcionarios`
--
ALTER TABLE `hitorico_de_funcionarios`
  MODIFY `id_do_funcionario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `registro_de_compras`
--
ALTER TABLE `registro_de_compras`
  MODIFY `id_da_passagem` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `rendadosvoos`
--
ALTER TABLE `rendadosvoos`
  MODIFY `idDoVoo` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT de tabela `rotas`
--
ALTER TABLE `rotas`
  MODIFY `id_da_rota` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
