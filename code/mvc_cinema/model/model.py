from mysql import connector

class Model:
    """
    *********************************************
    * A data model with MYSQL for a cinema DB *
    *********************************************
    """

    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d
    
    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor() #Para consultas u operaciones en MySQL

    def close_db(self):
        self.cnx.close()
    

    """
    ****************
    * Admin methods *
    ****************
    """

    # Registro de administradores
    def create_admin(self, name, flname, slname, email, password, phone, birthday):
        try: 
            sql = 'INSERT INTO admins (`a_fname`, `a_lname1`, `a_lname2`, `a_email`, `a_password`, `a_phone`, `a_birthday`) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            vals = (name, flname, slname, email, password, phone, birthday)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def admin_login(self, email, password):
        try:
            sql = 'SELECT id_admin, a_fname, a_lname1, a_lname2, a_email, a_phone, a_birthday FROM admins WHERE a_email = %s AND a_password = %s'
            vals = (email, password)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
        
    def read_an_admin(self, id_admin):
        try:
            sql = 'SELECT id_admin, a_fname, a_lname1, a_lname2, a_email, a_phone, a_birthday FROM admins WHERE id_admin = %s'
            vals = (id_admin)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_admins(self):
        try:
            sql = 'SELECT id_admin, a_fname, a_lname1, a_lname2, a_email, a_phone, a_birthday FROM admins'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_admins_birthday_month(self, month):
        try:
            sql = 'SELECT id_admin, a_fname, a_lname1, a_lname2, a_email, a_phone, a_birthday FROM admins WHERE MONTH(a_birthday) = %s'
            vals = (month,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_admin(self, fields, vals):
        try:
            sql = 'UPDATE admins SET '+','.join(fields)+' WHERE id_admin = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_admin(self, id_admin):
        try:
            sql = 'DELETE FROM admins WHERE id_admin = %s'
            vals = (id_admin)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    """
    ****************
    * User methods *
    ****************
    """

    # Regsitro de usuario
    def create_user(self, name, flname, slname, email, password, phone, birthday):
        try: 
            sql = 'INSERT INTO users (`u_fname`, `u_lname1`, `u_lname2`, `u_email`, `u_password`, `u_phone`, `u_birthday`) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            vals = (name, flname, slname, email, password, phone, birthday)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    # Login para el usuario (cliente)
    def user_login(self, email, password):
        try:
            sql = 'SELECT id_user, u_fname, u_lname1, u_lname2, u_email, u_phone, u_birthday FROM users WHERE u_email = %s AND u_password = %s'
            vals = (email, password)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    # Solo los admin pueden ver un usuario en especifico
    def read_a_user(self, id_user):
        try:
            sql = 'SELECT id_user, u_fname, u_lname1, u_lname2, u_email, u_phone, u_birthday FROM users WHERE id_user = %s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
     

    #Solo admins pueden ver todos los usuarios
    def read_all_users(self):
        try:
            sql = 'SELECT id_user, u_fname, u_lname1, u_lname2, u_email, u_phone, u_birthday FROM users'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_users_birthday_month(self, month):
        try:
            sql = 'SELECT id_user, u_fname, u_lname1, u_lname2, u_email, u_phone, u_birthday FROM users WHERE MONTH(u_birthday) = %s'
            vals = (month,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_user(self, fields, vals):
        try:
            sql = 'UPDATE users SET '+','.join(fields)+' WHERE id_user = %s AND u_email = %s AND u_password = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    #Solo adminiostrador puede dar de baja a un usuario por cuestiones de seguridad
    def delete_user(self, id_user):
        try:
            sql = 'DELETE FROM users WHERE id_user = %s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ****************
    * Movie methods *
    ****************
    """

    def create_movie(self, title, director, sypnosis, clasification, genre, language, country, premiere):
        try: 
            sql = 'INSERT INTO movies (`m_title`, `m_director`, `m_synopsis`, `m_clasification`, `m_genre`, `m_language`, `m_country`, `m_datepremiere`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'
            vals = (title, director, sypnosis, clasification, genre, language, country, premiere)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_movie(self, id_movie):
        try:
            sql = 'SELECT * FROM movies WHERE id_movie = %s'
            vals = (id_movie,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_movies(self):
        try:
            sql = 'SELECT * FROM movies'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_movies_director(self, director):
        try:
            sql = 'SELECT  * FROM movies WHERE m_director = %s'
            vals = (director,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err


    def read_movies_year(self, year):
        try:
            sql = 'SELECT  * FROM movies WHERE YEAR(m_datepremiere) = %s'
            vals = (year,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_movie(self, fields, vals):
        try:
            sql = 'UPDATE movies SET '+','.join(fields)+' WHERE id_movie = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_movie(self, id_movie):
        try:
            sql = 'DELETE FROM movies WHERE id_movie = %s'
            vals = (id_movie,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ****************
    * Hall methods *
    ****************
    """

    def create_hall(self, no_raws, no_seats):
        try: 
            sql = 'INSERT INTO halls (`h_raws`, `h_seats`) VALUES (%s, %s)'
            vals = (no_raws, no_seats)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_hall(self, id_hall):
        try:
            sql = 'SELECT * FROM halls WHERE id_hall = %s'
            vals = (id_hall,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_halls(self):
        try:
            sql = 'SELECT * FROM halls'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err


    def update_hall(self, fields, vals):
        try:
            sql = 'UPDATE halls SET '+','.join(fields)+' WHERE id_hall = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_hall(self, id_hall):
        try:
            sql = 'DELETE FROM halls WHERE id_hall = %s'
            vals = (id_hall,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    """
    ****************
    * Seat methods *
    ****************
    """

    def create_seat(self, id_seat, stype):
        try: 
            sql = 'INSERT INTO seats (`id_seat`, `s_type`) VALUES (%s, %s)'
            vals = (id_seat, stype)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_all_seats(self):
        try:
            sql = 'SELECT * FROM seats'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err


    def update_seat(self, fields, vals):
        try:
            sql = 'UPDATE seats SET '+','.join(fields)+' WHERE id_seat = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_seat(self, id_seat):
        try:
            sql = 'DELETE FROM seat WHERE id_seat = %s'
            vals = (id_seat,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    *********************
    * Functions methods *
    **********************
    """

    def create_function(self, id_movie, id_hall, typefunc, hour, date, duration, price):
        try: 
            sql = 'INSERT INTO functions (`id_movie`, `id_hall`, `f_typefun`, `f_hour`, `f_date`, `f_duration`, `f_price`) VALUES (%s, %s, %s, %s, %s, %s, %s)'
            vals = (id_movie, id_hall, typefunc, hour, date, duration, price)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_function(self, id_function):
        try:
            sql = 'SELECT functions.*, movies.m_title FROM functions JOIN movies ON functions.id_movie = movies.id_movie AND functions.id_function = %s'
            vals = (id_function,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_functions(self):
        try:
            sql = 'SELECT functions.*, movies.m_title FROM functions JOIN movies ON functions.id_movie = movies.id_movie'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_functions_hour(self, hour):
        try:
            sql = 'SELECT functions.*, movies.m_title FROM functions JOIN movies ON functions.id_movie = movies.id_movie AND functions.f_hour = %s'
            vals = (hour,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_functions_date(self, date):
        try:
            sql = 'SELECT functions.*, movies.m_title FROM functions JOIN movies ON functions.id_movie = movies.id_movie AND functions.f_date = %s'
            vals = (date,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_function(self, fields, vals):
        try:
            sql = 'UPDATE functions SET '+','.join(fields)+' WHERE id_function = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_function(self, id_function):
        try:
            sql = 'DELETE FROM functions WHERE id_function = %s'
            vals = (id_function,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    """
    *********************
    * ticket methods *
    **********************
    """

    def create_ticket(self, id_function, id_seat):
        try: 
            sql = 'INSERT INTO tickets(id_function, id_seat, t_total) SELECT functions.id_function, seats.id_seat, functions.f_price FROM functions, seats WHERE functions.id_function = %s AND seats.id_seat = %s'
            vals = (id_function, id_seat)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_ticket(self, id_ticket):
        try:
            sql = 'SELECT tickets.id_ticket, movies.m_title, functions.f_hour, functions.f_date, tickets.id_seat, tickets.t_total FROM tickets JOIN functions ON functions.id_function = tickets.id_function JOIN movies ON movies.id_movie = functions.id_movie AND tickets.id_ticket = %s'
            vals = (id_ticket,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_tickets(self):
        try:
            sql = 'SELECT tickets.id_ticket, movies.m_title, functions.f_hour, functions.f_date, tickets.id_seat, tickets.t_total FROM tickets JOIN functions ON functions.id_function = tickets.id_function JOIN movies ON movies.id_movie = functions.id_movie'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_tickets_function(self, id_function):
        try:
            sql = 'SELECT tickets.id_ticket, movies.m_title, functions.f_hour, functions.f_date, tickets.id_seat, tickets.t_total FROM tickets JOIN functions ON functions.id_function = tickets.id_function JOIN movies ON movies.id_movie = functions.id_movie AND id_function = %s'
            vals = (id_function,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_ticket(self, fields, vals):
        try:
            sql = 'UPDATE tickets SET '+','.join(fields)+' WHERE id_ticket = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_ticket(self, id_ticket):
        try:
            sql = 'DELETE FROM tickets WHERE id_ticket = %s'
            vals = (id_ticket,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    """
    *********************
    * Purchase methods *
    *********************
    """
    def create_purchase(self, id_admin, id_user, date, hour, total):
        try:
            sql = 'INSERT INTO purchases (`id_admin`, `id_user`, `p_date`, `p_hour`, `p_total`) VALUES (%s, %s, %s, %s, %s)'
            vals = (id_admin, id_user, date, hour, total)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            id_purchase = self.cursor.lastrowid
            return id_purchase
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_a_purchase(self, id_purchase):
        try:
            sql = 'SELECT purchases.*, admins.a_fname, admins.a_lname1,admins.a_lname2, users.u_fname, users.u_lname1, users.u_lname2 FROM purchases JOIN admins ON admins.id_admin = purchases.id_admin JOIN users ON users.id_user = purchases.id_user AND purchases.id_purchase = %s'
            vals = (id_purchase,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_purchases(self): #Caution with large amount of data
        try:
            sql = 'SELECT purchases.*, admins.a_fname, admins.a_lname1,admins.a_lname2, users.u_fname, users.u_lname1, users.u_lname2 FROM purchases JOIN admins ON admins.id_admin = purchases.id_admin JOIN users ON users.id_user = purchases.id_user'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_purchases_date(self, date):
        try:
            sql = 'SELECT purchases.*, admins.a_fname, admins.a_lname1,admins.a_lname2, users.u_fname, users.u_lname1, users.u_lname2 FROM purchases JOIN admins ON admins.id_admin = purchases.id_admin JOIN users ON users.id_user = purchases.id_user WHERE purchases.p_date=%s'
            vals = (date,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_purchases_user(self, id_user):
        try:
            sql = 'SELECT purchases.*, admins.a_fname, admins.a_lname1,admins.a_lname2, users.u_fname, users.u_lname1, users.u_lname2 FROM purchases JOIN admins ON admins.id_admin = purchases.id_admin JOIN users ON users.id_user = purchases.id_user WHERE purchases.id_user=%s'
            vals = (id_user,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_purchase(self, fields, vals):
        try:
            sql = 'UPDATE purchases SET '+','.join(fields)+' WHERE id_purchase = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_purchase(self, id_purchase):
        try:
            sql = 'DELETE FROM purchases WHERE id_purchase = %s'
            vals = (id_purchase,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    """
    ****************************
    * Purchase details methods *
    ****************************
    """
    def create_purchase_detail(self, id_purchase, id_ticket, pd_total):
        try:
            sql = 'INSERT INTO purchase_details (`id_purchase`, `id_ticket`, `pd_total`) VALUES (%s, %s, %s)'
            vals = (id_purchase, id_ticket, pd_total)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def read_a_purchase_detail(self, id_purchase, id_ticket):
        try:
            sql = 'SELECT tickets.id_ticket, tickets.id_function, movies.m_title, tickets.id_seat, purchase_details.pd_total FROM purchase_details JOIN tickets ON purchase_details.id_ticket = tickets.id_ticket JOIN functions ON functions.id_function = tickets.id_function JOIN movies ON movies.id_movie = functions.id_movie and purchase_details.id_purchase = %s and purchase_details.id_ticket = %s'
            vals = (id_purchase, id_ticket)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_purchase_details(self, id_order):
        try:
            sql = 'SELECT tickets.id_ticket, tickets.id_function, movies.m_title, tickets.id_seat, purchase_details.pd_total FROM purchase_details JOIN tickets ON purchase_details.id_ticket = tickets.id_ticket JOIN functions ON functions.id_function = tickets.id_function JOIN movies ON movies.id_movie = functions.id_movie and purchase_details.id_purchase = %s'
            vals = (id_order,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def update_purchase_details(self, fields, vals):
        try:
            sql = 'UPDATE purchase_details SET '+','.join(fields)+' WHERE id_purchase = %s and id_ticket = %s'
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def delete_purchase_details(self, id_purchase, id_ticket):
        try:
            sql = 'DELETE FROM purchase_details WHERE id_purchase = %s and id_ticket = %s'
            vals = (id_purchase, id_ticket)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err


    """
    ******************************
    * seat of a function methods *
    *******************************
    """

    def create_seats_for_function(self, id_function):
        try:
            sql = 'INSERT INTO function_seat(id_function, id_seat) SELECT functions.id_function, seats.id_seat FROM functions, seats WHERE functions.id_function = %s'
            vals = (id_function,)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def update_seats_for_function(self, id_function, id_seat):
        try:
            sql = 'UPDATE function_seat SET fs_status = 0 WHERE id_function = %s AND id_seat = %s'
            vals = (id_function, id_seat)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
        
    def read_avaliable_seats(self, id_function):  
        try:
            sql = 'SELECT  * FROM function_seat WHERE id_function = %s'
            vals = (id_function,)
            self.cursor.execute(sql, vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err