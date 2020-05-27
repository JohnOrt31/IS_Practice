class View:
    """
    ****************************
    * A view for a cinema DB *
    ****************************
    """

    def start(self):
        print('----------------------------------------------')
        print('****         BIENVENIDO A CINEFLIX        ****')
        print('*El mejor lugar para ver los mejores estrenos*')
        print('-----------------------------------------------\n')

    def end(self):
        print('----------------------------------------')
        print('****        HASTA LA PRÓXIMA        ****')
        print('----------------------------------------')

    def main_menu(self):
        print('----------------------------------------')
        print('****            INICIO              ****')
        print('----------------------------------------')
        print('****     ¿Qué deseas realizar?      ****')
        print('----------------------------------------')
        print('1. Iniciar sesión')
        print('2. Registrar')
        print('3. Salir')

    def login_menu(self):
        print('----------------------------------------')
        print('****         INICIAR SESIÓN         ****')
        print('----------------------------------------')
        print('****   ¿Qué tipo de usuario eres?   ****')
        print('----------------------------------------')
        print('1. Administrador')
        print('2. Cliente')
        print('3. Regresar')
    
    def signin_menu(self):
        print('----------------------------------------')
        print('****          REGISTRARSE           ****')
        print('----------------------------------------')
        print('****   ¿Qué tipo de usuario eres?   ****')
        print('----------------------------------------')
        print('1. Administrador')
        print('2. Cliente')
        print('3. Regresar')
    
    def option(self, last):
        print('Selecciona una opcion (1-'+last+'): ', end = '')
    
    def not_valid_option(self):
        print('Opcion no permitida\nVuelve a intentarlo')

    def ask(self, output):
        print(output, end = '')
    
    def msg(self, output):
        print(output)
    
    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' se '+op+' correctamente! +')
        print('+'*(len(str(id))+len(op)+24))

    def error(self, err):
        print(' ¡ERROR! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))
    
        """
    *********************************
    * Menus para el Administrador *
    *********************************
    """
    def admin_menu(self):
        print('----------------------------------------')
        print('****  xd     Menu Principal  xd     ****')
        print('----------------------------------------')
        print('1. Peliculas')
        print('2. Salas')
        print('3. Funciones')
        print('4. Menu de compra')
        print('5. Administradores')
        print('6. Usuarios')
        print('7. Salir')
    
    def admin_movies_menu(self):
        print('-----------------------------------------')
        print('****     xd  Peliculas Admin  xd     ****')
        print('-----------------------------------------')
        print('1. Agregar pelicula')
        print('2. Mostrar pelicula')
        print('3. Mostrar todas las peliculas')
        print('4. Mostrar peliculas de un director')
        print('5. Mostrar películas de un año ')
        print('6. Actualizar pelicula')
        print('7. Eliminar pelicula')
        print('8. Regresar')

    
    def admin_halls_menu(self):
        print('----------------------------------------')
        print('****       xd  Salas Admin  xd      ****')
        print('----------------------------------------')
        print('1. Agregar sala')
        print('2. Mostrar sala')
        print('3. Mostrar todas las salas')
        print('4. Actualizar sala')
        print('5. Eliminar sala')
        print('6. Regresar')
    
    
    def admin_functions_menu(self):
        print('-----------------------------------------')
        print('****     xd  Funciones Admin  xd     ****')
        print('-----------------------------------------')
        print('1. Agregar funcion')
        print('2. Agregar asientos a una funcion')
        print('3. Mostrar una funcion')
        print('4. Mostrar todas las funciones')
        print('5. Mostrar funciones de una hora')
        print('6. Mostrar funciones de una fecha')
        print('7. Actualizar funcion')
        print('8. Eliminar funcion')
        print('9. Regresar')
    
    def admin_buy_menu(self):
        print('----------------------------------------------')
        print('****      xd  Menu Compra Admin   xd      ****')
        print('----------------------------------------------')   
        print('1. Boletos')
        print('2. Compras')
        print('3. Regresar')
    

    def admin_tickets_menu(self):
        print('----------------------------------------------')
        print('****        xd  Boletos Admin   xd       ****')
        print('----------------------------------------------')   
        print('1. Crear boleto')
        print('2. Leer un boleto')
        print('3. Leer todos los boletos')
        print('4. Leer todos los boletos de una funcion')
        print('5. Actualizar boleto')
        print('6. Eliminar boleto')
        print('7. Regresar')

    def admin_purchase_menu(self):
        print('----------------------------------------------')
        print('****        xd  Compras Admin   xd       ****')
        print('----------------------------------------------')   
        print('1. Agregar compra')
        print('2. Leer compra')
        print('3. Leer todas las compras')
        print('4. Leer compras de una fecha')
        print('5. Leer compras de un cliente')
        print('6. Actualizar datos de compra')
        print('7. Agregar boletos a una compra')
        print('8. Modificar boletos de una compra')
        print('9. Borrar boletos de una compra')
        print('10. Borrar compra')
        print('11. Regresar')
    
    def admin_admins_menu(self):
        print('-----------------------------------------')
        print('****     xd  Administradores  xd     ****')
        print('-----------------------------------------')
        print('1. Mostrar un administrador')
        print('2. Mostrar todos los administradores')
        print('3. Mostrar administradores por cumpleaños')
        print('4. Actualizar administrador')
        print('5. Eliminar administrador')
        print('6. Regresar')
    
    def admin_users_menu(self):
        print('-----------------------------------------')
        print('****      xd     Usuarios     xd     ****')
        print('-----------------------------------------')
        print('1. Mostrar un usuario')
        print('2. Mostrar todos los usuarios')
        print('3. Mostrar usuarios por cumpleaños')
        print('4. Actualizar usuario')
        print('5. Eliminar usuario')
        print('6. Regresar')



    """
    *********************************
    * Menus para el Cliente *
    *********************************
    """
    def user_menu(self):
        print('----------------------------------------')
        print('****  xd     Menu Principal  xd     ****')
        print('----------------------------------------')
        print('1. Peliculas')
        print('2. Funciones')
        print('3. Compras')
        print('4. Salir')
    
    def user_movie_menu(self):
        print('----------------------------------------')
        print('****     xd  Peliculas User  xd     ****')
        print('----------------------------------------')
        print('1. Mostrar pelicula')
        print('2. Mostrar todas las peliculas')
        print('3. Mostrar peliculas de un director')
        print('4. Mostrar películas de un año ')
        print('5. Regresar')

    def user_functions_menu(self):
        print('-----------------------------------------')
        print('****      xd  Funciones User xd      ****')
        print('-----------------------------------------')
        print('1. Mostrar una funcion')
        print('2. Mostrar todas las funciones')
        print('3. Mostrar funciones de una hora')
        print('4. Mostrar funciones de una fecha')
        print('5. Regresar')

    """
    *********************************
    * Administrador y Cliente*
    *********************************
    """
    def show_a_user(self, record):
        print('ID: ', record[0])
        print('Nombre(s): ', record[1])
        print('Apellido Paterno: ', record[2])
        print('Apellido Materno: ', record[3])
        print('Correo: ', record[4])
        print('Telefono: ', record[5])
        print('Cumpleaños: ', record[6])

    def show_a_user_brief(self, record):
        print('ID: ', record[0])
        print('Nombre: ', record[1]+' '+record[2]+' '+record[3])
        print('Correo: ', record[4])
        print('Telefono: ', record[5])
        print('Cumpleaños: ', record[6])
        
    def show_user_header(self, header):
        print(header.center(100,'*'))
        print('-'*100)
    
    def show_user_midder(self):
        print('-'*100)

    def show_user_footer(self):
        print('*'*100)


    """
    ***********************
    Peliculas
    ***********************
    """

    def show_a_movie(self, record):
        print('Id Pelicula: ', record[0])
        print('Titulo: ', record[1])
        print('Director: ', record[2])
        print('Sinopsis: ', record[3])
        print('Clasificacion: ', record[4])
        print('Género: ', record[5])
        print('Idioma: ', record[6])
        print('País: ', record[7])
        print('Fecha de estreno: ', record[8])

    def show_movie_header(self, header):
        print(header.center(100,'*'))
        print('-'*100)
    
    def show_movie_midder(self):
        print('-'*100)

    def show_movie_footer(self):
        print('*'*100)


    """
    *********************************
    *Salas*
    *********************************
    """
    def show_a_hall(self, record):
        print('Sala: ', record[0])
        print('No. Filas: ', record[1])
        print('No. Asientos: ', record[2])
        
    def show_hall_header(self, header):
        print(header.center(81,'+'))
    
    def show_hall_midder(self):
        print('/'*81)

    def show_hall_footer(self):
        print('+'*81)


    """
    *********************************
    *Asientos*
    *********************************
    """
    def show_a_seat(self, record):
        print(f'{record[0]:<3}|{record[1]:<20}')
        
    def show_seat_header(self, header):
        print('-'*81)
        print('Asiento'.ljust(3)+'|'+'Tipo'.ljust(20))
        print('-'*81)

    def show_seat_footer(self):
        print('-'*81)
    
    """
    *********************************
    *Funciones*
    *********************************
    """
    def show_a_function(self, record):
        print('Funcion: ', record[0])
        print('Pelicula: ', record[8])
        print('Sala: ', record[2])
        print('Tipo:', record[3])
        print('Hora de la funcion:', record[4])
        print('Fecha de la funcion:', record[5])
        print('Duracion (min):', record[6])
        print('Precio de la función:', record[7])
        
    def show_function_header(self, header):
        print(header.center(81,'+'))
    
    def show_function_midder(self):
        print('/'*81)

    def show_function_footer(self):
        print('+'*81)
    

    
    """
    *********************************
    *Asientos en funciones*
    *********************************
    """
    def show_seat_function(self, record):
        print('Funcion: ', record[0])
        print('Asiento: ', record[1])
        print('Disponible: ', record[2])
        
    def show_seat_function_header(self, header):
        print(header.center(81,'+'))
    
    def show_seat_function_midder(self):
        print('/'*81)

    def show_seat_function_footer(self):
        print('+'*81)

    """
    *********************************
    *Asientos en funciones tabla*
    *********************************
    """
    def show_seat_function2(self, record):
        Tabla = """\
+---------------------------------------------------------------------+
| Funcion    Pelicula                       Asiento     Disponibilidad|
|---------------------------------------------------------------------|
{}
+---------------------------------------------------------------------+\
"""
        Tabla = (Tabla.format('\n'.join("| f'{record[0]:<10}| {record[1]:<30}| {record[2]:<3} |{record[4]:<2} |".format(*fila)
        for fila in record)))
        print (Tabla)
        
    def show_seat_function2_header(self, header):
        print(header.center(81,'+'))
    
    def show_seat_function2_midder(self):
        print('/'*81)

    def show_seat_function2_footer(self):
        print('+'*81)

    """
    *********************************
    *Compras*
    *********************************
    """
    def show_a_purchase(self, record):
        print('ID: ', record[0])
        print('ID administrador: ', record[1])
        print('Administrador: ', record[6]+' '+record[7]+' '+record[8])
        print('ID cliente: ', record[2])
        print('Cliente: ', record[9]+' '+record[10]+' '+record[11])
        print('Fecha de compra: ', record[3])
        print('Hora de compra: ', record[4])

    def show_purchase_header(self, header):
        print(header.center(81,'+'))
    
    def show_purchase_midder(self):
        print('/'*81)
    
    def show_purchase_total(self, record):
        print('Total de la compra: '+str(record[5]))

    def show_purchase_footer(self):
        print('+'*81)

    """
    *************************************
    * Vistas para tickets *
    *************************************
    """ 

    def show_a_ticket(self, record):
        print('ID Ticket: ', record[0])
        print('Pelicula: ', record[1])
        print('Hora de la función: ', record[2])
        print('Fecha de la función: ', record[3])
        print('Asiento: ', record[4])
        print('Precio Boleto: ', record[5])
        
    def show_ticket_header(self, header):
        print(header.center(100,'*'))
        print('-'*100)
    
    def show_ticket_midder(self):
        print('-'*100)

    def show_ticket_footer(self):
        print('*'*100)


    """
    *************************************
    * Vistas para detalles de la compra *
    *************************************
    """ 

    def show_a_purchase_details(self, record):
        print(f'{record[0]:<3}|{record[1]:<3}|{record[2]:<20}|{record[3]:<3}|{record[4]:<11}|')
        
    def show_purchase_details_header(self):
        print('-'*81)
        print('ID Ticket'.ljust(3)+'|'+'ID Funcion'.ljust(3)+'|'+'Pelicula'.ljust(20)+'|'+'Asiento'.ljust(3)+'|'+'Total'.ljust(11))
        print('-'*81)

    def show_purchase_details_footer(self):
        print('-'*81)
