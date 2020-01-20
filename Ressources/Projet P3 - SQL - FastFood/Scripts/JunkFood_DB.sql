DROP DATABASE IF EXISTS JunkFood;
CREATE OR REPLACE DATABASE JunkFood;
USE JunkFood;

CREATE TABLE Restaurants (
	id INT NOT NULL AUTO_INCREMENT,
	code_postal CHAR(5) NOT NULL UNIQUE,
	ville VARCHAR(12) NOT NULL UNIQUE,
	pays_id INT NOT NULL,
	capacite INT NOT NULL,
	espace_enfant TINYINT NOT NULL,
	borneCB TINYINT NOT NULL,
	handicap TINYINT NOT NULL,
	parking TINYINT NOT NULL,	
	PRIMARY KEY (id)
);

CREATE TABLE Postes (
	id INT NOT NULL AUTO_INCREMENT,
	ind_id INT NOT NULL,
	resto_id INT NOT NULL,
	poste ENUM('directeur','manager','employe') NOT NULL,
	domaine ENUM('cuisine','caisse'),
	superieur INT,
	duree_mois DECIMAL(10.1) NOT NULL,
	en_cours TINYINT NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE SalairesNotes (
	ind_id INT NOT NULL,
	annee CHAR(4) NOT NULL,
	salaire DECIMAL(10.2) NOT NULL,
	note INT,
	UNIQUE (ind_id, annee)
);

CREATE TABLE Personnel (
	id INT NOT NULL AUTO_INCREMENT,
	prenom VARCHAR(255) NOT NULL,
	nom VARCHAR(255) NOT NULL,
	adresse VARCHAR(255) NOT NULL,
	experience FLOAT NOT NULL,
	rib VARCHAR(255) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE Orders (
	id INT NOT NULL AUTO_INCREMENT,
	vendeur_id INT NOT NULL,
	resto_id INT NOT NULL,
	date_heure DATETIME,
	paiement CHAR(6) NOT NULL,
	somme double NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE Orders_items (
	order_id INT NOT NULL,
	item_id INT NOT NULL,
	quantite INT NOT NULL,
	UNIQUE (order_id, item_id)
);

CREATE TABLE Items (
	id INT NOT NULL AUTO_INCREMENT,
	nom VARCHAR(255) NOT NULL,
	type_item ENUM('plat','boisson','dessert','menu') NOT NULL,
	taille_boisson ENUM('S','M','L'),
	prix DOUBLE NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE Menus (
	id INT NOT NULL,
	plat INT NOT NULL,
	dessert INT NOT NULL,
	boisson INT NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE Pays (
	id INT NOT NULL,
	pays VARCHAR(255) NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE Cartes (
	pays_id INT NOT NULL,
	item_id INT,
	UNIQUE (pays_id,item_id)
);

CREATE TABLE Stocks (
	ing_id INT NOT NULL,
	rest_id INT NOT NULL,
	unites INT,
	UNIQUE (ing_id, rest_id)
);

CREATE TABLE Ingredients (
	id INT NOT NULL AUTO_INCREMENT,
	nom VARCHAR(255) NOT NULL,
	prix DOUBLE NOT NULL,
	PRIMARY KEY (id)
);

CREATE TABLE Recettes (
	item_id INT NOT NULL,
	ing_id INT NOT NULL,
	unites DOUBLE NOT NULL,
	UNIQUE (item_id, ing_id)
);

ALTER TABLE Restaurants ADD CONSTRAINT Restaurants_fk0 FOREIGN KEY (pays_id) REFERENCES Pays(id) ON DELETE CASCADE;

ALTER TABLE Postes ADD CONSTRAINT Postes_fk0 FOREIGN KEY (ind_id) REFERENCES Personnel(id) ON DELETE CASCADE;
ALTER TABLE Postes ADD CONSTRAINT Postes_fk1 FOREIGN KEY (resto_id) REFERENCES Restaurants(id) ON DELETE CASCADE;
ALTER TABLE Postes ADD CONSTRAINT Postes_fk2 FOREIGN KEY (superieur) REFERENCES Personnel(id) ON DELETE CASCADE;

ALTER TABLE SalairesNotes ADD CONSTRAINT Salaires_fk0 FOREIGN KEY (ind_id) REFERENCES Personnel(id) ON DELETE CASCADE;

ALTER TABLE Orders ADD CONSTRAINT Orders_fk1 FOREIGN KEY (resto_id) REFERENCES Restaurants(id) ON DELETE CASCADE;

ALTER TABLE Orders_items ADD CONSTRAINT Orders_items_fk0 FOREIGN KEY (order_id) REFERENCES Orders(id) ON DELETE CASCADE;
ALTER TABLE Orders_items ADD CONSTRAINT Orders_items_fk1 FOREIGN KEY (item_id) REFERENCES Items(id) ON DELETE CASCADE;

ALTER TABLE Cartes ADD CONSTRAINT Cartes_fk0 FOREIGN KEY (pays_id) REFERENCES Pays(id) ON DELETE CASCADE;
ALTER TABLE Cartes ADD CONSTRAINT Cartes_fk1 FOREIGN KEY (item_id) REFERENCES Items(id) ON DELETE CASCADE;

ALTER TABLE Menus ADD CONSTRAINT Menus_fk0 FOREIGN KEY (plat) REFERENCES Items(id) ON DELETE CASCADE;
ALTER TABLE Menus ADD CONSTRAINT Menus_fk1 FOREIGN KEY (dessert) REFERENCES Items(id) ON DELETE CASCADE;
ALTER TABLE Menus ADD CONSTRAINT Menus_fk2 FOREIGN KEY (boisson) REFERENCES Items(id) ON DELETE CASCADE;

ALTER TABLE Stocks ADD CONSTRAINT Stocks_fk0 FOREIGN KEY (ing_id) REFERENCES Ingredients(id) ON DELETE CASCADE;
ALTER TABLE Stocks ADD CONSTRAINT Stocks_fk1 FOREIGN KEY (rest_id) REFERENCES Restaurants(id) ON DELETE CASCADE;

ALTER TABLE Recettes ADD CONSTRAINT Recettes_fk0 FOREIGN KEY (item_id) REFERENCES Items(id) ON DELETE CASCADE;
ALTER TABLE Recettes ADD CONSTRAINT Recettes_fk1 FOREIGN KEY (ing_id) REFERENCES Ingredients(id) ON DELETE CASCADE;
