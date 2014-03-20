-- MySQL dump 10.14  Distrib 5.5.34-MariaDB, for Linux (x86_64)
--
-- Host: localhost    Database: ghl
-- ------------------------------------------------------
-- Server version	5.5.34-MariaDB

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
-- Table structure for table `arkestra_image_plugin_embeddedvideosetitem`
--

DROP TABLE IF EXISTS `arkestra_image_plugin_embeddedvideosetitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `arkestra_image_plugin_embeddedvideosetitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `plugin_id` int(11) NOT NULL,
  `service` varchar(50) NOT NULL,
  `video_code` varchar(255) NOT NULL,
  `video_title` varchar(250) NOT NULL,
  `video_autoplay` tinyint(1) NOT NULL,
  `aspect_ratio` double NOT NULL,
  `inline_item_ordering` smallint(5) unsigned NOT NULL,
  `active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `arkestra_image_plugin_embeddedvideosetitem_2857ccbf` (`plugin_id`),
  CONSTRAINT `plugin_id_refs_cmsplugin_ptr_id_50f850e` FOREIGN KEY (`plugin_id`) REFERENCES `cmsplugin_embeddedvideosetplugin` (`cmsplugin_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arkestra_image_plugin_embeddedvideosetitem`
--

LOCK TABLES `arkestra_image_plugin_embeddedvideosetitem` WRITE;
/*!40000 ALTER TABLE `arkestra_image_plugin_embeddedvideosetitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `arkestra_image_plugin_embeddedvideosetitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `arkestra_image_plugin_imagesetitem`
--

DROP TABLE IF EXISTS `arkestra_image_plugin_imagesetitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `arkestra_image_plugin_imagesetitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `plugin_id` int(11) NOT NULL,
  `image_id` int(11) NOT NULL,
  `alt_text` varchar(255) DEFAULT NULL,
  `auto_image_title` tinyint(1) NOT NULL,
  `manual_image_title` longtext,
  `auto_image_caption` tinyint(1) NOT NULL,
  `manual_image_caption` longtext,
  `auto_link_title` tinyint(1) NOT NULL,
  `manual_link_title` longtext,
  `auto_link_description` tinyint(1) NOT NULL,
  `manual_link_description` longtext,
  `destination_content_type_id` int(11) DEFAULT NULL,
  `destination_object_id` int(10) unsigned DEFAULT NULL,
  `inline_item_ordering` smallint(5) unsigned NOT NULL,
  `active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `arkestra_image_plugin_imagesetitem_2857ccbf` (`plugin_id`),
  KEY `arkestra_image_plugin_imagesetitem_6682136` (`image_id`),
  KEY `arkestra_image_plugin_imagesetitem_a1ae9087` (`destination_content_type_id`),
  CONSTRAINT `destination_content_type_id_refs_id_c41d1a4e` FOREIGN KEY (`destination_content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `image_id_refs_file_ptr_id_60886b3a` FOREIGN KEY (`image_id`) REFERENCES `filer_image` (`file_ptr_id`),
  CONSTRAINT `plugin_id_refs_cmsplugin_ptr_id_508c3b92` FOREIGN KEY (`plugin_id`) REFERENCES `cmsplugin_imagesetplugin` (`cmsplugin_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arkestra_image_plugin_imagesetitem`
--

LOCK TABLES `arkestra_image_plugin_imagesetitem` WRITE;
/*!40000 ALTER TABLE `arkestra_image_plugin_imagesetitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `arkestra_image_plugin_imagesetitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `arkestra_utilities_insert`
--

DROP TABLE IF EXISTS `arkestra_utilities_insert`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `arkestra_utilities_insert` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `insertion_point` varchar(60) NOT NULL,
  `content_id` int(11) DEFAULT NULL,
  `description` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `insertion_point` (`insertion_point`),
  KEY `arkestra_utilities_insert_cc8ff3c` (`content_id`),
  CONSTRAINT `content_id_refs_id_6a59c4b2` FOREIGN KEY (`content_id`) REFERENCES `cms_placeholder` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `arkestra_utilities_insert`
--

LOCK TABLES `arkestra_utilities_insert` WRITE;
/*!40000 ALTER TABLE `arkestra_utilities_insert` DISABLE KEYS */;
INSERT INTO `arkestra_utilities_insert` VALUES (1,'footer',4,NULL),(2,'newsflash',11,NULL);
/*!40000 ALTER TABLE `arkestra_utilities_insert` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_bda51c3c` (`group_id`),
  KEY `auth_group_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `group_id_refs_id_3cea63fe` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `permission_id_refs_id_a7792de1` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_e4470c6e` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_728de91f` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=270 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add carousel',1,'add_carousel'),(2,'Can change carousel',1,'change_carousel'),(3,'Can delete carousel',1,'delete_carousel'),(4,'Can add carousel item',2,'add_carouselitem'),(5,'Can change carousel item',2,'change_carouselitem'),(6,'Can delete carousel item',2,'delete_carouselitem'),(7,'Can add migration history',3,'add_migrationhistory'),(8,'Can change migration history',3,'change_migrationhistory'),(9,'Can delete migration history',3,'delete_migrationhistory'),(10,'Can add permission',4,'add_permission'),(11,'Can change permission',4,'change_permission'),(12,'Can delete permission',4,'delete_permission'),(13,'Can add group',5,'add_group'),(14,'Can change group',5,'change_group'),(15,'Can delete group',5,'delete_group'),(16,'Can add user',6,'add_user'),(17,'Can change user',6,'change_user'),(18,'Can delete user',6,'delete_user'),(19,'Can add content type',7,'add_contenttype'),(20,'Can change content type',7,'change_contenttype'),(21,'Can delete content type',7,'delete_contenttype'),(22,'Can add session',8,'add_session'),(23,'Can change session',8,'change_session'),(24,'Can delete session',8,'delete_session'),(25,'Can add site',9,'add_site'),(26,'Can change site',9,'change_site'),(27,'Can delete site',9,'delete_site'),(28,'Can add log entry',10,'add_logentry'),(29,'Can change log entry',10,'change_logentry'),(30,'Can delete log entry',10,'delete_logentry'),(31,'Can add arkestra user',6,'add_arkestrauser'),(32,'Can change arkestra user',6,'change_arkestrauser'),(33,'Can delete arkestra user',6,'delete_arkestrauser'),(34,'Can add insert',11,'add_insert'),(35,'Can change insert',11,'change_insert'),(36,'Can delete insert',11,'delete_insert'),(37,'Can add placeholder',13,'add_placeholder'),(38,'Can change placeholder',13,'change_placeholder'),(39,'Can delete placeholder',13,'delete_placeholder'),(40,'Can add cms plugin',14,'add_cmsplugin'),(41,'Can change cms plugin',14,'change_cmsplugin'),(42,'Can delete cms plugin',14,'delete_cmsplugin'),(43,'Can add page',15,'add_page'),(44,'Can change page',15,'change_page'),(45,'Can delete page',15,'delete_page'),(46,'Can view page',15,'view_page'),(47,'Can add PageModerator',16,'add_pagemoderator'),(48,'Can change PageModerator',16,'change_pagemoderator'),(49,'Can delete PageModerator',16,'delete_pagemoderator'),(50,'Can add Page moderator state',17,'add_pagemoderatorstate'),(51,'Can change Page moderator state',17,'change_pagemoderatorstate'),(52,'Can delete Page moderator state',17,'delete_pagemoderatorstate'),(53,'Can add Page global permission',18,'add_globalpagepermission'),(54,'Can change Page global permission',18,'change_globalpagepermission'),(55,'Can delete Page global permission',18,'delete_globalpagepermission'),(56,'Can add Page permission',19,'add_pagepermission'),(57,'Can change Page permission',19,'change_pagepermission'),(58,'Can delete Page permission',19,'delete_pagepermission'),(59,'Can add User (page)',20,'add_pageuser'),(60,'Can change User (page)',20,'change_pageuser'),(61,'Can delete User (page)',20,'delete_pageuser'),(62,'Can add User group (page)',21,'add_pageusergroup'),(63,'Can change User group (page)',21,'change_pageusergroup'),(64,'Can delete User group (page)',21,'delete_pageusergroup'),(65,'Can add title',22,'add_title'),(66,'Can change title',22,'change_title'),(67,'Can delete title',22,'delete_title'),(68,'Can add text',23,'add_text'),(69,'Can change text',23,'change_text'),(70,'Can delete text',23,'delete_text'),(71,'Can add Snippet',24,'add_snippet'),(72,'Can change Snippet',24,'change_snippet'),(73,'Can delete Snippet',24,'delete_snippet'),(74,'Can add Snippet',25,'add_snippetptr'),(75,'Can change Snippet',25,'change_snippetptr'),(76,'Can delete Snippet',25,'delete_snippetptr'),(77,'Can add cache key',26,'add_cachekey'),(78,'Can change cache key',26,'change_cachekey'),(79,'Can delete cache key',26,'delete_cachekey'),(80,'Can add Сайт',27,'add_site'),(81,'Can change Сайт',27,'change_site'),(82,'Can delete Сайт',27,'delete_site'),(83,'Can add building',28,'add_building'),(84,'Can change building',28,'change_building'),(85,'Can delete building',28,'delete_building'),(86,'Can add phone contact',29,'add_phonecontact'),(87,'Can change phone contact',29,'change_phonecontact'),(88,'Can delete phone contact',29,'delete_phonecontact'),(89,'Can add entity lite',30,'add_entitylite'),(90,'Can change entity lite',30,'change_entitylite'),(91,'Can delete entity lite',30,'delete_entitylite'),(92,'Can add entity',31,'add_entity'),(93,'Can change entity',31,'change_entity'),(94,'Can delete entity',31,'delete_entity'),(95,'Can add title',32,'add_title'),(96,'Can change title',32,'change_title'),(97,'Can delete title',32,'delete_title'),(98,'Can add person lite',33,'add_personlite'),(99,'Can change person lite',33,'change_personlite'),(100,'Can delete person lite',33,'delete_personlite'),(101,'Can add person',34,'add_person'),(102,'Can change person',34,'change_person'),(103,'Can delete person',34,'delete_person'),(104,'Can add membership',35,'add_membership'),(105,'Can change membership',35,'change_membership'),(106,'Can delete membership',35,'delete_membership'),(107,'Can add entity auto page link plugin editor',36,'add_entityautopagelinkplugineditor'),(108,'Can change entity auto page link plugin editor',36,'change_entityautopagelinkplugineditor'),(109,'Can delete entity auto page link plugin editor',36,'delete_entityautopagelinkplugineditor'),(110,'Can add entity directory plugin editor',37,'add_entitydirectoryplugineditor'),(111,'Can change entity directory plugin editor',37,'change_entitydirectoryplugineditor'),(112,'Can delete entity directory plugin editor',37,'delete_entitydirectoryplugineditor'),(113,'Can add entity members plugin editor',38,'add_entitymembersplugineditor'),(114,'Can change entity members plugin editor',38,'change_entitymembersplugineditor'),(115,'Can delete entity members plugin editor',38,'delete_entitymembersplugineditor'),(116,'Can add vacancy',39,'add_vacancy'),(117,'Can change vacancy',39,'change_vacancy'),(118,'Can delete vacancy',39,'delete_vacancy'),(119,'Can add studentship',40,'add_studentship'),(120,'Can change studentship',40,'change_studentship'),(121,'Can delete studentship',40,'delete_studentship'),(122,'Can add vacancies plugin',41,'add_vacanciesplugin'),(123,'Can change vacancies plugin',41,'change_vacanciesplugin'),(124,'Can delete vacancies plugin',41,'delete_vacanciesplugin'),(125,'Can add news article',42,'add_newsarticle'),(126,'Can change news article',42,'change_newsarticle'),(127,'Can delete news article',42,'delete_newsarticle'),(128,'Can add event',43,'add_event'),(129,'Can change event',43,'change_event'),(130,'Can delete event',43,'delete_event'),(131,'Can add event type',44,'add_eventtype'),(132,'Can change event type',44,'change_eventtype'),(133,'Can delete event type',44,'delete_eventtype'),(134,'Can add news source',45,'add_newssource'),(135,'Can change news source',45,'change_newssource'),(136,'Can delete news source',45,'delete_newssource'),(137,'Can add news and events plugin',46,'add_newsandeventsplugin'),(138,'Can change news and events plugin',46,'change_newsandeventsplugin'),(139,'Can delete news and events plugin',46,'delete_newsandeventsplugin'),(140,'Can add Link',47,'add_objectlink'),(141,'Can change Link',47,'change_objectlink'),(142,'Can delete Link',47,'delete_objectlink'),(143,'Can add generic link list plugin item',48,'add_genericlinklistpluginitem'),(144,'Can change generic link list plugin item',48,'change_genericlinklistpluginitem'),(145,'Can delete generic link list plugin item',48,'delete_genericlinklistpluginitem'),(146,'Can add external link',49,'add_externallink'),(147,'Can change external link',49,'change_externallink'),(148,'Can delete external link',49,'delete_externallink'),(149,'Can add link type',50,'add_linktype'),(150,'Can change link type',50,'change_linktype'),(151,'Can delete link type',50,'delete_linktype'),(152,'Can add domain',51,'add_externalsite'),(153,'Can change domain',51,'change_externalsite'),(154,'Can delete domain',51,'delete_externalsite'),(155,'Can add generic link list plugin',52,'add_genericlinklistplugin'),(156,'Can change generic link list plugin',52,'change_genericlinklistplugin'),(157,'Can delete generic link list plugin',52,'delete_genericlinklistplugin'),(158,'Can add carousel plugin',53,'add_carouselplugin'),(159,'Can change carousel plugin',53,'change_carouselplugin'),(160,'Can delete carousel plugin',53,'delete_carouselplugin'),(161,'Can add carousel plugin item',54,'add_carouselpluginitem'),(162,'Can change carousel plugin item',54,'change_carouselpluginitem'),(163,'Can delete carousel plugin item',54,'delete_carouselpluginitem'),(164,'Can add focus on plugin editor',55,'add_focusonplugineditor'),(165,'Can change focus on plugin editor',55,'change_focusonplugineditor'),(166,'Can delete focus on plugin editor',55,'delete_focusonplugineditor'),(167,'Can add focus on plugin item editor',56,'add_focusonpluginitemeditor'),(168,'Can change focus on plugin item editor',56,'change_focusonpluginitemeditor'),(169,'Can delete focus on plugin item editor',56,'delete_focusonpluginitemeditor'),(170,'Can add image set plugin',57,'add_imagesetplugin'),(171,'Can change image set plugin',57,'change_imagesetplugin'),(172,'Can delete image set plugin',57,'delete_imagesetplugin'),(173,'Can add image set item',58,'add_imagesetitem'),(174,'Can change image set item',58,'change_imagesetitem'),(175,'Can delete image set item',58,'delete_imagesetitem'),(176,'Can add embedded video set plugin',59,'add_embeddedvideosetplugin'),(177,'Can change embedded video set plugin',59,'change_embeddedvideosetplugin'),(178,'Can delete embedded video set plugin',59,'delete_embeddedvideosetplugin'),(179,'Can add embedded video set item',60,'add_embeddedvideosetitem'),(180,'Can change embedded video set item',60,'change_embeddedvideosetitem'),(181,'Can delete embedded video set item',60,'delete_embeddedvideosetitem'),(182,'Can add video',61,'add_video'),(183,'Can change video',61,'change_video'),(184,'Can delete video',61,'delete_video'),(185,'Can add Video',61,'add_arkestravideo'),(186,'Can change Video',61,'change_arkestravideo'),(187,'Can delete Video',61,'delete_arkestravideo'),(188,'Can add video plugin editor',62,'add_videoplugineditor'),(189,'Can change video plugin editor',62,'change_videoplugineditor'),(190,'Can delete video plugin editor',62,'delete_videoplugineditor'),(191,'Can add video version',63,'add_videoversion'),(192,'Can change video version',63,'change_videoversion'),(193,'Can delete video version',63,'delete_videoversion'),(194,'Can add CSS class category',65,'add_cssclasscategory'),(195,'Can change CSS class category',65,'change_cssclasscategory'),(196,'Can delete CSS class category',65,'delete_cssclasscategory'),(197,'Can add CSS class',66,'add_cssclass'),(198,'Can change CSS class',66,'change_cssclass'),(199,'Can delete CSS class',66,'delete_cssclass'),(200,'Can add source',67,'add_source'),(201,'Can change source',67,'change_source'),(202,'Can delete source',67,'delete_source'),(203,'Can add thumbnail',68,'add_thumbnail'),(204,'Can change thumbnail',68,'change_thumbnail'),(205,'Can delete thumbnail',68,'delete_thumbnail'),(206,'Can add Folder',69,'add_folder'),(207,'Can change Folder',69,'change_folder'),(208,'Can delete Folder',69,'delete_folder'),(209,'Can use directory listing',69,'can_use_directory_listing'),(210,'Can add folder permission',70,'add_folderpermission'),(211,'Can change folder permission',70,'change_folderpermission'),(212,'Can delete folder permission',70,'delete_folderpermission'),(213,'Can add file',71,'add_file'),(214,'Can change file',71,'change_file'),(215,'Can delete file',71,'delete_file'),(216,'Can add clipboard',72,'add_clipboard'),(217,'Can change clipboard',72,'change_clipboard'),(218,'Can delete clipboard',72,'delete_clipboard'),(219,'Can add clipboard item',73,'add_clipboarditem'),(220,'Can change clipboard item',73,'change_clipboarditem'),(221,'Can delete clipboard item',73,'delete_clipboarditem'),(222,'Can add image',74,'add_image'),(223,'Can change image',74,'change_image'),(224,'Can delete image',74,'delete_image'),(225,'Can add poll plugin',75,'add_pollplugin'),(226,'Can change poll plugin',75,'change_pollplugin'),(227,'Can delete poll plugin',75,'delete_pollplugin'),(228,'Can add poll',76,'add_poll'),(229,'Can change poll',76,'change_poll'),(230,'Can delete poll',76,'delete_poll'),(231,'Can add choice',77,'add_choice'),(232,'Can change choice',77,'change_choice'),(233,'Can delete choice',77,'delete_choice'),(234,'Can add grizzly plugin',78,'add_grizzlyplugin'),(235,'Can change grizzly plugin',78,'change_grizzlyplugin'),(236,'Can delete grizzly plugin',78,'delete_grizzlyplugin'),(240,'Can add player status',80,'add_playerstatus'),(241,'Can change player status',80,'change_playerstatus'),(242,'Can delete player status',80,'delete_playerstatus'),(243,'Can add player',81,'add_player'),(244,'Can change player',81,'change_player'),(245,'Can delete player',81,'delete_player'),(246,'Can add judge',82,'add_judge'),(247,'Can change judge',82,'change_judge'),(248,'Can delete judge',82,'delete_judge'),(249,'Can add insurance type',83,'add_insurancetype'),(250,'Can change insurance type',83,'change_insurancetype'),(251,'Can delete insurance type',83,'delete_insurancetype'),(252,'Can add player type',84,'add_playertype'),(253,'Can change player type',84,'change_playertype'),(254,'Can delete player type',84,'delete_playertype'),(255,'Can add judge type',85,'add_judgetype'),(256,'Can change judge type',85,'change_judgetype'),(257,'Can delete judge type',85,'delete_judgetype'),(258,'Can add trainer',86,'add_trainer'),(259,'Can change trainer',86,'change_trainer'),(260,'Can delete trainer',86,'delete_trainer'),(261,'Can add rink',87,'add_rink'),(262,'Can change rink',87,'change_rink'),(263,'Can delete rink',87,'delete_rink'),(264,'Can add team',88,'add_team'),(265,'Can change team',88,'change_team'),(266,'Can delete team',88,'delete_team'),(267,'Can add training',89,'add_training'),(268,'Can change training',89,'change_training'),(269,'Can delete training',89,'delete_training');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(128) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `last_login` datetime NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'root','','','w@w-495.ru','pbkdf2_sha256$10000$UUx8fINZtqOj$CFw5Rc/5Z+LSOb1STJT0392BHiHAMwmkXUVJrY8u0nQ=',1,1,1,'2014-02-20 02:51:21','2014-02-20 02:50:19');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_fbfc09f1` (`user_id`),
  KEY `auth_user_groups_bda51c3c` (`group_id`),
  CONSTRAINT `user_id_refs_id_831107f1` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `group_id_refs_id_f0ee9890` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_fbfc09f1` (`user_id`),
  KEY `auth_user_user_permissions_1e014c8f` (`permission_id`),
  CONSTRAINT `user_id_refs_id_f2045483` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `permission_id_refs_id_67e79cb` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cms_cmsplugin`
--

DROP TABLE IF EXISTS `cms_cmsplugin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cms_cmsplugin` (
  `language` varchar(15) NOT NULL,
  `position` smallint(6),
  `creation_date` datetime NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `plugin_type` varchar(50) NOT NULL,
  `parent_id` int(11),
  `tree_id` int(10) unsigned NOT NULL,
  `lft` int(10) unsigned NOT NULL,
  `rght` int(10) unsigned NOT NULL,
  `level` int(10) unsigned NOT NULL,
  `placeholder_id` int(11) DEFAULT NULL,
  `changed_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cms_cmsplugin_8a7ac9ab` (`language`),
  KEY `cms_cmsplugin_ad070cd0` (`plugin_type`),
  KEY `cms_cmsplugin_63f17a16` (`parent_id`),
  KEY `cms_cmsplugin_efd07f28` (`tree_id`),
  KEY `cms_cmsplugin_42b06ff6` (`lft`),
  KEY `cms_cmsplugin_91543e5a` (`rght`),
  KEY `cms_cmsplugin_2a8f42e8` (`level`),
  KEY `cms_cmsplugin_62e7be1f` (`placeholder_id`),
  CONSTRAINT `parent_id_refs_id_e0b32a03` FOREIGN KEY (`parent_id`) REFERENCES `cms_cmsplugin` (`id`),
  CONSTRAINT `placeholder_id_refs_id_df6bb944` FOREIGN KEY (`placeholder_id`) REFERENCES `cms_placeholder` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cms_cmsplugin`
--

LOCK TABLES `cms_cmsplugin` WRITE;
/*!40000 ALTER TABLE `cms_cmsplugin` DISABLE KEYS */;
INSERT INTO `cms_cmsplugin` VALUES ('ru',0,'2014-02-20 02:57:25',2,'CarouselPlugin',NULL,1,1,2,0,2,'2014-02-20 03:08:33'),('ru',0,'2014-02-20 03:10:00',3,'CMSNewsAndEventsPlugin',NULL,2,1,2,0,3,'2014-02-20 03:10:11'),('ru',0,'2014-02-20 03:15:45',4,'CMSNewsAndEventsPlugin',NULL,3,1,2,0,10,'2014-02-20 03:16:04'),('ru',NULL,'2014-02-20 03:16:49',5,'TextPlugin',NULL,4,1,2,0,9,'2014-02-20 04:00:19');
/*!40000 ALTER TABLE `cms_cmsplugin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cms_globalpagepermission`
--

DROP TABLE IF EXISTS `cms_globalpagepermission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cms_globalpagepermission` (
  `can_publish` tinyint(1) NOT NULL,
  `group_id` int(11) DEFAULT NULL,
  `can_moderate` tinyint(1) NOT NULL,
  `can_change` tinyint(1) NOT NULL,
  `can_change_permissions` tinyint(1) NOT NULL,
  `can_recover_page` tinyint(1) NOT NULL,
  `can_add` tinyint(1) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `can_delete` tinyint(1) NOT NULL,
  `can_move_page` tinyint(1) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `can_change_advanced_settings` tinyint(1) NOT NULL,
  `can_view` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cms_globalpagepermission_bda51c3c` (`group_id`),
  KEY `cms_globalpagepermission_fbfc09f1` (`user_id`),
  CONSTRAINT `group_id_refs_id_b12278f8` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_f5365069` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cms_globalpagepermission`
--

LOCK TABLES `cms_globalpagepermission` WRITE;
/*!40000 ALTER TABLE `cms_globalpagepermission` DISABLE KEYS */;
/*!40000 ALTER TABLE `cms_globalpagepermission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cms_globalpagepermission_sites`
--

DROP TABLE IF EXISTS `cms_globalpagepermission_sites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cms_globalpagepermission_sites` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `globalpagepermission_id` int(11) NOT NULL,
  `site_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cms_globalpagepermission_sites_f5debdc1` (`globalpagepermission_id`),
  KEY `cms_globalpagepermission_sites_6223029` (`site_id`),
  CONSTRAINT `site_id_refs_id_38dfe611` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`),
  CONSTRAINT `globalpagepermission_id_refs_id_2c730e06` FOREIGN KEY (`globalpagepermission_id`) REFERENCES `cms_globalpagepermission` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cms_globalpagepermission_sites`
--

LOCK TABLES `cms_globalpagepermission_sites` WRITE;
/*!40000 ALTER TABLE `cms_globalpagepermission_sites` DISABLE KEYS */;
/*!40000 ALTER TABLE `cms_globalpagepermission_sites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cms_page`
--

DROP TABLE IF EXISTS `cms_page`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cms_page` (
  `rght` int(10) unsigned NOT NULL,
  `level` int(10) unsigned NOT NULL,
  `navigation_extenders` varchar(80) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `reverse_id` varchar(40),
  `login_required` tinyint(1) NOT NULL,
  `soft_root` tinyint(1) NOT NULL,
  `creation_date` datetime NOT NULL,
  `lft` int(10) unsigned NOT NULL,
  `publication_end_date` datetime DEFAULT NULL,
  `template` varchar(100) NOT NULL,
  `tree_id` int(10) unsigned NOT NULL,
  `publication_date` datetime DEFAULT NULL,
  `in_navigation` tinyint(1) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `moderator_state` smallint(6) NOT NULL,
  `published` tinyint(1) NOT NULL,
  `site_id` int(11) NOT NULL,
  `changed_by` varchar(70) NOT NULL,
  `created_by` varchar(70) NOT NULL,
  `publisher_is_draft` tinyint(1) NOT NULL,
  `publisher_state` smallint(6) NOT NULL,
  `publisher_public_id` int(11),
  `limit_visibility_in_menu` smallint(6) DEFAULT NULL,
  `changed_date` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `publisher_public_id` (`publisher_public_id`),
  KEY `cms_page_91543e5a` (`rght`),
  KEY `cms_page_2a8f42e8` (`level`),
  KEY `cms_page_d98c6d14` (`navigation_extenders`),
  KEY `cms_page_63f17a16` (`parent_id`),
  KEY `cms_page_b56116b` (`reverse_id`),
  KEY `cms_page_baa27763` (`soft_root`),
  KEY `cms_page_42b06ff6` (`lft`),
  KEY `cms_page_a221fe64` (`publication_end_date`),
  KEY `cms_page_efd07f28` (`tree_id`),
  KEY `cms_page_ee664462` (`publication_date`),
  KEY `cms_page_3c0ea264` (`in_navigation`),
  KEY `cms_page_6223029` (`site_id`),
  KEY `cms_page_16d2d3fa` (`publisher_is_draft`),
  KEY `cms_page_a0014f5a` (`publisher_state`),
  KEY `cms_page_c909672f` (`limit_visibility_in_menu`),
  CONSTRAINT `parent_id_refs_id_653a773` FOREIGN KEY (`parent_id`) REFERENCES `cms_page` (`id`),
  CONSTRAINT `publisher_public_id_refs_id_653a773` FOREIGN KEY (`publisher_public_id`) REFERENCES `cms_page` (`id`),
  CONSTRAINT `site_id_refs_id_ed70f71a` FOREIGN KEY (`site_id`) REFERENCES `django_site` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cms_page`
--

LOCK TABLES `cms_page` WRITE;
/*!40000 ALTER TABLE `cms_page` DISABLE KEYS */;
INSERT INTO `cms_page` VALUES (2,0,'',NULL,NULL,0,0,'2014-02-20 02:51:39',1,NULL,'title.html',1,'2014-02-20 03:04:50',1,1,0,1,1,'root','root',1,1,NULL,NULL,'2014-02-20 03:04:50'),(2,0,'',NULL,NULL,0,0,'2014-02-20 03:13:17',1,NULL,'base.html',2,'2014-02-20 03:13:46',1,2,0,1,1,'root','root',1,1,NULL,NULL,'2014-02-20 03:14:38');
/*!40000 ALTER TABLE `cms_page` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cms_page_placeholders`
--

DROP TABLE IF EXISTS `cms_page_placeholders`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cms_page_placeholders` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `page_id` int(11) NOT NULL,
  `placeholder_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `cms_page_placeholders_page_id_598353cf6a0df834_uniq` (`page_id`,`placeholder_id`),
  KEY `cms_page_placeholders_32d04bc7` (`page_id`),
  KEY `cms_page_placeholders_c1ca2850` (`placeholder_id`),
  CONSTRAINT `placeholder_id_refs_id_b0df4960` FOREIGN KEY (`placeholder_id`) REFERENCES `cms_placeholder` (`id`),
  CONSTRAINT `page_id_refs_id_b22baae5` FOREIGN KEY (`page_id`) REFERENCES `cms_page` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cms_page_placeholders`
--

LOCK TABLES `cms_page_placeholders` WRITE;
/*!40000 ALTER TABLE `cms_page_placeholders` DISABLE KEYS */;
INSERT INTO `cms_page_placeholders` VALUES (1,1,1),(2,1,2),(3,1,3),(4,2,10);
/*!40000 ALTER TABLE `cms_page_placeholders` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cms_pagemoderator`
--

DROP TABLE IF EXISTS `cms_pagemoderator`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cms_pagemoderator` (
  `moderate_page` tinyint(1) NOT NULL,
  `moderate_children` tinyint(1) NOT NULL,
  `page_id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `moderate_descendants` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cms_pagemoderator_32d04bc7` (`page_id`),
  KEY `cms_pagemoderator_fbfc09f1` (`user_id`),
  CONSTRAINT `user_id_refs_id_c574e281` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `page_id_refs_id_92bc8605` FOREIGN KEY (`page_id`) REFERENCES `cms_page` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cms_pagemoderator`
--

LOCK TABLES `cms_pagemoderator` WRITE;
/*!40000 ALTER TABLE `cms_pagemoderator` DISABLE KEYS */;
/*!40000 ALTER TABLE `cms_pagemoderator` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cms_pagemoderatorstate`
--

DROP TABLE IF EXISTS `cms_pagemoderatorstate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cms_pagemoderatorstate` (
  `created` datetime NOT NULL,
  `page_id` int(11) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `action` varchar(3) DEFAULT NULL,
  `message` longtext NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`),
  KEY `cms_pagemoderatorstate_32d04bc7` (`page_id`),
  KEY `cms_pagemoderatorstate_fbfc09f1` (`user_id`),
  CONSTRAINT `user_id_refs_id_2808fb19` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `page_id_refs_id_f4dc9e9d` FOREIGN KEY (`page_id`) REFERENCES `cms_page` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cms_pagemoderatorstate`
--

LOCK TABLES `cms_pagemoderatorstate` WRITE;
/*!40000 ALTER TABLE `cms_pagemoderatorstate` DISABLE KEYS */;
/*!40000 ALTER TABLE `cms_pagemoderatorstate` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cms_pagepermission`
--

DROP TABLE IF EXISTS `cms_pagepermission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cms_pagepermission` (
  `group_id` int(11) DEFAULT NULL,
  `can_publish` tinyint(1) NOT NULL,
  `page_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `can_delete` tinyint(1) NOT NULL,
  `can_change_permissions` tinyint(1) NOT NULL,
  `can_moderate` tinyint(1) NOT NULL,
  `can_add` tinyint(1) NOT NULL,
  `grant_on` int(11) NOT NULL,
  `can_move_page` tinyint(1) NOT NULL,
  `can_change` tinyint(1) NOT NULL,
  `can_change_advanced_settings` tinyint(1) NOT NULL,
  `can_view` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `cms_pagepermission_bda51c3c` (`group_id`),
  KEY `cms_pagepermission_32d04bc7` (`page_id`),
  KEY `cms_pagepermission_fbfc09f1` (`user_id`),
  CONSTRAINT `group_id_refs_id_d3639033` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `page_id_refs_id_d31a36ca` FOREIGN KEY (`page_id`) REFERENCES `cms_page` (`id`),
  CONSTRAINT `user_id_refs_id_4f0ab76c` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cms_pagepermission`
--

LOCK TABLES `cms_pagepermission` WRITE;
/*!40000 ALTER TABLE `cms_pagepermission` DISABLE KEYS */;
/*!40000 ALTER TABLE `cms_pagepermission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cms_pageuser`
--

DROP TABLE IF EXISTS `cms_pageuser`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cms_pageuser` (
  `user_ptr_id` int(11) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  PRIMARY KEY (`user_ptr_id`),
  KEY `cms_pageuser_b5de30be` (`created_by_id`),
  CONSTRAINT `created_by_id_refs_id_16b8b1ea` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `user_ptr_id_refs_id_16b8b1ea` FOREIGN KEY (`user_ptr_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cms_pageuser`
--

LOCK TABLES `cms_pageuser` WRITE;
/*!40000 ALTER TABLE `cms_pageuser` DISABLE KEYS */;
/*!40000 ALTER TABLE `cms_pageuser` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cms_pageusergroup`
--

DROP TABLE IF EXISTS `cms_pageusergroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cms_pageusergroup` (
  `group_ptr_id` int(11) NOT NULL,
  `created_by_id` int(11) NOT NULL,
  PRIMARY KEY (`group_ptr_id`),
  KEY `cms_pageusergroup_b5de30be` (`created_by_id`),
  CONSTRAINT `created_by_id_refs_id_3dc63396` FOREIGN KEY (`created_by_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `group_ptr_id_refs_id_99e5e357` FOREIGN KEY (`group_ptr_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cms_pageusergroup`
--

LOCK TABLES `cms_pageusergroup` WRITE;
/*!40000 ALTER TABLE `cms_pageusergroup` DISABLE KEYS */;
/*!40000 ALTER TABLE `cms_pageusergroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cms_placeholder`
--

DROP TABLE IF EXISTS `cms_placeholder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cms_placeholder` (
  `slot` varchar(50) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `default_width` smallint(5) unsigned,
  PRIMARY KEY (`id`),
  KEY `cms_placeholder_400badfd` (`slot`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cms_placeholder`
--

LOCK TABLES `cms_placeholder` WRITE;
/*!40000 ALTER TABLE `cms_placeholder` DISABLE KEYS */;
INSERT INTO `cms_placeholder` VALUES ('body',1,NULL),('jumbotron',2,NULL),('new',3,NULL),('insert',4,NULL),('body',5,NULL),('body',6,NULL),('body',7,NULL),('body',8,NULL),('body',9,NULL),('body',10,NULL),('insert',11,NULL);
/*!40000 ALTER TABLE `cms_placeholder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cms_title`
--

DROP TABLE IF EXISTS `cms_title`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cms_title` (
  `language` varchar(15) NOT NULL,
  `title` varchar(255) NOT NULL,
  `page_id` int(11) NOT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `path` varchar(255) NOT NULL,
  `creation_date` datetime NOT NULL,
  `slug` varchar(255) NOT NULL,
  `has_url_overwrite` tinyint(1) NOT NULL,
  `application_urls` varchar(200),
  `redirect` varchar(255),
  `meta_keywords` varchar(255),
  `meta_description` longtext,
  `page_title` varchar(255),
  `menu_title` varchar(255),
  PRIMARY KEY (`id`),
  UNIQUE KEY `cms_title_page_id_45628dc0e8a26dd5_uniq` (`page_id`,`language`),
  KEY `cms_title_8a7ac9ab` (`language`),
  KEY `cms_title_32d04bc7` (`page_id`),
  KEY `cms_title_6a8a34e2` (`path`),
  KEY `cms_title_a951d5d6` (`slug`),
  KEY `cms_title_c269b1d2` (`has_url_overwrite`),
  KEY `cms_title_23b1fc68` (`application_urls`),
  CONSTRAINT `page_id_refs_id_fc98665f` FOREIGN KEY (`page_id`) REFERENCES `cms_page` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cms_title`
--

LOCK TABLES `cms_title` WRITE;
/*!40000 ALTER TABLE `cms_title` DISABLE KEYS */;
INSERT INTO `cms_title` VALUES ('ru','Главная',1,1,'','2014-02-20 02:51:39','glavnaya',0,'','','','','',''),('ru','Новости',2,2,'news','2014-02-20 03:13:17','news',0,'','','','','','');
/*!40000 ALTER TABLE `cms_title` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmsplugin_bootstrap_carousel_carouselitem`
--

DROP TABLE IF EXISTS `cmsplugin_bootstrap_carousel_carouselitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmsplugin_bootstrap_carousel_carouselitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `carousel_id` int(11) NOT NULL,
  `caption_title` varchar(100) DEFAULT NULL,
  `caption_content` longtext,
  `image_id` int(11) DEFAULT NULL,
  `caption_link` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `cmsplugin_bootstrap_carousel_carouselitem_45002e36` (`carousel_id`),
  KEY `cmsplugin_bootstrap_carousel_carouselitem_6682136` (`image_id`),
  CONSTRAINT `carousel_id_refs_cmsplugin_ptr_id_196b025` FOREIGN KEY (`carousel_id`) REFERENCES `cmsplugin_carousel` (`cmsplugin_ptr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmsplugin_bootstrap_carousel_carouselitem`
--

LOCK TABLES `cmsplugin_bootstrap_carousel_carouselitem` WRITE;
/*!40000 ALTER TABLE `cmsplugin_bootstrap_carousel_carouselitem` DISABLE KEYS */;
INSERT INTO `cmsplugin_bootstrap_carousel_carouselitem` VALUES (1,2,'Первая','',1,'http://yandex.ru'),(2,2,'Вторая','',2,'http://google.ru');
/*!40000 ALTER TABLE `cmsplugin_bootstrap_carousel_carouselitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmsplugin_carousel`
--

DROP TABLE IF EXISTS `cmsplugin_carousel`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmsplugin_carousel` (
  `cmsplugin_ptr_id` int(11) NOT NULL,
  `domid` varchar(50) NOT NULL,
  `interval` int(11) NOT NULL,
  PRIMARY KEY (`cmsplugin_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmsplugin_carousel`
--

LOCK TABLES `cmsplugin_carousel` WRITE;
/*!40000 ALTER TABLE `cmsplugin_carousel` DISABLE KEYS */;
INSERT INTO `cmsplugin_carousel` VALUES (2,'Carousel1',5000);
/*!40000 ALTER TABLE `cmsplugin_carousel` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmsplugin_carouselplugin`
--

DROP TABLE IF EXISTS `cmsplugin_carouselplugin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmsplugin_carouselplugin` (
  `cmsplugin_ptr_id` int(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `width` double NOT NULL,
  `aspect_ratio` double DEFAULT NULL,
  PRIMARY KEY (`cmsplugin_ptr_id`),
  CONSTRAINT `cmsplugin_ptr_id_refs_id_23a5fe32` FOREIGN KEY (`cmsplugin_ptr_id`) REFERENCES `cms_cmsplugin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmsplugin_carouselplugin`
--

LOCK TABLES `cmsplugin_carouselplugin` WRITE;
/*!40000 ALTER TABLE `cmsplugin_carouselplugin` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmsplugin_carouselplugin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmsplugin_embeddedvideosetplugin`
--

DROP TABLE IF EXISTS `cmsplugin_embeddedvideosetplugin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmsplugin_embeddedvideosetplugin` (
  `cmsplugin_ptr_id` int(11) NOT NULL,
  `width` double NOT NULL,
  PRIMARY KEY (`cmsplugin_ptr_id`),
  CONSTRAINT `cmsplugin_ptr_id_refs_id_83ca62f7` FOREIGN KEY (`cmsplugin_ptr_id`) REFERENCES `cms_cmsplugin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmsplugin_embeddedvideosetplugin`
--

LOCK TABLES `cmsplugin_embeddedvideosetplugin` WRITE;
/*!40000 ALTER TABLE `cmsplugin_embeddedvideosetplugin` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmsplugin_embeddedvideosetplugin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmsplugin_entityautopagelinkplugineditor`
--

DROP TABLE IF EXISTS `cmsplugin_entityautopagelinkplugineditor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmsplugin_entityautopagelinkplugineditor` (
  `cmsplugin_ptr_id` int(11) NOT NULL,
  `link_to` varchar(50) NOT NULL,
  `entity_id` int(11),
  `text_override` varchar(256) DEFAULT NULL,
  PRIMARY KEY (`cmsplugin_ptr_id`),
  KEY `cmsplugin_entityautopagelinkplugineditor_2ce815e9` (`entity_id`),
  CONSTRAINT `entity_id_refs_entitylite_ptr_id_426c0934` FOREIGN KEY (`entity_id`) REFERENCES `contacts_and_people_entity` (`entitylite_ptr_id`),
  CONSTRAINT `cmsplugin_ptr_id_refs_id_33298722` FOREIGN KEY (`cmsplugin_ptr_id`) REFERENCES `cms_cmsplugin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmsplugin_entityautopagelinkplugineditor`
--

LOCK TABLES `cmsplugin_entityautopagelinkplugineditor` WRITE;
/*!40000 ALTER TABLE `cmsplugin_entityautopagelinkplugineditor` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmsplugin_entityautopagelinkplugineditor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmsplugin_entitydirectoryplugineditor`
--

DROP TABLE IF EXISTS `cmsplugin_entitydirectoryplugineditor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmsplugin_entitydirectoryplugineditor` (
  `cmsplugin_ptr_id` int(11) NOT NULL,
  `entity_id` int(11),
  `levels` smallint(5) unsigned DEFAULT NULL,
  `display_descriptions_to_level` smallint(5) unsigned DEFAULT NULL,
  `link_icons` tinyint(1) NOT NULL,
  `use_short_names` tinyint(1) NOT NULL,
  PRIMARY KEY (`cmsplugin_ptr_id`),
  KEY `cmsplugin_entitydirectoryplugineditor_2ce815e9` (`entity_id`),
  CONSTRAINT `entity_id_refs_entitylite_ptr_id_52c0f774` FOREIGN KEY (`entity_id`) REFERENCES `contacts_and_people_entity` (`entitylite_ptr_id`),
  CONSTRAINT `cmsplugin_ptr_id_refs_id_43964f1e` FOREIGN KEY (`cmsplugin_ptr_id`) REFERENCES `cms_cmsplugin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmsplugin_entitydirectoryplugineditor`
--

LOCK TABLES `cmsplugin_entitydirectoryplugineditor` WRITE;
/*!40000 ALTER TABLE `cmsplugin_entitydirectoryplugineditor` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmsplugin_entitydirectoryplugineditor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmsplugin_entitymembersplugineditor`
--

DROP TABLE IF EXISTS `cmsplugin_entitymembersplugineditor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmsplugin_entitymembersplugineditor` (
  `cmsplugin_ptr_id` int(11) NOT NULL,
  `entity_id` int(11),
  PRIMARY KEY (`cmsplugin_ptr_id`),
  KEY `cmsplugin_entitymembersplugineditor_2ce815e9` (`entity_id`),
  CONSTRAINT `entity_id_refs_entitylite_ptr_id_b8f6fd82` FOREIGN KEY (`entity_id`) REFERENCES `contacts_and_people_entity` (`entitylite_ptr_id`),
  CONSTRAINT `cmsplugin_ptr_id_refs_id_a0993a28` FOREIGN KEY (`cmsplugin_ptr_id`) REFERENCES `cms_cmsplugin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmsplugin_entitymembersplugineditor`
--

LOCK TABLES `cmsplugin_entitymembersplugineditor` WRITE;
/*!40000 ALTER TABLE `cmsplugin_entitymembersplugineditor` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmsplugin_entitymembersplugineditor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmsplugin_focusonplugineditor`
--

DROP TABLE IF EXISTS `cmsplugin_focusonplugineditor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmsplugin_focusonplugineditor` (
  `cmsplugin_ptr_id` int(11) NOT NULL,
  `heading_level` smallint(5) unsigned NOT NULL,
  PRIMARY KEY (`cmsplugin_ptr_id`),
  CONSTRAINT `cmsplugin_ptr_id_refs_id_a162ce6b` FOREIGN KEY (`cmsplugin_ptr_id`) REFERENCES `cms_cmsplugin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmsplugin_focusonplugineditor`
--

LOCK TABLES `cmsplugin_focusonplugineditor` WRITE;
/*!40000 ALTER TABLE `cmsplugin_focusonplugineditor` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmsplugin_focusonplugineditor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmsplugin_genericlinklistplugin`
--

DROP TABLE IF EXISTS `cmsplugin_genericlinklistplugin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmsplugin_genericlinklistplugin` (
  `cmsplugin_ptr_id` int(11) NOT NULL,
  `insert_as` smallint(5) unsigned NOT NULL,
  `use_link_icons` tinyint(1) NOT NULL,
  `separator` varchar(20) DEFAULT NULL,
  `final_separator` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`cmsplugin_ptr_id`),
  CONSTRAINT `cmsplugin_ptr_id_refs_id_ae6ffdfe` FOREIGN KEY (`cmsplugin_ptr_id`) REFERENCES `cms_cmsplugin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmsplugin_genericlinklistplugin`
--

LOCK TABLES `cmsplugin_genericlinklistplugin` WRITE;
/*!40000 ALTER TABLE `cmsplugin_genericlinklistplugin` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmsplugin_genericlinklistplugin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmsplugin_grizzlyplugin`
--

DROP TABLE IF EXISTS `cmsplugin_grizzlyplugin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmsplugin_grizzlyplugin` (
  `cmsplugin_ptr_id` int(11) NOT NULL,
  `player_id` int(11) NOT NULL,
  `judge_id` int(11) NOT NULL,
  `judgetype_id` int(11) NOT NULL,
  `playerstatus_id` int(11) NOT NULL,
  `insurancetype_id` int(11) NOT NULL,
  `trainer_id` int(11) NOT NULL,
  `rink_id` int(11) NOT NULL,
  `team_id` int(11) NOT NULL,
  `training_id` int(11) NOT NULL,
  PRIMARY KEY (`cmsplugin_ptr_id`),
  KEY `cmsplugin_grizzlyplugin_ea2d1965` (`player_id`),
  KEY `cmsplugin_grizzlyplugin_bcb024b0` (`judge_id`),
  KEY `cmsplugin_grizzlyplugin_f613d214` (`judgetype_id`),
  KEY `cmsplugin_grizzlyplugin_a0f8eb2d` (`playerstatus_id`),
  KEY `cmsplugin_grizzlyplugin_3ed7fb09` (`insurancetype_id`),
  KEY `cmsplugin_grizzlyplugin_c207bcac` (`trainer_id`),
  KEY `cmsplugin_grizzlyplugin_fa5e043e` (`rink_id`),
  KEY `cmsplugin_grizzlyplugin_fcf8ac47` (`team_id`),
  KEY `cmsplugin_grizzlyplugin_e9213ad6` (`training_id`),
  CONSTRAINT `training_id_refs_id_55481147` FOREIGN KEY (`training_id`) REFERENCES `grizzly_training` (`id`),
  CONSTRAINT `cmsplugin_ptr_id_refs_id_65538fc4` FOREIGN KEY (`cmsplugin_ptr_id`) REFERENCES `cms_cmsplugin` (`id`),
  CONSTRAINT `insurancetype_id_refs_id_65ec2284` FOREIGN KEY (`insurancetype_id`) REFERENCES `grizzly_insurancetype` (`id`),
  CONSTRAINT `judgetype_id_refs_id_25c83a8d` FOREIGN KEY (`judgetype_id`) REFERENCES `grizzly_judgetype` (`id`),
  CONSTRAINT `judge_id_refs_id_7e32c827` FOREIGN KEY (`judge_id`) REFERENCES `grizzly_judge` (`id`),
  CONSTRAINT `playerstatus_id_refs_id_1e0a4afc` FOREIGN KEY (`playerstatus_id`) REFERENCES `grizzly_playerstatus` (`id`),
  CONSTRAINT `player_id_refs_id_7592d174` FOREIGN KEY (`player_id`) REFERENCES `grizzly_player` (`id`),
  CONSTRAINT `rink_id_refs_id_564e0265` FOREIGN KEY (`rink_id`) REFERENCES `grizzly_rink` (`id`),
  CONSTRAINT `team_id_refs_id_c19bfebe` FOREIGN KEY (`team_id`) REFERENCES `grizzly_team` (`id`),
  CONSTRAINT `trainer_id_refs_id_48d92d1` FOREIGN KEY (`trainer_id`) REFERENCES `grizzly_trainer` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmsplugin_grizzlyplugin`
--

LOCK TABLES `cmsplugin_grizzlyplugin` WRITE;
/*!40000 ALTER TABLE `cmsplugin_grizzlyplugin` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmsplugin_grizzlyplugin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmsplugin_imagesetplugin`
--

DROP TABLE IF EXISTS `cmsplugin_imagesetplugin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmsplugin_imagesetplugin` (
  `cmsplugin_ptr_id` int(11) NOT NULL,
  `kind` varchar(50) NOT NULL,
  `width` double NOT NULL,
  `height` int(10) unsigned DEFAULT NULL,
  `aspect_ratio` double DEFAULT NULL,
  `float` varchar(10) DEFAULT NULL,
  `items_per_row` smallint(5) unsigned DEFAULT NULL,
  PRIMARY KEY (`cmsplugin_ptr_id`),
  CONSTRAINT `cmsplugin_ptr_id_refs_id_b4b4d8e9` FOREIGN KEY (`cmsplugin_ptr_id`) REFERENCES `cms_cmsplugin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmsplugin_imagesetplugin`
--

LOCK TABLES `cmsplugin_imagesetplugin` WRITE;
/*!40000 ALTER TABLE `cmsplugin_imagesetplugin` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmsplugin_imagesetplugin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmsplugin_newsandeventsplugin`
--

DROP TABLE IF EXISTS `cmsplugin_newsandeventsplugin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmsplugin_newsandeventsplugin` (
  `cmsplugin_ptr_id` int(11) NOT NULL,
  `entity_id` int(11),
  `layout` varchar(25) NOT NULL,
  `format` varchar(25) NOT NULL,
  `heading_level` smallint(5) unsigned NOT NULL,
  `order_by` varchar(25) NOT NULL,
  `list_format` varchar(25) NOT NULL,
  `group_dates` tinyint(1) NOT NULL,
  `limit_to` smallint(5) unsigned DEFAULT NULL,
  `display` varchar(25) NOT NULL,
  `show_previous_events` tinyint(1) NOT NULL,
  `news_heading_text` varchar(25) NOT NULL,
  `events_heading_text` varchar(25) NOT NULL,
  PRIMARY KEY (`cmsplugin_ptr_id`),
  KEY `cmsplugin_newsandeventsplugin_2ce815e9` (`entity_id`),
  CONSTRAINT `entity_id_refs_entitylite_ptr_id_970c7c32` FOREIGN KEY (`entity_id`) REFERENCES `contacts_and_people_entity` (`entitylite_ptr_id`),
  CONSTRAINT `cmsplugin_ptr_id_refs_id_14cac7c8` FOREIGN KEY (`cmsplugin_ptr_id`) REFERENCES `cms_cmsplugin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmsplugin_newsandeventsplugin`
--

LOCK TABLES `cmsplugin_newsandeventsplugin` WRITE;
/*!40000 ALTER TABLE `cmsplugin_newsandeventsplugin` DISABLE KEYS */;
INSERT INTO `cmsplugin_newsandeventsplugin` VALUES (3,NULL,'sidebyside','details image',2,'importance/date','vertical',1,5,'news & events',0,'News','Events'),(4,NULL,'stacked','details image',2,'importance/date','vertical',1,NULL,'news & events',0,'News','Events');
/*!40000 ALTER TABLE `cmsplugin_newsandeventsplugin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmsplugin_pollplugin`
--

DROP TABLE IF EXISTS `cmsplugin_pollplugin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmsplugin_pollplugin` (
  `cmsplugin_ptr_id` int(11) NOT NULL,
  `poll_id` int(11) NOT NULL,
  PRIMARY KEY (`cmsplugin_ptr_id`),
  KEY `cmsplugin_pollplugin_763e883` (`poll_id`),
  CONSTRAINT `poll_id_refs_id_f2a11304` FOREIGN KEY (`poll_id`) REFERENCES `polls_poll` (`id`),
  CONSTRAINT `cmsplugin_ptr_id_refs_id_3c01b707` FOREIGN KEY (`cmsplugin_ptr_id`) REFERENCES `cms_cmsplugin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmsplugin_pollplugin`
--

LOCK TABLES `cmsplugin_pollplugin` WRITE;
/*!40000 ALTER TABLE `cmsplugin_pollplugin` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmsplugin_pollplugin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmsplugin_snippetptr`
--

DROP TABLE IF EXISTS `cmsplugin_snippetptr`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmsplugin_snippetptr` (
  `cmsplugin_ptr_id` int(11) NOT NULL,
  `snippet_id` int(11) NOT NULL,
  UNIQUE KEY `cmsplugin_ptr_id` (`cmsplugin_ptr_id`),
  KEY `snippet_snippetptr_37e31bc4` (`snippet_id`),
  CONSTRAINT `cmsplugin_ptr_id_refs_id_62cab895` FOREIGN KEY (`cmsplugin_ptr_id`) REFERENCES `cms_cmsplugin` (`id`),
  CONSTRAINT `snippet_id_refs_id_ce9512ce` FOREIGN KEY (`snippet_id`) REFERENCES `snippet_snippet` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmsplugin_snippetptr`
--

LOCK TABLES `cmsplugin_snippetptr` WRITE;
/*!40000 ALTER TABLE `cmsplugin_snippetptr` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmsplugin_snippetptr` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmsplugin_text`
--

DROP TABLE IF EXISTS `cmsplugin_text`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmsplugin_text` (
  `body` longtext NOT NULL,
  `cmsplugin_ptr_id` int(11) NOT NULL,
  UNIQUE KEY `cmsplugin_ptr_id` (`cmsplugin_ptr_id`),
  CONSTRAINT `cmsplugin_ptr_id_refs_id_bf9780bc` FOREIGN KEY (`cmsplugin_ptr_id`) REFERENCES `cms_cmsplugin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmsplugin_text`
--

LOCK TABLES `cmsplugin_text` WRITE;
/*!40000 ALTER TABLE `cmsplugin_text` DISABLE KEYS */;
INSERT INTO `cmsplugin_text` VALUES ('<p>фыфыфы</p><p>фыфыфыфы фыфыфы</p><p>фыфыфы</p><p>фыыыыыыыыыыыыыыыыыыыыыы</p>',5);
/*!40000 ALTER TABLE `cmsplugin_text` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmsplugin_vacanciesplugin`
--

DROP TABLE IF EXISTS `cmsplugin_vacanciesplugin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmsplugin_vacanciesplugin` (
  `cmsplugin_ptr_id` int(11) NOT NULL,
  `entity_id` int(11),
  `layout` varchar(25) NOT NULL,
  `format` varchar(25) NOT NULL,
  `heading_level` smallint(5) unsigned NOT NULL,
  `order_by` varchar(25) NOT NULL,
  `list_format` varchar(25) NOT NULL,
  `group_dates` tinyint(1) NOT NULL,
  `limit_to` smallint(5) unsigned DEFAULT NULL,
  `display` varchar(25) NOT NULL,
  `vacancies_heading_text` varchar(25) NOT NULL,
  `studentships_heading_text` varchar(25) NOT NULL,
  PRIMARY KEY (`cmsplugin_ptr_id`),
  KEY `cmsplugin_vacanciesplugin_2ce815e9` (`entity_id`),
  CONSTRAINT `entity_id_refs_entitylite_ptr_id_edfebe16` FOREIGN KEY (`entity_id`) REFERENCES `contacts_and_people_entity` (`entitylite_ptr_id`),
  CONSTRAINT `cmsplugin_ptr_id_refs_id_7f207e40` FOREIGN KEY (`cmsplugin_ptr_id`) REFERENCES `cms_cmsplugin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmsplugin_vacanciesplugin`
--

LOCK TABLES `cmsplugin_vacanciesplugin` WRITE;
/*!40000 ALTER TABLE `cmsplugin_vacanciesplugin` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmsplugin_vacanciesplugin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cmsplugin_videoplugineditor`
--

DROP TABLE IF EXISTS `cmsplugin_videoplugineditor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `cmsplugin_videoplugineditor` (
  `cmsplugin_ptr_id` int(11) NOT NULL,
  `video_id` int(11) NOT NULL,
  `width` double DEFAULT NULL,
  `use_description_as_caption` tinyint(1) NOT NULL,
  `caption` longtext,
  `float` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`cmsplugin_ptr_id`),
  KEY `cmsplugin_videoplugineditor_fa26288c` (`video_id`),
  CONSTRAINT `video_id_refs_file_ptr_id_fcb8d23e` FOREIGN KEY (`video_id`) REFERENCES `video_video` (`file_ptr_id`),
  CONSTRAINT `cmsplugin_ptr_id_refs_id_7f7f54db` FOREIGN KEY (`cmsplugin_ptr_id`) REFERENCES `cms_cmsplugin` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cmsplugin_videoplugineditor`
--

LOCK TABLES `cmsplugin_videoplugineditor` WRITE;
/*!40000 ALTER TABLE `cmsplugin_videoplugineditor` DISABLE KEYS */;
/*!40000 ALTER TABLE `cmsplugin_videoplugineditor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacts_and_people_building`
--

DROP TABLE IF EXISTS `contacts_and_people_building`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contacts_and_people_building` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) DEFAULT NULL,
  `number` varchar(10) DEFAULT NULL,
  `street` varchar(100) DEFAULT NULL,
  `additional_street_address` varchar(100) DEFAULT NULL,
  `postcode` varchar(9) DEFAULT NULL,
  `site_id` int(11) NOT NULL,
  `slug` varchar(255) DEFAULT NULL,
  `image_id` int(11),
  `summary` longtext NOT NULL,
  `description_id` int(11) DEFAULT NULL,
  `getting_here_id` int(11) DEFAULT NULL,
  `access_and_parking_id` int(11) DEFAULT NULL,
  `map` tinyint(1) NOT NULL,
  `latitude` double DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  `zoom` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `contacts_and_people_building_6223029` (`site_id`),
  KEY `contacts_and_people_building_6682136` (`image_id`),
  KEY `contacts_and_people_building_902c968b` (`description_id`),
  KEY `contacts_and_people_building_ac905ec9` (`getting_here_id`),
  KEY `contacts_and_people_building_37dfe81` (`access_and_parking_id`),
  CONSTRAINT `site_id_refs_id_d887b26c` FOREIGN KEY (`site_id`) REFERENCES `contacts_and_people_site` (`id`),
  CONSTRAINT `access_and_parking_id_refs_id_6aa28e29` FOREIGN KEY (`access_and_parking_id`) REFERENCES `cms_placeholder` (`id`),
  CONSTRAINT `description_id_refs_id_6aa28e29` FOREIGN KEY (`description_id`) REFERENCES `cms_placeholder` (`id`),
  CONSTRAINT `getting_here_id_refs_id_6aa28e29` FOREIGN KEY (`getting_here_id`) REFERENCES `cms_placeholder` (`id`),
  CONSTRAINT `image_id_refs_file_ptr_id_551fe060` FOREIGN KEY (`image_id`) REFERENCES `filer_image` (`file_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts_and_people_building`
--

LOCK TABLES `contacts_and_people_building` WRITE;
/*!40000 ALTER TABLE `contacts_and_people_building` DISABLE KEYS */;
/*!40000 ALTER TABLE `contacts_and_people_building` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacts_and_people_entity`
--

DROP TABLE IF EXISTS `contacts_and_people_entity`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contacts_and_people_entity` (
  `entitylite_ptr_id` int(11) NOT NULL,
  `url` varchar(200) DEFAULT NULL,
  `external_url_id` int(11),
  `slug` varchar(60) NOT NULL,
  `precise_location` varchar(255) DEFAULT NULL,
  `access_note` varchar(255) DEFAULT NULL,
  `email` varchar(75) DEFAULT NULL,
  `image_id` int(11),
  `short_name` varchar(100) DEFAULT NULL,
  `abstract_entity` tinyint(1) NOT NULL,
  `parent_id` int(11),
  `display_parent` tinyint(1) NOT NULL,
  `building_recapitulates_entity_name` tinyint(1) NOT NULL,
  `building_id` int(11),
  `website_id` int(11),
  `auto_news_page` tinyint(1) NOT NULL,
  `news_page_menu_title` varchar(50) NOT NULL,
  `news_page_intro_id` int(11) DEFAULT NULL,
  `auto_contacts_page` tinyint(1) NOT NULL,
  `contacts_page_menu_title` varchar(50) NOT NULL,
  `contacts_page_intro_id` int(11) DEFAULT NULL,
  `auto_vacancies_page` tinyint(1) NOT NULL,
  `vacancies_page_menu_title` varchar(50) NOT NULL,
  `vacancies_page_intro_id` int(11) DEFAULT NULL,
  `lft` int(10) unsigned NOT NULL,
  `rght` int(10) unsigned NOT NULL,
  `tree_id` int(10) unsigned NOT NULL,
  `level` int(10) unsigned NOT NULL,
  PRIMARY KEY (`entitylite_ptr_id`),
  UNIQUE KEY `slug` (`slug`),
  UNIQUE KEY `website_id` (`website_id`),
  KEY `contacts_and_people_entity_b68122a1` (`external_url_id`),
  KEY `contacts_and_people_entity_6682136` (`image_id`),
  KEY `contacts_and_people_entity_63f17a16` (`parent_id`),
  KEY `contacts_and_people_entity_57000c84` (`building_id`),
  KEY `contacts_and_people_entity_43e749d3` (`news_page_intro_id`),
  KEY `contacts_and_people_entity_ea46b2bd` (`contacts_page_intro_id`),
  KEY `contacts_and_people_entity_5c7493f4` (`vacancies_page_intro_id`),
  KEY `contacts_and_people_entity_42b06ff6` (`lft`),
  KEY `contacts_and_people_entity_91543e5a` (`rght`),
  KEY `contacts_and_people_entity_efd07f28` (`tree_id`),
  KEY `contacts_and_people_entity_2a8f42e8` (`level`),
  CONSTRAINT `external_url_id_refs_id_55e9fd53` FOREIGN KEY (`external_url_id`) REFERENCES `links_externallink` (`id`),
  CONSTRAINT `building_id_refs_id_ddf4f3b4` FOREIGN KEY (`building_id`) REFERENCES `contacts_and_people_building` (`id`),
  CONSTRAINT `contacts_page_intro_id_refs_id_ebf26c1a` FOREIGN KEY (`contacts_page_intro_id`) REFERENCES `cms_placeholder` (`id`),
  CONSTRAINT `entitylite_ptr_id_refs_id_7a5f8605` FOREIGN KEY (`entitylite_ptr_id`) REFERENCES `contacts_and_people_entitylite` (`id`),
  CONSTRAINT `image_id_refs_file_ptr_id_16c31591` FOREIGN KEY (`image_id`) REFERENCES `filer_image` (`file_ptr_id`),
  CONSTRAINT `news_page_intro_id_refs_id_ebf26c1a` FOREIGN KEY (`news_page_intro_id`) REFERENCES `cms_placeholder` (`id`),
  CONSTRAINT `parent_id_refs_entitylite_ptr_id_4f8e9143` FOREIGN KEY (`parent_id`) REFERENCES `contacts_and_people_entity` (`entitylite_ptr_id`),
  CONSTRAINT `vacancies_page_intro_id_refs_id_ebf26c1a` FOREIGN KEY (`vacancies_page_intro_id`) REFERENCES `cms_placeholder` (`id`),
  CONSTRAINT `website_id_refs_id_5a877ed5` FOREIGN KEY (`website_id`) REFERENCES `cms_page` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts_and_people_entity`
--

LOCK TABLES `contacts_and_people_entity` WRITE;
/*!40000 ALTER TABLE `contacts_and_people_entity` DISABLE KEYS */;
INSERT INTO `contacts_and_people_entity` VALUES (1,NULL,NULL,'default','','','',4,'default',1,NULL,0,0,NULL,NULL,0,'News & events',5,0,'Contacts & people',6,0,'Vacancies & studentships',7,1,2,1,0);
/*!40000 ALTER TABLE `contacts_and_people_entity` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacts_and_people_entitylite`
--

DROP TABLE IF EXISTS `contacts_and_people_entitylite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contacts_and_people_entitylite` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts_and_people_entitylite`
--

LOCK TABLES `contacts_and_people_entitylite` WRITE;
/*!40000 ALTER TABLE `contacts_and_people_entitylite` DISABLE KEYS */;
INSERT INTO `contacts_and_people_entitylite` VALUES (1,'default');
/*!40000 ALTER TABLE `contacts_and_people_entitylite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacts_and_people_membership`
--

DROP TABLE IF EXISTS `contacts_and_people_membership`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contacts_and_people_membership` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) NOT NULL,
  `entity_id` int(11) NOT NULL,
  `display_role_id` int(11),
  `key_contact` tinyint(1) NOT NULL,
  `role` varchar(50) DEFAULT NULL,
  `importance_to_person` int(11) DEFAULT NULL,
  `importance_to_entity` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `contacts_and_people_membership_21b911c5` (`person_id`),
  KEY `contacts_and_people_membership_2ce815e9` (`entity_id`),
  KEY `contacts_and_people_membership_e4b479db` (`display_role_id`),
  CONSTRAINT `display_role_id_refs_id_134f1719` FOREIGN KEY (`display_role_id`) REFERENCES `contacts_and_people_membership` (`id`),
  CONSTRAINT `entity_id_refs_entitylite_ptr_id_7df8ceb0` FOREIGN KEY (`entity_id`) REFERENCES `contacts_and_people_entity` (`entitylite_ptr_id`),
  CONSTRAINT `person_id_refs_personlite_ptr_id_6472bf96` FOREIGN KEY (`person_id`) REFERENCES `contacts_and_people_person` (`personlite_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts_and_people_membership`
--

LOCK TABLES `contacts_and_people_membership` WRITE;
/*!40000 ALTER TABLE `contacts_and_people_membership` DISABLE KEYS */;
/*!40000 ALTER TABLE `contacts_and_people_membership` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacts_and_people_person`
--

DROP TABLE IF EXISTS `contacts_and_people_person`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contacts_and_people_person` (
  `personlite_ptr_id` int(11) NOT NULL,
  `url` varchar(200) DEFAULT NULL,
  `external_url_id` int(11),
  `slug` varchar(60) NOT NULL,
  `precise_location` varchar(255) DEFAULT NULL,
  `access_note` varchar(255) DEFAULT NULL,
  `email` varchar(75) DEFAULT NULL,
  `image_id` int(11),
  `user_id` int(11),
  `institutional_username` varchar(10) DEFAULT NULL,
  `active` tinyint(1) NOT NULL,
  `description_id` int(11) DEFAULT NULL,
  `building_id` int(11),
  `override_entity_id` int(11),
  `please_contact_id` int(11),
  `staff_id` varchar(20) DEFAULT NULL,
  `data_feed_locked` tinyint(1) NOT NULL,
  PRIMARY KEY (`personlite_ptr_id`),
  UNIQUE KEY `slug` (`slug`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `contacts_and_people_person_b68122a1` (`external_url_id`),
  KEY `contacts_and_people_person_6682136` (`image_id`),
  KEY `contacts_and_people_person_902c968b` (`description_id`),
  KEY `contacts_and_people_person_57000c84` (`building_id`),
  KEY `contacts_and_people_person_278ed1c7` (`override_entity_id`),
  KEY `contacts_and_people_person_730876fd` (`please_contact_id`),
  CONSTRAINT `external_url_id_refs_id_3d172719` FOREIGN KEY (`external_url_id`) REFERENCES `links_externallink` (`id`),
  CONSTRAINT `building_id_refs_id_139f34fa` FOREIGN KEY (`building_id`) REFERENCES `contacts_and_people_building` (`id`),
  CONSTRAINT `description_id_refs_id_c1701694` FOREIGN KEY (`description_id`) REFERENCES `cms_placeholder` (`id`),
  CONSTRAINT `image_id_refs_file_ptr_id_1fccff1d` FOREIGN KEY (`image_id`) REFERENCES `filer_image` (`file_ptr_id`),
  CONSTRAINT `override_entity_id_refs_entitylite_ptr_id_7a8a45f1` FOREIGN KEY (`override_entity_id`) REFERENCES `contacts_and_people_entity` (`entitylite_ptr_id`),
  CONSTRAINT `personlite_ptr_id_refs_id_91d2ce13` FOREIGN KEY (`personlite_ptr_id`) REFERENCES `contacts_and_people_personlite` (`id`),
  CONSTRAINT `please_contact_id_refs_personlite_ptr_id_4326dec3` FOREIGN KEY (`please_contact_id`) REFERENCES `contacts_and_people_person` (`personlite_ptr_id`),
  CONSTRAINT `user_id_refs_id_5c43437b` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts_and_people_person`
--

LOCK TABLES `contacts_and_people_person` WRITE;
/*!40000 ALTER TABLE `contacts_and_people_person` DISABLE KEYS */;
/*!40000 ALTER TABLE `contacts_and_people_person` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacts_and_people_personlite`
--

DROP TABLE IF EXISTS `contacts_and_people_personlite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contacts_and_people_personlite` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `given_name` varchar(50) DEFAULT NULL,
  `middle_names` varchar(100) DEFAULT NULL,
  `surname` varchar(50) NOT NULL,
  `title_id` int(11),
  PRIMARY KEY (`id`),
  KEY `title_id_refs_id_ce776e7f` (`title_id`),
  CONSTRAINT `title_id_refs_id_ce776e7f` FOREIGN KEY (`title_id`) REFERENCES `contacts_and_people_title` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts_and_people_personlite`
--

LOCK TABLES `contacts_and_people_personlite` WRITE;
/*!40000 ALTER TABLE `contacts_and_people_personlite` DISABLE KEYS */;
/*!40000 ALTER TABLE `contacts_and_people_personlite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacts_and_people_phonecontact`
--

DROP TABLE IF EXISTS `contacts_and_people_phonecontact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contacts_and_people_phonecontact` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `label` varchar(64) DEFAULT NULL,
  `country_code` varchar(5) NOT NULL,
  `area_code` varchar(5) NOT NULL,
  `number` varchar(12) NOT NULL,
  `internal_extension` varchar(6) DEFAULT NULL,
  `content_type_id` int(11) NOT NULL,
  `object_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `contacts_and_people_phonecontact_e4470c6e` (`content_type_id`),
  KEY `contacts_and_people_phonecontact_829e37fd` (`object_id`),
  CONSTRAINT `content_type_id_refs_id_67a4ad78` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts_and_people_phonecontact`
--

LOCK TABLES `contacts_and_people_phonecontact` WRITE;
/*!40000 ALTER TABLE `contacts_and_people_phonecontact` DISABLE KEYS */;
/*!40000 ALTER TABLE `contacts_and_people_phonecontact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacts_and_people_site`
--

DROP TABLE IF EXISTS `contacts_and_people_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contacts_and_people_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `site_name` varchar(50) NOT NULL,
  `post_town` varchar(50) NOT NULL,
  `country` varchar(50) NOT NULL,
  `description` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `site_name` (`site_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts_and_people_site`
--

LOCK TABLES `contacts_and_people_site` WRITE;
/*!40000 ALTER TABLE `contacts_and_people_site` DISABLE KEYS */;
/*!40000 ALTER TABLE `contacts_and_people_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacts_and_people_teacher`
--

DROP TABLE IF EXISTS `contacts_and_people_teacher`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contacts_and_people_teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `person_id` int(11) DEFAULT NULL,
  `dummy_field_one` varchar(100) DEFAULT NULL,
  `dummy_field_two` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `person_id` (`person_id`),
  CONSTRAINT `person_id_refs_personlite_ptr_id_e0a40e41` FOREIGN KEY (`person_id`) REFERENCES `contacts_and_people_person` (`personlite_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts_and_people_teacher`
--

LOCK TABLES `contacts_and_people_teacher` WRITE;
/*!40000 ALTER TABLE `contacts_and_people_teacher` DISABLE KEYS */;
/*!40000 ALTER TABLE `contacts_and_people_teacher` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `contacts_and_people_title`
--

DROP TABLE IF EXISTS `contacts_and_people_title`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `contacts_and_people_title` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `abbreviation` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `title` (`title`),
  UNIQUE KEY `abbreviation` (`abbreviation`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `contacts_and_people_title`
--

LOCK TABLES `contacts_and_people_title` WRITE;
/*!40000 ALTER TABLE `contacts_and_people_title` DISABLE KEYS */;
INSERT INTO `contacts_and_people_title` VALUES (1,'Prof','Prof'),(2,'Dr','Dr'),(3,'Ms','Ms'),(4,'Mr','Mr'),(5,'Mrs','Mrs'),(6,'Rev','Rev'),(7,'Miss','Miss');
/*!40000 ALTER TABLE `contacts_and_people_title` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_fbfc09f1` (`user_id`),
  KEY `django_admin_log_e4470c6e` (`content_type_id`),
  CONSTRAINT `user_id_refs_id_c8665aa` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `content_type_id_refs_id_288599e6` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2014-02-20 02:51:39',1,15,'1','Главная',1,''),(2,'2014-02-20 02:52:34',1,15,'1','Главная',2,'Изменен moderator_state.'),(3,'2014-02-20 03:04:50',1,15,'1','Главная',2,'Изменен published,in_navigation и moderator_state.'),(4,'2014-02-20 03:12:02',1,31,'1','default',1,''),(5,'2014-02-20 03:12:09',1,42,'1','Новость дня',1,''),(6,'2014-02-20 03:12:20',1,42,'1','Новость дня',2,'Изменен published и body.'),(7,'2014-02-20 03:13:17',1,15,'2','default-news',1,''),(8,'2014-02-20 03:13:22',1,15,'2','default-news',2,'Изменен moderator_state.'),(9,'2014-02-20 03:13:46',1,15,'2','default-news',2,'Изменен published,in_navigation и moderator_state.'),(10,'2014-02-20 03:14:19',1,15,'2','default-news',2,'Изменен slug и moderator_state.'),(11,'2014-02-20 03:14:38',1,15,'2','default-news',2,'Изменен title и moderator_state.'),(12,'2014-02-20 03:16:57',1,42,'1','Новость дня',2,'Изменен sticky_until,is_sticky_everywhere и body.'),(13,'2014-02-20 05:37:03',1,80,'1','as',1,''),(14,'2014-02-20 05:37:21',1,74,'4','c63c4a2cee556ab011801e389f20486d.jpeg',2,'Ни одно поле не изменено.'),(15,'2014-02-20 05:39:34',1,81,'2','sds',1,''),(16,'2014-02-20 05:39:38',1,81,'2','sds',2,'Ни одно поле не изменено.'),(17,'2014-02-20 05:39:47',1,81,'2','sds',2,'Изменен image.'),(18,'2014-02-20 06:20:13',1,85,'1','test',1,''),(19,'2014-02-20 06:20:27',1,85,'2','sssssssssssssssssssssssssssssssss',1,''),(20,'2014-02-20 06:21:35',1,82,'2','Иванов Иван Иванович',1,''),(21,'2014-02-20 06:25:23',1,82,'2','Иванов Иван Иванович',2,'Изменен types.'),(22,'2014-02-20 07:32:15',1,83,'1','Нет страховки',1,''),(23,'2014-02-20 07:33:32',1,80,'1','капитан',1,''),(24,'2014-02-20 07:33:44',1,84,'1','бомбардир',1,''),(25,'2014-02-20 07:33:46',1,81,'1','Пупкин Василий Васильевич',1,''),(26,'2014-02-20 07:34:17',1,81,'1','Пупкин Василий Васильевич',2,'Изменен role.'),(27,'2014-02-20 07:34:32',1,81,'1','Пупкин Василий Васильевич',2,'Изменен game_number.'),(28,'2014-02-20 07:35:50',1,87,'1','Лужники',1,''),(29,'2014-02-20 07:36:10',1,87,'1','Лужники',2,'Изменен street.'),(30,'2014-02-20 07:36:51',1,82,'2','Иванов Иван Иванович',2,'Изменен types.'),(31,'2014-02-20 07:38:42',1,85,'3','ФХМ',1,''),(32,'2014-02-20 07:38:44',1,85,'3','ФХМ',2,'Ни одно поле не изменено.'),(33,'2014-02-20 07:38:56',1,85,'4','МХЛ',1,''),(34,'2014-02-20 07:39:05',1,85,'5','ВХЛ',1,''),(35,'2014-02-20 07:39:08',1,85,'5','ВХЛ',2,'Ни одно поле не изменено.'),(36,'2014-02-20 07:39:19',1,85,'6','КХЛ',1,''),(37,'2014-02-20 07:39:36',1,82,'2','Иванов Иван Иванович',2,'Изменен types.'),(38,'2014-02-20 07:40:50',1,82,'3','Петров Петр Петрович',1,''),(39,'2014-02-20 07:41:24',1,86,'1','Арсеньев Арсений Арсениевич',1,''),(40,'2014-02-20 07:42:38',1,83,'2','Есть стаховка',1,''),(41,'2014-02-20 07:43:09',1,80,'2','врач',1,''),(42,'2014-02-20 07:43:21',1,84,'2','вратарь',1,''),(43,'2014-02-20 07:43:34',1,81,'2','Ашотов Ашот Ашотович',1,''),(44,'2014-02-20 07:44:25',1,88,'1','Крылья Советов',1,''),(45,'2014-02-20 07:45:04',1,89,'1','Training object',1,''),(46,'2014-02-20 07:45:12',1,89,'1','Training object',2,'Ни одно поле не изменено.');
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=90 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'carousel','cmsplugin_bootstrap_carousel','carousel'),(2,'carousel item','cmsplugin_bootstrap_carousel','carouselitem'),(3,'migration history','south','migrationhistory'),(4,'permission','auth','permission'),(5,'group','auth','group'),(6,'user','auth','user'),(7,'content type','contenttypes','contenttype'),(8,'session','sessions','session'),(9,'site','sites','site'),(10,'log entry','admin','logentry'),(11,'insert','arkestra_utilities','insert'),(12,'arkestra user','arkestra_utilities','arkestrauser'),(13,'placeholder','cms','placeholder'),(14,'cms plugin','cms','cmsplugin'),(15,'page','cms','page'),(16,'PageModerator','cms','pagemoderator'),(17,'Page moderator state','cms','pagemoderatorstate'),(18,'Page global permission','cms','globalpagepermission'),(19,'Page permission','cms','pagepermission'),(20,'User (page)','cms','pageuser'),(21,'User group (page)','cms','pageusergroup'),(22,'title','cms','title'),(23,'text','text','text'),(24,'Snippet','snippet','snippet'),(25,'Snippet','snippet','snippetptr'),(26,'cache key','menus','cachekey'),(27,'Сайт','contacts_and_people','site'),(28,'building','contacts_and_people','building'),(29,'phone contact','contacts_and_people','phonecontact'),(30,'entity lite','contacts_and_people','entitylite'),(31,'entity','contacts_and_people','entity'),(32,'title','contacts_and_people','title'),(33,'person lite','contacts_and_people','personlite'),(34,'person','contacts_and_people','person'),(35,'membership','contacts_and_people','membership'),(36,'entity auto page link plugin editor','contacts_and_people','entityautopagelinkplugineditor'),(37,'entity directory plugin editor','contacts_and_people','entitydirectoryplugineditor'),(38,'entity members plugin editor','contacts_and_people','entitymembersplugineditor'),(39,'vacancy','vacancies_and_studentships','vacancy'),(40,'studentship','vacancies_and_studentships','studentship'),(41,'vacancies plugin','vacancies_and_studentships','vacanciesplugin'),(42,'news article','news_and_events','newsarticle'),(43,'event','news_and_events','event'),(44,'event type','news_and_events','eventtype'),(45,'news source','news_and_events','newssource'),(46,'news and events plugin','news_and_events','newsandeventsplugin'),(47,'Link','links','objectlink'),(48,'generic link list plugin item','links','genericlinklistpluginitem'),(49,'external link','links','externallink'),(50,'link type','links','linktype'),(51,'domain','links','externalsite'),(52,'generic link list plugin','links','genericlinklistplugin'),(53,'carousel plugin','links','carouselplugin'),(54,'carousel plugin item','links','carouselpluginitem'),(55,'focus on plugin editor','links','focusonplugineditor'),(56,'focus on plugin item editor','links','focusonpluginitemeditor'),(57,'image set plugin','arkestra_image_plugin','imagesetplugin'),(58,'image set item','arkestra_image_plugin','imagesetitem'),(59,'embedded video set plugin','arkestra_image_plugin','embeddedvideosetplugin'),(60,'embedded video set item','arkestra_image_plugin','embeddedvideosetitem'),(61,'video','video','video'),(62,'video plugin editor','video','videoplugineditor'),(63,'video version','video','videoversion'),(64,'Video','video','arkestravideo'),(65,'CSS class category','semanticeditor','cssclasscategory'),(66,'CSS class','semanticeditor','cssclass'),(67,'source','easy_thumbnails','source'),(68,'thumbnail','easy_thumbnails','thumbnail'),(69,'Folder','filer','folder'),(70,'folder permission','filer','folderpermission'),(71,'file','filer','file'),(72,'clipboard','filer','clipboard'),(73,'clipboard item','filer','clipboarditem'),(74,'image','filer','image'),(75,'poll plugin','polls','pollplugin'),(76,'poll','polls','poll'),(77,'choice','polls','choice'),(78,'grizzly plugin','grizzly','grizzlyplugin'),(80,'player status','grizzly','playerstatus'),(81,'player','grizzly','player'),(82,'judge','grizzly','judge'),(83,'insurance type','grizzly','insurancetype'),(84,'player type','grizzly','playertype'),(85,'judge type','grizzly','judgetype'),(86,'trainer','grizzly','trainer'),(87,'rink','grizzly','rink'),(88,'team','grizzly','team'),(89,'training','grizzly','training');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_c25c2c28` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('efb08ba72875c41533d1287480e861d6','ZmRhMWYzODk5MGRiMjc2ZDQ4YmY0ZjkyNDlkZGU0ZTc2MWY3YTc5YzqAAn1xAShVDmNtc19hZG1p\nbl9zaXRligEBVQ1fYXV0aF91c2VyX2lkigEBVRJfYXV0aF91c2VyX2JhY2tlbmRVKWRqYW5nby5j\nb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kVRRmaWxlcl9sYXN0X2ZvbGRlcl9pZE51\nLg==\n','2014-03-06 08:44:07');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_site`
--

DROP TABLE IF EXISTS `django_site`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `django_site` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `domain` varchar(100) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_site`
--

LOCK TABLES `django_site` WRITE;
/*!40000 ALTER TABLE `django_site` DISABLE KEYS */;
INSERT INTO `django_site` VALUES (1,'example.com','example.com');
/*!40000 ALTER TABLE `django_site` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `easy_thumbnails_source`
--

DROP TABLE IF EXISTS `easy_thumbnails_source`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `easy_thumbnails_source` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `modified` datetime NOT NULL,
  `storage_hash` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `easy_thumbnails_source_name_7549c98cc6dd6969_uniq` (`name`,`storage_hash`),
  KEY `easy_thumbnails_source_52094d6e` (`name`),
  KEY `easy_thumbnails_source_3a997c55` (`storage_hash`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `easy_thumbnails_source`
--

LOCK TABLES `easy_thumbnails_source` WRITE;
/*!40000 ALTER TABLE `easy_thumbnails_source` DISABLE KEYS */;
INSERT INTO `easy_thumbnails_source` VALUES (1,'filer_public/f1/50/f150ddda-c683-46bb-851f-af631cea0fd4/shutterstock_79666759.jpg','2014-02-20 03:03:53','f9bde26a1556cd667f742bd34ec7c55e'),(2,'filer_public/a5/bf/a5bf4d8d-dc4c-4936-9119-6d1ee53a6c96/futuristic_city.jpg','2014-02-20 03:07:59','f9bde26a1556cd667f742bd34ec7c55e'),(3,'filer_public/9d/65/9d6598c2-2859-407e-b2fa-2ef7be00740f/pybasd-1-arch-1-res.png','2014-02-20 03:11:07','f9bde26a1556cd667f742bd34ec7c55e'),(4,'filer_public/08/68/08684ce2-5166-480e-bed6-6782dc46c848/c63c4a2cee556ab011801e389f20486d.jpeg','2014-02-20 03:11:43','f9bde26a1556cd667f742bd34ec7c55e'),(5,'filer_public/2a/89/2a8995ff-bbfe-4915-8e9a-20587dee6a73/0_b7_5b4281f6_l.gif','2014-02-20 07:32:08','f9bde26a1556cd667f742bd34ec7c55e'),(6,'filer_public/db/2a/db2ab6a5-90c4-40c1-9fd6-48d07734dead/t_7c2451b7e98547a7b5efc12cfd39f1d3.jpg','2014-02-20 07:32:30','f9bde26a1556cd667f742bd34ec7c55e'),(7,'filer_public/59/46/59460e47-653c-4da6-8c63-2d0bc84c2ffe/futurecity.jpg','2014-02-20 07:35:27','f9bde26a1556cd667f742bd34ec7c55e'),(8,'filer_public/93/a9/93a98250-f899-455d-bbfe-50150cbd28a4/claude_shannon6.jpg','2014-02-20 07:40:25','f9bde26a1556cd667f742bd34ec7c55e'),(9,'filer_public/56/6c/566c697c-9f85-48fe-8a45-37d82d1c925d/shutterstock_75527092.jpg','2014-02-20 07:42:31','f9bde26a1556cd667f742bd34ec7c55e');
/*!40000 ALTER TABLE `easy_thumbnails_source` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `easy_thumbnails_thumbnail`
--

DROP TABLE IF EXISTS `easy_thumbnails_thumbnail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `easy_thumbnails_thumbnail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `modified` datetime NOT NULL,
  `source_id` int(11) NOT NULL,
  `storage_hash` varchar(40) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `easy_thumbnails_thumbnail_source_id_1f50d53db8191480_uniq` (`source_id`,`name`,`storage_hash`),
  KEY `easy_thumbnails_thumbnail_89f89e85` (`source_id`),
  KEY `easy_thumbnails_thumbnail_52094d6e` (`name`),
  KEY `easy_thumbnails_thumbnail_3a997c55` (`storage_hash`),
  CONSTRAINT `source_id_refs_id_5bffe8f5` FOREIGN KEY (`source_id`) REFERENCES `easy_thumbnails_source` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=40 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `easy_thumbnails_thumbnail`
--

LOCK TABLES `easy_thumbnails_thumbnail` WRITE;
/*!40000 ALTER TABLE `easy_thumbnails_thumbnail` DISABLE KEYS */;
INSERT INTO `easy_thumbnails_thumbnail` VALUES (1,'filer_public_thumbnails/filer_public/f1/50/f150ddda-c683-46bb-851f-af631cea0fd4/shutterstock_79666759.jpg__32x32_q85_crop_upscale.jpg','2014-02-20 03:03:55',1,'f9bde26a1556cd667f742bd34ec7c55e'),(2,'filer_public_thumbnails/filer_public/f1/50/f150ddda-c683-46bb-851f-af631cea0fd4/shutterstock_79666759.jpg__64x64_q85_crop_upscale.jpg','2014-02-20 03:03:56',1,'f9bde26a1556cd667f742bd34ec7c55e'),(3,'filer_public_thumbnails/filer_public/f1/50/f150ddda-c683-46bb-851f-af631cea0fd4/shutterstock_79666759.jpg__48x48_q85_crop_upscale.jpg','2014-02-20 03:03:57',1,'f9bde26a1556cd667f742bd34ec7c55e'),(4,'filer_public_thumbnails/filer_public/f1/50/f150ddda-c683-46bb-851f-af631cea0fd4/shutterstock_79666759.jpg__16x16_q85_crop_upscale.jpg','2014-02-20 03:03:58',1,'f9bde26a1556cd667f742bd34ec7c55e'),(5,'filer_public_thumbnails/filer_public/a5/bf/a5bf4d8d-dc4c-4936-9119-6d1ee53a6c96/futuristic_city.jpg__32x32_q85_crop_upscale.jpg','2014-02-20 03:08:00',2,'f9bde26a1556cd667f742bd34ec7c55e'),(6,'filer_public_thumbnails/filer_public/a5/bf/a5bf4d8d-dc4c-4936-9119-6d1ee53a6c96/futuristic_city.jpg__64x64_q85_crop_upscale.jpg','2014-02-20 03:08:00',2,'f9bde26a1556cd667f742bd34ec7c55e'),(7,'filer_public_thumbnails/filer_public/a5/bf/a5bf4d8d-dc4c-4936-9119-6d1ee53a6c96/futuristic_city.jpg__48x48_q85_crop_upscale.jpg','2014-02-20 03:08:00',2,'f9bde26a1556cd667f742bd34ec7c55e'),(8,'filer_public_thumbnails/filer_public/a5/bf/a5bf4d8d-dc4c-4936-9119-6d1ee53a6c96/futuristic_city.jpg__16x16_q85_crop_upscale.jpg','2014-02-20 03:08:00',2,'f9bde26a1556cd667f742bd34ec7c55e'),(9,'filer_public_thumbnails/filer_public/9d/65/9d6598c2-2859-407e-b2fa-2ef7be00740f/pybasd-1-arch-1-res.png__32x32_q85_crop_upscale.jpg','2014-02-20 03:11:07',3,'f9bde26a1556cd667f742bd34ec7c55e'),(10,'filer_public_thumbnails/filer_public/9d/65/9d6598c2-2859-407e-b2fa-2ef7be00740f/pybasd-1-arch-1-res.png__64x64_q85_crop_upscale.jpg','2014-02-20 03:11:07',3,'f9bde26a1556cd667f742bd34ec7c55e'),(11,'filer_public_thumbnails/filer_public/9d/65/9d6598c2-2859-407e-b2fa-2ef7be00740f/pybasd-1-arch-1-res.png__48x48_q85_crop_upscale.jpg','2014-02-20 03:11:07',3,'f9bde26a1556cd667f742bd34ec7c55e'),(12,'filer_public_thumbnails/filer_public/9d/65/9d6598c2-2859-407e-b2fa-2ef7be00740f/pybasd-1-arch-1-res.png__16x16_q85_crop_upscale.jpg','2014-02-20 03:11:07',3,'f9bde26a1556cd667f742bd34ec7c55e'),(13,'filer_public_thumbnails/filer_public/08/68/08684ce2-5166-480e-bed6-6782dc46c848/c63c4a2cee556ab011801e389f20486d.jpeg__32x32_q85_crop_upscale.jpg','2014-02-20 03:11:43',4,'f9bde26a1556cd667f742bd34ec7c55e'),(14,'filer_public_thumbnails/filer_public/08/68/08684ce2-5166-480e-bed6-6782dc46c848/c63c4a2cee556ab011801e389f20486d.jpeg__64x64_q85_crop_upscale.jpg','2014-02-20 03:11:43',4,'f9bde26a1556cd667f742bd34ec7c55e'),(15,'filer_public_thumbnails/filer_public/08/68/08684ce2-5166-480e-bed6-6782dc46c848/c63c4a2cee556ab011801e389f20486d.jpeg__48x48_q85_crop_upscale.jpg','2014-02-20 03:11:43',4,'f9bde26a1556cd667f742bd34ec7c55e'),(16,'filer_public_thumbnails/filer_public/08/68/08684ce2-5166-480e-bed6-6782dc46c848/c63c4a2cee556ab011801e389f20486d.jpeg__16x16_q85_crop_upscale.jpg','2014-02-20 03:11:43',4,'f9bde26a1556cd667f742bd34ec7c55e'),(17,'filer_public_thumbnails/filer_public/9d/65/9d6598c2-2859-407e-b2fa-2ef7be00740f/pybasd-1-arch-1-res.png__75x75_q85_crop.jpg','2014-02-20 03:12:23',3,'f9bde26a1556cd667f742bd34ec7c55e'),(18,'filer_public_thumbnails/filer_public/9d/65/9d6598c2-2859-407e-b2fa-2ef7be00740f/pybasd-1-arch-1-res.png__294x196_q85_crop.jpg','2014-02-20 03:17:02',3,'f9bde26a1556cd667f742bd34ec7c55e'),(19,'filer_public_thumbnails/filer_public/08/68/08684ce2-5166-480e-bed6-6782dc46c848/c63c4a2cee556ab011801e389f20486d.jpeg__210x10000_q85.jpg','2014-02-20 05:37:19',4,'f9bde26a1556cd667f742bd34ec7c55e'),(20,'filer_public_thumbnails/filer_public/2a/89/2a8995ff-bbfe-4915-8e9a-20587dee6a73/0_b7_5b4281f6_l.gif__32x32_q85_crop_upscale.jpg','2014-02-20 07:32:08',5,'f9bde26a1556cd667f742bd34ec7c55e'),(21,'filer_public_thumbnails/filer_public/2a/89/2a8995ff-bbfe-4915-8e9a-20587dee6a73/0_b7_5b4281f6_l.gif__64x64_q85_crop_upscale.jpg','2014-02-20 07:32:08',5,'f9bde26a1556cd667f742bd34ec7c55e'),(22,'filer_public_thumbnails/filer_public/2a/89/2a8995ff-bbfe-4915-8e9a-20587dee6a73/0_b7_5b4281f6_l.gif__48x48_q85_crop_upscale.jpg','2014-02-20 07:32:08',5,'f9bde26a1556cd667f742bd34ec7c55e'),(23,'filer_public_thumbnails/filer_public/2a/89/2a8995ff-bbfe-4915-8e9a-20587dee6a73/0_b7_5b4281f6_l.gif__16x16_q85_crop_upscale.jpg','2014-02-20 07:32:08',5,'f9bde26a1556cd667f742bd34ec7c55e'),(24,'filer_public_thumbnails/filer_public/db/2a/db2ab6a5-90c4-40c1-9fd6-48d07734dead/t_7c2451b7e98547a7b5efc12cfd39f1d3.jpg__32x32_q85_crop_upscale.jpg','2014-02-20 07:32:30',6,'f9bde26a1556cd667f742bd34ec7c55e'),(25,'filer_public_thumbnails/filer_public/db/2a/db2ab6a5-90c4-40c1-9fd6-48d07734dead/t_7c2451b7e98547a7b5efc12cfd39f1d3.jpg__64x64_q85_crop_upscale.jpg','2014-02-20 07:32:30',6,'f9bde26a1556cd667f742bd34ec7c55e'),(26,'filer_public_thumbnails/filer_public/db/2a/db2ab6a5-90c4-40c1-9fd6-48d07734dead/t_7c2451b7e98547a7b5efc12cfd39f1d3.jpg__48x48_q85_crop_upscale.jpg','2014-02-20 07:32:30',6,'f9bde26a1556cd667f742bd34ec7c55e'),(27,'filer_public_thumbnails/filer_public/db/2a/db2ab6a5-90c4-40c1-9fd6-48d07734dead/t_7c2451b7e98547a7b5efc12cfd39f1d3.jpg__16x16_q85_crop_upscale.jpg','2014-02-20 07:32:31',6,'f9bde26a1556cd667f742bd34ec7c55e'),(28,'filer_public_thumbnails/filer_public/59/46/59460e47-653c-4da6-8c63-2d0bc84c2ffe/futurecity.jpg__32x32_q85_crop_upscale.jpg','2014-02-20 07:35:28',7,'f9bde26a1556cd667f742bd34ec7c55e'),(29,'filer_public_thumbnails/filer_public/59/46/59460e47-653c-4da6-8c63-2d0bc84c2ffe/futurecity.jpg__64x64_q85_crop_upscale.jpg','2014-02-20 07:35:28',7,'f9bde26a1556cd667f742bd34ec7c55e'),(30,'filer_public_thumbnails/filer_public/59/46/59460e47-653c-4da6-8c63-2d0bc84c2ffe/futurecity.jpg__48x48_q85_crop_upscale.jpg','2014-02-20 07:35:29',7,'f9bde26a1556cd667f742bd34ec7c55e'),(31,'filer_public_thumbnails/filer_public/59/46/59460e47-653c-4da6-8c63-2d0bc84c2ffe/futurecity.jpg__16x16_q85_crop_upscale.jpg','2014-02-20 07:35:29',7,'f9bde26a1556cd667f742bd34ec7c55e'),(32,'filer_public_thumbnails/filer_public/93/a9/93a98250-f899-455d-bbfe-50150cbd28a4/claude_shannon6.jpg__32x32_q85_crop_upscale.jpg','2014-02-20 07:40:25',8,'f9bde26a1556cd667f742bd34ec7c55e'),(33,'filer_public_thumbnails/filer_public/93/a9/93a98250-f899-455d-bbfe-50150cbd28a4/claude_shannon6.jpg__64x64_q85_crop_upscale.jpg','2014-02-20 07:40:25',8,'f9bde26a1556cd667f742bd34ec7c55e'),(34,'filer_public_thumbnails/filer_public/93/a9/93a98250-f899-455d-bbfe-50150cbd28a4/claude_shannon6.jpg__48x48_q85_crop_upscale.jpg','2014-02-20 07:40:25',8,'f9bde26a1556cd667f742bd34ec7c55e'),(35,'filer_public_thumbnails/filer_public/93/a9/93a98250-f899-455d-bbfe-50150cbd28a4/claude_shannon6.jpg__16x16_q85_crop_upscale.jpg','2014-02-20 07:40:25',8,'f9bde26a1556cd667f742bd34ec7c55e'),(36,'filer_public_thumbnails/filer_public/56/6c/566c697c-9f85-48fe-8a45-37d82d1c925d/shutterstock_75527092.jpg__32x32_q85_crop_upscale.jpg','2014-02-20 07:42:31',9,'f9bde26a1556cd667f742bd34ec7c55e'),(37,'filer_public_thumbnails/filer_public/56/6c/566c697c-9f85-48fe-8a45-37d82d1c925d/shutterstock_75527092.jpg__64x64_q85_crop_upscale.jpg','2014-02-20 07:42:32',9,'f9bde26a1556cd667f742bd34ec7c55e'),(38,'filer_public_thumbnails/filer_public/56/6c/566c697c-9f85-48fe-8a45-37d82d1c925d/shutterstock_75527092.jpg__48x48_q85_crop_upscale.jpg','2014-02-20 07:42:32',9,'f9bde26a1556cd667f742bd34ec7c55e'),(39,'filer_public_thumbnails/filer_public/56/6c/566c697c-9f85-48fe-8a45-37d82d1c925d/shutterstock_75527092.jpg__16x16_q85_crop_upscale.jpg','2014-02-20 07:42:32',9,'f9bde26a1556cd667f742bd34ec7c55e');
/*!40000 ALTER TABLE `easy_thumbnails_thumbnail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `filer_clipboard`
--

DROP TABLE IF EXISTS `filer_clipboard`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `filer_clipboard` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `filer_clipboard_fbfc09f1` (`user_id`),
  CONSTRAINT `user_id_refs_id_e9ec83e0` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `filer_clipboard`
--

LOCK TABLES `filer_clipboard` WRITE;
/*!40000 ALTER TABLE `filer_clipboard` DISABLE KEYS */;
INSERT INTO `filer_clipboard` VALUES (1,1);
/*!40000 ALTER TABLE `filer_clipboard` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `filer_clipboarditem`
--

DROP TABLE IF EXISTS `filer_clipboarditem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `filer_clipboarditem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `file_id` int(11) NOT NULL,
  `clipboard_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `filer_clipboarditem_2243e3be` (`file_id`),
  KEY `filer_clipboarditem_a22db775` (`clipboard_id`),
  CONSTRAINT `clipboard_id_refs_id_46496bc2` FOREIGN KEY (`clipboard_id`) REFERENCES `filer_clipboard` (`id`),
  CONSTRAINT `file_id_refs_id_3533711` FOREIGN KEY (`file_id`) REFERENCES `filer_file` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `filer_clipboarditem`
--

LOCK TABLES `filer_clipboarditem` WRITE;
/*!40000 ALTER TABLE `filer_clipboarditem` DISABLE KEYS */;
INSERT INTO `filer_clipboarditem` VALUES (1,1,1),(2,2,1),(3,3,1),(4,4,1),(5,5,1),(6,6,1),(7,7,1),(8,8,1),(9,9,1);
/*!40000 ALTER TABLE `filer_clipboarditem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `filer_file`
--

DROP TABLE IF EXISTS `filer_file`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `filer_file` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `folder_id` int(11) DEFAULT NULL,
  `file` varchar(255),
  `_file_size` int(11) DEFAULT NULL,
  `has_all_mandatory_data` tinyint(1) NOT NULL,
  `original_filename` varchar(255) DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `owner_id` int(11) DEFAULT NULL,
  `uploaded_at` datetime NOT NULL,
  `modified_at` datetime NOT NULL,
  `description` longtext,
  `is_public` tinyint(1) NOT NULL,
  `sha1` varchar(40) NOT NULL,
  `polymorphic_ctype_id` int(11),
  PRIMARY KEY (`id`),
  KEY `filer_file_4e5f642` (`folder_id`),
  KEY `filer_file_5d52dd10` (`owner_id`),
  KEY `filer_file_97604479` (`polymorphic_ctype_id`),
  CONSTRAINT `folder_id_refs_id_5276dead` FOREIGN KEY (`folder_id`) REFERENCES `filer_folder` (`id`),
  CONSTRAINT `owner_id_refs_id_95417f77` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `polymorphic_ctype_id_refs_id_d63e96cb` FOREIGN KEY (`polymorphic_ctype_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `filer_file`
--

LOCK TABLES `filer_file` WRITE;
/*!40000 ALTER TABLE `filer_file` DISABLE KEYS */;
INSERT INTO `filer_file` VALUES (1,NULL,'filer_public/f1/50/f150ddda-c683-46bb-851f-af631cea0fd4/shutterstock_79666759.jpg',4370255,0,'shutterstock_79666759.jpg','',1,'2014-02-20 03:03:53','2014-02-20 03:03:53',NULL,1,'d4d06c2bdfa77adc04f1ae273f3677dd5a37d4f7',74),(2,NULL,'filer_public/a5/bf/a5bf4d8d-dc4c-4936-9119-6d1ee53a6c96/futuristic_city.jpg',767818,0,'futuristic_city.jpg','',1,'2014-02-20 03:07:59','2014-02-20 03:07:59',NULL,1,'31926e76226d2fd51f3447f5d35e3093cc413639',74),(3,NULL,'filer_public/9d/65/9d6598c2-2859-407e-b2fa-2ef7be00740f/pybasd-1-arch-1-res.png',12801,0,'pybasd-1-arch-1-res.png','',1,'2014-02-20 03:11:07','2014-02-20 03:11:07',NULL,1,'46b615f321512fe6bf1e61926ac2af72a95b0a4c',74),(4,NULL,'filer_public/08/68/08684ce2-5166-480e-bed6-6782dc46c848/c63c4a2cee556ab011801e389f20486d.jpeg',29594,0,'c63c4a2cee556ab011801e389f20486d.jpeg','',1,'2014-02-20 03:11:43','2014-02-20 05:37:21','',1,'20343c4378be89ab6effbc810d5ec2f62e86a746',74),(5,NULL,'filer_public/2a/89/2a8995ff-bbfe-4915-8e9a-20587dee6a73/0_b7_5b4281f6_l.gif',783033,0,'0_b7_5b4281f6_L.gif','',1,'2014-02-20 07:32:08','2014-02-20 07:32:08',NULL,1,'808d8f2ded0b752d8d53de6c8812e32bcaaa3e78',74),(6,NULL,'filer_public/db/2a/db2ab6a5-90c4-40c1-9fd6-48d07734dead/t_7c2451b7e98547a7b5efc12cfd39f1d3.jpg',28469,0,'t_7c2451b7e98547a7b5efc12cfd39f1d3.jpg','',1,'2014-02-20 07:32:30','2014-02-20 07:32:30',NULL,1,'3060ce98943b485fa2f637d0c039027cdc3e2728',74),(7,NULL,'filer_public/59/46/59460e47-653c-4da6-8c63-2d0bc84c2ffe/futurecity.jpg',617092,0,'futurecity.jpg','',1,'2014-02-20 07:35:27','2014-02-20 07:35:27',NULL,1,'7a739cbfd2484316d77a934972be350f16d5de99',74),(8,NULL,'filer_public/93/a9/93a98250-f899-455d-bbfe-50150cbd28a4/claude_shannon6.jpg',39637,0,'claude_shannon6.jpg','',1,'2014-02-20 07:40:25','2014-02-20 07:40:25',NULL,1,'1cf6e392057744e49023be4afae0b3cdaeec19cc',74),(9,NULL,'filer_public/56/6c/566c697c-9f85-48fe-8a45-37d82d1c925d/shutterstock_75527092.jpg',394305,0,'shutterstock_75527092.jpg','',1,'2014-02-20 07:42:31','2014-02-20 07:42:31',NULL,1,'a74c5e42f408ac6846566f1f6ebd7619c96474cc',74);
/*!40000 ALTER TABLE `filer_file` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `filer_folder`
--

DROP TABLE IF EXISTS `filer_folder`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `filer_folder` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `parent_id` int(11) DEFAULT NULL,
  `name` varchar(255) NOT NULL,
  `owner_id` int(11) DEFAULT NULL,
  `uploaded_at` datetime NOT NULL,
  `created_at` datetime NOT NULL,
  `modified_at` datetime NOT NULL,
  `lft` int(10) unsigned NOT NULL,
  `rght` int(10) unsigned NOT NULL,
  `tree_id` int(10) unsigned NOT NULL,
  `level` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `filer_folder_parent_id_30ad83e34d901e49_uniq` (`parent_id`,`name`),
  KEY `filer_folder_63f17a16` (`parent_id`),
  KEY `filer_folder_5d52dd10` (`owner_id`),
  KEY `filer_folder_42b06ff6` (`lft`),
  KEY `filer_folder_91543e5a` (`rght`),
  KEY `filer_folder_efd07f28` (`tree_id`),
  KEY `filer_folder_2a8f42e8` (`level`),
  CONSTRAINT `owner_id_refs_id_4709f467` FOREIGN KEY (`owner_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `parent_id_refs_id_60f1d8bd` FOREIGN KEY (`parent_id`) REFERENCES `filer_folder` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `filer_folder`
--

LOCK TABLES `filer_folder` WRITE;
/*!40000 ALTER TABLE `filer_folder` DISABLE KEYS */;
/*!40000 ALTER TABLE `filer_folder` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `filer_folderpermission`
--

DROP TABLE IF EXISTS `filer_folderpermission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `filer_folderpermission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `folder_id` int(11) DEFAULT NULL,
  `type` smallint(6) NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  `group_id` int(11) DEFAULT NULL,
  `everybody` tinyint(1) NOT NULL,
  `can_edit` smallint(6) DEFAULT NULL,
  `can_read` smallint(6) DEFAULT NULL,
  `can_add_children` smallint(6) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `filer_folderpermission_4e5f642` (`folder_id`),
  KEY `filer_folderpermission_fbfc09f1` (`user_id`),
  KEY `filer_folderpermission_bda51c3c` (`group_id`),
  CONSTRAINT `folder_id_refs_id_565b7e06` FOREIGN KEY (`folder_id`) REFERENCES `filer_folder` (`id`),
  CONSTRAINT `group_id_refs_id_91cff1c5` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `user_id_refs_id_4ab53c64` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `filer_folderpermission`
--

LOCK TABLES `filer_folderpermission` WRITE;
/*!40000 ALTER TABLE `filer_folderpermission` DISABLE KEYS */;
/*!40000 ALTER TABLE `filer_folderpermission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `filer_image`
--

DROP TABLE IF EXISTS `filer_image`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `filer_image` (
  `file_ptr_id` int(11) NOT NULL,
  `_height` int(11) DEFAULT NULL,
  `_width` int(11) DEFAULT NULL,
  `date_taken` datetime DEFAULT NULL,
  `default_alt_text` varchar(255) DEFAULT NULL,
  `default_caption` varchar(255) DEFAULT NULL,
  `author` varchar(255) DEFAULT NULL,
  `must_always_publish_author_credit` tinyint(1) NOT NULL,
  `must_always_publish_copyright` tinyint(1) NOT NULL,
  `subject_location` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`file_ptr_id`),
  CONSTRAINT `file_ptr_id_refs_id_d8c3bde1` FOREIGN KEY (`file_ptr_id`) REFERENCES `filer_file` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `filer_image`
--

LOCK TABLES `filer_image` WRITE;
/*!40000 ALTER TABLE `filer_image` DISABLE KEYS */;
INSERT INTO `filer_image` VALUES (1,2703,2703,'2014-02-20 03:03:53',NULL,NULL,NULL,0,0,NULL),(2,700,1500,'2014-02-20 03:07:59',NULL,NULL,NULL,0,0,NULL),(3,544,344,'2014-02-20 03:11:07',NULL,NULL,NULL,0,0,NULL),(4,420,420,'2014-02-20 03:11:43','','',NULL,0,0,''),(5,281,500,'2014-02-20 07:32:08',NULL,NULL,NULL,0,0,NULL),(6,300,300,'2014-02-20 07:32:30',NULL,NULL,NULL,0,0,NULL),(7,1200,1920,'2014-02-20 07:35:27',NULL,NULL,NULL,0,0,NULL),(8,452,400,'2014-02-20 07:40:25',NULL,NULL,NULL,0,0,NULL),(9,669,1000,'2014-02-20 07:42:31',NULL,NULL,NULL,0,0,NULL);
/*!40000 ALTER TABLE `filer_image` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grizzly_insurancetype`
--

DROP TABLE IF EXISTS `grizzly_insurancetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grizzly_insurancetype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `description` longtext,
  `image_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `grizzly_insurancetype_6682136` (`image_id`),
  CONSTRAINT `image_id_refs_file_ptr_id_aa955dad` FOREIGN KEY (`image_id`) REFERENCES `filer_image` (`file_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grizzly_insurancetype`
--

LOCK TABLES `grizzly_insurancetype` WRITE;
/*!40000 ALTER TABLE `grizzly_insurancetype` DISABLE KEYS */;
/*!40000 ALTER TABLE `grizzly_insurancetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grizzly_judge`
--

DROP TABLE IF EXISTS `grizzly_judge`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grizzly_judge` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(200) NOT NULL,
  `patronymic` varchar(200) NOT NULL,
  `second_name` varchar(200) NOT NULL,
  `birthday` date NOT NULL,
  `image_id` int(11) DEFAULT NULL,
  `description` longtext,
  PRIMARY KEY (`id`),
  KEY `grizzly_judge_6682136` (`image_id`),
  CONSTRAINT `image_id_refs_file_ptr_id_b60b6d78` FOREIGN KEY (`image_id`) REFERENCES `filer_image` (`file_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grizzly_judge`
--

LOCK TABLES `grizzly_judge` WRITE;
/*!40000 ALTER TABLE `grizzly_judge` DISABLE KEYS */;
/*!40000 ALTER TABLE `grizzly_judge` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grizzly_judge_types`
--

DROP TABLE IF EXISTS `grizzly_judge_types`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grizzly_judge_types` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `judge_id` int(11) NOT NULL,
  `judgetype_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `grizzly_judge_types_judge_id_22f44a05bcdacec2_uniq` (`judge_id`,`judgetype_id`),
  KEY `grizzly_judge_types_bcb024b0` (`judge_id`),
  KEY `grizzly_judge_types_f613d214` (`judgetype_id`),
  CONSTRAINT `judgetype_id_refs_id_6129de37` FOREIGN KEY (`judgetype_id`) REFERENCES `grizzly_judgetype` (`id`),
  CONSTRAINT `judge_id_refs_id_e4e94d03` FOREIGN KEY (`judge_id`) REFERENCES `grizzly_judge` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grizzly_judge_types`
--

LOCK TABLES `grizzly_judge_types` WRITE;
/*!40000 ALTER TABLE `grizzly_judge_types` DISABLE KEYS */;
/*!40000 ALTER TABLE `grizzly_judge_types` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grizzly_judgetype`
--

DROP TABLE IF EXISTS `grizzly_judgetype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grizzly_judgetype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `description` longtext,
  `image_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `grizzly_judgetype_6682136` (`image_id`),
  CONSTRAINT `image_id_refs_file_ptr_id_f9b6556c` FOREIGN KEY (`image_id`) REFERENCES `filer_image` (`file_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grizzly_judgetype`
--

LOCK TABLES `grizzly_judgetype` WRITE;
/*!40000 ALTER TABLE `grizzly_judgetype` DISABLE KEYS */;
/*!40000 ALTER TABLE `grizzly_judgetype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grizzly_player`
--

DROP TABLE IF EXISTS `grizzly_player`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grizzly_player` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(200) NOT NULL,
  `patronymic` varchar(200) NOT NULL,
  `second_name` varchar(200) NOT NULL,
  `birthday` date NOT NULL,
  `image_id` int(11) DEFAULT NULL,
  `insurance_type_id` int(11) DEFAULT NULL,
  `description` longtext,
  `height` int(11) NOT NULL,
  `weight` int(11) NOT NULL,
  `game_number` varchar(200) NOT NULL,
  `role` varchar(200) NOT NULL,
  `qualification` longtext NOT NULL,
  `status_id` int(11) DEFAULT NULL,
  `type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `grizzly_player_6682136` (`image_id`),
  KEY `grizzly_player_58f1ced7` (`insurance_type_id`),
  KEY `grizzly_player_44224078` (`status_id`),
  KEY `grizzly_player_777d41c8` (`type_id`),
  CONSTRAINT `type_id_refs_id_f8ac01f1` FOREIGN KEY (`type_id`) REFERENCES `grizzly_playertype` (`id`),
  CONSTRAINT `image_id_refs_file_ptr_id_f5f40d03` FOREIGN KEY (`image_id`) REFERENCES `filer_image` (`file_ptr_id`),
  CONSTRAINT `insurance_type_id_refs_id_edbabdd3` FOREIGN KEY (`insurance_type_id`) REFERENCES `grizzly_insurancetype` (`id`),
  CONSTRAINT `status_id_refs_id_deb34a5` FOREIGN KEY (`status_id`) REFERENCES `grizzly_playerstatus` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grizzly_player`
--

LOCK TABLES `grizzly_player` WRITE;
/*!40000 ALTER TABLE `grizzly_player` DISABLE KEYS */;
/*!40000 ALTER TABLE `grizzly_player` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grizzly_playerstatus`
--

DROP TABLE IF EXISTS `grizzly_playerstatus`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grizzly_playerstatus` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `description` longtext,
  `image_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `grizzly_playerstatus_6682136` (`image_id`),
  CONSTRAINT `image_id_refs_file_ptr_id_380069eb` FOREIGN KEY (`image_id`) REFERENCES `filer_image` (`file_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grizzly_playerstatus`
--

LOCK TABLES `grizzly_playerstatus` WRITE;
/*!40000 ALTER TABLE `grizzly_playerstatus` DISABLE KEYS */;
/*!40000 ALTER TABLE `grizzly_playerstatus` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grizzly_playertype`
--

DROP TABLE IF EXISTS `grizzly_playertype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grizzly_playertype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `description` longtext,
  `image_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `grizzly_playertype_6682136` (`image_id`),
  CONSTRAINT `image_id_refs_file_ptr_id_4a26bba7` FOREIGN KEY (`image_id`) REFERENCES `filer_image` (`file_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grizzly_playertype`
--

LOCK TABLES `grizzly_playertype` WRITE;
/*!40000 ALTER TABLE `grizzly_playertype` DISABLE KEYS */;
/*!40000 ALTER TABLE `grizzly_playertype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grizzly_rink`
--

DROP TABLE IF EXISTS `grizzly_rink`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grizzly_rink` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `description` longtext,
  `image_id` int(11) DEFAULT NULL,
  `birthday` datetime NOT NULL,
  `town` varchar(200) NOT NULL,
  `street` varchar(200) NOT NULL,
  `house` varchar(200) NOT NULL,
  `building` varchar(200) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `grizzly_rink_6682136` (`image_id`),
  CONSTRAINT `image_id_refs_file_ptr_id_7c4fed5a` FOREIGN KEY (`image_id`) REFERENCES `filer_image` (`file_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grizzly_rink`
--

LOCK TABLES `grizzly_rink` WRITE;
/*!40000 ALTER TABLE `grizzly_rink` DISABLE KEYS */;
/*!40000 ALTER TABLE `grizzly_rink` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grizzly_team`
--

DROP TABLE IF EXISTS `grizzly_team`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grizzly_team` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) NOT NULL,
  `description` longtext,
  `image_id` int(11) DEFAULT NULL,
  `birthday` date NOT NULL,
  PRIMARY KEY (`id`),
  KEY `grizzly_team_6682136` (`image_id`),
  CONSTRAINT `image_id_refs_file_ptr_id_f7548e09` FOREIGN KEY (`image_id`) REFERENCES `filer_image` (`file_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grizzly_team`
--

LOCK TABLES `grizzly_team` WRITE;
/*!40000 ALTER TABLE `grizzly_team` DISABLE KEYS */;
/*!40000 ALTER TABLE `grizzly_team` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grizzly_team_players`
--

DROP TABLE IF EXISTS `grizzly_team_players`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grizzly_team_players` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `team_id` int(11) NOT NULL,
  `player_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `grizzly_team_players_team_id_4536b448cc36efe0_uniq` (`team_id`,`player_id`),
  KEY `grizzly_team_players_fcf8ac47` (`team_id`),
  KEY `grizzly_team_players_ea2d1965` (`player_id`),
  CONSTRAINT `player_id_refs_id_e2f96d14` FOREIGN KEY (`player_id`) REFERENCES `grizzly_player` (`id`),
  CONSTRAINT `team_id_refs_id_ce7c249e` FOREIGN KEY (`team_id`) REFERENCES `grizzly_team` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grizzly_team_players`
--

LOCK TABLES `grizzly_team_players` WRITE;
/*!40000 ALTER TABLE `grizzly_team_players` DISABLE KEYS */;
/*!40000 ALTER TABLE `grizzly_team_players` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grizzly_trainer`
--

DROP TABLE IF EXISTS `grizzly_trainer`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grizzly_trainer` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `first_name` varchar(200) NOT NULL,
  `patronymic` varchar(200) NOT NULL,
  `second_name` varchar(200) NOT NULL,
  `birthday` date NOT NULL,
  `image_id` int(11) DEFAULT NULL,
  `description` longtext,
  PRIMARY KEY (`id`),
  KEY `grizzly_trainer_6682136` (`image_id`),
  CONSTRAINT `image_id_refs_file_ptr_id_855e32e0` FOREIGN KEY (`image_id`) REFERENCES `filer_image` (`file_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grizzly_trainer`
--

LOCK TABLES `grizzly_trainer` WRITE;
/*!40000 ALTER TABLE `grizzly_trainer` DISABLE KEYS */;
/*!40000 ALTER TABLE `grizzly_trainer` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `grizzly_training`
--

DROP TABLE IF EXISTS `grizzly_training`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `grizzly_training` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(200) DEFAULT NULL,
  `description` longtext,
  `image_id` int(11) DEFAULT NULL,
  `team_id` int(11) DEFAULT NULL,
  `rink_id` int(11) DEFAULT NULL,
  `trainer_id` int(11) DEFAULT NULL,
  `date` date NOT NULL,
  `start_time` time NOT NULL,
  `stop_time` time NOT NULL,
  `price` int(11) NOT NULL,
  `loan` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `grizzly_training_6682136` (`image_id`),
  KEY `grizzly_training_fcf8ac47` (`team_id`),
  KEY `grizzly_training_fa5e043e` (`rink_id`),
  KEY `grizzly_training_c207bcac` (`trainer_id`),
  CONSTRAINT `trainer_id_refs_id_c677d73f` FOREIGN KEY (`trainer_id`) REFERENCES `grizzly_trainer` (`id`),
  CONSTRAINT `image_id_refs_file_ptr_id_d7e54962` FOREIGN KEY (`image_id`) REFERENCES `filer_image` (`file_ptr_id`),
  CONSTRAINT `rink_id_refs_id_7f5690a3` FOREIGN KEY (`rink_id`) REFERENCES `grizzly_rink` (`id`),
  CONSTRAINT `team_id_refs_id_68a55080` FOREIGN KEY (`team_id`) REFERENCES `grizzly_team` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `grizzly_training`
--

LOCK TABLES `grizzly_training` WRITE;
/*!40000 ALTER TABLE `grizzly_training` DISABLE KEYS */;
/*!40000 ALTER TABLE `grizzly_training` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `links_carouselpluginitem`
--

DROP TABLE IF EXISTS `links_carouselpluginitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `links_carouselpluginitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `destination_content_type_id` int(11) NOT NULL,
  `destination_object_id` int(10) unsigned NOT NULL,
  `plugin_id` int(11) NOT NULL,
  `image_id` int(11) NOT NULL,
  `link_title` varchar(35) NOT NULL,
  `inline_item_ordering` smallint(5) unsigned NOT NULL,
  `active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `links_carouselpluginitem_a1ae9087` (`destination_content_type_id`),
  KEY `links_carouselpluginitem_2857ccbf` (`plugin_id`),
  KEY `links_carouselpluginitem_6682136` (`image_id`),
  CONSTRAINT `destination_content_type_id_refs_id_e1e5b2cc` FOREIGN KEY (`destination_content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `image_id_refs_file_ptr_id_29e83b08` FOREIGN KEY (`image_id`) REFERENCES `filer_image` (`file_ptr_id`),
  CONSTRAINT `plugin_id_refs_cmsplugin_ptr_id_aa15ea5f` FOREIGN KEY (`plugin_id`) REFERENCES `cmsplugin_carouselplugin` (`cmsplugin_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `links_carouselpluginitem`
--

LOCK TABLES `links_carouselpluginitem` WRITE;
/*!40000 ALTER TABLE `links_carouselpluginitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `links_carouselpluginitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `links_externallink`
--

DROP TABLE IF EXISTS `links_externallink`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `links_externallink` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(256) NOT NULL,
  `url` varchar(255) NOT NULL,
  `external_site_id` int(11),
  `description` longtext,
  `kind_id` int(11),
  PRIMARY KEY (`id`),
  KEY `links_externallink_e4cb7c2c` (`external_site_id`),
  KEY `links_externallink_e52ac752` (`kind_id`),
  CONSTRAINT `external_site_id_refs_id_a92dcba` FOREIGN KEY (`external_site_id`) REFERENCES `links_externalsite` (`id`),
  CONSTRAINT `kind_id_refs_id_287ce282` FOREIGN KEY (`kind_id`) REFERENCES `links_linktype` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `links_externallink`
--

LOCK TABLES `links_externallink` WRITE;
/*!40000 ALTER TABLE `links_externallink` DISABLE KEYS */;
/*!40000 ALTER TABLE `links_externallink` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `links_externalsite`
--

DROP TABLE IF EXISTS `links_externalsite`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `links_externalsite` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `site` varchar(50) DEFAULT NULL,
  `domain` varchar(256) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `lft` int(10) unsigned NOT NULL,
  `rght` int(10) unsigned NOT NULL,
  `tree_id` int(10) unsigned NOT NULL,
  `level` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  KEY `links_externalsite_63f17a16` (`parent_id`),
  KEY `links_externalsite_42b06ff6` (`lft`),
  KEY `links_externalsite_91543e5a` (`rght`),
  KEY `links_externalsite_efd07f28` (`tree_id`),
  KEY `links_externalsite_2a8f42e8` (`level`),
  CONSTRAINT `parent_id_refs_id_b6fec16b` FOREIGN KEY (`parent_id`) REFERENCES `links_externalsite` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `links_externalsite`
--

LOCK TABLES `links_externalsite` WRITE;
/*!40000 ALTER TABLE `links_externalsite` DISABLE KEYS */;
/*!40000 ALTER TABLE `links_externalsite` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `links_focusonpluginitemeditor`
--

DROP TABLE IF EXISTS `links_focusonpluginitemeditor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `links_focusonpluginitemeditor` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `destination_content_type_id` int(11) NOT NULL,
  `destination_object_id` int(10) unsigned NOT NULL,
  `plugin_id` int(11) NOT NULL,
  `text_override` varchar(256) DEFAULT NULL,
  `short_text_override` varchar(256) DEFAULT NULL,
  `description_override` longtext,
  `image_override_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `links_focusonpluginitemeditor_a1ae9087` (`destination_content_type_id`),
  KEY `links_focusonpluginitemeditor_2857ccbf` (`plugin_id`),
  KEY `links_focusonpluginitemeditor_a677f154` (`image_override_id`),
  CONSTRAINT `image_override_id_refs_file_ptr_id_be6f67` FOREIGN KEY (`image_override_id`) REFERENCES `filer_image` (`file_ptr_id`),
  CONSTRAINT `destination_content_type_id_refs_id_2a02c06d` FOREIGN KEY (`destination_content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `plugin_id_refs_cmsplugin_ptr_id_943b9491` FOREIGN KEY (`plugin_id`) REFERENCES `cmsplugin_focusonplugineditor` (`cmsplugin_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `links_focusonpluginitemeditor`
--

LOCK TABLES `links_focusonpluginitemeditor` WRITE;
/*!40000 ALTER TABLE `links_focusonpluginitemeditor` DISABLE KEYS */;
/*!40000 ALTER TABLE `links_focusonpluginitemeditor` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `links_genericlinklistpluginitem`
--

DROP TABLE IF EXISTS `links_genericlinklistpluginitem`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `links_genericlinklistpluginitem` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `destination_content_type_id` int(11) NOT NULL,
  `destination_object_id` int(10) unsigned NOT NULL,
  `include_description` tinyint(1) NOT NULL,
  `text_override` varchar(256) DEFAULT NULL,
  `description_override` longtext,
  `heading_override` varchar(256) DEFAULT NULL,
  `metadata_override` varchar(256) DEFAULT NULL,
  `html_title_attribute` varchar(256) DEFAULT NULL,
  `plugin_id` int(11) NOT NULL,
  `key_link` tinyint(1) NOT NULL,
  `inline_item_ordering` smallint(5) unsigned NOT NULL,
  `active` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `links_genericlinklistpluginitem_a1ae9087` (`destination_content_type_id`),
  KEY `links_genericlinklistpluginitem_2857ccbf` (`plugin_id`),
  CONSTRAINT `destination_content_type_id_refs_id_f025d9b6` FOREIGN KEY (`destination_content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `plugin_id_refs_cmsplugin_ptr_id_14237479` FOREIGN KEY (`plugin_id`) REFERENCES `cmsplugin_genericlinklistplugin` (`cmsplugin_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `links_genericlinklistpluginitem`
--

LOCK TABLES `links_genericlinklistpluginitem` WRITE;
/*!40000 ALTER TABLE `links_genericlinklistpluginitem` DISABLE KEYS */;
/*!40000 ALTER TABLE `links_genericlinklistpluginitem` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `links_linktype`
--

DROP TABLE IF EXISTS `links_linktype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `links_linktype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `scheme` varchar(50) NOT NULL,
  `name` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `scheme` (`scheme`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `links_linktype`
--

LOCK TABLES `links_linktype` WRITE;
/*!40000 ALTER TABLE `links_linktype` DISABLE KEYS */;
INSERT INTO `links_linktype` VALUES (1,'https','Secure hypertext'),(2,'http','Hypertext'),(3,'mailto','Email address'),(4,'ftp','File Transfer Protocol');
/*!40000 ALTER TABLE `links_linktype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `links_objectlink`
--

DROP TABLE IF EXISTS `links_objectlink`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `links_objectlink` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `destination_content_type_id` int(11) NOT NULL,
  `destination_object_id` int(10) unsigned NOT NULL,
  `include_description` tinyint(1) NOT NULL,
  `text_override` varchar(256) DEFAULT NULL,
  `description_override` longtext,
  `heading_override` varchar(256) DEFAULT NULL,
  `metadata_override` varchar(256) DEFAULT NULL,
  `html_title_attribute` varchar(256) DEFAULT NULL,
  `content_type_id` int(11) NOT NULL,
  `object_id` int(10) unsigned NOT NULL,
  `key_link` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `links_objectlink_a1ae9087` (`destination_content_type_id`),
  KEY `links_objectlink_e4470c6e` (`content_type_id`),
  CONSTRAINT `content_type_id_refs_id_bf72db45` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `destination_content_type_id_refs_id_bf72db45` FOREIGN KEY (`destination_content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `links_objectlink`
--

LOCK TABLES `links_objectlink` WRITE;
/*!40000 ALTER TABLE `links_objectlink` DISABLE KEYS */;
/*!40000 ALTER TABLE `links_objectlink` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `menus_cachekey`
--

DROP TABLE IF EXISTS `menus_cachekey`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `menus_cachekey` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `language` varchar(255) NOT NULL,
  `site` int(10) unsigned NOT NULL,
  `key` varchar(255) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `menus_cachekey`
--

LOCK TABLES `menus_cachekey` WRITE;
/*!40000 ALTER TABLE `menus_cachekey` DISABLE KEYS */;
INSERT INTO `menus_cachekey` VALUES (4,'ru',1,'cms-menu_nodes_ru_1'),(5,'ru',1,'cms-menu_nodes_ru_1_1_user');
/*!40000 ALTER TABLE `menus_cachekey` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news_and_events_event`
--

DROP TABLE IF EXISTS `news_and_events_event`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news_and_events_event` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(200) DEFAULT NULL,
  `external_url_id` int(11),
  `slug` varchar(60) NOT NULL,
  `precise_location` varchar(255) DEFAULT NULL,
  `access_note` varchar(255) DEFAULT NULL,
  `title` varchar(255) NOT NULL,
  `short_title` varchar(255) DEFAULT NULL,
  `summary` longtext NOT NULL,
  `published` tinyint(1) NOT NULL,
  `in_lists` tinyint(1) NOT NULL,
  `body_id` int(11) DEFAULT NULL,
  `image_id` int(11),
  `hosted_by_id` int(11),
  `importance` int(10) unsigned DEFAULT NULL,
  `content` longtext,
  `type_id` int(11) NOT NULL,
  `parent_id` int(11),
  `series` tinyint(1) NOT NULL,
  `show_titles` varchar(25) NOT NULL,
  `display_series_summary` tinyint(1) NOT NULL,
  `child_list_heading` varchar(50) DEFAULT NULL,
  `date` date DEFAULT NULL,
  `start_time` time DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  `end_time` time DEFAULT NULL,
  `single_day_event` tinyint(1) NOT NULL,
  `building_id` int(11),
  `jumps_queue_on` date DEFAULT NULL,
  `jumps_queue_everywhere` tinyint(1) NOT NULL,
  `lft` int(10) unsigned NOT NULL,
  `rght` int(10) unsigned NOT NULL,
  `tree_id` int(10) unsigned NOT NULL,
  `level` int(10) unsigned NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `news_and_events_event_b68122a1` (`external_url_id`),
  KEY `news_and_events_event_86f19268` (`published`),
  KEY `news_and_events_event_452ad3f4` (`in_lists`),
  KEY `news_and_events_event_5b892844` (`body_id`),
  KEY `news_and_events_event_6682136` (`image_id`),
  KEY `news_and_events_event_e998008a` (`hosted_by_id`),
  KEY `news_and_events_event_777d41c8` (`type_id`),
  KEY `news_and_events_event_63f17a16` (`parent_id`),
  KEY `news_and_events_event_57000c84` (`building_id`),
  KEY `news_and_events_event_42b06ff6` (`lft`),
  KEY `news_and_events_event_91543e5a` (`rght`),
  KEY `news_and_events_event_efd07f28` (`tree_id`),
  KEY `news_and_events_event_2a8f42e8` (`level`),
  CONSTRAINT `body_id_refs_id_4abba978` FOREIGN KEY (`body_id`) REFERENCES `cms_placeholder` (`id`),
  CONSTRAINT `building_id_refs_id_1de086ee` FOREIGN KEY (`building_id`) REFERENCES `contacts_and_people_building` (`id`),
  CONSTRAINT `external_url_id_refs_id_d417e5db` FOREIGN KEY (`external_url_id`) REFERENCES `links_externallink` (`id`),
  CONSTRAINT `hosted_by_id_refs_entitylite_ptr_id_72ba2ae5` FOREIGN KEY (`hosted_by_id`) REFERENCES `contacts_and_people_entity` (`entitylite_ptr_id`),
  CONSTRAINT `image_id_refs_file_ptr_id_3f34aeef` FOREIGN KEY (`image_id`) REFERENCES `filer_image` (`file_ptr_id`),
  CONSTRAINT `parent_id_refs_id_8d5aaa1b` FOREIGN KEY (`parent_id`) REFERENCES `news_and_events_event` (`id`),
  CONSTRAINT `type_id_refs_id_57d964e9` FOREIGN KEY (`type_id`) REFERENCES `news_and_events_eventtype` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news_and_events_event`
--

LOCK TABLES `news_and_events_event` WRITE;
/*!40000 ALTER TABLE `news_and_events_event` DISABLE KEYS */;
/*!40000 ALTER TABLE `news_and_events_event` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news_and_events_event_featuring`
--

DROP TABLE IF EXISTS `news_and_events_event_featuring`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news_and_events_event_featuring` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `news_and_events_event_featuring_event_id_2afec085321ff11b_uniq` (`event_id`,`person_id`),
  KEY `news_and_events_event_featuring_e9b82f95` (`event_id`),
  KEY `news_and_events_event_featuring_21b911c5` (`person_id`),
  CONSTRAINT `person_id_refs_personlite_ptr_id_dcaf4b61` FOREIGN KEY (`person_id`) REFERENCES `contacts_and_people_person` (`personlite_ptr_id`),
  CONSTRAINT `event_id_refs_id_44dae08b` FOREIGN KEY (`event_id`) REFERENCES `news_and_events_event` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news_and_events_event_featuring`
--

LOCK TABLES `news_and_events_event_featuring` WRITE;
/*!40000 ALTER TABLE `news_and_events_event_featuring` DISABLE KEYS */;
/*!40000 ALTER TABLE `news_and_events_event_featuring` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news_and_events_event_please_contact`
--

DROP TABLE IF EXISTS `news_and_events_event_please_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news_and_events_event_please_contact` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `news_and_events_event_please_con_event_id_3221c131f12984ee_uniq` (`event_id`,`person_id`),
  KEY `news_and_events_event_please_contact_e9b82f95` (`event_id`),
  KEY `news_and_events_event_please_contact_21b911c5` (`person_id`),
  CONSTRAINT `person_id_refs_personlite_ptr_id_ec6a5324` FOREIGN KEY (`person_id`) REFERENCES `contacts_and_people_person` (`personlite_ptr_id`),
  CONSTRAINT `event_id_refs_id_85ab4cb8` FOREIGN KEY (`event_id`) REFERENCES `news_and_events_event` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news_and_events_event_please_contact`
--

LOCK TABLES `news_and_events_event_please_contact` WRITE;
/*!40000 ALTER TABLE `news_and_events_event_please_contact` DISABLE KEYS */;
/*!40000 ALTER TABLE `news_and_events_event_please_contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news_and_events_event_publish_to`
--

DROP TABLE IF EXISTS `news_and_events_event_publish_to`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news_and_events_event_publish_to` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) NOT NULL,
  `entity_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `news_and_events_event_publish_to_event_id_108985aabe886eb8_uniq` (`event_id`,`entity_id`),
  KEY `news_and_events_event_publish_to_e9b82f95` (`event_id`),
  KEY `news_and_events_event_publish_to_2ce815e9` (`entity_id`),
  CONSTRAINT `entity_id_refs_entitylite_ptr_id_542f75e2` FOREIGN KEY (`entity_id`) REFERENCES `contacts_and_people_entity` (`entitylite_ptr_id`),
  CONSTRAINT `event_id_refs_id_51dd50e8` FOREIGN KEY (`event_id`) REFERENCES `news_and_events_event` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news_and_events_event_publish_to`
--

LOCK TABLES `news_and_events_event_publish_to` WRITE;
/*!40000 ALTER TABLE `news_and_events_event_publish_to` DISABLE KEYS */;
/*!40000 ALTER TABLE `news_and_events_event_publish_to` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news_and_events_event_registration_enquiries`
--

DROP TABLE IF EXISTS `news_and_events_event_registration_enquiries`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news_and_events_event_registration_enquiries` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `news_and_events_event_registrati_event_id_2387eb8e74647c18_uniq` (`event_id`,`person_id`),
  KEY `news_and_events_event_registration_enquiries_e9b82f95` (`event_id`),
  KEY `news_and_events_event_registration_enquiries_21b911c5` (`person_id`),
  CONSTRAINT `person_id_refs_personlite_ptr_id_cc8541ce` FOREIGN KEY (`person_id`) REFERENCES `contacts_and_people_person` (`personlite_ptr_id`),
  CONSTRAINT `event_id_refs_id_c6e0267e` FOREIGN KEY (`event_id`) REFERENCES `news_and_events_event` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news_and_events_event_registration_enquiries`
--

LOCK TABLES `news_and_events_event_registration_enquiries` WRITE;
/*!40000 ALTER TABLE `news_and_events_event_registration_enquiries` DISABLE KEYS */;
/*!40000 ALTER TABLE `news_and_events_event_registration_enquiries` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news_and_events_eventtype`
--

DROP TABLE IF EXISTS `news_and_events_eventtype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news_and_events_eventtype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `event_type` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news_and_events_eventtype`
--

LOCK TABLES `news_and_events_eventtype` WRITE;
/*!40000 ALTER TABLE `news_and_events_eventtype` DISABLE KEYS */;
/*!40000 ALTER TABLE `news_and_events_eventtype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news_and_events_newsarticle`
--

DROP TABLE IF EXISTS `news_and_events_newsarticle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news_and_events_newsarticle` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(200) DEFAULT NULL,
  `external_url_id` int(11),
  `slug` varchar(60) NOT NULL,
  `title` varchar(255) NOT NULL,
  `short_title` varchar(255) DEFAULT NULL,
  `summary` longtext NOT NULL,
  `published` tinyint(1) NOT NULL,
  `in_lists` tinyint(1) NOT NULL,
  `body_id` int(11) DEFAULT NULL,
  `image_id` int(11),
  `hosted_by_id` int(11),
  `importance` int(10) unsigned DEFAULT NULL,
  `content` longtext,
  `date` datetime NOT NULL,
  `display_indefinitely` tinyint(1) NOT NULL,
  `external_news_source_id` int(11) DEFAULT NULL,
  `sticky_until` date DEFAULT NULL,
  `is_sticky_everywhere` tinyint(1) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `news_and_events_newsarticle_b68122a1` (`external_url_id`),
  KEY `news_and_events_newsarticle_86f19268` (`published`),
  KEY `news_and_events_newsarticle_452ad3f4` (`in_lists`),
  KEY `news_and_events_newsarticle_5b892844` (`body_id`),
  KEY `news_and_events_newsarticle_6682136` (`image_id`),
  KEY `news_and_events_newsarticle_e998008a` (`hosted_by_id`),
  KEY `news_and_events_newsarticle_9a811acb` (`external_news_source_id`),
  CONSTRAINT `external_url_id_refs_id_cdd7436` FOREIGN KEY (`external_url_id`) REFERENCES `links_externallink` (`id`),
  CONSTRAINT `body_id_refs_id_57f0904f` FOREIGN KEY (`body_id`) REFERENCES `cms_placeholder` (`id`),
  CONSTRAINT `external_news_source_id_refs_id_633a3d47` FOREIGN KEY (`external_news_source_id`) REFERENCES `news_and_events_newssource` (`id`),
  CONSTRAINT `hosted_by_id_refs_entitylite_ptr_id_25eaecd4` FOREIGN KEY (`hosted_by_id`) REFERENCES `contacts_and_people_entity` (`entitylite_ptr_id`),
  CONSTRAINT `image_id_refs_file_ptr_id_a244cc3a` FOREIGN KEY (`image_id`) REFERENCES `filer_image` (`file_ptr_id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news_and_events_newsarticle`
--

LOCK TABLES `news_and_events_newsarticle` WRITE;
/*!40000 ALTER TABLE `news_and_events_newsarticle` DISABLE KEYS */;
INSERT INTO `news_and_events_newsarticle` VALUES (1,NULL,NULL,'novost-dnya','Новость дня','Самая жуткая новость','Самая жуткая новость\r\nСамая жуткая новость\r\nСамая жуткая новость\r\n',1,1,9,3,1,0,NULL,'2014-02-20 03:11:17',0,NULL,NULL,1);
/*!40000 ALTER TABLE `news_and_events_newsarticle` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news_and_events_newsarticle_please_contact`
--

DROP TABLE IF EXISTS `news_and_events_newsarticle_please_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news_and_events_newsarticle_please_contact` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `newsarticle_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `news_and_events_newsarticle_newsarticle_id_fb38766c1a3907c_uniq` (`newsarticle_id`,`person_id`),
  KEY `news_and_events_newsarticle_please_contact_e34f5ca2` (`newsarticle_id`),
  KEY `news_and_events_newsarticle_please_contact_21b911c5` (`person_id`),
  CONSTRAINT `person_id_refs_personlite_ptr_id_3c049ee7` FOREIGN KEY (`person_id`) REFERENCES `contacts_and_people_person` (`personlite_ptr_id`),
  CONSTRAINT `newsarticle_id_refs_id_6d387d28` FOREIGN KEY (`newsarticle_id`) REFERENCES `news_and_events_newsarticle` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news_and_events_newsarticle_please_contact`
--

LOCK TABLES `news_and_events_newsarticle_please_contact` WRITE;
/*!40000 ALTER TABLE `news_and_events_newsarticle_please_contact` DISABLE KEYS */;
/*!40000 ALTER TABLE `news_and_events_newsarticle_please_contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news_and_events_newsarticle_publish_to`
--

DROP TABLE IF EXISTS `news_and_events_newsarticle_publish_to`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news_and_events_newsarticle_publish_to` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `newsarticle_id` int(11) NOT NULL,
  `entity_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `news_and_events_newsarticl_newsarticle_id_58bf7c765d5c2fda_uniq` (`newsarticle_id`,`entity_id`),
  KEY `news_and_events_newsarticle_publish_to_e34f5ca2` (`newsarticle_id`),
  KEY `news_and_events_newsarticle_publish_to_2ce815e9` (`entity_id`),
  CONSTRAINT `entity_id_refs_entitylite_ptr_id_17b12a07` FOREIGN KEY (`entity_id`) REFERENCES `contacts_and_people_entity` (`entitylite_ptr_id`),
  CONSTRAINT `newsarticle_id_refs_id_98985274` FOREIGN KEY (`newsarticle_id`) REFERENCES `news_and_events_newsarticle` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news_and_events_newsarticle_publish_to`
--

LOCK TABLES `news_and_events_newsarticle_publish_to` WRITE;
/*!40000 ALTER TABLE `news_and_events_newsarticle_publish_to` DISABLE KEYS */;
/*!40000 ALTER TABLE `news_and_events_newsarticle_publish_to` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `news_and_events_newssource`
--

DROP TABLE IF EXISTS `news_and_events_newssource`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `news_and_events_newssource` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `external_news_source` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `news_and_events_newssource`
--

LOCK TABLES `news_and_events_newssource` WRITE;
/*!40000 ALTER TABLE `news_and_events_newssource` DISABLE KEYS */;
/*!40000 ALTER TABLE `news_and_events_newssource` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_choice`
--

DROP TABLE IF EXISTS `polls_choice`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `polls_choice` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `poll_id` int(11) NOT NULL,
  `choice_text` varchar(200) NOT NULL,
  `votes` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `polls_choice_763e883` (`poll_id`),
  CONSTRAINT `poll_id_refs_id_a27693dd` FOREIGN KEY (`poll_id`) REFERENCES `polls_poll` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_choice`
--

LOCK TABLES `polls_choice` WRITE;
/*!40000 ALTER TABLE `polls_choice` DISABLE KEYS */;
/*!40000 ALTER TABLE `polls_choice` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `polls_poll`
--

DROP TABLE IF EXISTS `polls_poll`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `polls_poll` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `question` varchar(200) NOT NULL,
  `pub_date` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `polls_poll`
--

LOCK TABLES `polls_poll` WRITE;
/*!40000 ALTER TABLE `polls_poll` DISABLE KEYS */;
/*!40000 ALTER TABLE `polls_poll` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `semanticeditor_cssclass`
--

DROP TABLE IF EXISTS `semanticeditor_cssclass`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `semanticeditor_cssclass` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `verbose_name` varchar(255) NOT NULL,
  `description` longtext NOT NULL,
  `allowed_elements` varchar(255) NOT NULL,
  `column_equiv` int(11) DEFAULT NULL,
  `templates` longtext NOT NULL,
  `category_id` int(11),
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`),
  UNIQUE KEY `verbose_name` (`verbose_name`),
  KEY `semanticeditor_cssclass_42dc49bc` (`category_id`),
  CONSTRAINT `category_id_refs_id_9dcb025` FOREIGN KEY (`category_id`) REFERENCES `semanticeditor_cssclasscategory` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `semanticeditor_cssclass`
--

LOCK TABLES `semanticeditor_cssclass` WRITE;
/*!40000 ALTER TABLE `semanticeditor_cssclass` DISABLE KEYS */;
/*!40000 ALTER TABLE `semanticeditor_cssclass` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `semanticeditor_cssclasscategory`
--

DROP TABLE IF EXISTS `semanticeditor_cssclasscategory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `semanticeditor_cssclasscategory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `semanticeditor_cssclasscategory`
--

LOCK TABLES `semanticeditor_cssclasscategory` WRITE;
/*!40000 ALTER TABLE `semanticeditor_cssclasscategory` DISABLE KEYS */;
/*!40000 ALTER TABLE `semanticeditor_cssclasscategory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `snippet_snippet`
--

DROP TABLE IF EXISTS `snippet_snippet`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `snippet_snippet` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `html` longtext NOT NULL,
  `template` varchar(50) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `snippet_snippet`
--

LOCK TABLES `snippet_snippet` WRITE;
/*!40000 ALTER TABLE `snippet_snippet` DISABLE KEYS */;
/*!40000 ALTER TABLE `snippet_snippet` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `south_migrationhistory`
--

DROP TABLE IF EXISTS `south_migrationhistory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `south_migrationhistory` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_name` varchar(255) NOT NULL,
  `migration` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=120 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `south_migrationhistory`
--

LOCK TABLES `south_migrationhistory` WRITE;
/*!40000 ALTER TABLE `south_migrationhistory` DISABLE KEYS */;
INSERT INTO `south_migrationhistory` VALUES (1,'arkestra_utilities','0001_initial','2014-02-20 02:50:25'),(2,'cms','0001_initial','2014-02-20 02:50:26'),(3,'cms','0002_auto_start','2014-02-20 02:50:27'),(4,'cms','0003_remove_placeholder','2014-02-20 02:50:27'),(5,'cms','0004_textobjects','2014-02-20 02:50:27'),(6,'cms','0005_mptt_added_to_plugins','2014-02-20 02:50:27'),(7,'text','0001_initial','2014-02-20 02:50:27'),(8,'text','0002_freeze','2014-02-20 02:50:27'),(9,'cms','0006_apphook','2014-02-20 02:50:27'),(10,'cms','0007_apphook_longer','2014-02-20 02:50:27'),(11,'cms','0008_redirects','2014-02-20 02:50:28'),(12,'cms','0009_added_meta_fields','2014-02-20 02:50:28'),(13,'cms','0010_5char_language','2014-02-20 02:50:28'),(14,'cms','0011_title_overwrites','2014-02-20 02:50:28'),(15,'cms','0012_publisher','2014-02-20 02:50:30'),(16,'text','0003_publisher','2014-02-20 02:50:30'),(17,'snippet','0001_initial','2014-02-20 02:50:31'),(18,'snippet','0002_publisher','2014-02-20 02:50:31'),(19,'cms','0013_site_copy','2014-02-20 02:50:31'),(20,'cms','0014_sites_removed','2014-02-20 02:50:31'),(21,'cms','0015_modified_by_added','2014-02-20 02:50:31'),(22,'cms','0016_author_copy','2014-02-20 02:50:31'),(23,'cms','0017_author_removed','2014-02-20 02:50:32'),(24,'cms','0018_site_permissions','2014-02-20 02:50:32'),(25,'cms','0019_public_table_renames','2014-02-20 02:50:32'),(26,'text','0004_table_rename','2014-02-20 02:50:33'),(27,'text','0005_publisher2','2014-02-20 02:50:33'),(28,'snippet','0003_table_rename','2014-02-20 02:50:33'),(29,'snippet','0004_publisher2','2014-02-20 02:50:33'),(30,'cms','0020_advanced_permissions','2014-02-20 02:50:33'),(31,'cms','0021_publisher2','2014-02-20 02:50:34'),(32,'cms','0022_login_required_added','2014-02-20 02:50:35'),(33,'cms','0023_plugin_table_naming_function_changed','2014-02-20 02:50:35'),(34,'cms','0024_added_placeholder_model','2014-02-20 02:50:35'),(35,'cms','0025_placeholder_migration','2014-02-20 02:50:35'),(36,'cms','0026_finish_placeholder_migration','2014-02-20 02:50:35'),(37,'cms','0027_added_width_to_placeholder','2014-02-20 02:50:35'),(38,'cms','0028_limit_visibility_in_menu_step1of3','2014-02-20 02:50:36'),(39,'cms','0029_limit_visibility_in_menu_step2of3_data','2014-02-20 02:50:36'),(40,'cms','0030_limit_visibility_in_menu_step3of3','2014-02-20 02:50:36'),(41,'cms','0031_improved_language_code_support','2014-02-20 02:50:36'),(42,'cms','0032_auto__del_field_cmsplugin_publisher_public__del_field_cmsplugin_publis','2014-02-20 02:50:36'),(43,'cms','0033_auto__del_field_title_publisher_is_draft__del_field_title_publisher_st','2014-02-20 02:50:36'),(44,'cms','0034_auto__chg_field_title_language__chg_field_cmsplugin_language__add_fiel','2014-02-20 02:50:37'),(45,'cms','0035_auto__add_field_globalpagepermission_can_view__add_field_pagepermissio','2014-02-20 02:50:37'),(46,'cms','0036_auto__add_field_cmsplugin_changed_date','2014-02-20 02:50:37'),(47,'menus','0001_initial','2014-02-20 02:50:37'),(48,'text','0006_2_1_4_upgrade','2014-02-20 02:50:37'),(49,'snippet','0005_template_added','2014-02-20 02:50:38'),(50,'contacts_and_people','0001_initial','2014-02-20 02:50:40'),(51,'contacts_and_people','0002_auto__chg_field_entityautopagelinkplugineditor_entity__chg_field_perso','2014-02-20 02:50:41'),(52,'contacts_and_people','0003_renaming_column_personlite_title','2014-02-20 02:50:41'),(53,'contacts_and_people','0004_backup_column_personlite_title','2014-02-20 02:50:41'),(54,'contacts_and_people','0005_delete_column_personlite_title_backup','2014-02-20 02:50:42'),(55,'contacts_and_people','0006_auto__chg_field_entity_image__chg_field_entity_external_url__chg_field','2014-02-20 02:50:42'),(56,'vacancies_and_studentships','0001_initial','2014-02-20 02:50:44'),(57,'vacancies_and_studentships','0002_auto__chg_field_studentship_hosted_by__chg_field_studentship_image__ch','2014-02-20 02:50:45'),(58,'vacancies_and_studentships','0003_rename_date_fields','2014-02-20 02:50:45'),(59,'news_and_events','0001_initial','2014-02-20 02:50:47'),(60,'news_and_events','0002_auto__chg_field_newsandeventsplugin_entity__chg_field_event_image__chg','2014-02-20 02:50:49'),(61,'news_and_events','0003_rename_event_date_field','2014-02-20 02:50:49'),(62,'links','0001_initial','2014-02-20 02:50:50'),(63,'links','0002_auto__add_field_objectlink_key_link','2014-02-20 02:50:50'),(64,'links','0003_auto__add_field_genericlinklistpluginitem_inline_item_ordering__add_fi','2014-02-20 02:50:51'),(65,'links','0004_auto__chg_field_externallink_kind__chg_field_externallink_external_sit','2014-02-20 02:50:51'),(66,'arkestra_image_plugin','0001_initial','2014-02-20 02:50:52'),(67,'arkestra_image_plugin','0002_embedded_video_plugin','2014-02-20 02:50:52'),(68,'arkestra_image_plugin','0003_auto__add_field_embeddedvideosetitem_inline_item_ordering__add_field_e','2014-02-20 02:50:52'),(69,'arkestra_image_plugin','0004_convert_old_filer_plugin','2014-02-20 02:50:52'),(70,'arkestra_image_plugin','0005_remove_filer_plugin','2014-02-20 02:50:52'),(71,'video','0001_initial','2014-02-20 02:50:53'),(72,'video','0002_auto__add_video__chg_field_videoversion_source__chg_field_videoplugine','2014-02-20 02:50:53'),(73,'semanticeditor','0001_initial','2014-02-20 02:50:53'),(74,'semanticeditor','0002_cssclass_template','2014-02-20 02:50:53'),(75,'semanticeditor','0003_auto__chg_field_cssclass_templates','2014-02-20 02:50:53'),(76,'semanticeditor','0004_auto__add_cssclasscategory','2014-02-20 02:50:53'),(77,'semanticeditor','0005_auto__add_field_cssclass_category','2014-02-20 02:50:53'),(78,'easy_thumbnails','0001_initial','2014-02-20 02:50:54'),(79,'easy_thumbnails','0002_filename_indexes','2014-02-20 02:50:54'),(80,'easy_thumbnails','0003_auto__add_storagenew','2014-02-20 02:50:54'),(81,'easy_thumbnails','0004_auto__add_field_source_storage_new__add_field_thumbnail_storage_new','2014-02-20 02:50:54'),(82,'easy_thumbnails','0005_storage_fks_null','2014-02-20 02:50:55'),(83,'easy_thumbnails','0006_copy_storage','2014-02-20 02:50:55'),(84,'easy_thumbnails','0007_storagenew_fks_not_null','2014-02-20 02:50:55'),(85,'easy_thumbnails','0008_auto__del_field_source_storage__del_field_thumbnail_storage','2014-02-20 02:50:55'),(86,'easy_thumbnails','0009_auto__del_storage','2014-02-20 02:50:55'),(87,'easy_thumbnails','0010_rename_storage','2014-02-20 02:50:55'),(88,'easy_thumbnails','0011_auto__add_field_source_storage_hash__add_field_thumbnail_storage_hash','2014-02-20 02:50:56'),(89,'easy_thumbnails','0012_build_storage_hashes','2014-02-20 02:50:56'),(90,'easy_thumbnails','0013_auto__del_storage__del_field_source_storage__del_field_thumbnail_stora','2014-02-20 02:50:56'),(91,'easy_thumbnails','0014_auto__add_unique_source_name_storage_hash__add_unique_thumbnail_name_s','2014-02-20 02:50:56'),(92,'easy_thumbnails','0015_auto__del_unique_thumbnail_name_storage_hash__add_unique_thumbnail_sou','2014-02-20 02:50:56'),(93,'filer','0001_initial','2014-02-20 02:50:57'),(94,'filer','0002_rename_file_field','2014-02-20 02:50:57'),(95,'filer','0003_add_description_field','2014-02-20 02:50:57'),(96,'filer','0004_auto__del_field_file__file__add_field_file_file__add_field_file_is_pub','2014-02-20 02:50:57'),(97,'filer','0005_auto__add_field_file_sha1__chg_field_file_file','2014-02-20 02:50:58'),(98,'filer','0006_polymorphic__add_field_file_polymorphic_ctype','2014-02-20 02:50:58'),(99,'filer','0007_polymorphic__content_type_data','2014-02-20 02:50:58'),(100,'filer','0008_polymorphic__del_field_file__file_type_plugin_name','2014-02-20 02:50:58'),(101,'filer','0009_auto__add_field_folderpermission_can_edit_new__add_field_folderpermiss','2014-02-20 02:50:58'),(102,'filer','0010_folderpermissions','2014-02-20 02:50:58'),(103,'filer','0011_auto__del_field_folderpermission_can_add_children__del_field_folderper','2014-02-20 02:50:58'),(104,'filer','0012_renaming_folderpermissions','2014-02-20 02:50:59'),(105,'filer','0013_remove_null_file_name','2014-02-20 02:50:59'),(106,'filer','0014_auto__add_field_image_related_url__chg_field_file_name','2014-02-20 02:50:59'),(107,'polls','0001_initial','2014-02-20 04:42:40'),(108,'grizzly','0001_initial','2014-02-20 05:14:03'),(117,'grizzly','0002_initial','2014-02-20 08:36:22'),(118,'grizzly','0003_initial','2014-02-20 08:40:01'),(119,'grizzly','0004_initial','2014-02-20 08:51:15');
/*!40000 ALTER TABLE `south_migrationhistory` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacancies_and_studentships_studentship`
--

DROP TABLE IF EXISTS `vacancies_and_studentships_studentship`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vacancies_and_studentships_studentship` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(200) DEFAULT NULL,
  `external_url_id` int(11),
  `slug` varchar(60) NOT NULL,
  `title` varchar(255) NOT NULL,
  `short_title` varchar(255) DEFAULT NULL,
  `summary` longtext NOT NULL,
  `published` tinyint(1) NOT NULL,
  `in_lists` tinyint(1) NOT NULL,
  `body_id` int(11) DEFAULT NULL,
  `image_id` int(11),
  `hosted_by_id` int(11),
  `importance` int(10) unsigned DEFAULT NULL,
  `date` date NOT NULL,
  `description` longtext,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `vacancies_and_studentships_studentship_b68122a1` (`external_url_id`),
  KEY `vacancies_and_studentships_studentship_86f19268` (`published`),
  KEY `vacancies_and_studentships_studentship_452ad3f4` (`in_lists`),
  KEY `vacancies_and_studentships_studentship_5b892844` (`body_id`),
  KEY `vacancies_and_studentships_studentship_6682136` (`image_id`),
  KEY `vacancies_and_studentships_studentship_e998008a` (`hosted_by_id`),
  CONSTRAINT `body_id_refs_id_acfaf3e3` FOREIGN KEY (`body_id`) REFERENCES `cms_placeholder` (`id`),
  CONSTRAINT `external_url_id_refs_id_506a264a` FOREIGN KEY (`external_url_id`) REFERENCES `links_externallink` (`id`),
  CONSTRAINT `hosted_by_id_refs_entitylite_ptr_id_3af9ad40` FOREIGN KEY (`hosted_by_id`) REFERENCES `contacts_and_people_entity` (`entitylite_ptr_id`),
  CONSTRAINT `image_id_refs_file_ptr_id_5f1d7f5a` FOREIGN KEY (`image_id`) REFERENCES `filer_image` (`file_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacancies_and_studentships_studentship`
--

LOCK TABLES `vacancies_and_studentships_studentship` WRITE;
/*!40000 ALTER TABLE `vacancies_and_studentships_studentship` DISABLE KEYS */;
/*!40000 ALTER TABLE `vacancies_and_studentships_studentship` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacancies_and_studentships_studentship_please_contact`
--

DROP TABLE IF EXISTS `vacancies_and_studentships_studentship_please_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vacancies_and_studentships_studentship_please_contact` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `studentship_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vacancies_and_studentships__studentship_id_cbbab08f3f53dbe_uniq` (`studentship_id`,`person_id`),
  KEY `vacancies_and_studentships_studentship_please_contact_67cc45b4` (`studentship_id`),
  KEY `vacancies_and_studentships_studentship_please_contact_21b911c5` (`person_id`),
  CONSTRAINT `person_id_refs_personlite_ptr_id_a425fd35` FOREIGN KEY (`person_id`) REFERENCES `contacts_and_people_person` (`personlite_ptr_id`),
  CONSTRAINT `studentship_id_refs_id_362ee970` FOREIGN KEY (`studentship_id`) REFERENCES `vacancies_and_studentships_studentship` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacancies_and_studentships_studentship_please_contact`
--

LOCK TABLES `vacancies_and_studentships_studentship_please_contact` WRITE;
/*!40000 ALTER TABLE `vacancies_and_studentships_studentship_please_contact` DISABLE KEYS */;
/*!40000 ALTER TABLE `vacancies_and_studentships_studentship_please_contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacancies_and_studentships_studentship_publish_to`
--

DROP TABLE IF EXISTS `vacancies_and_studentships_studentship_publish_to`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vacancies_and_studentships_studentship_publish_to` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `studentship_id` int(11) NOT NULL,
  `entity_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vacancies_and_studentships_studentship_id_723b76736c6e91a8_uniq` (`studentship_id`,`entity_id`),
  KEY `vacancies_and_studentships_studentship_publish_to_67cc45b4` (`studentship_id`),
  KEY `vacancies_and_studentships_studentship_publish_to_2ce815e9` (`entity_id`),
  CONSTRAINT `entity_id_refs_entitylite_ptr_id_18b9a217` FOREIGN KEY (`entity_id`) REFERENCES `contacts_and_people_entity` (`entitylite_ptr_id`),
  CONSTRAINT `studentship_id_refs_id_4867bcb0` FOREIGN KEY (`studentship_id`) REFERENCES `vacancies_and_studentships_studentship` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacancies_and_studentships_studentship_publish_to`
--

LOCK TABLES `vacancies_and_studentships_studentship_publish_to` WRITE;
/*!40000 ALTER TABLE `vacancies_and_studentships_studentship_publish_to` DISABLE KEYS */;
/*!40000 ALTER TABLE `vacancies_and_studentships_studentship_publish_to` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacancies_and_studentships_studentship_supervisors`
--

DROP TABLE IF EXISTS `vacancies_and_studentships_studentship_supervisors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vacancies_and_studentships_studentship_supervisors` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `studentship_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vacancies_and_studentships_studentship_id_572fb50a5db0be7b_uniq` (`studentship_id`,`person_id`),
  KEY `vacancies_and_studentships_studentship_supervisors_67cc45b4` (`studentship_id`),
  KEY `vacancies_and_studentships_studentship_supervisors_21b911c5` (`person_id`),
  CONSTRAINT `person_id_refs_personlite_ptr_id_50c2996e` FOREIGN KEY (`person_id`) REFERENCES `contacts_and_people_person` (`personlite_ptr_id`),
  CONSTRAINT `studentship_id_refs_id_aa36b29f` FOREIGN KEY (`studentship_id`) REFERENCES `vacancies_and_studentships_studentship` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacancies_and_studentships_studentship_supervisors`
--

LOCK TABLES `vacancies_and_studentships_studentship_supervisors` WRITE;
/*!40000 ALTER TABLE `vacancies_and_studentships_studentship_supervisors` DISABLE KEYS */;
/*!40000 ALTER TABLE `vacancies_and_studentships_studentship_supervisors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacancies_and_studentships_vacancy`
--

DROP TABLE IF EXISTS `vacancies_and_studentships_vacancy`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vacancies_and_studentships_vacancy` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `url` varchar(200) DEFAULT NULL,
  `external_url_id` int(11),
  `slug` varchar(60) NOT NULL,
  `title` varchar(255) NOT NULL,
  `short_title` varchar(255) DEFAULT NULL,
  `summary` longtext NOT NULL,
  `published` tinyint(1) NOT NULL,
  `in_lists` tinyint(1) NOT NULL,
  `body_id` int(11) DEFAULT NULL,
  `image_id` int(11),
  `hosted_by_id` int(11),
  `importance` int(10) unsigned DEFAULT NULL,
  `date` date NOT NULL,
  `description` longtext,
  `job_number` varchar(9) NOT NULL,
  `salary` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `slug` (`slug`),
  KEY `vacancies_and_studentships_vacancy_b68122a1` (`external_url_id`),
  KEY `vacancies_and_studentships_vacancy_86f19268` (`published`),
  KEY `vacancies_and_studentships_vacancy_452ad3f4` (`in_lists`),
  KEY `vacancies_and_studentships_vacancy_5b892844` (`body_id`),
  KEY `vacancies_and_studentships_vacancy_6682136` (`image_id`),
  KEY `vacancies_and_studentships_vacancy_e998008a` (`hosted_by_id`),
  CONSTRAINT `body_id_refs_id_1c4fc79f` FOREIGN KEY (`body_id`) REFERENCES `cms_placeholder` (`id`),
  CONSTRAINT `external_url_id_refs_id_54261f1a` FOREIGN KEY (`external_url_id`) REFERENCES `links_externallink` (`id`),
  CONSTRAINT `hosted_by_id_refs_entitylite_ptr_id_79159084` FOREIGN KEY (`hosted_by_id`) REFERENCES `contacts_and_people_entity` (`entitylite_ptr_id`),
  CONSTRAINT `image_id_refs_file_ptr_id_a618f976` FOREIGN KEY (`image_id`) REFERENCES `filer_image` (`file_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacancies_and_studentships_vacancy`
--

LOCK TABLES `vacancies_and_studentships_vacancy` WRITE;
/*!40000 ALTER TABLE `vacancies_and_studentships_vacancy` DISABLE KEYS */;
/*!40000 ALTER TABLE `vacancies_and_studentships_vacancy` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacancies_and_studentships_vacancy_please_contact`
--

DROP TABLE IF EXISTS `vacancies_and_studentships_vacancy_please_contact`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vacancies_and_studentships_vacancy_please_contact` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vacancy_id` int(11) NOT NULL,
  `person_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vacancies_and_studentships_vac_vacancy_id_61b58bb4f2251c62_uniq` (`vacancy_id`,`person_id`),
  KEY `vacancies_and_studentships_vacancy_please_contact_48a3cbe4` (`vacancy_id`),
  KEY `vacancies_and_studentships_vacancy_please_contact_21b911c5` (`person_id`),
  CONSTRAINT `person_id_refs_personlite_ptr_id_e3afb7a7` FOREIGN KEY (`person_id`) REFERENCES `contacts_and_people_person` (`personlite_ptr_id`),
  CONSTRAINT `vacancy_id_refs_id_4fb59cf8` FOREIGN KEY (`vacancy_id`) REFERENCES `vacancies_and_studentships_vacancy` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacancies_and_studentships_vacancy_please_contact`
--

LOCK TABLES `vacancies_and_studentships_vacancy_please_contact` WRITE;
/*!40000 ALTER TABLE `vacancies_and_studentships_vacancy_please_contact` DISABLE KEYS */;
/*!40000 ALTER TABLE `vacancies_and_studentships_vacancy_please_contact` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vacancies_and_studentships_vacancy_publish_to`
--

DROP TABLE IF EXISTS `vacancies_and_studentships_vacancy_publish_to`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `vacancies_and_studentships_vacancy_publish_to` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `vacancy_id` int(11) NOT NULL,
  `entity_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `vacancies_and_studentships_vac_vacancy_id_5ae59e5c6bd84b84_uniq` (`vacancy_id`,`entity_id`),
  KEY `vacancies_and_studentships_vacancy_publish_to_48a3cbe4` (`vacancy_id`),
  KEY `vacancies_and_studentships_vacancy_publish_to_2ce815e9` (`entity_id`),
  CONSTRAINT `entity_id_refs_entitylite_ptr_id_98b90cab` FOREIGN KEY (`entity_id`) REFERENCES `contacts_and_people_entity` (`entitylite_ptr_id`),
  CONSTRAINT `vacancy_id_refs_id_f6e67970` FOREIGN KEY (`vacancy_id`) REFERENCES `vacancies_and_studentships_vacancy` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vacancies_and_studentships_vacancy_publish_to`
--

LOCK TABLES `vacancies_and_studentships_vacancy_publish_to` WRITE;
/*!40000 ALTER TABLE `vacancies_and_studentships_vacancy_publish_to` DISABLE KEYS */;
/*!40000 ALTER TABLE `vacancies_and_studentships_vacancy_publish_to` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `video_video`
--

DROP TABLE IF EXISTS `video_video`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `video_video` (
  `file_ptr_id` int(11) NOT NULL,
  PRIMARY KEY (`file_ptr_id`),
  CONSTRAINT `file_ptr_id_refs_id_101e8ddc` FOREIGN KEY (`file_ptr_id`) REFERENCES `filer_file` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `video_video`
--

LOCK TABLES `video_video` WRITE;
/*!40000 ALTER TABLE `video_video` DISABLE KEYS */;
/*!40000 ALTER TABLE `video_video` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `video_videoversion`
--

DROP TABLE IF EXISTS `video_videoversion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `video_videoversion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `source_id` int(11) NOT NULL,
  `size` smallint(6) DEFAULT NULL,
  `codec` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `video_videoversion_89f89e85` (`source_id`),
  CONSTRAINT `source_id_refs_file_ptr_id_d67516c4` FOREIGN KEY (`source_id`) REFERENCES `video_video` (`file_ptr_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `video_videoversion`
--

LOCK TABLES `video_videoversion` WRITE;
/*!40000 ALTER TABLE `video_videoversion` DISABLE KEYS */;
/*!40000 ALTER TABLE `video_videoversion` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2014-02-20 16:05:00
