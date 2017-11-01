-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema dblaberinto
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema dblaberinto
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `dblaberinto` DEFAULT CHARACTER SET utf8 ;
USE `dblaberinto` ;

-- -----------------------------------------------------
-- Table `dblaberinto`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `dblaberinto`.`usuario` (
  `usuario` VARCHAR(10) NOT NULL,
  `password` VARCHAR(45) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellido` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`usuario`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

INSERT INTO `dblaberinto`.`usuario` (`usuario`, `password`, `nombre`, `apellido`) VALUES ('rodrija', '1234', 'Javier', 'Rodriguez');
INSERT INTO `dblaberinto`.`usuario` (`usuario`, `password`, `nombre`, `apellido`) VALUES ('merome', '1234', 'Melisa', 'Romero');
INSERT INTO `dblaberinto`.`usuario` (`usuario`, `password`, `nombre`, `apellido`) VALUES ('dasanto', '1234', 'Damian', 'Santos');
