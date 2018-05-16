def verUsuarios():
    '''Esta función retorna una lista de los usuarios registrados con sus respectivas contraseñas
    '''
    f = open('inicio_sesión.txt','r')
    lista_usuarios = []
    for linea in f:
        linea = linea.replace('\n','')
        sub_list = linea.split(',')
        lista_usuarios.append(sub_list)
    f.close
    return lista_usuarios


def contraseña(usuario):
    '''Esta funcion recibe como parametro un usuario y retorna la contraseña correspondiente si está registrado
    '''
    a = verUsuarios()
    i = 0
    while i < len (a):
        if a[i][0] == usuario:
            return a[i][1]
        else:
            i = i + 1

def verificarUsuario(usuario,contraseña):
    '''Esta funcion recibe como parametros un usuario con su respectiva contraseña y 
    retorna True si el usuario está registrado con esa contraseña, de lo contrario retorna False
    '''
    lista_buscar = []
    lista_buscar.append(usuario)
    lista_buscar.append(contraseña)
    a = verUsuarios()
    if lista_buscar in a:
        return True
    else:
        return False
    
def compararUsuario(usuario):
    '''Esta funcion recibe como parametro el nombre de un usuario y retorna True si el usuario
    no se encuentra registrado, de lo contrario retorna False
    '''
    a = verUsuarios()
    i = 0
    estado = True
    print(a)
    while i < len(a):
        if usuario == a[i][0]:
            estado = False
            return estado
        else:
            i += 1
    return estado


def verAdministradores():
    '''Esta funcion retorna una lista de listas de los usuarios que se encuentran registrados como
    administradores 
    '''
    f = open('cuentas_administradores.txt','r')
    lista_usuarios = []
    for linea in f:
        linea = linea.replace('\n','')
        sub_list = linea.split(',')
        lista_usuarios.append(sub_list)
    f.close
    return lista_usuarios

def verificarAdministrador(administrador,contraseña):
    '''Esta función recibe como parametros un nombre de administrador y una contraseña. Retorna True si
    el adimnistrador se encuentra registrado con esa contraseña, de lo contrario retorn False.
    '''
    lista_buscar = []
    lista_buscar.append(administrador)
    lista_buscar.append(contraseña)
    a = verAdministradores()
    if lista_buscar in a:
        return True
    else:
        return False




    
'''
def verificarUsuarioContraseña(usuario,contraseña):
    i = 0
    b = 0
    a = verUsuarios()
    while b < len(a) :
        if a[b][i] == usuario:
            if a[b][i+1] == contraseña:
                return True
            else:
                print('contraseña incorrecta')
                return False
        else:
            b = b + 1
    print('El usuario no existe')
    return False
    
'''
