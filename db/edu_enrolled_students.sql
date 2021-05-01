-- MySQL dump 10.13  Distrib 8.0.20, for Win64 (x86_64)
--
-- Host: localhost    Database: edu
-- ------------------------------------------------------
-- Server version	8.0.20

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `enrolled_students`
--

DROP TABLE IF EXISTS `enrolled_students`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `enrolled_students` (
  `StudentId` int NOT NULL,
  `CourseId` varchar(45) NOT NULL,
  `FinalGrade` varchar(45) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `enrolled_students`
--

LOCK TABLES `enrolled_students` WRITE;
/*!40000 ALTER TABLE `enrolled_students` DISABLE KEYS */;
INSERT INTO `enrolled_students` VALUES (1,'12','A'),(2,'12','A'),(3,'12','A'),(4,'12','A'),(5,'12','A'),(6,'12','A'),(7,'12','A'),(8,'12','A'),(9,'12','A'),(10,'12','A'),(11,'12','A'),(1,'21','B'),(2,'21','B'),(3,'21','B'),(4,'21','B'),(5,'21','A'),(6,'21','A'),(7,'21','A'),(8,'21','A'),(9,'21','A'),(10,'21','A'),(11,'21','B'),(1,'22','B'),(2,'22','B'),(3,'22','B'),(4,'22','B'),(5,'22','B'),(6,'22','B'),(7,'22','B'),(8,'22','B'),(9,'22','B'),(10,'22','B'),(11,'22','C'),(1,'23','C'),(2,'23','C'),(3,'23','C'),(4,'23','C'),(4,'23','B'),(5,'23','B'),(6,'23','B'),(7,'23','B'),(8,'23','B'),(9,'23','B'),(10,'23','B'),(11,'23','B'),(1,'24','A'),(2,'24','A'),(3,'24','A'),(4,'24','A'),(5,'24','A'),(6,'24','C'),(7,'24','C'),(8,'24','A'),(9,'24','A'),(10,'24','A'),(11,'24','A'),(1,'30','C'),(2,'30','B'),(3,'30','B'),(4,'30','B'),(5,'30','B'),(6,'30','B'),(7,'30','B'),(7,'30','A'),(8,'30','A'),(9,'30','A'),(10,'30','A'),(11,'30','A'),(1,'31','A'),(2,'31','A'),(3,'31','A'),(4,'31','A'),(5,'31','A'),(6,'31','A'),(7,'31','A'),(8,'31','A'),(9,'31','A'),(10,'31','C'),(10,'31','C'),(11,'31','C'),(1,'32','C'),(2,'32','A'),(3,'32','A'),(4,'32','A'),(5,'32','A'),(6,'32','A'),(7,'32','A'),(8,'32','A'),(9,'32','A'),(10,'32','A'),(11,'32','B'),(1,'32','B'),(1,'40','B'),(2,'40','A'),(3,'40','A'),(4,'40','A'),(5,'40','A'),(6,'40','A'),(7,'40','A'),(8,'40','A'),(9,'40','A'),(10,'40','A'),(11,'40','A'),(11,'50','A'),(1,'50','A'),(2,'50','A'),(3,'50','A'),(4,'50','A'),(5,'50','A'),(6,'50','A'),(7,'50','A'),(8,'50','A'),(9,'50','A'),(10,'50','A');
/*!40000 ALTER TABLE `enrolled_students` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-04-28  9:45:30
