from model.model import Model
from view.view import View
from datetime import date, datetime

class Controller:
    """
    *******************************
    * A controller for a library DB *
    *******************************
    """
    def __init__(self):
        self.model = Model()
        self.view = View()

    def start(self):
        self.view.start()
        self.main_menu()

    """
    ***********************
    * General controllers *
    ***********************
    """

    def main_menu(self):
        o = '0'
        while o != '3':
            self.view.main_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.login_menu()
            elif o == '2':
                self.signin_menu()
            elif o == '3':
                self.view.end()
            else:
                self.view.not_valid_option()
        return
    
    def update_lists(self, fs, vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields,vals

    def login_menu(self):
        o = '0'
        while o != '3':
            self.view.login_menu()
            self.view.option('3')
            o = input()
            if o == '1': #Administrador
                loginadmin = self.admin_login()
                if loginadmin == True:
                    self.admin_menu()
            elif o == '2':#Cliente
                loginuser = self.user_login()
                if loginuser == True:
                    self.user_menu()
            elif o == '3':
                return
            else:
                self.view.not_valid_option()
        return

    def signin_menu(self):
        o = '0'
        secret = ''
        while o != '3':
            self.view.signin_menu()
            self.view.option('3')
            o = input()
            if o == '1':#Administrador
                print('Ingrese la clave para registro de administrador')
                secret = input()
                if secret == 'CineMemex':
                    self.create_admin()
                    return
                else:
                    print('La clave es incorrecta')
                    return
            elif o == '2': #Cliente
                self.create_user()
                return

            elif o == '3':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_user(self):
        self.view.ask('Nombre: ')
        name = input()
        self.view.ask('Apellido paterno: ')
        lname1 = input()
        self.view.ask('Apellido materno: ')
        lname2 = input()
        self.view.ask('Email: ')
        email = input()
        self.view.ask('Contraseña: ')
        password = input()
        self.view.ask('Telefono: ')
        phone = input()
        self.view.ask('Cumpleaños(AAAA-MM-DD): ')
        birthday = input()
        return [name,lname1,lname2,email,password,phone,birthday]

    """
    ****************************
    * Controllers for Admins *
    ****************************
    """
    def admin_menu(self):
        o = '0'
        while o != '9':
            self.view.admin_menu()
            self.view.option('9')
            o = input()
            if o == '1':
                self.admin_movies_menu()
            elif o == '2':
                self.admin_halls_menu()
            elif o == '3':
                self.admin_functions_menu()
            elif o == '4':
                self.admin_buy_menu()
            elif o == '5':
                self.admin_admins_menu()
            elif o == '6': 
                self.admin_users_menu()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
    
    def admin_admins_menu(self):
        o = '0'
        while o != '6':
            self.view.admin_admins_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.read_an_admin()
            elif o == '2':
                self.read_all_admins()
            elif o == '3':
                self.read_admins_birthday_month()
            elif o == '4':
                self.update_admin()
            elif o == '5':
                self.delete_admin()
            elif o == '6': 
                return
            else:
                self.view.not_valid_option()
    
    def admin_users_menu(self):
        o = '0'
        while o != '6':
            self.view.admin_users_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.read_a_user()
            elif o == '2':
                self.read_all_users()
            elif o == '3':
                self.read_users_birthday_month()
            elif o == '4':
                self.update_user()
            elif o == '5':
                self.delete_user()
            elif o == '6': 
                return
            else:
                self.view.not_valid_option()
        
    """
    ****************************
    * Admins *
    ****************************
    """
    def create_admin(self):
        name,lname1,lname2,email,password,phone,birthday = self.ask_user()
        out = self.model.create_admin(name,lname1,lname2,email,password,phone,birthday)
        if out == True:
            self.view.ok(name+' '+lname1+' '+lname2, 'creó su cuenta de administrador')
        else:
            self.view.error('Error al agregar administrador')
        return
    
    def admin_login(self):
        self.view.ask('Correo: ')
        email = input()
        self.view.ask('Contraseña: ')
        password = input()
        admin = self.model.admin_login(email,password)
        if type(admin) == tuple:
            login = True
            self.view.show_user_header(' Datos del usuario '+email+' ')
            self.view.show_a_user(admin)
            self.view.show_user_midder()
            self.view.show_user_footer()
            return login
        
        else:
            if admin == None:
                self.view.error('El administrador no existe')
            else:
                self.view.error('Error al leer el usuario')
        return
    
    def read_an_admin(self):
        self.view.ask('ID Admin: ')
        id_admin = input()
        admin = self.model.read_an_admin(id_admin)
        if type(admin) == tuple:
            self.view.show_user_header(' Datos del administrador '+id_admin+' ')
            self.view.show_a_user(admin)
            self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            if admin == None:
                self.view.error('EL ADMIN NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER AL ADMIN. REVISA.')
        return

    def read_all_admins(self):
        admins = self.model.read_all_admins()
        if type(admins) == list:
            self.view.show_user_header(' Todos los administradores ')
            for admin in admins:
                self.view.show_a_user(admin)
                self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ADMINS. REVISA.')
        return

    def read_admins_birthday_month(self):
        self.view.ask('Mes (Numero(01,02,...)): ')
        mes = input()
        admins = self.model.read_admins_birthday_month(mes)
        if type(admins) == list:
            self.view.show_user_header('Admins del mes '+mes+' ')
            for admin in admins:
                self.view.show_a_user(admin)
                self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ADMINS. REVISA.')
        return

    def update_admin(self):
        self.view.ask('ID deL ADMIN a modificar: ')
        id_admin = input()
        admin = self.model.read_an_admin(id_admin)
        if type(admin) == tuple:
            self.view.show_user_header(' Datos del admin '+id_admin+' ')
            self.view.show_a_user(admin)
            self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            if admin == None:
                self.view.error('EL ADMIN NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER AL ADMIN. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_user()
        fields, vals = self.update_lists(['a_fname', 'a_lname1', 'a_lname2', 'a_email', 'a_password', 'a_phone', 'a_birthday'], whole_vals)
        vals.append(id_admin)
        vals = tuple(vals)
        out = self.model.update_admin(fields, vals)
        if out == True:
            self.view.ok(id_admin, 'se actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR AL ADMIN. REVISA.')
        return

    def delete_admin(self):
        self.view.ask('Id del ADMIN a borrar: ')
        id_admin = input()
        count = self.model.delete_admin(id_admin)
        if count != 0:
            self.view.ok(id_admin, 'se borro')
        else:
            if count == 0:
                self.view.error('EL ADMIN NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR AL ADMIN. REVISA.')
        return
        
    """
    ****************************
    * User *
    ****************************
    """
    def read_a_user(self):
        self.view.ask('ID cliente: ')
        id_user = input()
        user = self.model.read_a_user(id_user)
        if type(user) == tuple:
            self.view.show_user_header(' Datos del cliente '+id_user+' ')
            self.view.show_a_user(user)
            self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            if user == None:
                self.view.error('EL CLIENTE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER AL CLIENTE. REVISA.')
        return

    def read_all_users(self):
        users = self.model.read_all_users()
        if type(users) == list:
            self.view.show_user_header(' Todos los usuarios ')
            for user in users:
                self.view.show_a_user(user)
                self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS CLIENTES. REVISA.')
        return

    def read_users_birthday_month(self):
        self.view.ask('Mes (Numero(01,02,...)): ')
        mes = input()
        users = self.model.read_users_birthday_month(mes)
        if type(users) == list:
            self.view.show_user_header('Clientes del mes '+mes+' ')
            for user in users:
                self.view.show_a_user(user)
                self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS CLIENTES . REVISA.')
        return

    def update_user(self):
        self.view.ask('ID deL CLIENTE a modificar: ')
        id_user = input()
        user = self.model.read_a_user(id_user)
        if type(user) == tuple:
            self.view.show_user_header(' Datos del cliente '+id_user+' ')
            self.view.show_a_user(user)
            self.view.show_user_midder()
            self.view.show_user_footer()
        else:
            if user == None:
                self.view.error('EL CLIENTE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER AL CLIENTE. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_user()
        fields, vals = self.update_lists(['u_fname', 'u_lname1', 'u_lname2', 'u_email', 'u_password', 'u_phone', 'u_birthday'], whole_vals)
        vals.append(id_user)
        vals = tuple(vals)
        out = self.model.update_user(fields, vals)
        if out == True:
            self.view.ok(id_user, 'se actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR AL CLIENTE. REVISA.')
        return

    def delete_user(self):
        self.view.ask('Id del CLIENTE a borrar: ')
        id_user = input()
        count = self.model.delete_user(id_user)
        if count != 0:
            self.view.ok(id_user, 'se borro')
        else:
            if count == 0:
                self.view.error('EL CLIENTE NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR AL CLIENTE. REVISA.')
        return


    """
    ****************************
    * Controllers for Users *
    ****************************
    """

    def user_menu(self):
        o = '0'
        while o != '4':
            self.view.user_menu()
            self.view.option('4')
            o = input()
            if o == '1': 
                self.user_movies_menu()
            elif o == '2':
                self.user_functions_menu()
            elif o == '3':
                self.admin_buy_menu()
            elif o == '4': 
                return
            else:
                self.view.not_valid_option()

    
    def create_user(self):
        name,lname1,lname2,email,password,phone,birthday = self.ask_user()
        out = self.model.create_user(name,lname1,lname2,email,password,phone,birthday)
        if out == True:
            self.view.ok(name+' '+lname1+' '+lname2, 'creó su cuenta de cliente')
        else:
            self.view.error('Error al agregar usuario')
        return
    
    def user_login(self):
        self.view.ask('Correo: ')
        email = input()
        self.view.ask('Contraseña: ')
        password = input()
        user = self.model.user_login(email,password)
        if type(user) == tuple:
            login = True
            self.view.show_user_header(' Datos del usuario '+email+' ')
            self.view.show_a_user(user)
            self.view.show_user_midder()
            self.view.show_user_footer()
            return login 
        else:
            if user == None:
                self.view.error('El usuario no existe')
            else:
                self.view.error('Error al leer el usuario')
        return
    
    """
    ****************************
    * Controllers for Movies *
    ****************************
    """
    def admin_movies_menu(self):
        o = '0'
        while o != '8':
            self.view.admin_movies_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.create_movie()
            elif o == '2':
                self.read_a_movie()
            elif o == '3':
                self.read_all_movies()
            elif o == '4': 
                self.read_movies_director()
            elif o == '5':
                self.read_movies_year()
            elif o == '6':
                self.update_movie()
            elif o == '7': 
                self.delete_movie()
            elif o == '8':
                return
            else:
                self.view.not_valid_option()
    
    def user_movies_menu(self):
        o = '0'
        while o != '5':
            self.view.user_movie_menu()
            self.view.option('5')
            o = input()
            if o == '1':
                self.read_a_movie()
            elif o == '2':
                self.read_all_movies()
            elif o == '3':
                self.read_movies_director()
            elif o == '4': 
                self.read_movies_year()
            elif o == '5':
                return
            else:
                self.view.not_valid_option()
    
    def ask_movie(self):
        self.view.ask('Titulo: ')
        title = input()
        self.view.ask('Director: ')
        director = input()
        self.view.ask('Sinopsis: ')
        sypnosis = input()
        self.view.ask('Clasificacion: ')
        clasification = input()
        self.view.ask('Genero: ')
        genre = input()
        self.view.ask('Lenguaje: ')
        language = input()
        self.view.ask('País: ')
        country = input()
        self.view.ask('Fecha de estreno: ')
        premiere = input()

        return [title, director, sypnosis, clasification, genre, language, country, premiere]

    def create_movie(self):
        title, director, sypnosis, clasification, genre, language, country, premiere = self.ask_movie()
        out = self.model.create_movie(title, director, sypnosis, clasification, genre, language, country, premiere)
        if out == True:
            self.view.ok(title+' de '+director, 'se agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR LA PELICULA. REVISA.')
        return

    def read_a_movie(self):
        self.view.ask('ID Pelicula: ')
        id_movie = input()
        movie = self.model.read_a_movie(id_movie)
        if type(movie) == tuple:
            self.view.show_movie_header(' Datos de la pelicula '+id_movie+' ')
            self.view.show_a_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if movie == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA.')
        return

    def read_all_movies(self):
        movies = self.model.read_all_movies()
        if type(movies) == list:
            self.view.show_movie_header(' Todos las peliculas ')
            for movie in movies:
                self.view.show_a_movie(movie)
                self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS PELICULAS. REVISA.')
        return

    def read_movies_director(self):
        self.view.ask('Director: ')
        director = input()
        movies = self.model.read_movies_director(director)
        if type(movies) == list:
            self.view.show_movie_header('Peliculas del director '+director+' ')
            for movie in movies:
                self.view.show_a_movie(movie)
                self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS PELICULAS. REVISA.')
        return

    def read_movies_year(self):
        self.view.ask('Año: ')
        year = input()
        movies = self.model.read_movies_year(year)
        if type(movies) == list:
            self.view.show_movie_header('Peliculas del año '+year+' ')
            for movie in movies:
                self.view.show_a_movie(movie)
                self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS PELICULAS. REVISA.')
        return

    def update_movie(self):
        self.view.ask('ID de la pelicula a modificar: ')
        id_movie = input()
        movie = self.model.read_a_movie(id_movie)
        if type(movie) == tuple:
            self.view.show_movie_header(' Datos de la pelicula '+id_movie+' ')
            self.view.show_a_movie(movie)
            self.view.show_movie_midder()
            self.view.show_movie_footer()
        else:
            if movie == None:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA PELICULA. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_movie()
        fields, vals = self.update_lists(['m_title','m_director','m_synopsis','m_clasification','m_genre','m_language','m_country','m_datepremiere'], whole_vals)
        vals.append(id_movie)
        vals = tuple(vals)
        out = self.model.update_movie(fields, vals)
        if out == True:
            self.view.ok(id_movie, 'se actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA PELICULA. REVISA.')
        return

    def delete_movie(self):
        self.view.ask('Id de la pelicula a borrar: ')
        id_movie = input()
        count = self.model.delete_movie(id_movie)
        if count != 0:
            self.view.ok(id_movie, 'se borro')
        else:
            if count == 0:
                self.view.error('LA PELICULA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA PELICULA. REVISA.')
        return

    
    """
    ****************************
    * Controllers for Halls *
    ****************************
    """

    def admin_halls_menu(self):
        o = '0'
        while o != '6':
            self.view.admin_halls_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_hall()
            elif o == '2':
                self.read_a_hall()
            elif o == '3':
                self.read_all_halls()
            elif o == '4': 
                self.update_hall()
            elif o == '5':
                self.delete_hall()
            elif o == '6':
                return
            else:
                self.view.not_valid_option()
    
    def ask_hall(self):
        self.view.ask('No. Filas: ')
        nraws = input()
        self.view.ask('No. Asiento: ')
        nseats = input()
        
        return [nraws, nseats]

    def create_hall(self):
        nraws, nseats = self.ask_hall()
        out = self.model.create_hall(nraws, nseats)
        if out == True:
            self.view.ok(nraws+' y '+nseats, 'se agregaron a la sala nueva')
        else:
            self.view.error('NO SE PUDO AGREGAR LA SALA. REVISA.')
        return

    def read_a_hall(self):
        self.view.ask('ID sala: ')
        id_hall = input()
        hall = self.model.read_a_hall(id_hall)
        if type(hall) == tuple:
            self.view.show_hall_header(' Datos de la sala '+id_hall+' ')
            self.view.show_a_hall(hall)
            self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            if hall == None:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA SALA. REVISA.')
        return
    
    

    def read_all_halls(self):
        halls = self.model.read_all_halls()
        if type(halls) == list:
            self.view.show_hall_header(' Todos las salas ')
            for hall in halls:
                self.view.show_a_hall(hall)
                self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS SALAS. REVISA.')
        return

    def update_hall(self):
        self.view.ask('ID de la sala a modificar: ')
        id_hall = input()
        hall = self.model.read_a_hall(id_hall)
        if type(hall) == tuple:
            self.view.show_hall_header(' Datos de la sala '+id_hall+' ')
            self.view.show_a_hall(hall)
            self.view.show_hall_midder()
            self.view.show_hall_footer()
        else:
            if hall == None:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA SALA. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_hall()
        fields, vals = self.update_lists(['h_raws','h_seats'], whole_vals)
        vals.append(id_hall)
        vals = tuple(vals)
        out = self.model.update_hall(fields, vals)
        if out == True:
            self.view.ok(id_hall, 'se actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA SALA. REVISA.')
        return

    def delete_hall(self):
        self.view.ask('Id de la sala a borrar: ')
        id_hall = input()
        count = self.model.delete_hall(id_hall)
        if count != 0:
            self.view.ok(id_hall, 'se borro')
        else:
            if count == 0:
                self.view.error('LA SALA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA SALA. REVISA.')
        return
    

    
    """
    **********************************
    * Controllers for Functions *
    **********************************
    """
    def admin_functions_menu(self):
        o = '0'
        while o != '9':
            self.view.admin_functions_menu()
            self.view.option('9')
            o = input()
            if o == '1':
                self.create_function()
            elif o == '2': 
                self.create_seats_for_function()
            elif o == '3':
                self.read_a_function()
            elif o == '4':
                self.read_all_functions()
            elif o == '5': 
                self.read_functions_hour()
            elif o == '6':
                self.read_functions_date()
            elif o == '7':
                self.update_function()
            elif o == '8': 
                self.delete_function()
            elif o == '9':
                return
            else:
                self.view.not_valid_option()
                
    def user_functions_menu(self):
        o = '0'
        while o != '5':
            self.view.user_functions_menu()
            self.view.option('5')
            o = input()
            if o == '1':
                self.read_a_function()
            elif o == '2':
                self.read_all_functions()
            elif o == '3':
                self.read_functions_hour()
            elif o == '4': 
                self.read_functions_date()
            elif o == '5':
                return
            else:
                self.view.not_valid_option()
    
    def ask_function(self):
        self.view.ask('ID pelicula: ')
        id_movie = input()
        self.view.ask('ID sala: ')
        id_hall = input()
        self.view.ask('Tipo Funcion: ')
        typefunc = input()
        self.view.ask('Hora de la Funcion: ')
        hour = input()
        self.view.ask('Fecha de la Funcion: ')
        date = input()
        self.view.ask('Duracion de la Funcion: ')
        duration = input()
        self.view.ask('Precio: ')
        price = input()
        return [id_movie, id_hall, typefunc, hour, date, duration, price]

    def create_function(self):
        id_movie, id_hall, typefunc, hour, date, duration, price = self.ask_function()
        out = self.model.create_function(id_movie, id_hall, typefunc, hour, date, duration, price)
        if out == True:
            self.view.ok(id_movie+' en '+id_hall, 'se agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR LA FUNCION. REVISA.')
        return
    
    def create_seats_for_function(self):
        self.view.ask('ID Funcion: ')
        id_function = input()
        out = self.model.create_seats_for_function(id_function)
        if out == True:
            self.view.ok(id_function, ' se agrego')
        else:
            self.view.error('NO SE PUDO AGREGAR LA FUNCION. REVISA.')
        return

    def read_a_function(self):
        self.view.ask('ID Funcion: ')
        id_function = input()
        function = self.model.read_a_function(id_function)
        if type(function) == tuple:
            self.view.show_function_header(' Datos de la funcion '+id_function+' ')
            self.view.show_a_function(function)
            self.view.show_function_midder()
            self.view.show_function_footer()
        else:
            if function == None:
                self.view.error('LA FUNCION NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA FUNCION. REVISA.')
        return

    def read_all_functions(self):
        functions = self.model.read_all_functions()
        if type(functions) == list:
            self.view.show_function_header(' Todos las funciones ')
            for function in functions:
                self.view.show_a_function(function)
                self.view.show_function_midder()
            self.view.show_function_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS FUNCIONES. REVISA.')
        return

    def read_functions_hour(self):
        self.view.ask('Hora: ')
        hour = input()
        functions = self.model.read_functions_hour(hour)
        if type(functions) == list:
            self.view.show_function_header('Funciones a la hora '+hour+' ')
            for function in functions:
                self.view.show_a_function(function)
                self.view.show_function_midder()
            self.view.show_function_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS FUNCIONES. REVISA.')
        return

    def read_functions_date(self):
        self.view.ask('Fecha: ')
        date = input()
        functions = self.model.read_functions_date(date)
        if type(functions) == list:
            self.view.show_function_header('Funciones a la hora '+date+' ')
            for function in functions:
                self.view.show_a_function(function)
                self.view.show_function_midder()
            self.view.show_function_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS FUNCIONES. REVISA.')
        return

    def update_function(self):
        self.view.ask('ID de la funcion a modificar: ')
        id_function = input()
        function = self.model.read_a_function(id_function)
        if type(function) == tuple:
            self.view.show_function_header(' Datos de la funcion '+id_function+' ')
            self.view.show_a_function(function)
            self.view.show_function_midder()
            self.view.show_function_footer()
        else:
            if function == None:
                self.view.error('LA FUNCION NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA FUNCION. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_function()
        fields, vals = self.update_lists(['id_movie','id_hall','f_typefun','f_hour','f_date','f_duration','f_price'], whole_vals)
        vals.append(id_function)
        vals = tuple(vals)
        out = self.model.update_function(fields, vals)
        if out == True:
            self.view.ok(id_function, 'se actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA FUNCION. REVISA.')
        return

    def delete_function(self):
        self.view.ask('Id de la FUNCION a borrar: ')
        id_function= input()
        count = self.model.delete_function(id_function)
        if count != 0:
            self.view.ok(id_function, 'se borro')
        else:
            if count == 0:
                self.view.error('LA FUNCION NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA FUNCION. REVISA.')
        return
    
    """
    *****************************
    * Controllers for buy tickets *
    *****************************
    """
    def admin_buy_menu(self):
        o = '0'
        while o != '2':
            self.view.admin_buy_menu()
            self.view.option('2')
            o = input()
            if o == '1':
                self.admin_tickets_menu()
            elif o == '2':
                self.admin_purchase_menu()
            elif o == '3':
                return
            else:
                self.view.not_valid_option()
        return



    """
    ****************************
    * Controllers for tickets *
    ****************************
    """

    def admin_tickets_menu(self):
        o = '0'
        while o != '7':
            self.view.admin_tickets_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.read_avaliable_seats()
                self.create_ticket()
            elif o == '2':
                self.read_a_ticket()
            elif o == '3':
                self.read_all_tickets()
            elif o == '4':
                self.read_tickets_function()
            elif o == '5':
                self.update_ticket()
            elif o == '6':
                self.delete_ticket()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def ask_ticket(self):
        self.view.ask('Funcion: ')
        id_function = input()
        self.view.ask('Asiento: ')
        id_seat = input()
        return [id_function,id_seat]
    
    def read_avaliable_seats(self):
        self.view.ask('ID funcion: ')
        id_function = input()
        functions = self.model.read_avaliable_seats(id_function)
        if type(functions) == list:
            self.view.show_seat_function_header('Asientos')
            for function in functions:
                self.view.show_seat_function(function)
                self.view.show_seat_function_midder()
            self.view.show_seat_function_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ASIENTOS DE LA FUNCION. REVISA.')
        return
        

    def create_ticket(self):
        #self.model.read_all_seats()
        id_function, id_seat = self.ask_ticket()
        self.model.update_seats_for_function(id_function, id_seat)
        out = self.model.create_ticket(id_function,id_seat)
        if out == True:
            self.view.ok(id_function+' con siento'+id_seat, 'se reservo ')
        else:
            self.view.error('NO SE PUDO AGREGAR EL TICKET. REVISA.')
        return

    def read_a_ticket(self):
        self.view.ask('ID boleto: ')
        id_ticket = input()
        ticket = self.model.read_a_ticket(id_ticket)
        if type(ticket) == tuple:
            self.view.show_ticket_header(' Datos del ticket '+id_ticket+' ')
            self.view.show_a_ticket(ticket)
            self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            if ticket == None:
                self.view.error('EL BOLETO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL BOLETO. REVISA.')
        return

    def read_all_tickets(self):
        tickets = self.model.read_all_tickets()
        if type(tickets) == list:
            self.view.show_ticket_header(' Todos los tickets ')
            for ticket in tickets:
                self.view.show_a_ticket(ticket)
                self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS BOLETOS. REVISA.')
        return

    def read_tickets_function(self):
        self.view.ask('ID funcion: ')
        id_function = input()
        functions = self.model.read_tickets_function(id_function)
        if type(functions) == list:
            self.view.show_ticket_header('Boletos')
            for function in functions:
                self.view.show_a_ticket(function)
                self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            self.view.error('PROBLEMA AL LEER LOS ASIENTOS DE LA FUNCION. REVISA.')
        return


    def update_ticket(self):
        self.view.ask('ID del boleto a modificar: ')
        id_ticket = input()
        ticket = self.model.read_a_ticket(id_ticket)
        if type(ticket) == tuple:
            self.view.show_ticket_header(' Datos del boleto'+id_ticket+' ')
            self.view.show_a_ticket(ticket)
            self.view.show_ticket_midder()
            self.view.show_ticket_footer()
        else:
            if ticket == None:
                self.view.error('EL BOLETO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER EL BOLETO. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        whole_vals = self.ask_ticket()
        fields, vals = self.update_lists(['id_function','id_seat','t_total'], whole_vals)
        vals.append(id_ticket)
        vals = tuple(vals)
        out = self.model.update_ticket(fields, vals)
        if out == True:
            self.view.ok(id_ticket, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR EL BOLETO. REVISA.')
        return

    def delete_ticket(self):
        self.view.ask('Id de boleto a borrar: ')
        id_ticket = input()
        count = self.model.delete_ticket(id_ticket)
        if count != 0:
            self.view.ok(id_ticket, 'borro')
        else:
            if count == 0:
                self.view.error('EL BOLETO NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BOLETO. REVISA.')
        return

    """
    ****************************
    * Controllers for purchases *
    ****************************
    """

    def admin_purchase_menu(self):
        o = '0'
        while o != '11':
            self.view.admin_purchase_menu()
            self.view.option('11')
            o = input()
            if o == '1':
                self.create_purchase()
            elif o == '2':
                self.read_a_purchase()
            elif o == '3':
                self.read_all_purchases()
            elif o == '4':
                self.read_purchases_date()
            elif o == '5':
                self.read_purchases_user()
            elif o == '6':
                self.update_purchase()
            elif o == '7':
                self.add_purchase_details()
            elif o == '8':
                self.update_purchase_details()
            elif o == '9':
                self.delete_purchase_details()
            elif o == '10':
                self.delete_purchase()
            elif o == '11':
                return
            else:
                self.view.not_valid_option()
        return

    def create_purchase(self):
        self.view.ask('ID admin: ')
        id_admin = input()
        self.view.ask('ID cliente: ')
        id_user = input()
        p_date = date.today()
        p_hour = datetime.now().time().strftime("%H:%M:%S")
        p_total = 0.0
        id_purchase = self.model.create_purchase(id_admin, id_user, p_date, p_hour, p_total)
        if type(id_purchase) == int:
            id_ticket = ' '
            while id_ticket != '':
                self.view.msg('---- Agrega boletos a la compra (deja vacio el id del boleto para salir) ---')
                id_ticket, pd_total = self.create_purchase_details(id_ticket)
                p_total += pd_total
            self.model.update_purchase(('p_total = %s',),(p_total, id_purchase))
        else:
            self.view.error('NO SE PUDO CREAR LA COMPRA. REVISA.')
        return

    def read_a_purchase(self):
        self.view.ask('ID Compra: ')
        id_purchase= input()
        purchase = self.model.read_a_purchase(id_purchase)
        if type(purchase) == tuple:
            purchase_details = self.model.read_purchase_details(id_purchase)
            if type(purchase_details) != list and purchase_details != None:
                self.view.error('PROBLEMA AL LEER LA COMPRA. REVISA.')
            else:
                self.view.show_purchase_header(' Datos de la compra '+id_purchase+' ')
                self.view.show_a_purchase(purchase)
                self.view.show_purchase_details_header()
                for purchase_detail in purchase_details:
                    self.view.show_a_purchase_details(purchase_detail)
                self.view.show_purchase_details_footer()
                self.view.show_purchase_total(id_purchase)
                self.view.show_purchase_footer()
                return purchase
        else:
            if purchase == None:
                self.view.error('LA COMPRA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA COMPRA. REVISA.')
        return

    def read_all_purchases(self):
        purchases = self.model.read_all_purchases()
        if type(purchases) == list:
            self.view.show_purchase_header(' Todas las compras ')
            for purchase in purchases:
                id_purchase = purchase[0]
                purchase_details = self.model.read_purchase_details(id_purchase)
                if type(purchase_details) != list and purchase_details != None:
                    self.view.error('PROBLEMA AL LEER LA COMPRA '+id_purchase+'. REVISA.')
                else:
                    self.view.show_a_purchase(purchase)
                    self.view.show_purchase_details_header()
                    for purchase_detail in purchase_details:
                        self.view.show_a_purchase_details(purchase_detail)
                    self.view.show_purchase_details_footer()
                    self.view.show_purchase_total(purchase)
                    self.view.show_purchase_midder()
            self.view.show_purchase_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS COMPRAS. REVISA.')
        return

    def read_purchases_date(self):
        self.view.ask('Fecha: ')
        date = input()
        purchases = self.model.read_purchases_date(date)
        if type(purchases) == list:
            self.view.show_purchase_header(' Compras para la fecha '+date+' ')
            for purchase in purchases:
                id_purchase = purchase[0]
                purchase_details = self.model.read_purchase_details(id_purchase)
                if type(purchase_details) != list and purchase_details != None:
                    self.view.error('PROBLEMA AL LEER LA COMPRA '+id_purchase+'. REVISA.')
                else:
                    self.view.show_a_purchase(purchase)
                    self.view.show_purchase_details_header()
                    for purchase_detail in purchase_details:
                        self.view.show_a_purchase_details(purchase_detail)
                    self.view.show_purchase_details_footer()
                    self.view.show_purchase_total(purchase)
                    self.view.show_purchase_midder()
            self.view.show_purchase_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS COMPRAS. REVISA.')
        return

    def read_purchases_user(self):
        self.view.ask('ID cliente: ')
        id_user = input()
        purchases = self.model.read_purchases_user(id_user)
        if type(purchases) == list:
            self.view.show_purchase_header(' Ordenes para el cliente '+id_user+' ')
            for purchase in purchases:
                id_purchase = purchase[0]
                purchase_details = self.model.read_purchase_details(id_purchase)
                if type(purchase_details) != list and purchase_details != None:
                    self.view.error('PROBLEMA AL LEER LA COMPRA '+id_purchase+'. REVISA.')
                else:
                    self.view.show_a_purchase(purchase)
                    self.view.show_purchase_details_header()
                    for purchase_detail in purchase_details:
                        self.view.show_a_purchase_details(purchase_detail)
                    self.view.show_purchase_details_footer()
                    self.view.show_purchase_total(purchase)
                    self.view.show_purchase_midder()
            self.view.show_purchase_footer()
        else:
            self.view.error('PROBLEMA AL LEER LAS COMPRAS. REVISA.')
        return

    def update_purchase(self):
        self.view.ask('ID de compra a modificar: ')
        id_purchase = input()
        purchase = self.model.read_a_purchase(id_purchase)
        if type(purchase) == tuple:
            self.view.show_purchase_header(' Datos de la compra '+id_purchase+' ')
            self.view.show_a_purchase(purchase)
            self.view.show_purchase_total(purchase)
            self.view.show_purchase_footer()
        else:
            if purchase == None:
                self.view.error('LA COMPRA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL LEER LA COMPRA. REVISA.')
            return
        self.view.msg('Ingresa los valores a modificar (vacio para dejarlo igual):')
        self.view.ask('ID admin: ')
        id_admin = input()
        self.view.ask('ID cliente: ')
        id_user = input()
        self.view.ask('Fecha (yyyy/mm/dd): ')
        p_date = input()
        self.view.ask('Hora (hh:mm:ss): ')
        p_hour = input()
        whole_vals = [id_admin, id_user, p_date, p_hour]
        fields, vals = self.update_lists(['id_admin','id_user','p_date','p_hour'], whole_vals)
        vals.append(id_purchase)
        vals = tuple(vals)
        out = self.model.update_purchase(fields, vals)
        if out == True:
            self.view.ok(id_purchase, 'actualizo')
        else:
            self.view.error('NO SE PUDO ACTUALIZAR LA COMPRA. REVISA.')
        return 

    def delete_purchase(self):
        self.view.ask('Id de compra a borrar: ')
        id_purchase = input()
        count = self.model.delete_purchase(id_purchase)
        if count != 0:
            self.view.ok(id_purchase, ' se borro')
        else:
            if count == 0:
                self.view.error('LA COMPRA NO EXISTE')
            else:
                self.view.error('PROBLEMA AL BORRAR LA COMPRA. REVISA.')
        return

    """
    *********************************
    * Controllers for PURCHASE details *
    *********************************
    """
    def create_purchase_details(self, id_purchase):
        pd_total = 0.0
        self.view.ask('ID boleto: ')
        id_ticket = input()
        if id_ticket != '':
            ticket = self.model.read_a_ticket(id_ticket)
            if type(ticket) == tuple:
                self.view.show_ticket_header(' Datos del boleto '+id_ticket+' ')
                self.view.show_a_ticket(ticket)
                self.view.show_ticket_footer()
                pd_total = ticket[5]
                out = self.model.create_purchase_detail(id_purchase, id_ticket, pd_total)
                if out == True:
                    self.view.ok(ticket[0], 'agrego a la compra')
                else:
                    if out.errno == 1062:
                        self.view.error('EL BOLETO YA ESTA EN LA COMPRA')
                    else:
                        self.view.error('NO SE PUDO AGREGAR EL BOLETO. REVISA.')
                    pd_total = 0.0
            else:
                if ticket == None:
                    self.view.error('EL BOLETO NO EXISTE')
                else:
                    self.view.error('PROBLEMA AL LEER EL BOLETO. REVISA.')
        return id_ticket, pd_total

    def add_purchase_details(self):
        purchase = self.read_a_purchase()
        if type(purchase) == tuple:
            id_purchase = purchase[0]
            p_total = purchase[5]
            id_ticket = ' '
            while id_ticket != '':
                self.view.msg('---- Agrega boletos a la compra (deja vacio el id del boleto para salir) ---')
                id_ticket, pd_total = self.create_purchase_details(id_purchase)
                p_total += pd_total
            self.model.update_purchase(('p_total = %s',),(p_total, id_purchase))
        return

    def update_purchase_details(self):
        purchase = self.read_a_purchase()
        if type(purchase) == tuple:
            id_purchase = purchase[0]
            p_total = purchase[5]
            id_ticket = ' '
            while id_ticket != '':
                self.view.msg('---- Modifica boletos de la compra (deja vacio el id del boleto para salir) ---')
                self.view.ask('ID boleto: ')
                id_ticket = input()
                if id_ticket != '':
                    purchase_detail = self.model.read_a_purchase_detail(id_purchase, id_ticket)
                    if type(purchase_detail) == tuple:
                        pd_total_old = purchase_detail[4]
                        p_total -= pd_total_old
                        ticket = self.model.read_a_ticket(id_ticket)
                        price = ticket[3]
                        pd_total = price
                        p_total += pd_total
                        fields, whole_vals = self.update_lists(['pd_total'],[pd_total])
                        whole_vals.append(id_purchase)
                        whole_vals.append(id_ticket)
                        self.model.update_purchase_details(fields, whole_vals)
                        self.view.ok(id_ticket, 'actualizo en la compra ')
                    else:
                        if purchase_detail == None:
                            self.view.error('EL BOLETO NO EXISTE EN LA COMPRA')
                        else:
                            self.view.error('PROBLEMA AL ACTUALIZAR EL BOLETO. REVISA.')
            self.model.update_purchase(('p_total = %s',),(p_total, id_purchase))
        return

    def delete_purchase_details(self):
        purchase = self.read_a_purchase()
        if type(purchase) == tuple:
            id_purchase = purchase[0]
            p_total = purchase[5]
            id_ticket = ' '
            while id_ticket != '':
                self.view.msg('---- Borra boletos de la compra (deja vacio el id del boleto para salir) ---')
                self.view.ask('ID boleto: ')
                id_ticket = input()
                if id_ticket != '':
                    purchase_detail = self.model.read_a_purchase_detail(id_purchase, id_ticket)
                    count = self.model.delete_purchase_details(id_purchase, id_ticket)
                    if type(purchase_detail) == tuple and count != 0:
                        pd_total = purchase_detail[4]
                        p_total -= pd_total
                        self.view.ok(id_ticket, 'borro de la compra ')
                    else:
                        if purchase_detail == None:
                            self.view.error('EL BOLETO NO EXISTE EN LA COMPRA')
                        else:
                            self.view.error('PROBLEMA AL BORRAR EL BOLETO. REVISA.')
            self.model.update_purchase(('p_total = %s',),(p_total, id_purchase))
        return



