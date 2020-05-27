DROP DATABASE IF EXISTS cinema_carranza;

# Create the DB
CREATE DATABASE IF NOT EXISTS cinema_carranza;

# Select the database to work with
USE cinema_carranza;

CREATE TABLE IF NOT EXISTS admins(
	id_admin INT NOT NULL AUTO_INCREMENT,
    a_fname VARCHAR(50) NOT NULL,
    a_lname1 VARCHAR(50) NOT NULL,
    a_lname2 VARCHAR(50) NOT NULL,
    a_email VARCHAR(50) NOT NULL,
    a_password VARCHAR(20) NOT NULL,
    a_phone VARCHAR(13) NOT NULL,
    a_birthday DATE NOT NULL,
    UNIQUE(a_email),
    PRIMARY KEY(id_admin)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS users(
	id_user INT NOT NULL AUTO_INCREMENT,
    u_fname VARCHAR(50) NOT NULL,
    u_lname1 VARCHAR(50) NOT NULL,
    u_lname2 VARCHAR(50) NOT NULL,
    u_email VARCHAR(50) NOT NULL,
    u_password VARCHAR(20) NOT NULL,
    u_phone VARCHAR(13) NOT NULL,
    u_birthday DATE NOT NULL,
    UNIQUE(u_email),
    PRIMARY KEY(id_user)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS movies(
	id_movie INT NOT NULL AUTO_INCREMENT,
    m_title VARCHAR(50) NOT NULL,
    m_director VARCHAR(50) NOT NULL,
    m_synopsis VARCHAR(200) NOT NULL,
    m_clasification VARCHAR(50) NOT NULL,
    m_genre VARCHAR(20) NOT NULL,
    m_language VARCHAR(20) NOT NULL,
    m_country VARCHAR(50) NOT NULL,
    m_datepremiere DATE NOT NULL,
    PRIMARY KEY(id_movie)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS seats(
	id_seat VARCHAR(3) NOT NULL,
    s_type VARCHAR(50) NOT NULL,
    PRIMARY KEY(id_seat)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS halls(
	id_hall INT NOT NULL AUTO_INCREMENT,
    h_raws INT NOT NULL,
    h_seats INT NOT NULL,
    PRIMARY KEY(id_hall)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS functions(
	id_function INT NOT NULL AUTO_INCREMENT,
    id_movie INT NOT NULL,
    id_hall INT NOT NULL,
    f_typefun VARCHAR(30) NOT NULL,
    f_hour TIME NOT NULL,
    f_date DATE NOT NULL,
    f_duration INT NOT NULL,
    f_price INT NOT NULL,
    UNIQUE(id_hall, f_hour, f_date),
    PRIMARY KEY(id_function),
    CONSTRAINT fkid_movie FOREIGN KEY(id_movie)
		REFERENCES movies(id_movie)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
	CONSTRAINT fkid_hall FOREIGN KEY(id_hall)
		REFERENCES halls(id_hall)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS function_seat(
	id_function INT NOT NULL,
	id_seat VARCHAR(3) NOT NULL,
    fs_status BOOLEAN DEFAULT 1 NOT NULL,
    PRIMARY KEY(id_function, id_seat),
    CONSTRAINT fkid_function FOREIGN KEY(id_function)
		REFERENCES functions(id_function)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
	CONSTRAINT fkid_seat FOREIGN KEY(id_seat)
		REFERENCES seats(id_seat)
        ON DELETE CASCADE
        ON UPDATE CASCADE 
)ENGINE = INNODB;


CREATE TABLE IF NOT EXISTS purchases(
	id_purchase INT NOT NULL AUTO_INCREMENT,
    id_admin INT NOT NULL,
    id_user INT NOT NULL,
    p_date DATE NOT NULL,
    p_hour TIME NOT NULL,
    p_total INT NOT NULL,
    PRIMARY KEY(id_purchase),
    CONSTRAINT fkid_admin FOREIGN KEY(id_admin)
		REFERENCES admins(id_admin)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
    CONSTRAINT fkid_user FOREIGN KEY(id_user)
		REFERENCES users(id_user)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;


CREATE TABLE IF NOT EXISTS tickets(
	id_ticket INT NOT NULL AUTO_INCREMENT,
    id_function INT NOT NULL,
    id_seat VARCHAR(3) NOT NULL,
    t_total INT NOT NULL,
    UNIQUE(id_function, id_seat),
    PRIMARY KEY(id_ticket),
	CONSTRAINT fkdpid_function FOREIGN KEY(id_function)
		REFERENCES functions(id_function)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
	CONSTRAINT fkdpid_seat FOREIGN KEY(id_seat)
		REFERENCES seats(id_seat)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;


CREATE TABLE IF NOT EXISTS tickets_purchases(
	id_purchase INT NOT NULL,
    id_ticket INT NOT NULL,
    tp_total INT NOT NULL,
    UNIQUE(id_ticket),
    PRIMARY KEY(id_purchase, id_ticket),
    CONSTRAINT fktpid_purchase FOREIGN KEY(id_purchase)
		REFERENCES purchases(id_purchase)
        ON DELETE CASCADE
        ON UPDATE CASCADE,
	CONSTRAINT fktpid_ticket FOREIGN KEY(id_ticket)
		REFERENCES tickets(id_ticket)
        ON DELETE CASCADE
        ON UPDATE CASCADE
)ENGINE = INNODB;



# SELECT * FROM admins WHERE MONTH(a_birthday) = 1;
# SELECT * FROM users WHERE MONTH(u_birthday) = 12;
# SELECT purchases.*, admins.a_fname, admins.a_lname1, admins.a_lname2, users.u_fname, users.u_lname1, users.u_lname2 FROM purchases JOIN admins ON admins.id_admin = purchases.id_admin JOIN users ON users.id_user = purchases.id_user;
# SELECT id_admin, a_fname, a_lname1, a_lname2, a_email, a_phone, a_birthday FROM admins WHERE id_admin = 1 AND a_email = 'jjco@gmail.com' AND a_password = '123';
# SELECT id_admin, a_fname, a_lname1, a_lname2, a_email, a_phone, a_birthday FROM admins;
# SELECT id_user, u_fname, u_lname1, u_lname2, u_email, u_phone, u_birthday FROM users;
# SELECT * FROM movies WHERE id_movie = 2;
# SELECT  * FROM movies WHERE YEAR (m_datepremiere) = 2019;
# SELECT * FROM halls;
# SELECT functions.*, movies.m_title FROM functions JOIN movies ON functions.id_movie = movies.id_movie AND functions.id_function = 1;
# SELECT functions.*, movies.m_title FROM functions JOIN movies ON functions.id_movie = movies.id_movie;
# SELECT functions.*, movies.m_title FROM functions JOIN movies ON functions.id_movie = movies.id_movie AND functions.f_hour = '16:45:00';
# SELECT functions.*, movies.m_title FROM functions JOIN movies ON functions.id_movie = movies.id_movie AND functions.f_date = '2020-05-27';

# SELECT purchases.*, admins.a_fname, admins.a_lname1, admins.a_lname2, users.u_fname, users.u_lname1, users.u_lname2 FROM purchases JOIN admins ON admins.id_admin = purchases.id_admin JOIN users ON users.id_user = purchases.id_user AND purchases.id_purchase = 1;
# SELECT purchases.*, admins.a_fname, admins.a_lname1, admins.a_lname2, users.u_fname, users.u_lname1, users.u_lname2 FROM purchases JOIN admins ON admins.id_admin = purchases.id_admin JOIN users ON users.id_user = purchases.id_user AND purchases.id_user = 2;
# SELECT tickets.id_ticket, tickets.id_purchase, users.u_fname, users.u_lname1, users.u_lname2, movies.m_title, functions.id_function, functions.f_hour, functions.f_date, functions.f_price, tickets.id_seat, tickets.t_total FROM tickets JOIN functions ON functions.id_function = tickets.id_function JOIN movies ON movies.id_movie = functions.id_movie JOIN purchases ON purchases.id_purchase = tickets.id_purchase JOIN users ON purchases.id_user = users.id_user AND tickets.id_ticket = 1;
# SELECT tickets.id_ticket, tickets.id_purchase, users.u_fname, users.u_lname1, users.u_lname2, movies.m_title, functions.f_hour, functions.f_date, functions.f_price, tickets.id_seat, tickets.t_total FROM tickets JOIN functions ON functions.id_function = tickets.id_function JOIN movies ON movies.id_movie = functions.id_movie JOIN purchases ON purchases.id_purchase = tickets.id_purchase JOIN users ON purchases.id_user = users.id_user;
# SELECT purchases.id_purchase,admins.a_fname, admins.a_lname1, admins.a_lname2, users.u_fname, users.u_lname1, users.u_lname2, purchases.p_hour, purchases.p_date, purchases.p_total  FROM purchases JOIN admins ON admins.id_admin = purchases.id_admin JOIN users ON users.id_user = purchases.id_user;

# SELECT * FROM seats;

# SELECT function_seat.id_function, movies.m_title, function_seat.id_seat, function_seat.fs_status FROM function_seat JOIN functions ON functions.id_function = function_seat.id_function JOIN movies ON movies.id_movie = functions.id_movie AND function_seat.id_function = 1 AND function_seat.fs_status = 1;

# SELECT function_seat.id_function, movies.m_title, function_seat.id_seat, function_seat.fs_status FROM function_seat JOIN functions ON functions.id_function = function_seat.id_function JOIN movies ON movies.id_movie = functions.id_movie AND function_seat.id_function = 1 AND function_seat.id_seat = 'A1';

#SELECT id_purchase, COUNT(*), SUM(t_total) FROM tickets GROUP BY id_purchase;

# Llenar una funcion de asientos
# INSERT INTO function_seat(id_function, id_seat) SELECT functions.id_function, seats.id_seat FROM functions, seats WHERE functions.id_function = 1;
# SELECT * FROM function_seat;

# Crear boleto

# Creamos Administradores
INSERT INTO admins (a_fname, a_lname1, a_lname2, a_email, a_password, a_phone, a_birthday)VALUES('Jonathan', 'Corona', 'Ortega', 'jjco@gmail.com', '1234', '4646519093', '1998-01-31');
INSERT INTO admins (a_fname, a_lname1, a_lname2, a_email, a_password, a_phone, a_birthday)VALUES('Diego', 'Rosas', 'González', 'diego@gmail.com', '1234', '4451129673', '1997-12-12');
INSERT INTO admins (a_fname, a_lname1, a_lname2, a_email, a_password, a_phone, a_birthday)VALUES('Jose', 'Vilchis', 'Mar', 'abelmar@gmail.com', '1234', '4641556390', '1997-09-12');

# Creamos usuarios
INSERT INTO users (u_fname, u_lname1, u_lname2, u_email, u_password, u_phone, u_birthday)VALUES('Ivan', 'Rocha', 'Rios', 'ivan@gmail.com', '1234', '4451129673', '1997-12-12');
INSERT INTO users (u_fname, u_lname1, u_lname2, u_email, u_password, u_phone, u_birthday)VALUES('Braulio', 'Mac', 'Chipe', 'mac@gmail.com', '1234', '4451129673', '1997-12-12');
INSERT INTO users (u_fname, u_lname1, u_lname2, u_email, u_password, u_phone, u_birthday)VALUES('Adan', 'Hernandez', 'Baena', 'adan@gmail.com', '1234', '4451129673', '1997-12-12');

# Creamos Peliculas
INSERT INTO movies (m_title,m_director,m_synopsis,m_clasification,m_genre,m_language,m_country,m_datepremiere) VALUES ('ParasitoS','Un koreano', 'peli','Adultos','drama','coreano','corea del sur', '2019-01-01');
INSERT INTO movies (m_title,m_director,m_synopsis,m_clasification,m_genre,m_language,m_country,m_datepremiere) VALUES ('EndGame','Los hermanos ruso', 'se muere iron man','B','acción','Inglés','USA', '2019-04-27');

# Creamos Asientos
INSERT INTO seats VALUES ('A1', 'Discapacidad');
INSERT INTO seats VALUES ('A2', 'Discapacidad');
INSERT INTO seats VALUES ('A3', 'Normal');
INSERT INTO seats VALUES ('A4', 'Normal');
INSERT INTO seats VALUES ('A5', 'Discapacidad');
INSERT INTO seats VALUES ('B1', 'Normal');
INSERT INTO seats VALUES ('B2', 'Normal');
INSERT INTO seats VALUES ('B3', 'Normal');
INSERT INTO seats VALUES ('B4', 'Normal');
INSERT INTO seats VALUES ('B5', 'Normal');
INSERT INTO seats VALUES ('C1', 'Normal');
INSERT INTO seats VALUES ('C2', 'Normal');
INSERT INTO seats VALUES ('C3', 'Normal');
INSERT INTO seats VALUES ('C4', 'Normal');
INSERT INTO seats VALUES ('C5', 'Normal');
INSERT INTO seats VALUES ('D1', 'Normal');
INSERT INTO seats VALUES ('D2', 'Normal');
INSERT INTO seats VALUES ('D3', 'Normal');
INSERT INTO seats VALUES ('D4', 'Normal');
INSERT INTO seats VALUES ('D5', 'Normal');

# Creamos salas
INSERT INTO halls (h_raws,h_seats) VALUES(4,20);
INSERT INTO halls (h_raws,h_seats) VALUES(4,20);
INSERT INTO halls (h_raws,h_seats) VALUES(4,20);
INSERT INTO halls (h_raws,h_seats) VALUES(4,20);
INSERT INTO halls (h_raws,h_seats) VALUES(4,20);

# Creamos una funcion 
INSERT INTO functions(id_movie, id_hall, f_typefun, f_hour, f_date, f_duration, f_price) VALUES (1,1,'Estreno','16:45:00','2020-05-29', 112, 50);
INSERT INTO functions(id_movie, id_hall, f_typefun, f_hour, f_date, f_duration, f_price) VALUES (1,2,'Estreno','16:45:00','2020-05-29', 112, 100);
INSERT INTO functions(id_movie, id_hall, f_typefun, f_hour, f_date, f_duration, f_price) VALUES (2,2,'Estreno','16:45:00','2020-05-27', 112, 100);

# Agregamos asientos a una funcion
INSERT INTO function_seat(id_function, id_seat) SELECT functions.id_function, seats.id_seat FROM functions, seats WHERE functions.id_function = 1 ;
SELECT function_seat.id_function, movies.m_title, function_seat.id_seat, function_seat.fs_status FROM function_seat JOIN functions ON functions.id_function = function_seat.id_function JOIN movies ON movies.id_movie = functions.id_movie AND function_seat.id_function = 1 AND function_seat.fs_status = 0;
SELECT * FROM function_seat;
# Creamos un boleto
#INSERT INTO tickets (id_function,id_seat,t_total) VALUES (1,'A1',100);
#INSERT INTO tickets (id_function,id_seat,t_total) VALUES (1,'A2',100);
#INSERT INTO tickets (id_function,id_seat,t_total) VALUES (1,'D5',100);
INSERT INTO tickets(id_function, id_seat, t_total) SELECT functions.id_function, seats.id_seat, functions.f_price FROM functions, seats WHERE functions.id_function = 1 AND seats.id_seat = 'A4';
INSERT INTO tickets(id_function, id_seat, t_total) SELECT functions.id_function, seats.id_seat, functions.f_price FROM functions, seats WHERE functions.id_function = 1 AND seats.id_seat = 'A2';
INSERT INTO tickets(id_function, id_seat, t_total) SELECT functions.id_function, seats.id_seat, functions.f_price FROM functions, seats WHERE functions.id_function = 1 AND seats.id_seat = 'D5';

INSERT INTO tickets(id_function, id_seat, t_total) SELECT functions.id_function, seats.id_seat, functions.f_price FROM functions, seats WHERE functions.id_function = 2 AND seats.id_seat = 'A2';
INSERT INTO tickets(id_function, id_seat, t_total) SELECT functions.id_function, seats.id_seat, functions.f_price FROM functions, seats WHERE functions.id_function = 2 AND seats.id_seat = 'D5';
#SELECT * from tickets;

#SELECT tickets.id_ticket, movies.m_title, functions.f_hour, functions.f_date, functions.f_price, tickets.id_seat, tickets.t_total FROM tickets JOIN functions ON functions.id_function = tickets.id_function JOIN movies ON movies.id_movie = functions.id_movie AND tickets.id_ticket = 1;
#SELECT tickets.id_ticket, movies.m_title, functions.f_hour, functions.f_date, functions.f_price, tickets.id_seat, tickets.t_total FROM tickets JOIN functions ON functions.id_function = tickets.id_function JOIN movies ON movies.id_movie = functions.id_movie;

# Creamos una compra
INSERT INTO purchases(id_admin,id_user,p_date,p_hour,p_total) VALUES (1,3, '2020-05-24', '12:00:00',0);
INSERT INTO purchases(id_admin,id_user,p_date,p_hour,p_total) VALUES (2,1, '2020-05-24', '12:00:00',0);
INSERT INTO purchases(id_admin,id_user,p_date,p_hour,p_total) VALUES (3,2, '2020-05-24', '12:00:00',0);

# Linking Table Compra-Boleto
INSERT INTO tickets_purchases(id_purchase, id_ticket, tp_total) SELECT purchases.id_purchase, tickets.id_ticket, tickets.t_total FROM purchases, tickets WHERE purchases.id_purchase = 1  AND tickets.id_ticket = 1;
INSERT INTO tickets_purchases(id_purchase, id_ticket, tp_total) SELECT purchases.id_purchase, tickets.id_ticket, tickets.t_total FROM purchases, tickets WHERE purchases.id_purchase = 1  AND tickets.id_ticket = 2;
INSERT INTO tickets_purchases(id_purchase, id_ticket, tp_total) SELECT purchases.id_purchase, tickets.id_ticket, tickets.t_total FROM purchases, tickets WHERE purchases.id_purchase = 1  AND tickets.id_ticket = 3;

INSERT INTO tickets_purchases(id_purchase, id_ticket, tp_total) SELECT purchases.id_purchase, tickets.id_ticket, tickets.t_total FROM purchases, tickets WHERE purchases.id_purchase = 2  AND tickets.id_ticket = 4;
INSERT INTO tickets_purchases(id_purchase, id_ticket, tp_total) SELECT purchases.id_purchase, tickets.id_ticket, tickets.t_total FROM purchases, tickets WHERE purchases.id_purchase = 2  AND tickets.id_ticket = 5;
SELECT * FROM tickets_purchases;

SELECT * FROM purchases;
# SELECT id_purchase, SUM(tp_total) AS total FROM tickets_purchases GROUP BY (id_purchase);
UPDATE purchases SET p_total = (SELECT SUM(tp_total) FROM tickets_purchases WHERE id_purchase = 1 GROUP BY (id_purchase)) WHERE id_purchase = 1;
UPDATE purchases SET p_total = (SELECT SUM(tp_total) FROM tickets_purchases WHERE id_purchase = 2 GROUP BY (id_purchase)) WHERE id_purchase = 2;
#SELECT * FROM purchases;

#SELECT tickets.id_ticket, movies.m_title, functions.f_hour, functions.f_date, functions.f_price, tickets.id_seat, tickets.t_total FROM tickets JOIN functions ON functions.id_function = tickets.id_function JOIN movies ON movies.id_movie = functions.id_movie AND tickets.id_ticket = 1;

#SELECT tickets_purchases.id_purchase, tickets_purchases.id_ticket, users.u_fname, users.u_lname1, users.u_lname2, tickets_purchases.tp_total, tickets.id_seat, tickets.id_function,  movies.m_title, functions.f_hour, functions.f_date FROM tickets_purchases JOIN purchases ON purchases.id_purchase = tickets_purchases.id_purchase JOIN users ON users.id_user = purchases.id_user  JOIN tickets ON tickets_purchases.id_ticket = tickets.id_ticket JOIN functions ON functions.id_function = tickets.id_function JOIN movies ON movies.id_movie = functions.id_movie AND tickets_purchases.id_ticket = 1;

