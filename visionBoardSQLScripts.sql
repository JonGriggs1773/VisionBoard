-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema vision_board
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `vision_board` ;

-- -----------------------------------------------------
-- Schema vision_board
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `vision_board` DEFAULT CHARACTER SET utf8 ;
USE `vision_board` ;

-- -----------------------------------------------------
-- Table `vision_board`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vision_board`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `first_name` VARCHAR(255) NOT NULL,
  `last_name` VARCHAR(255) NOT NULL,
  `email` VARCHAR(255) NOT NULL,
  `password` VARCHAR(255) NOT NULL,
  `username` VARCHAR(255) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 2
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `vision_board`.`long_term_goals`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vision_board`.`long_term_goals` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `goal_date` DATE NOT NULL,
  `is_complete` ENUM('Yes', 'No') NOT NULL,
  `image` BLOB NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_long_term_goals_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_long_term_goals_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `vision_board`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `vision_board`.`short_term_goals`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vision_board`.`short_term_goals` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `goal_date` DATE NOT NULL,
  `is_complete` ENUM('Yes', 'No') NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `long_term_goal_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_short_term_goals_long_term_goals_idx` (`long_term_goal_id` ASC) VISIBLE,
  INDEX `fk_short_term_goals_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_short_term_goals_long_term_goals`
    FOREIGN KEY (`long_term_goal_id`)
    REFERENCES `vision_board`.`long_term_goals` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_short_term_goals_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `vision_board`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `vision_board`.`tasks`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `vision_board`.`tasks` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `title` VARCHAR(45) NOT NULL,
  `description` VARCHAR(255) NOT NULL,
  `goal_date` DATE NOT NULL,
  `is_complete` ENUM('Yes', 'No') NOT NULL,
  `created_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `short_term_goal_id` INT NOT NULL,
  `user_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `fk_tasks_short_term_goals1_idx` (`short_term_goal_id` ASC) VISIBLE,
  INDEX `fk_tasks_users1_idx` (`user_id` ASC) VISIBLE,
  CONSTRAINT `fk_tasks_short_term_goals1`
    FOREIGN KEY (`short_term_goal_id`)
    REFERENCES `vision_board`.`short_term_goals` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE,
  CONSTRAINT `fk_tasks_users1`
    FOREIGN KEY (`user_id`)
    REFERENCES `vision_board`.`users` (`id`)
    ON DELETE CASCADE
    ON UPDATE CASCADE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
