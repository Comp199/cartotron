-- MySQL dump 10.13  Distrib 5.7.12, for Win64 (x86_64)
--
-- Host: localhost    Database: cartotron
-- ------------------------------------------------------
-- Server version	5.7.12-log

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
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add category',7,'add_category'),(20,'Can change category',7,'change_category'),(21,'Can delete category',7,'delete_category'),(22,'Can add product',8,'add_product'),(23,'Can change product',8,'change_product'),(24,'Can delete product',8,'delete_product');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$24000$HQhEevgE7BJP$vgCQCBpgNldH5wVR5EJWM9b8w0ekgyGdcQ7sUTGzFpA=','2016-04-17 23:25:40.219000',1,'andrea','','','a@b.com',1,1,'2016-04-17 23:25:13.224000');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2016-04-17 23:25:51.172000','1','Clothing!',1,'Added.',7,1),(2,'2016-04-17 23:25:54.996000','2','Toys!',1,'Added.',7,1),(3,'2016-04-17 23:49:36.779000','4','Cleaning Supplies',1,'Added.',7,1),(4,'2016-04-17 23:49:50.957000','5','Kitchen',1,'Added.',7,1),(5,'2016-04-17 23:50:27.627000','1','Dawn',1,'Added.',8,1),(6,'2016-04-17 23:53:37.695000','2','Pepe',1,'Added.',8,1),(7,'2016-04-17 23:54:15.882000','3','Spoon',1,'Added.',8,1),(8,'2016-04-17 23:54:40.898000','4','Pen',1,'Added.',8,1),(9,'2016-04-17 23:55:04.990000','5','Fork',1,'Added.',8,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(6,'sessions','session'),(7,'shop','category'),(8,'shop','product');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-04-17 23:24:56.763000'),(2,'auth','0001_initial','2016-04-17 23:24:57.946000'),(3,'admin','0001_initial','2016-04-17 23:24:58.226000'),(4,'admin','0002_logentry_remove_auto_add','2016-04-17 23:24:58.268000'),(5,'contenttypes','0002_remove_content_type_name','2016-04-17 23:24:58.993000'),(6,'auth','0002_alter_permission_name_max_length','2016-04-17 23:24:59.109000'),(7,'auth','0003_alter_user_email_max_length','2016-04-17 23:24:59.218000'),(8,'auth','0004_alter_user_username_opts','2016-04-17 23:24:59.243000'),(9,'auth','0005_alter_user_last_login_null','2016-04-17 23:24:59.390000'),(10,'auth','0006_require_contenttypes_0002','2016-04-17 23:24:59.400000'),(11,'auth','0007_alter_validators_add_error_messages','2016-04-17 23:24:59.419000'),(12,'sessions','0001_initial','2016-04-17 23:24:59.540000'),(13,'shop','0001_initial','2016-04-17 23:24:59.616000'),(14,'shop','0002_product','2016-04-17 23:48:27.810000');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('si5cngq888hdq9a8y8ax0hjc5mln4vk2','YmUyNjBhYWNjMDg1ZGRkM2IyYjI2YWFmNTE1NzlhMGMzMWZjN2I4Njp7Il9hdXRoX3VzZXJfaGFzaCI6IjQ3OGI4OGIzNDI5MzZjMTI0NWJmNjk4NmQxNzRiZDg3YzUzMTU5NjIiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2016-05-01 23:25:40.230000');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `shop_category`
--

LOCK TABLES `shop_category` WRITE;
/*!40000 ALTER TABLE `shop_category` DISABLE KEYS */;
INSERT INTO `shop_category` VALUES (1,'Clothing'),(2,'Toys'),(3,'Houseware'),(4,'Cleaning Supplies'),(5,'Kitchen');
/*!40000 ALTER TABLE `shop_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `shop_product`
--

LOCK TABLES `shop_product` WRITE;
/*!40000 ALTER TABLE `shop_product` DISABLE KEYS */;
INSERT INTO `shop_product` VALUES (1,'Dawn',6.99,20,'Some fantastic Soap!','ABC1231231'),(2,'Pepe',30.00,4,'Pepe! The coolest bird around.','as23465442'),(3,'Spoon',1.00,100,'A spoon','qwe2398rhd'),(4,'Pen',3.00,25,'gajln','ghoho38398'),(5,'Fork',1.00,20,'hgdoa','uhg38huafh');
/*!40000 ALTER TABLE `shop_product` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `shop_product_categories`
--

LOCK TABLES `shop_product_categories` WRITE;
/*!40000 ALTER TABLE `shop_product_categories` DISABLE KEYS */;
INSERT INTO `shop_product_categories` VALUES (1,1,3),(2,1,4),(3,1,5),(4,2,2),(5,3,3),(6,3,5),(7,4,3),(8,5,3),(9,5,5);
/*!40000 ALTER TABLE `shop_product_categories` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-04-17 19:17:40
