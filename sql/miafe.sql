-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: mysql.metropolia.fi
-- Generation Time: 27.11.2024 klo 16:46
-- Palvelimen versio: 10.5.27-MariaDB
-- PHP Version: 8.3.13

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `miafe`
--

-- --------------------------------------------------------

--
-- Rakenne taululle `antidotes`
--

CREATE TABLE `antidotes` (
  `antidotes_id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `country_atm` int(11) NOT NULL,
  `description` text NOT NULL,
  `healthbar` int(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Rakenne taululle `event`
--

CREATE TABLE `event` (
  `event_id` int(11) NOT NULL,
  `description` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

-- --------------------------------------------------------

--
-- Rakenne taululle `leaderboard`
--

CREATE TABLE `leaderboard` (
  `leaderboard_id` int(11) NOT NULL,
  `player_id` int(11) NOT NULL,
  `healthbar_final` int(10) NOT NULL,
  `time` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci COMMENT='pisteet ja sijoitus';

-- --------------------------------------------------------

--
-- Rakenne taululle `player`
--

CREATE TABLE `player` (
  `player_id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `healthbar` int(10) NOT NULL,
  `current_airport` varchar(11) NOT NULL DEFAULT current_timestamp(),
  `countries_visited` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`countries_visited`)),
  `collected_antidotes` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL CHECK (json_valid(`collected_antidotes`)),
  `start_time` int(11) NOT NULL DEFAULT current_timestamp(),
  `ending_time` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci COMMENT='Pelaajan tiedot, terveys ja sijainti ';

-- --------------------------------------------------------

--
-- Rakenne taululle `tasks`
--

CREATE TABLE `tasks` (
  `tasks_id` int(11) NOT NULL,
  `description` text NOT NULL,
  `reward_health` int(1) NOT NULL,
  `penalty_health` int(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COLLATE=latin1_swedish_ci;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `antidotes`
--
ALTER TABLE `antidotes`
  ADD PRIMARY KEY (`antidotes_id`);

--
-- Indexes for table `event`
--
ALTER TABLE `event`
  ADD PRIMARY KEY (`event_id`);

--
-- Indexes for table `leaderboard`
--
ALTER TABLE `leaderboard`
  ADD PRIMARY KEY (`leaderboard_id`);

--
-- Indexes for table `player`
--
ALTER TABLE `player`
  ADD PRIMARY KEY (`player_id`);

--
-- Indexes for table `tasks`
--
ALTER TABLE `tasks`
  ADD PRIMARY KEY (`tasks_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
