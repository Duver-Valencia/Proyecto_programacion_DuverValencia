def verRepuesta():
    '''
    Esta funcion retorna la lista de los indices de las repuestas y otra con los ids de las preguntas
    '''
    f = open('respuesta.txt','r')
    f.readline()
    respuestas = []
    id_preguntas = []
    for linea in f:
        linea = linea.replace('\n','')
        sub_lista = linea.split(',')
        id_preguntas.append(int(sub_lista[0]))
        respuestas.append(int(sub_lista[1]))
    f.close
    print(respuestas,id_preguntas)
    return [respuestas,id_preguntas]



def verGrado(usuario):
    '''Esta función recibe como parametro el nombre de un usuario y retorna el grado en el que está
    '''
    l=[]
    f = open('perfil.txt','r')
    for line in f:
        line = line.replace('\n','')
        sub_lista = line.split(',')
        l.append(sub_lista)
    f.close()
    c = 0
    while c < len(l):
        if l[c][0] == usuario:
            return l[c][1]
            c = c + 1
        else:
            c = c + 1

def verVidas(usuario):
    '''Esta función recibe como parametro el nombre de un usuario y retorna el grado en el que está
    '''
    l=[]
    f = open('perfil.txt','r')
    for line in f:
        line = line.replace('\n','')
        sub_lista = line.split(',')
        l.append(sub_lista)
    f.close()
    c = 0
    while c < len(l):
        if l[c][0] == usuario:
            return l[c][2]
        else:
            c = c + 1

def buscarPreguntas(grado,materia):
    '''
    Esta función recibe como parametros un grado
     y una materia y retorna la lista de preguntas correspondiente
    '''
    l=[]
    l_preguntas = []
    f = open('preguntas.txt','r')
    for line in f:
        line = line.replace('\n','')
        sub_lista = line.split(',')
        l.append(sub_lista)
    f.close()
    i = 0
    while i < len(l):
        if len(l[i]) > 2:
            if (l[i][2]) == str(grado) and (l[i][1]) == materia:
                print(l[i])
                i = i + 1
            else:
                i = i + 1
        else:
            i = i + 1

def buscarRespuestas(id_pregunta):
    '''Esta funcion recibe como parametro un id de una pregunta y retorna una lista con las opciones
    de repuesta para esta pregunta y el id de las respuestas
    '''
    l=[]
    f = open('respuestas.txt','r')
    for line in f:
        line = line.replace('\n','')
        sub_lista = line.split(',')
        l.append(sub_lista)
    f.close()
    respuestas = []
    for linea in l[1:]:
        if len(linea) > 1:
            if (linea[1]) == str(id_pregunta):
                respuestas.append(linea)
    return(respuestas)



'''
def verOpciones(lista_preguntas):
    f = open('opciones.txt','r')
    l_opciones = []
    f.readline()
    for linea in f:
        linea = linea.replace('\n','')
        sub_lista = linea.split(',')
        l_opciones.append(sub_lista)
    f.close
    opciones = []
    ids_lista = []
    for pregunta in lista_preguntas:
        id_ = pregunta[0]
        sub_lista = []
        for opcion in l_opciones:
            if int(opcion[1]) == int(id_):
                sub_lista.append(opcion[2])
        ids_lista.append(id_)
        opciones.append(sub_lista)
    return()
'''







'''
def getQuestion(grado):
    l=[]
    l_preguntas = []
    f = open('preguntas.txt','r')
    for line in f:
        line = line.replace('\n','')
        sub_list = line.split(',')
        l.append(sub_list)
    f.close()
    for linea in l[1:]:
        if int(linea[2]) == grado:
            l_preguntas.append(linea)
    print(l_preguntas)

getQuestion(0)
'''
