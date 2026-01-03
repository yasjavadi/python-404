-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 03, 2026 at 06:21 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `new_db`
--

-- --------------------------------------------------------

--
-- Table structure for table `kala`
--

CREATE TABLE `kala` (
  `name` varchar(100) NOT NULL,
  `cod` int(25) NOT NULL,
  `price` int(10) NOT NULL,
  `count` int(25) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `kala`
--

INSERT INTO `kala` (`name`, `cod`, `price`, `count`) VALUES
('mouse', 1001, 122200000, 25),
('phone', 1003, 1222222, 30),
('ipad', 1006, 12222000, 555),
('phone', 1007, 12200000, 15),
('ipad', 1012, 12, 120000),
('tv2', 1013, 2000000, 15),
('ipad1', 1014, 25, 140000),
('key3', 1015, 8, 12222);

-- --------------------------------------------------------

--
-- Table structure for table `test.p`
--

CREATE TABLE `test.p` (
  `city` varchar(11) NOT NULL,
  `gender` varchar(11) NOT NULL,
  `count` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `test.p`
--

INSERT INTO `test.p` (`city`, `gender`, `count`) VALUES
('tehran', 'man', 1500),
('tehran', 'man', 1500),
('zanjan', 'woman', 2000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `kala`
--
ALTER TABLE `kala`
  ADD PRIMARY KEY (`cod`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `kala`
--
ALTER TABLE `kala`
  MODIFY `cod` int(25) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=1016;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
