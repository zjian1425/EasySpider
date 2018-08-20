CREATE TABLE `tm_comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `auctionSku` varchar(255) DEFAULT NULL,
  `rateContent` text,
  `reply` text,
  `rateDate` varchar(255) DEFAULT NULL,
  `tradeEndtime` char(20) DEFAULT NULL,
  `crawls_time` date DEFAULT NULL,
  `com_id` char(20) DEFAULT NULL,
  `shop_name` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=18087 DEFAULT CHARSET=utf8;




CREATE TABLE `tm_commoditydetail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `com_id` char(20) NOT NULL,
  `shop_name` varchar(255) NOT NULL,
  `title` varchar(500) DEFAULT NULL,
  `o_price` varchar(50) DEFAULT NULL,
  `n_price` varchar(50) DEFAULT NULL,
  `sale_nums` int(11) DEFAULT NULL,
  `comment_nums` int(11) DEFAULT NULL,
  `fav_nums` varchar(255) DEFAULT NULL,
  `product_params` text,
  `crawls_time` date NOT NULL,
  PRIMARY KEY (`com_id`,`crawls_time`),
  KEY `id` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2527 DEFAULT CHARSET=utf8 COMMENT='…Ã∆∑œÍœ∏';





CREATE TABLE `tm_commodityid` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `com_id` char(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `shop_name` varchar(500) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `crawls_time` date NOT NULL,
  PRIMARY KEY (`com_id`,`crawls_time`),
  KEY `id` (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=20310 DEFAULT CHARSET=utf8;





CREATE TABLE `tm_tagwords` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `com_id` char(20) DEFAULT NULL,
  `tag` varchar(255) DEFAULT NULL,
  `posi` char(20) DEFAULT NULL,
  `tag_count` int(10) DEFAULT NULL,
  `crawls_time` datetime DEFAULT NULL,
  `c_id` int(5) DEFAULT NULL,
  `weight` int(5) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;





CREATE TABLE `jd_comments` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `com_url` varchar(255) NOT NULL,
  `tag_string` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `content` text CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci,
  `creation_time` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `useful_vote_count` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `useless_vote_count` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `score` char(20) DEFAULT NULL,
  `product_color` varchar(255) DEFAULT NULL,
  `product_size` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `user_level_name` varchar(255) DEFAULT NULL,
  `user_client_show` varchar(255) DEFAULT NULL,
  `shop_name` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci DEFAULT NULL,
  `crawl_time` date DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `j` (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=51363 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;




CREATE TABLE `jd_commoditydetail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `com_url` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `title` varchar(500) NOT NULL,
  `n_price` varchar(100) DEFAULT NULL,
  `o_price` varchar(100) DEFAULT NULL,
  `comment_nums` char(50) DEFAULT NULL,
  `product_params` text,
  `shop_name` varchar(255) DEFAULT NULL,
  `good` varchar(100) DEFAULT NULL,
  `general` varchar(100) DEFAULT NULL,
  `poor` varchar(100) DEFAULT NULL,
  `good_rate` float(5,2) DEFAULT NULL,
  `poor_rate` float(5,2) DEFAULT NULL,
  `general_rate` float(5,2) DEFAULT NULL,
  `average_score` float(10,2) DEFAULT NULL,
  `DefaultGoodCount` varchar(100) DEFAULT NULL,
  `crawl_time` date DEFAULT NULL,
  PRIMARY KEY (`com_url`),
  KEY `a` (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4408 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;





CREATE TABLE `jd_url` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `com_url` varchar(500) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `shop_name` varchar(255) NOT NULL,
  `crawl_time` date DEFAULT NULL,
  PRIMARY KEY (`com_url`),
  KEY `ji` (`id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=4348 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;



