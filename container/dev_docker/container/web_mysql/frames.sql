-- phpMyAdmin SQL Dump
-- version 4.2.7.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Erstellungszeit: 20. Mrz 2016 um 22:59
-- Server Version: 5.6.20
-- PHP-Version: 5.5.15

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Datenbank: `frames`
--

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `frames_requests`
--

CREATE TABLE IF NOT EXISTS `frames_requests` (
  `request_id` int(32) NOT NULL,
  `request_data` text NOT NULL,
  `request_timestamp` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `request_rel` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `frames_user`
--

CREATE TABLE IF NOT EXISTS `frames_user` (
  `user_id` int(32) NOT NULL,
  `user_name` varchar(11) NOT NULL,
  `user_permission` int(2) DEFAULT NULL,
  `user_email` varchar(32) DEFAULT NULL,
  `user_created` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `user_updated` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Daten für Tabelle `frames_user`
--

INSERT INTO `frames_user` (`user_id`, `user_name`, `user_permission`, `user_email`, `user_created`, `user_updated`) VALUES
(1, 'cory', 12, 'info@corykey.com', '2016-03-20 20:10:03', '2016-03-20 20:10:03'),
(2, 'peter', 1, 'peter@corykey.com', '2016-03-20 21:45:59', '2016-03-20 21:45:59'),
(3, 'Henry', 3, 'henry@corykey.com', '2016-03-20 21:46:28', '2016-03-20 21:46:28');

-- --------------------------------------------------------

--
-- Tabellenstruktur für Tabelle `frames_user_status`
--

CREATE TABLE IF NOT EXISTS `frames_user_status` (
  `status_user` int(12) NOT NULL DEFAULT '0',
  `status_online` int(1) DEFAULT NULL,
  `status_permission` int(12) DEFAULT NULL,
  `status_account` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `frames_user`
--
ALTER TABLE `frames_user`
 ADD PRIMARY KEY (`user_id`), ADD UNIQUE KEY `user_id` (`user_id`);

--
-- Indexes for table `frames_user_status`
--
ALTER TABLE `frames_user_status`
 ADD PRIMARY KEY (`status_user`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
