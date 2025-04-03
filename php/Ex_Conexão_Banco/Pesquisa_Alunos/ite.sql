-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 29/03/2025 às 01:21
-- Versão do servidor: 10.4.32-MariaDB
-- Versão do PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `ite`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `alunos`
--

CREATE TABLE `alunos` (
  `ra` int(11) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `idade` int(11) NOT NULL,
  `curso` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `alunos`
--

INSERT INTO `alunos` (`ra`, `nome`, `idade`, `curso`) VALUES
(2025000001, 'Lucas Oliveira', 20, 'Engenharia Civil'),
(2025000002, 'Mariana Santos', 22, 'Administração'),
(2025000003, 'Felipe Souza', 19, 'Ciência da Computação'),
(2025000004, 'Ana Paula Lima', 21, 'Medicina'),
(2025000005, 'Carlos Eduardo Silva', 23, 'Direito'),
(2025000006, 'Bruno Mendes', 18, 'Arquitetura'),
(2025000007, 'Fernanda Carvalho', 20, 'Psicologia'),
(2025000008, 'Rafael Costa', 22, 'Engenharia de Produção'),
(2025000009, 'Gabriela Almeida', 19, 'Publicidade e Propaganda'),
(2025000010, 'Lucas Oliveira', 21, 'Ciência da Computação'),
(2025000011, 'Amanda Rocha', 22, 'Biomedicina'),
(2025000012, 'Vinícius Lima', 20, 'Engenharia Mecânica'),
(2025000013, 'Camila Pereira', 19, 'Moda'),
(2025000014, 'Juliana Souza', 23, 'Enfermagem'),
(2025000015, 'Pedro Henrique Santos', 22, 'Direito'),
(2025000016, 'Tatiane Almeida', 21, 'Relações Internacionais'),
(2025000017, 'Ricardo Nunes', 18, 'Matemática'),
(2025000018, 'Jessica Oliveira', 20, 'Física'),
(2025000019, 'Thiago Mendes', 22, 'História'),
(2025000020, 'Patrícia Carvalho', 19, 'Farmácia'),
(2025000021, 'Lucas Souza', 21, 'Engenharia Química'),
(2025000022, 'Rafaela Costa', 23, 'Design Gráfico'),
(2025000023, 'Gustavo Pereira', 18, 'Jornalismo'),
(2025000024, 'Adriana Silva', 20, 'Nutrição'),
(2025000025, 'Anderson Lima', 22, 'Odontologia'),
(2025000026, 'Rodrigo Nunes', 19, 'Educação Física'),
(2025000027, 'Vanessa Santos', 21, 'Fisioterapia'),
(2025000028, 'Bruna Rocha', 23, 'Gastronomia'),
(2025000029, 'Matheus Almeida', 18, 'Economia'),
(2025000030, 'Fernanda Costa', 20, 'Geografia'),
(2025000031, 'Gabriel Oliveira', 22, 'Letras'),
(2025000032, 'Patrícia Mendes', 19, 'Química'),
(2025000033, 'Diego Carvalho', 21, 'Medicina Veterinária'),
(2025000034, 'Aline Lima', 23, 'Engenharia Ambiental'),
(2025000035, 'Roberto Souza', 18, 'Ciências Contábeis'),
(2025000036, 'Lucas Silva', 20, 'Engenharia Elétrica'),
(2025000037, 'Juliana Rocha', 22, 'Serviço Social'),
(2025000038, 'Daniel Pereira', 19, 'Biologia'),
(2025000039, 'Mariana Nunes', 21, 'Engenharia Civil'),
(2025000040, 'Carlos Eduardo Costa', 23, 'Administração'),
(2025000041, 'Fernanda Souza', 18, 'Ciência da Computação'),
(2025000042, 'Rafael Mendes', 20, 'Medicina'),
(2025000043, 'Camila Oliveira', 22, 'Direito'),
(2025000044, 'Pedro Henrique Lima', 19, 'Arquitetura'),
(2025000045, 'Jessica Pereira', 21, 'Psicologia'),
(2025000046, 'Vinícius Carvalho', 23, 'Engenharia de Produção'),
(2025000047, 'Amanda Santos', 18, 'Publicidade e Propaganda'),
(2025000048, 'Bruno Costa', 20, 'Biomedicina'),
(2025000049, 'Juliana Almeida', 22, 'Engenharia Mecânica'),
(2025000050, 'Rodrigo Silva', 19, 'Moda'),
(2025000051, 'Gabriela Rocha', 21, 'Enfermagem'),
(2025000052, 'Lucas Nunes', 23, 'Direito'),
(2025000053, 'Mariana Lima', 18, 'Relações Internacionais'),
(2025000054, 'Felipe Carvalho', 20, 'Matemática'),
(2025000055, 'Ana Paula Souza', 22, 'Física'),
(2025000056, 'Carlos Eduardo Mendes', 19, 'História'),
(2025000057, 'Fernanda Santos', 21, 'Farmácia'),
(2025000058, 'Thiago Almeida', 23, 'Engenharia Química'),
(2025000059, 'Bruno Pereira', 18, 'Design Gráfico'),
(2025000060, 'Tatiane Costa', 20, 'Jornalismo'),
(2025000061, 'Gabriel Lima', 22, 'Nutrição'),
(2025000062, 'Aline Nunes', 19, 'Odontologia'),
(2025000063, 'Rafael Rocha', 21, 'Educação Física'),
(2025000064, 'Juliana Carvalho', 23, 'Fisioterapia'),
(2025000065, 'Patrícia Silva', 18, 'Gastronomia'),
(2025000066, 'Rodrigo Mendes', 20, 'Economia'),
(2025000067, 'Lucas Costa', 22, 'Geografia'),
(2025000068, 'Jessica Almeida', 19, 'Letras'),
(2025000069, 'Carlos Eduardo Pereira', 21, 'Química'),
(2025000070, 'Ana Paula Nunes', 23, 'Medicina Veterinária'),
(2025000071, 'Felipe Santos', 18, 'Engenharia Ambiental'),
(2025000072, 'Gustavo Souza', 20, 'Ciências Contábeis'),
(2025000073, 'Bruna Lima', 22, 'Engenharia Elétrica'),
(2025000074, 'Matheus Rocha', 19, 'Serviço Social'),
(2025000075, 'Vinícius Pereira', 21, 'Biologia'),
(2025000076, 'Diego Costa', 23, 'Engenharia Civil'),
(2025000077, 'Amanda Almeida', 18, 'Administração'),
(2025000078, 'Pedro Henrique Mendes', 20, 'Ciência da Computação'),
(2025000079, 'Rafaela Carvalho', 22, 'Medicina'),
(2025000080, 'Rodrigo Lima', 19, 'Direito'),
(2025000081, 'Fernanda Nunes', 21, 'Arquitetura'),
(2025000082, 'Gustavo Silva', 23, 'Psicologia'),
(2025000083, 'Carlos Eduardo Rocha', 18, 'Engenharia de Produção'),
(2025000084, 'Camila Santos', 20, 'Publicidade e Propaganda'),
(2025000085, 'Lucas Pereira', 22, 'Biomedicina'),
(2025000086, 'Tatiane Almeida', 19, 'Engenharia Mecânica'),
(2025000087, 'Bruna Nunes', 21, 'Moda'),
(2025000088, 'Rafael Souza', 23, 'Enfermagem'),
(2025000089, 'Jessica Carvalho', 18, 'Direito'),
(2025000090, 'Gabriela Lima', 20, 'Relações Internacionais'),
(2025000091, 'Vinícius Santos', 22, 'Matemática'),
(2025000092, 'Rodrigo Pereira', 19, 'Física'),
(2025000093, 'Lucas Mendes', 21, 'História'),
(2025000094, 'Aline Costa', 23, 'Farmácia'),
(2025000095, 'Carlos Eduardo Almeida', 18, 'Engenharia Química'),
(2025000096, 'Mariana Rocha', 20, 'Design Gráfico'),
(2025000097, 'Felipe Nunes', 22, 'Jornalismo'),
(2025000098, 'Gabriela Santos', 19, 'Nutrição'),
(2025000099, 'Thiago Carvalho', 21, 'Odontologia'),
(2025000100, 'Juliana Souza', 23, 'Educação Física');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `alunos`
--
ALTER TABLE `alunos`
  ADD PRIMARY KEY (`ra`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
