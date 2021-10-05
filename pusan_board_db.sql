-- pusan_board_db 데이터베이스 구조 내보내기
CREATE DATABASE
IF NOT EXISTS `pusan_board_db` /*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_unicode_ci */;
USE `pusan_board_db`;

-- 테이블 pusan_board_db.board_table 구조 내보내기
CREATE TABLE
IF NOT EXISTS `board_table`
(
  `board_idx` int
(11) NOT NULL AUTO_INCREMENT,
  `board_name` varchar
(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY
(`board_idx`),
  UNIQUE KEY `board_unique`
(`board_name`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 테이블 pusan_board_db.user_table 구조 내보내기
CREATE TABLE
IF NOT EXISTS `user_table`
(
  `user_idx` int
(11) NOT NULL AUTO_INCREMENT,
  `user_name` char
(10) COLLATE utf8_unicode_ci NOT NULL,
  `user_id` varchar
(100) COLLATE utf8_unicode_ci NOT NULL,
  `user_pw` varchar
(100) COLLATE utf8_unicode_ci NOT NULL,
  PRIMARY KEY
(`user_idx`),
  UNIQUE KEY `user_unique`
(`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 테이블 데이터 pusan_board_db.board_table:~4 rows (대략적) 내보내기
/*!40000 ALTER TABLE `board_table` DISABLE KEYS */;
INSERT INTO `board_table` (`
board_idx`,
`board_name
`) VALUES
(4, '스포츠 게시판'),
(2, '유머 게시판'),
(1, '자유 게시판'),
(3, '정치 게시판');
/*!40000 ALTER TABLE `board_table` ENABLE KEYS */;

-- 테이블 pusan_board_db.content_table 구조 내보내기
CREATE TABLE
IF NOT EXISTS `content_table`
(
  `content_idx` int
(11) NOT NULL AUTO_INCREMENT,
  `content_subject` varchar
(500) COLLATE utf8_unicode_ci NOT NULL,
  `content_date` date NOT NULL,
  `content_writer_idx` int
(11) NOT NULL,
  `content_text` varchar
(500) COLLATE utf8_unicode_ci NOT NULL,
  `content_file` varchar
(500) COLLATE utf8_unicode_ci DEFAULT NULL,
  `content_board_idx` int
(11) NOT NULL,
  PRIMARY KEY
(`content_idx`),
  KEY `content_fk1`
(`content_writer_idx`),
  KEY `content_fk2`
(`content_board_idx`),
  CONSTRAINT `content_fk1` FOREIGN KEY
(`content_writer_idx`) REFERENCES `user_table`
(`user_idx`),
  CONSTRAINT `content_fk2` FOREIGN KEY
(`content_board_idx`) REFERENCES `board_table`
(`board_idx`)
) ENGINE=InnoDB AUTO_INCREMENT=694 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

-- 테이블 데이터 pusan_board_db.user_table:~4 rows (대략적) 내보내기
/*!40000 ALTER TABLE `user_table` DISABLE KEYS */;
INSERT INTO `user_table` (`
user_idx`,
`user_name
`, `user_id`, `user_pw`) VALUES
(1, 'dongja', 'dongja', '1234');
/*!40000 ALTER TABLE `user_table` ENABLE KEYS */;

-- 테이블 데이터 pusan_board_db.content_table:~691 rows (대략적) 내보내기
/*!40000 ALTER TABLE `content_table` DISABLE KEYS */;
INSERT INTO `content_table` (`
content_idx`,
`content_subject
`, `content_date`,
 `content_writer_idx`, `content_text`, `content_file`, `content_board_idx`) VALUES
(1, '자유', '2021-03-09', 1, '테스트', NULL, 1),
(2, '유머', '2021-03-09', 1, '테스트', NULL, 2),
(3, '정치', '2021-03-09', 1, '테스트', '1615266379헐크.jfif', 3),
(4, '스포츠', '2021-03-09', 1, '테스트', '1615266418헐크.jfif', 4)
/*!40000 ALTER TABLE `content_table` ENABLE KEYS */;






