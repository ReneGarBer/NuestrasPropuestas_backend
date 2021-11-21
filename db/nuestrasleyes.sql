-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Nov 15, 2021 at 08:21 AM
-- Server version: 5.7.24
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `nuestrasleyes`
--

-- --------------------------------------------------------

--
-- Table structure for table `actualizacion`
--

CREATE TABLE `actualizacion` (
  `Id` int(11) NOT NULL,
  `Infolej` int(255) DEFAULT NULL,
  `FechaRegistro` date DEFAULT NULL,
  `NumSesion` int(255) DEFAULT NULL,
  `Estado` text,
  `Condicion` text,
  `NumAcuerdo` int(255) DEFAULT NULL,
  `Documento` text,
  `DateBorn` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `autores`
--

CREATE TABLE `autores` (
  `Id` int(11) NOT NULL,
  `Infolej` int(255) DEFAULT NULL,
  `Legislador` int(255) DEFAULT NULL,
  `Tipo` text,
  `DateBorn` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `bancadas`
--

CREATE TABLE `bancadas` (
  `Id` int(11) NOT NULL,
  `Legislador` int(255) DEFAULT NULL,
  `Partido` text,
  `Inicio` date DEFAULT NULL,
  `Fin` date DEFAULT NULL,
  `DateBorn` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `clasificaciones`
--

CREATE TABLE `clasificaciones` (
  `Id` int(11) NOT NULL,
  `Nombre` text,
  `DateBorn` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `comisiones`
--

CREATE TABLE `comisiones` (
  `Id` int(11) NOT NULL,
  `Legislatura` int(255) DEFAULT NULL,
  `Nombre` text,
  `Permanente` smallint(255) DEFAULT NULL,
  `DateBorn` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `comisionestudio`
--

CREATE TABLE `comisionestudio` (
  `Id` int(11) NOT NULL,
  `Infolej` int(255) DEFAULT NULL,
  `Comision` int(255) DEFAULT NULL,
  `DateBorn` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `diarios`
--

CREATE TABLE `diarios` (
  `Id` int(11) NOT NULL,
  `Infolej` int(255) DEFAULT NULL,
  `Liga` text,
  `DateBorn` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `infolej`
--

CREATE TABLE `infolej` (
  `Id` int(11) NOT NULL,
  `Legislatura` int(255) DEFAULT NULL,
  `FechaIngreso` date DEFAULT NULL,
  `Titulo` text,
  `Tipo` text,
  `DateBorn` datetime DEFAULT NULL,
  `FechaActualizacion` date DEFAULT NULL,
  `Actualizar` int(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `legisladores`
--

CREATE TABLE `legisladores` (
  `Id` int(11) NOT NULL,
  `Nombre` text,
  `Tipo` text,
  `Legislatura` int(255) DEFAULT NULL,
  `Partido` text,
  `Data` text,
  `DateBorn` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `legislatura`
--

CREATE TABLE `legislatura` (
  `Numero` int(255) NOT NULL,
  `AnioInicio` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `temas`
--

CREATE TABLE `temas` (
  `Id` int(11) NOT NULL,
  `Clasificacion` int(255) DEFAULT NULL,
  `Nombre` text,
  `DateBorn` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `temasinfolej`
--

CREATE TABLE `temasinfolej` (
  `Id` int(11) NOT NULL,
  `Tema` int(255) DEFAULT NULL,
  `Infolej` int(255) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `actualizacion`
--
ALTER TABLE `actualizacion`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Infolej` (`Infolej`);

--
-- Indexes for table `autores`
--
ALTER TABLE `autores`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Infolej` (`Infolej`),
  ADD KEY `Legislador` (`Legislador`);

--
-- Indexes for table `bancadas`
--
ALTER TABLE `bancadas`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Legislador` (`Legislador`);

--
-- Indexes for table `clasificaciones`
--
ALTER TABLE `clasificaciones`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `comisiones`
--
ALTER TABLE `comisiones`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Legislatura` (`Legislatura`);

--
-- Indexes for table `comisionestudio`
--
ALTER TABLE `comisionestudio`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Infolej` (`Infolej`),
  ADD KEY `Comision` (`Comision`);

--
-- Indexes for table `diarios`
--
ALTER TABLE `diarios`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Infolej` (`Infolej`);

--
-- Indexes for table `infolej`
--
ALTER TABLE `infolej`
  ADD PRIMARY KEY (`Id`);

--
-- Indexes for table `legisladores`
--
ALTER TABLE `legisladores`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Legislatura` (`Legislatura`);

--
-- Indexes for table `legislatura`
--
ALTER TABLE `legislatura`
  ADD PRIMARY KEY (`Numero`);

--
-- Indexes for table `temas`
--
ALTER TABLE `temas`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Clasificacion` (`Clasificacion`);

--
-- Indexes for table `temasinfolej`
--
ALTER TABLE `temasinfolej`
  ADD PRIMARY KEY (`Id`),
  ADD KEY `Tema` (`Tema`),
  ADD KEY `Infolej` (`Infolej`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `actualizacion`
--
ALTER TABLE `actualizacion`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `autores`
--
ALTER TABLE `autores`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `bancadas`
--
ALTER TABLE `bancadas`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `clasificaciones`
--
ALTER TABLE `clasificaciones`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `comisiones`
--
ALTER TABLE `comisiones`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `comisionestudio`
--
ALTER TABLE `comisionestudio`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `diarios`
--
ALTER TABLE `diarios`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `infolej`
--
ALTER TABLE `infolej`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `legisladores`
--
ALTER TABLE `legisladores`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `temas`
--
ALTER TABLE `temas`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `temasinfolej`
--
ALTER TABLE `temasinfolej`
  MODIFY `Id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `actualizacion`
--
ALTER TABLE `actualizacion`
  ADD CONSTRAINT `actualizacion_ibfk_1` FOREIGN KEY (`Infolej`) REFERENCES `infolej` (`Id`);

--
-- Constraints for table `autores`
--
ALTER TABLE `autores`
  ADD CONSTRAINT `autores_ibfk_1` FOREIGN KEY (`Infolej`) REFERENCES `infolej` (`Id`),
  ADD CONSTRAINT `autores_ibfk_2` FOREIGN KEY (`Legislador`) REFERENCES `legisladores` (`Id`);

--
-- Constraints for table `bancadas`
--
ALTER TABLE `bancadas`
  ADD CONSTRAINT `bancadas_ibfk_1` FOREIGN KEY (`Legislador`) REFERENCES `legisladores` (`Id`);

--
-- Constraints for table `comisiones`
--
ALTER TABLE `comisiones`
  ADD CONSTRAINT `comisiones_ibfk_1` FOREIGN KEY (`Legislatura`) REFERENCES `legislatura` (`Numero`);

--
-- Constraints for table `comisionestudio`
--
ALTER TABLE `comisionestudio`
  ADD CONSTRAINT `comisionestudio_ibfk_1` FOREIGN KEY (`Infolej`) REFERENCES `infolej` (`Id`),
  ADD CONSTRAINT `comisionestudio_ibfk_2` FOREIGN KEY (`Comision`) REFERENCES `comisiones` (`Id`);

--
-- Constraints for table `diarios`
--
ALTER TABLE `diarios`
  ADD CONSTRAINT `diarios_ibfk_1` FOREIGN KEY (`Infolej`) REFERENCES `infolej` (`Id`);

--
-- Constraints for table `legisladores`
--
ALTER TABLE `legisladores`
  ADD CONSTRAINT `legisladores_ibfk_1` FOREIGN KEY (`Legislatura`) REFERENCES `legislatura` (`Numero`);

--
-- Constraints for table `temas`
--
ALTER TABLE `temas`
  ADD CONSTRAINT `temas_ibfk_1` FOREIGN KEY (`Clasificacion`) REFERENCES `clasificaciones` (`Id`);

--
-- Constraints for table `temasinfolej`
--
ALTER TABLE `temasinfolej`
  ADD CONSTRAINT `temasinfolej_ibfk_1` FOREIGN KEY (`Tema`) REFERENCES `temas` (`Id`),
  ADD CONSTRAINT `temasinfolej_ibfk_2` FOREIGN KEY (`Infolej`) REFERENCES `infolej` (`Id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
