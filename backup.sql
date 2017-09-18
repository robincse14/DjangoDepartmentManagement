-- MySQL dump 10.13  Distrib 5.7.15, for Linux (x86_64)
--
-- Host: localhost    Database: DBMS
-- ------------------------------------------------------
-- Server version	5.7.15-0ubuntu0.16.04.1

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
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `admin` (
  `username` int(11) NOT NULL,
  `pass` varchar(20) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (14075046,'Chawla');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alloted`
--

DROP TABLE IF EXISTS `alloted`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alloted` (
  `dept_name` varchar(50) NOT NULL,
  `Hostel_id` int(11) NOT NULL,
  PRIMARY KEY (`dept_name`,`Hostel_id`),
  KEY `Hostel_id` (`Hostel_id`),
  CONSTRAINT `alloted_ibfk_1` FOREIGN KEY (`dept_name`) REFERENCES `department` (`dept_name`),
  CONSTRAINT `alloted_ibfk_2` FOREIGN KEY (`Hostel_id`) REFERENCES `hostel` (`hostel_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alloted`
--

LOCK TABLES `alloted` WRITE;
/*!40000 ALTER TABLE `alloted` DISABLE KEYS */;
INSERT INTO `alloted` VALUES ('dept1',1),('dept1',2),('dept2',2),('dept3',2),('dept3',3),('dept4',3),('dept5',3),('dept5',4);
/*!40000 ALTER TABLE `alloted` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course`
--

DROP TABLE IF EXISTS `course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `course` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `credits` int(11) NOT NULL,
  `Course_name` varchar(50) NOT NULL,
  `dept_name` varchar(50) NOT NULL,
  PRIMARY KEY (`course_id`),
  KEY `dept_name` (`dept_name`),
  CONSTRAINT `course_ibfk_1` FOREIGN KEY (`dept_name`) REFERENCES `department` (`dept_name`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course`
--

LOCK TABLES `course` WRITE;
/*!40000 ALTER TABLE `course` DISABLE KEYS */;
INSERT INTO `course` VALUES (1,10,'Course1','dept1'),(2,8,'Course2','dept1'),(3,8,'Course3','dept2'),(4,8,'Course4','dept3'),(5,8,'Course5','dept5');
/*!40000 ALTER TABLE `course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `department`
--

DROP TABLE IF EXISTS `department`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `department` (
  `dept_name` varchar(50) NOT NULL,
  `NoOfStudents` int(11) DEFAULT NULL,
  `NoOfTeachers` int(11) DEFAULT NULL,
  `Established` date NOT NULL,
  `YearlyFund` int(11) DEFAULT NULL,
  PRIMARY KEY (`dept_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `department`
--

LOCK TABLES `department` WRITE;
/*!40000 ALTER TABLE `department` DISABLE KEYS */;
INSERT INTO `department` VALUES ('dept1',3,2,'1996-02-16',10000),('dept2',NULL,1,'1996-05-18',100000),('dept3',2,NULL,'1996-09-21',200000),('dept4',NULL,NULL,'1993-01-29',300000),('dept5',2,0,'1993-01-29',120000);
/*!40000 ALTER TABLE `department` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dept_facility`
--

DROP TABLE IF EXISTS `dept_facility`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dept_facility` (
  `dept_name` varchar(50) NOT NULL DEFAULT '',
  `facility_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`dept_name`,`facility_id`),
  KEY `facility_id` (`facility_id`),
  CONSTRAINT `dept_facility_ibfk_1` FOREIGN KEY (`dept_name`) REFERENCES `department` (`dept_name`),
  CONSTRAINT `dept_facility_ibfk_2` FOREIGN KEY (`facility_id`) REFERENCES `facility` (`facility_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dept_facility`
--

LOCK TABLES `dept_facility` WRITE;
/*!40000 ALTER TABLE `dept_facility` DISABLE KEYS */;
INSERT INTO `dept_facility` VALUES ('dept1',1),('dept3',1),('dept1',2),('dept1',3),('dept1',4),('dept3',5),('dept3',6),('dept3',7),('dept4',8);
/*!40000 ALTER TABLE `dept_facility` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `facility`
--

DROP TABLE IF EXISTS `facility`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `facility` (
  `facility_id` int(11) NOT NULL AUTO_INCREMENT,
  `Facility_name` varchar(50) NOT NULL,
  `Budget` int(11) DEFAULT NULL,
  PRIMARY KEY (`facility_id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `facility`
--

LOCK TABLES `facility` WRITE;
/*!40000 ALTER TABLE `facility` DISABLE KEYS */;
INSERT INTO `facility` VALUES (1,'facility1',10000),(2,'facility2',NULL),(3,'facility3',2000),(4,'facility4',20000),(5,'facility5',30000),(6,'facility6',30004),(7,'facility7',NULL),(8,'facility8',NULL);
/*!40000 ALTER TABLE `facility` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `hostel`
--

DROP TABLE IF EXISTS `hostel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `hostel` (
  `hostel_id` int(11) NOT NULL AUTO_INCREMENT,
  `No_of_rooms` int(11) DEFAULT NULL,
  `hostel_name` varchar(50) NOT NULL,
  PRIMARY KEY (`hostel_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `hostel`
--

LOCK TABLES `hostel` WRITE;
/*!40000 ALTER TABLE `hostel` DISABLE KEYS */;
INSERT INTO `hostel` VALUES (1,10,'hostel1'),(2,3,'hostel2'),(3,NULL,'hostel3'),(4,0,'hostel4');
/*!40000 ALTER TABLE `hostel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `inst_sec`
--

DROP TABLE IF EXISTS `inst_sec`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `inst_sec` (
  `sec_id` int(11) NOT NULL DEFAULT '0',
  `semester` int(11) NOT NULL DEFAULT '0',
  `year` int(11) NOT NULL DEFAULT '0',
  `course_id` int(11) NOT NULL DEFAULT '0',
  `id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`sec_id`,`semester`,`year`,`course_id`,`id`),
  KEY `id` (`id`),
  CONSTRAINT `inst_sec_ibfk_1` FOREIGN KEY (`sec_id`, `semester`, `year`, `course_id`) REFERENCES `section` (`sec_id`, `semester`, `year`, `course_id`),
  CONSTRAINT `inst_sec_ibfk_2` FOREIGN KEY (`id`) REFERENCES `instructor` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inst_sec`
--

LOCK TABLES `inst_sec` WRITE;
/*!40000 ALTER TABLE `inst_sec` DISABLE KEYS */;
INSERT INTO `inst_sec` VALUES (1,1,2016,1,1),(1,1,2016,2,1),(1,2,2016,1,2),(1,2,2016,1,3),(3,1,2014,1,3),(3,1,2014,1,4);
/*!40000 ALTER TABLE `inst_sec` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `instructor`
--

DROP TABLE IF EXISTS `instructor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `instructor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_name` varchar(50) NOT NULL,
  `salary` int(11) DEFAULT NULL,
  `dept_name` varchar(50) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `dept_name` (`dept_name`),
  CONSTRAINT `instructor_ibfk_1` FOREIGN KEY (`dept_name`) REFERENCES `department` (`dept_name`)
) ENGINE=InnoDB AUTO_INCREMENT=113 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `instructor`
--

LOCK TABLES `instructor` WRITE;
/*!40000 ALTER TABLE `instructor` DISABLE KEYS */;
INSERT INTO `instructor` VALUES (1,'ins1',10000,'dept1','Default'),(2,'ins2',NULL,'dept1','Default'),(3,'ins3',NULL,'dept3','Default'),(4,'ins4',200000,'dept2','Default'),(5,'ins5',200010,'dept4','Default'),(6,'ins6',200010,'dept4','Default'),(111,'Robin Chawl',100000,'dept1','Default'),(112,'New Member',100000,'dept2','abcdefghij');
/*!40000 ALTER TABLE `instructor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `section`
--

DROP TABLE IF EXISTS `section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `section` (
  `sec_id` int(11) NOT NULL DEFAULT '0',
  `semester` int(11) NOT NULL DEFAULT '0',
  `year` int(11) NOT NULL DEFAULT '0',
  `course_id` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`sec_id`,`semester`,`year`,`course_id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `section_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `course` (`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `section`
--

LOCK TABLES `section` WRITE;
/*!40000 ALTER TABLE `section` DISABLE KEYS */;
INSERT INTO `section` VALUES (1,1,2016,1),(1,2,2016,1),(3,1,2014,1),(1,1,2016,2),(3,2,2014,2),(2,3,2014,3),(2,2,2015,4);
/*!40000 ALTER TABLE `section` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stud_facility`
--

DROP TABLE IF EXISTS `stud_facility`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stud_facility` (
  `facility_id` int(11) NOT NULL,
  `Roll_no` int(11) NOT NULL,
  PRIMARY KEY (`facility_id`,`Roll_no`),
  KEY `Roll_no` (`Roll_no`),
  CONSTRAINT `stud_facility_ibfk_1` FOREIGN KEY (`Roll_no`) REFERENCES `student` (`Roll_no`),
  CONSTRAINT `stud_facility_ibfk_2` FOREIGN KEY (`facility_id`) REFERENCES `facility` (`facility_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stud_facility`
--

LOCK TABLES `stud_facility` WRITE;
/*!40000 ALTER TABLE `stud_facility` DISABLE KEYS */;
INSERT INTO `stud_facility` VALUES (1,11),(2,11),(3,11),(4,11),(1,12),(2,12),(3,12),(4,12),(1,13),(2,13),(3,13),(4,13),(1,31),(5,31),(6,31),(7,31),(1,32),(5,32),(6,32),(7,32),(8,41),(8,42),(8,43);
/*!40000 ALTER TABLE `stud_facility` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stud_sec`
--

DROP TABLE IF EXISTS `stud_sec`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stud_sec` (
  `roll_no` int(11) NOT NULL DEFAULT '0',
  `sec_id` int(11) NOT NULL DEFAULT '0',
  `semester` int(11) NOT NULL DEFAULT '0',
  `year` int(11) NOT NULL DEFAULT '0',
  `course_id` int(11) NOT NULL DEFAULT '0',
  `grade` int(11) DEFAULT NULL,
  `attendance` int(11) DEFAULT NULL,
  PRIMARY KEY (`roll_no`,`sec_id`,`semester`,`year`,`course_id`),
  KEY `sec_id` (`sec_id`,`semester`,`year`,`course_id`),
  CONSTRAINT `stud_sec_ibfk_1` FOREIGN KEY (`sec_id`, `semester`, `year`, `course_id`) REFERENCES `section` (`sec_id`, `semester`, `year`, `course_id`),
  CONSTRAINT `stud_sec_ibfk_2` FOREIGN KEY (`roll_no`) REFERENCES `student` (`Roll_no`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stud_sec`
--

LOCK TABLES `stud_sec` WRITE;
/*!40000 ALTER TABLE `stud_sec` DISABLE KEYS */;
INSERT INTO `stud_sec` VALUES (11,1,1,2016,1,7,NULL),(11,1,1,2016,2,8,NULL),(12,1,1,2016,2,8,NULL),(12,1,2,2016,1,8,NULL),(12,3,1,2014,1,8,80),(13,3,1,2014,1,8,90),(21,3,2,2014,2,8,78);
/*!40000 ALTER TABLE `stud_sec` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `stud_signing`
--

DROP TABLE IF EXISTS `stud_signing`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `stud_signing` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `stud_signing`
--

LOCK TABLES `stud_signing` WRITE;
/*!40000 ALTER TABLE `stud_signing` DISABLE KEYS */;
/*!40000 ALTER TABLE `stud_signing` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `student` (
  `Roll_no` int(11) NOT NULL,
  `stud_name` varchar(50) NOT NULL,
  `Contact_no` char(10) NOT NULL,
  `dept_name` varchar(50) NOT NULL,
  `hostel_id` int(11) NOT NULL,
  `Room_no` int(11) NOT NULL,
  `dateofbirth` date NOT NULL,
  `gender` char(1) NOT NULL,
  `email` varchar(50) NOT NULL,
  `pass` varchar(20) NOT NULL,
  PRIMARY KEY (`Roll_no`),
  UNIQUE KEY `email` (`email`),
  KEY `hostel_id` (`hostel_id`),
  KEY `dept_name` (`dept_name`),
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`hostel_id`) REFERENCES `hostel` (`hostel_id`),
  CONSTRAINT `student_ibfk_2` FOREIGN KEY (`dept_name`) REFERENCES `department` (`dept_name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES (11,'stud1','9876510329','dept1',1,123,'1996-06-16','F','stud1@gmail.com','Default'),(12,'stud2','9876510320','dept1',1,124,'1996-06-16','F','stud2@gmail.com','Default'),(13,'stud3','9876510321','dept1',2,111,'1996-06-16','F','stud3@gmail.com','Default'),(21,'stud4','9876510322','dept2',2,112,'1996-06-16','F','stud4@gmail.com','Default'),(31,'stud5','9876510323','dept3',2,113,'1996-06-16','F','stud5@gmail.com','Default'),(32,'stud6','9876510324','dept3',3,119,'1996-06-16','F','stud6@gmail.com','Default'),(41,'stud7','9876510325','dept4',3,120,'1996-06-16','F','stud7@gmail.com','Default'),(42,'stud8','9876510329','dept4',3,121,'1996-06-16','F','stud8@gmail.com','Default'),(43,'stud9','9876510310','dept4',3,122,'1996-06-16','F','stud9@gmail.com','Default'),(51,'stud10','9876510311','dept5',3,123,'1996-06-16','F','stud10@gmail.com','Default'),(52,'stud11','9876510312','dept5',3,128,'1996-06-16','F','stud11@gmail.com','Default'),(61,'Robin chhhh1','9855221223','dept2',1,111,'1996-06-06','M','robin.chawla.cse14@itbhu.ac.in','abcdefgh');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-10-22 17:12:18
