/*
SQLyog Community v13.2.0 (64 bit)
MySQL - 8.0.12 : Database - dfstock
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`dfstock` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */;

USE `dfstock`;

/*Table structure for table `stock_concepts` */

DROP TABLE IF EXISTS `stock_concepts`;

CREATE TABLE `stock_concepts` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ts_code` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `trade_date` date NOT NULL,
  `concepts` varchar(2000) COLLATE utf8mb4_general_ci DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `unique_ts_code_trade_date` (`ts_code`,`trade_date`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*Table structure for table `stock_data` */

DROP TABLE IF EXISTS `stock_data`;

CREATE TABLE `stock_data` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ts_code` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `trade_date` date NOT NULL,
  `open` float(10,4) DEFAULT NULL,
  `high` float(10,4) DEFAULT NULL,
  `low` float(10,4) DEFAULT NULL,
  `close` float(10,4) DEFAULT NULL,
  `pre_close` float(10,4) DEFAULT NULL,
  `change` float(10,4) DEFAULT NULL,
  `pct_chg` float(10,4) DEFAULT NULL,
  `vol` bigint(20) DEFAULT NULL,
  `amount` decimal(20,5) DEFAULT NULL,
  PRIMARY KEY (`id`) USING BTREE,
  UNIQUE KEY `unique_ts_code_trade_date` (`ts_code`,`trade_date`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
