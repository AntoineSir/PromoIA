-- MySQL dump 10.13  Distrib 5.5.62, for Win64 (AMD64)
--
-- Host: localhost    Database: themoviepredictor
-- ------------------------------------------------------
-- Server version	5.5.5-10.4.10-MariaDB

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `companies`
--

DROP TABLE IF EXISTS `companies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `companies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companies`
--

LOCK TABLES `companies` WRITE;
/*!40000 ALTER TABLE `companies` DISABLE KEYS */;
/*!40000 ALTER TABLE `companies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `companies_roles`
--

DROP TABLE IF EXISTS `companies_roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `companies_roles` (
  `movie_id` int(11) NOT NULL,
  `company_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  KEY `companies_roles_fk0` (`movie_id`),
  KEY `companies_roles_fk1` (`company_id`),
  KEY `companies_roles_fk2` (`role_id`),
  CONSTRAINT `companies_roles_fk0` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`),
  CONSTRAINT `companies_roles_fk1` FOREIGN KEY (`company_id`) REFERENCES `companies` (`id`),
  CONSTRAINT `companies_roles_fk2` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `companies_roles`
--

LOCK TABLES `companies_roles` WRITE;
/*!40000 ALTER TABLE `companies_roles` DISABLE KEYS */;
/*!40000 ALTER TABLE `companies_roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movies`
--

DROP TABLE IF EXISTS `movies`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movies` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `imdb_id` varchar(255) NOT NULL,
  `original_title` varchar(255) NOT NULL,
  `budget` int(11) DEFAULT NULL,
  `country` varchar(2) NOT NULL,
  `duration` int(11) NOT NULL,
  `release_date` date NOT NULL,
  `age_rating` varchar(3) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `imdb_id` (`imdb_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies`
--

LOCK TABLES `movies` WRITE;
/*!40000 ALTER TABLE `movies` DISABLE KEYS */;
INSERT INTO `movies` VALUES (1,'tt7286456','Joker',55000000,'US',122,'2019-10-09','-12'),(2,'tt4520988','Frozen II',NULL,'US',103,'2019-11-20','TP');
/*!40000 ALTER TABLE `movies` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movies_people`
--

DROP TABLE IF EXISTS `movies_people`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movies_people` (
  `movie_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  `role_id` int(11) NOT NULL,
  KEY `movies_people_fk0` (`movie_id`),
  KEY `movies_people_fk1` (`person_id`),
  KEY `movies_people_fk2` (`role_id`),
  CONSTRAINT `movies_people_fk0` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`),
  CONSTRAINT `movies_people_fk1` FOREIGN KEY (`person_id`) REFERENCES `people` (`id`),
  CONSTRAINT `movies_people_fk2` FOREIGN KEY (`role_id`) REFERENCES `roles` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies_people`
--

LOCK TABLES `movies_people` WRITE;
/*!40000 ALTER TABLE `movies_people` DISABLE KEYS */;
/*!40000 ALTER TABLE `movies_people` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `movies_tags`
--

DROP TABLE IF EXISTS `movies_tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `movies_tags` (
  `tag_id` int(11) NOT NULL,
  `movie_id` int(11) NOT NULL,
  KEY `movies_tags_fk0` (`tag_id`),
  KEY `movies_tags_fk1` (`movie_id`),
  CONSTRAINT `movies_tags_fk0` FOREIGN KEY (`tag_id`) REFERENCES `tags` (`id`),
  CONSTRAINT `movies_tags_fk1` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `movies_tags`
--

LOCK TABLES `movies_tags` WRITE;
/*!40000 ALTER TABLE `movies_tags` DISABLE KEYS */;
/*!40000 ALTER TABLE `movies_tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `people`
--

DROP TABLE IF EXISTS `people`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `people` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `firstname` varchar(255) NOT NULL,
  `lastname` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `people`
--

LOCK TABLES `people` WRITE;
/*!40000 ALTER TABLE `people` DISABLE KEYS */;
/*!40000 ALTER TABLE `people` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `roles`
--

DROP TABLE IF EXISTS `roles`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `roles` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `roles`
--

LOCK TABLES `roles` WRITE;
/*!40000 ALTER TABLE `roles` DISABLE KEYS */;
/*!40000 ALTER TABLE `roles` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tags`
--

DROP TABLE IF EXISTS `tags`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `tags` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tags`
--

LOCK TABLES `tags` WRITE;
/*!40000 ALTER TABLE `tags` DISABLE KEYS */;
/*!40000 ALTER TABLE `tags` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vote`
--

DROP TABLE IF EXISTS `vote`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vote` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `movie_id` int(11) NOT NULL,
  `rate` float NOT NULL,
  `source` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `vote_fk0` (`movie_id`),
  CONSTRAINT `vote_fk0` FOREIGN KEY (`movie_id`) REFERENCES `movies` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vote`
--

LOCK TABLES `vote` WRITE;
/*!40000 ALTER TABLE `vote` DISABLE KEYS */;
/*!40000 ALTER TABLE `vote` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'themoviepredictor'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-11-28 16:21:57
