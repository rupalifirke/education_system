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
-- Table structure for table `exam`
--

DROP TABLE IF EXISTS `exam`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `exam` (
  `ExamId` int NOT NULL AUTO_INCREMENT,
  `CourseId` int DEFAULT NULL,
  `Instructions` varchar(45) DEFAULT NULL,
  `MaxMarks` int DEFAULT NULL,
  `due_date` datetime DEFAULT NULL,
  PRIMARY KEY (`ExamId`)
) ENGINE=InnoDB AUTO_INCREMENT=25 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exam`
--

LOCK TABLES `exam` WRITE;
/*!40000 ALTER TABLE `exam` DISABLE KEYS */;
INSERT INTO `exam` VALUES (1,12,'5 subjective questions 20 marks each',100,NULL),(2,12,'Stack and Queues',100,NULL),(3,12,'Trees and Graphs',100,NULL),(4,12,'Dynamic programming',100,NULL),(5,21,'Algebra',100,NULL),(6,21,'Derivations',100,NULL),(7,21,'time limit: 45 mins',100,NULL),(8,22,'time limit: 1 hour',100,NULL),(9,23,'time limit: 1 hour',100,NULL),(10,23,'4 questions, 25 marks each',100,NULL),(11,24,'4 questions, 25 marks each',100,NULL),(12,24,'5 questions, 20 marks each',100,NULL),(13,30,'5 questions, 20 marks each',100,NULL),(14,30,'4 questions, 25 marks each',100,NULL),(15,30,'4 questions, 25 marks each',100,NULL),(16,31,'4 questions, 25 marks each',100,NULL),(17,31,'4 questions, 25 marks each',100,NULL),(18,31,'5 questions, 20 marks each',100,NULL),(19,32,'5 questions, 20 marks each',100,NULL),(20,32,'4 questions, 25 marks each',100,NULL),(21,40,'Make a 1 page website in 1 hour',100,NULL),(22,40,'Explains use of HTML and CSS',100,NULL),(23,50,'Make mockups in PS',100,NULL),(24,50,'Draw this desgin in Illustrator',100,NULL);
/*!40000 ALTER TABLE `exam` ENABLE KEYS */;
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
