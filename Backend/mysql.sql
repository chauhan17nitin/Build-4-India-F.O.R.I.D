CREATE TABLE `user` (
	`user_name` varchar(50) NOT NULL,
	`first_name` varchar(50) NOT NULL,
	`last_name` varchar(50),
	`dob` TIMESTAMP,
	`password` varchar(150) NOT NULL,
	`address` varchar(150),
	`mobile` INT(15),
	`city` varchar(60) NOT NULL,
	`state` varchar(60) NOT NULL,
	PRIMARY KEY (`user_name`)
);

CREATE TABLE `fields` (
	`field_id` INT(100) NOT NULL AUTO_INCREMENT,
	`user_name` varchar(50) NOT NULL,
	`field_name` varchar(100) NOT NULL UNIQUE,
	`length` INT(100) NOT NULL,
	`width` INT(100) NOT NULL,
	PRIMARY KEY (`field_id`,`user_name`)
);

CREATE TABLE `crop_history` (
	`user_name` varchar(50) NOT NULL,
	`field_id` INT(100) NOT NULL,
	`sowing_time` TIMESTAMP NOT NULL,
	`crop_id` INT(100) NOT NULL,
	`harvesting_time` TIMESTAMP,
	`total_yield` INT(100),
	`amount_sold` INT(100),
	PRIMARY KEY (`user_name`,`field_id`,`sowing_time`)
);

CREATE TABLE `crops` (
	`crop_id` INT(100) NOT NULL AUTO_INCREMENT,
	`crop_name` varchar(100) NOT NULL UNIQUE,
	`seasonality` varchar(100) NOT NULL ,
	`crop_wiki` varchar(1000) NOT NULL,
	PRIMARY KEY (`crop_id`)
);

CREATE TABLE `scan_history` (
	`user_name` varchar(50) NOT NULL,
	`field_id` INT(100) NOT NULL,
	`scan_time` TIMESTAMP NOT NULL,
	`percent_damage` INT(100) NOT NULL,
	`spray_status` BOOLEAN(10) NOT NULL,
	`crop_id` INT(100) NOT NULL,
	PRIMARY KEY (`user_name`,`field_id`,`scan_time`)
);

ALTER TABLE `fields` ADD CONSTRAINT `fields_fk0` FOREIGN KEY (`user_name`) REFERENCES `user`(`user_name`);

ALTER TABLE `crop_history` ADD CONSTRAINT `crop_history_fk0` FOREIGN KEY (`user_name`) REFERENCES `user`(`user_name`);

ALTER TABLE `crop_history` ADD CONSTRAINT `crop_history_fk1` FOREIGN KEY (`field_id`) REFERENCES `fields`(`field_id`);

ALTER TABLE `crop_history` ADD CONSTRAINT `crop_history_fk2` FOREIGN KEY (`crop_id`) REFERENCES `crops`(`crop_id`);

ALTER TABLE `scan_hostory` ADD CONSTRAINT `scan_hostory_fk0` FOREIGN KEY (`user_name`) REFERENCES `user`(`user_name`);

ALTER TABLE `scan_hostory` ADD CONSTRAINT `scan_hostory_fk1` FOREIGN KEY (`field_id`) REFERENCES `fields`(`field_id`);

ALTER TABLE `scan_hostory` ADD CONSTRAINT `scan_hostory_fk2` FOREIGN KEY (`crop_id`) REFERENCES `crops`(`crop_id`);


