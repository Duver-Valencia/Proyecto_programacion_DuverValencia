def verUsuarios():
    f = open('inicio_sesión.txt','r')
    lista_usuarios = []
    for linea in f:
        linea = linea.replace('\n','')
        sub_list = linea.split(',')
        lista_usuarios.append(sub_list)
    f.close
    return lista_usuarios

def contraseña(usuario):
    a = verUsuarios()
    i = 0
    while i < len (a):
        if a[i][0] == usuario:
            return a[i][1]
        else:
            i = i + 1

def verificarUsuario(usuario,contraseña):
    lista_buscar = []
    lista_buscar.append(usuario)
    lista_buscar.append(contraseña)
    a = verUsuarios()
    if lista_buscar in a:
        return True
    else:
        return False
    


def compararUsuario(usuario):
    a = verUsuarios()
    i = 0
    estado = True
    if usuario in a[i]:
        estado = False
        return estado
    else:
        estado = True
    return estado

def verAdministradores():
    f = open('cuentas_administradores.txt','r')
    lista_usuarios = []
    for linea in f:
        linea = linea.replace('\n','')
        sub_list = linea.split(',')
        lista_usuarios.append(sub_list)
    f.close
    return lista_usuarios


def verificarAdministrador(administrador,contraseña):
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
