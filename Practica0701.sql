
SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';


-- -----------------------------------------------------
-- Schema funkotienda
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `funkotienda` DEFAULT CHARACTER SET utf8mb3 ;
USE `funkotienda` ;

-- -----------------------------------------------------
-- Table `funkotienda`.`cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `funkotienda`.`cliente` (
  `num_socio` INT NOT NULL,
  `dni` VARCHAR(45) NOT NULL,
  `prestigio` VARCHAR(45) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellidos` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`num_socio`),
  UNIQUE INDEX `DNI_UNIQUE` (`dni` ASC) VISIBLE,
  UNIQUE INDEX `num_socio_UNIQUE` (`num_socio` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `funkotienda`.`jefe`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `funkotienda`.`jefe` (
  `jefe_id` INT NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellidos` VARCHAR(45) NOT NULL,
  `DNI` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`jefe_id`),
  UNIQUE INDEX `jefe_id_UNIQUE` (`jefe_id` ASC) VISIBLE,
  UNIQUE INDEX `DNI_UNIQUE` (`DNI` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `funkotienda`.`dependiente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `funkotienda`.`dependiente` (
  `dependiente_id` INT NOT NULL,
  `dni` VARCHAR(45) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellidos` VARCHAR(45) NOT NULL,
  `gerente_id` INT NULL DEFAULT NULL,
  `Jefe_jefe_id` INT NOT NULL,
  PRIMARY KEY (`dependiente_id`),
  UNIQUE INDEX `dependiente_id_UNIQUE` (`dependiente_id` ASC) VISIBLE,
  UNIQUE INDEX `dni_UNIQUE` (`dni` ASC) VISIBLE,
  INDEX `fk_Dependiente_Dependiente_idx` (`gerente_id` ASC) VISIBLE,
  INDEX `fk_Dependiente_Jefe1_idx` (`Jefe_jefe_id` ASC) VISIBLE,
  CONSTRAINT `fk_Dependiente_Dependiente`
    FOREIGN KEY (`gerente_id`)
    REFERENCES `funkotienda`.`dependiente` (`dependiente_id`),
  CONSTRAINT `fk_Dependiente_Jefe1`
    FOREIGN KEY (`Jefe_jefe_id`)
    REFERENCES `funkotienda`.`jefe` (`jefe_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `funkotienda`.`distribuidor`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `funkotienda`.`distribuidor` (
  `cif` VARCHAR(45) NOT NULL,
  `nombre_empresa` VARCHAR(45) NOT NULL,
  `frecuencia_entrega_mes` INT NOT NULL,
  PRIMARY KEY (`cif`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `funkotienda`.`funkopop`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `funkotienda`.`funkopop` (
  `funko_id` INT NOT NULL,
  `funko_nombre` VARCHAR(45) NOT NULL,
  `funko_franquicia` VARCHAR(45) NOT NULL,
  `funko_fecha` DATE NOT NULL,
  `funko_cantidad` INT NOT NULL,
  `funko_precio` INT NOT NULL,
  PRIMARY KEY (`funko_id`),
  UNIQUE INDEX `funko_id_UNIQUE` (`funko_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `funkotienda`.`distribuidor_funkopop`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `funkotienda`.`distribuidor_funkopop` (
  `Distribuidor_cif` VARCHAR(45) NOT NULL,
  `FunkoPop_funko_id` INT NOT NULL,
  PRIMARY KEY (`Distribuidor_cif`, `FunkoPop_funko_id`),
  INDEX `fk_Distribuidor_has_FunkoPop_FunkoPop1_idx` (`FunkoPop_funko_id` ASC) VISIBLE,
  INDEX `fk_Distribuidor_has_FunkoPop_Distribuidor1_idx` (`Distribuidor_cif` ASC) VISIBLE,
  CONSTRAINT `fk_Distribuidor_has_FunkoPop_Distribuidor1`
    FOREIGN KEY (`Distribuidor_cif`)
    REFERENCES `funkotienda`.`distribuidor` (`cif`),
  CONSTRAINT `fk_Distribuidor_has_FunkoPop_FunkoPop1`
    FOREIGN KEY (`FunkoPop_funko_id`)
    REFERENCES `funkotienda`.`funkopop` (`funko_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `funkotienda`.`juegomesa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `funkotienda`.`juegomesa` (
  `juegomesa_id` INT NOT NULL,
  `sistema` VARCHAR(45) NOT NULL,
  `precio` VARCHAR(45) NOT NULL,
  `genero` VARCHAR(45) NOT NULL,
  `cantidad` INT NOT NULL,
  PRIMARY KEY (`juegomesa_id`),
  UNIQUE INDEX `juegomesa_id_UNIQUE` (`juegomesa_id` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `funkotienda`.`distribuidor_juegomesa`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `funkotienda`.`distribuidor_juegomesa` (
  `Distribuidor_cif` VARCHAR(45) NOT NULL,
  `JuegoMesa_juegomesa_id` INT NOT NULL,
  PRIMARY KEY (`Distribuidor_cif`, `JuegoMesa_juegomesa_id`),
  INDEX `fk_Distribuidor_has_JuegoMesa_JuegoMesa1_idx` (`JuegoMesa_juegomesa_id` ASC) VISIBLE,
  INDEX `fk_Distribuidor_has_JuegoMesa_Distribuidor1_idx` (`Distribuidor_cif` ASC) VISIBLE,
  CONSTRAINT `fk_Distribuidor_has_JuegoMesa_Distribuidor1`
    FOREIGN KEY (`Distribuidor_cif`)
    REFERENCES `funkotienda`.`distribuidor` (`cif`),
  CONSTRAINT `fk_Distribuidor_has_JuegoMesa_JuegoMesa1`
    FOREIGN KEY (`JuegoMesa_juegomesa_id`)
    REFERENCES `funkotienda`.`juegomesa` (`juegomesa_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `funkotienda`.`funkopop_cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `funkotienda`.`funkopop_cliente` (
  `FunkoPop_funko_id` INT NOT NULL,
  `Cliente_num_socio` INT NOT NULL,
  PRIMARY KEY (`FunkoPop_funko_id`, `Cliente_num_socio`),
  INDEX `fk_FunkoPop_has_Cliente_Cliente1_idx` (`Cliente_num_socio` ASC) VISIBLE,
  INDEX `fk_FunkoPop_has_Cliente_FunkoPop1_idx` (`FunkoPop_funko_id` ASC) VISIBLE,
  CONSTRAINT `fk_FunkoPop_has_Cliente_Cliente1`
    FOREIGN KEY (`Cliente_num_socio`)
    REFERENCES `funkotienda`.`cliente` (`num_socio`),
  CONSTRAINT `fk_FunkoPop_has_Cliente_FunkoPop1`
    FOREIGN KEY (`FunkoPop_funko_id`)
    REFERENCES `funkotienda`.`funkopop` (`funko_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `funkotienda`.`gamemaster`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `funkotienda`.`gamemaster` (
  `master_id` INT NOT NULL,
  `dni` VARCHAR(45) NOT NULL,
  `nombre` VARCHAR(45) NOT NULL,
  `apellidos` VARCHAR(45) NOT NULL,
  `Jefe_jefe_id` INT NOT NULL,
  PRIMARY KEY (`master_id`),
  UNIQUE INDEX `master_id_UNIQUE` (`master_id` ASC) VISIBLE,
  UNIQUE INDEX `dni_UNIQUE` (`dni` ASC) VISIBLE,
  INDEX `fk_GameMaster_Jefe1_idx` (`Jefe_jefe_id` ASC) VISIBLE,
  CONSTRAINT `fk_GameMaster_Jefe1`
    FOREIGN KEY (`Jefe_jefe_id`)
    REFERENCES `funkotienda`.`jefe` (`jefe_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `funkotienda`.`juegomesa_cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `funkotienda`.`juegomesa_cliente` (
  `JuegoMesa_juegomesa_id` INT NOT NULL,
  `Cliente_num_socio` INT NOT NULL,
  PRIMARY KEY (`JuegoMesa_juegomesa_id`, `Cliente_num_socio`),
  INDEX `fk_JuegoMesa_has_Cliente_Cliente1_idx` (`Cliente_num_socio` ASC) VISIBLE,
  INDEX `fk_JuegoMesa_has_Cliente_JuegoMesa1_idx` (`JuegoMesa_juegomesa_id` ASC) VISIBLE,
  CONSTRAINT `fk_JuegoMesa_has_Cliente_Cliente1`
    FOREIGN KEY (`Cliente_num_socio`)
    REFERENCES `funkotienda`.`cliente` (`num_socio`),
  CONSTRAINT `fk_JuegoMesa_has_Cliente_JuegoMesa1`
    FOREIGN KEY (`JuegoMesa_juegomesa_id`)
    REFERENCES `funkotienda`.`juegomesa` (`juegomesa_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `funkotienda`.`partidarol`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `funkotienda`.`partidarol` (
  `partida_id` INT NOT NULL,
  `fecha` VARCHAR(45) NOT NULL,
  `num_participantes` VARCHAR(45) NOT NULL,
  `GameMaster_master_id` INT NOT NULL,
  `JuegoMesa_juegomesa_id` INT NOT NULL,
  PRIMARY KEY (`partida_id`),
  UNIQUE INDEX `partida_id_UNIQUE` (`partida_id` ASC) VISIBLE,
  INDEX `fk_PartidaRol_GameMaster1_idx` (`GameMaster_master_id` ASC) VISIBLE,
  INDEX `fk_PartidaRol_JuegoMesa1_idx` (`JuegoMesa_juegomesa_id` ASC) VISIBLE,
  CONSTRAINT `fk_PartidaRol_GameMaster1`
    FOREIGN KEY (`GameMaster_master_id`)
    REFERENCES `funkotienda`.`gamemaster` (`master_id`),
  CONSTRAINT `fk_PartidaRol_JuegoMesa1`
    FOREIGN KEY (`JuegoMesa_juegomesa_id`)
    REFERENCES `funkotienda`.`juegomesa` (`juegomesa_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


-- -----------------------------------------------------
-- Table `funkotienda`.`partidarol_cliente`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `funkotienda`.`partidarol_cliente` (
  `PartidaRol_partida_id` INT NOT NULL,
  `Cliente_num_socio` INT NOT NULL,
  PRIMARY KEY (`PartidaRol_partida_id`, `Cliente_num_socio`),
  INDEX `fk_PartidaRol_has_Cliente_Cliente1_idx` (`Cliente_num_socio` ASC) VISIBLE,
  INDEX `fk_PartidaRol_has_Cliente_PartidaRol1_idx` (`PartidaRol_partida_id` ASC) VISIBLE,
  CONSTRAINT `fk_PartidaRol_has_Cliente_Cliente1`
    FOREIGN KEY (`Cliente_num_socio`)
    REFERENCES `funkotienda`.`cliente` (`num_socio`),
  CONSTRAINT `fk_PartidaRol_has_Cliente_PartidaRol1`
    FOREIGN KEY (`PartidaRol_partida_id`)
    REFERENCES `funkotienda`.`partidarol` (`partida_id`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb3;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;





INSERT INTO cliente (num_socio, dni, prestigio, nombre, apellidos) VALUES
(1234, '12345678A', 'ORO', 'Pepe', 'Arenas'),
(2345, '23456789X', 'ORO', 'Curro', 'Curriendo'),
(4634, '23456789Z', 'ORO', 'Tomas', 'Tomasito'),
(8764, '23456789Y', 'PLATA', 'Mago', 'Malvado'),
(9976, '23456789E', 'PLATA', 'Duende', 'Martinez'),
(9966, '23456789R', 'PLATA', 'Armando', 'Bronca'),
(3583, '23456789F', 'BRONCE', 'El Elegido', 'Sanchez'),
(8421, '23456789K', 'BRONCE', 'Curro Malvado', 'Andando'),
(8422, '26260073F', 'ORO', 'Victawel', 'Vera'),
(3345, '34567890P', 'BRONCE', 'Jorge', 'Profe');

SELECT * FROM cliente;


INSERT INTO dependiente (dependiente_id, dni, nombre, apellidos, gerente_id, Jefe_jefe_id) VALUES
(1, '45678901D', 'Jorge', 'SQL', 1, 545),
(2, '56789012E', 'Kiko', 'Cook', 2, 545),
(4, '67890173F', 'Medinilla', 'Goat', 1, 545),
(5, '27890123F', 'Salva', 'X', 1, 546),
(6, '17890183F', 'Gloria', 'Dollars', 2, 546),
(7, '67890193F', 'Alejandra', 'Rocio', 2, 546);

SELECT * FROM cliente;
SELECT * FROM dependiente;
SELECT * FROM jefe;
SELECT * FROM distribuidor;

INSERT INTO jefe (jefe_id, nombre, apellidos, DNI) VALUES
(545, 'TheGrefg', 'Fortnite', '90123456I'),
(546, 'Gemita', 'Cabrales', '89012345H');

SELECT * FROM jefe;


INSERT INTO distribuidor (cif, nombre_empresa, frecuencia_entrega_mes) VALUES
('A12345678', 'Monstruos SA', 2),
('B23456789', 'Skibidi SL', 3),
('C34567890', 'Sigmas Distribution COOP',3 ),
('D34564590', 'Curro Holdings SL', 6);


SELECT * FROM distribuidor;


INSERT INTO funkopop (funko_id, funko_nombre, funko_franquicia, funko_fecha, funko_cantidad, funko_precio ) VALUES
(10, 'Batman', 'DC', '2023-01-01', 100, 15.99),
(20, 'Superman', 'DC', '2023-02-01', 150, 12.99),
(25, 'Chun Li', 'Fortnite', '2023-02-02', 1500, 19.99),
(26, 'Kai Cenat', 'Twitch', '2023-02-03', 20, 10.99),
(24, 'KSI', 'Twitch', '2023-02-28', 50, 2.40),
(28, 'Isabel Ayuso', 'Fortnite', '2024-03-03', 150, 15.99),
(34, 'Pinguino', 'DC', '2020-03-01', 4, 330.99),
(37, 'Bob Cavernicola', 'Spongebob', '2023-06-28', 200, 12.99),
(38, 'Goku Super Chayanne 5', 'Esencia', '2023-12-25', 500, 9.99);

SELECT * FROM cliente;
SELECT * FROM dependiente;
SELECT * FROM jefe;
SELECT * FROM distribuidor;
SELECT *  from funkopop;


INSERT INTO gamemaster (master_id, dni, nombre, apellidos, Jefe_jefe_id) VALUES
(81, '88901234G', 'Carlos', 'Maria', 545),
(82, '89012345H', 'Javi', 'Fernandez', 545),
(83, '80123456I', 'Sergio', 'Suarez', 546);


SELECT * FROM cliente;
SELECT * FROM dependiente;
SELECT * FROM jefe;
SELECT * FROM distribuidor;
SELECT *  from funkopop;
SELECT * FROM gamemaster;


INSERT INTO juegomesa (juegomesa_id, sistema, precio, genero, cantidad) VALUES
(100, 'Skibidis & Toilets', 50.00, 'RPG', 200),
(200, 'Rizz', 35.00, 'Estrategia', 200),
(700, 'Hundirla ', 100.00, 'Cyberpunk', 200),
(400, 'Maxxing', 36.00, 'Clasico', 201),
(500, 'Mewing Tramposo', 50.00, 'Estrategia', 199),
(600, 'Edge Runners', 25.00, 'Cyberpunk', 2),
(300, 'Sigmapoly', 25.00, 'Clasico', 700);

SELECT * FROM cliente;
SELECT * FROM dependiente;
SELECT * FROM jefe;
SELECT * FROM distribuidor;
SELECT *  from funkopop;
SELECT * FROM gamemaster;
select * from juegomesa;

INSERT INTO partidarol (partida_id, fecha, num_participantes, GameMaster_master_id, JuegoMesa_juegomesa_id) VALUES
(600, '2023-04-01', 15, 81, 100),
(601, '2023-05-01', 24, 83, 500),
(602, '2023-06-01', 60, 82, 300);


SELECT * FROM cliente;
SELECT * FROM dependiente;
SELECT * FROM jefe;
SELECT * FROM distribuidor;
SELECT *  from funkopop;
SELECT * FROM gamemaster;
select * from juegomesa;
select * from partidarol;

INSERT INTO partidarol_cliente (PartidaRol_partida_id, Cliente_num_socio) VALUES
(600, 1234),
(600, 9976),
(600, 3583),
(601, 8764),
(601, 2345),
(602, 9966),
(602, 8422),
(602, 4634);

SELECT * FROM cliente;
SELECT * FROM dependiente;
SELECT * FROM jefe;
SELECT * FROM distribuidor;
SELECT *  from funkopop;
SELECT * FROM gamemaster;
select * from juegomesa;
select * from partidarol;
Select * from partidarol_cliente;

INSERT INTO distribuidor_funkopop (distribuidor_cif, FunkoPop_funko_id) VALUES
('A12345678', 10),
('B23456789', 20),
('D34564590', 24),
('C34567890', 25);

SELECT * FROM cliente;
SELECT * FROM dependiente;
SELECT * FROM jefe;
SELECT * FROM distribuidor;
SELECT *  from funkopop;
SELECT * FROM gamemaster;
select * from juegomesa;
select * from partidarol;
Select * from partidarol_cliente;
Select * from distribuidor_funkopop;


INSERT INTO distribuidor_juegomesa (distribuidor_cif, JuegoMesa_juegomesa_id) VALUES
('A12345678', 100),
('B23456789', 200),
('C34567890', 700);


SELECT * FROM cliente;
SELECT * FROM dependiente;
SELECT * FROM jefe;
SELECT * FROM distribuidor;
SELECT *  from funkopop;
SELECT * FROM gamemaster;
select * from juegomesa;
select * from partidarol;
Select * from partidarol_cliente;
Select * from distribuidor_funkopop;
Select * from distribuidor_juegomesa;


INSERT INTO funkopop_cliente (FunkoPop_funko_id, Cliente_num_socio) VALUES
(10, '1234'),
(20, '2345' ),
(25, '3345' );

SELECT * FROM cliente;
SELECT * FROM dependiente;
SELECT * FROM jefe;
SELECT * FROM distribuidor;
SELECT *  from funkopop;
SELECT * FROM gamemaster;
select * from juegomesa;
select * from partidarol;
Select * from partidarol_cliente;
Select * from distribuidor_funkopop;
Select * from distribuidor_juegomesa;
Select * from funkopop_cliente;


ALTER TABLE `funkotienda`.`cliente`
  MODIFY COLUMN `num_socio` INT NOT NULL AUTO_INCREMENT,
  ADD PRIMARY KEY (`num_socio`);




SELECT * FROM cliente;
SELECT * FROM dependiente;
SELECT * FROM jefe;
SELECT * FROM distribuidor;
SELECT *  from funkopop;
SELECT * FROM gamemaster;
select * from juegomesa;
select * from partidarol;
Select * from partidarol_cliente;
Select * from distribuidor_funkopop;
Select * from distribuidor_juegomesa;
Select * from funkopop_cliente;





