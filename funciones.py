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


def diccionarioPreguntas():
    d2 = {0:{'Matematicas':{
      'id_preguntas':[0,1,2,3],
      'preguntas':['¿Cuanto es 3-2?','¿Cuanto es 7+8?','¿Cuanto es 3-1?','¿Que numero sigue del 3?'],
      'index':[2,1,3,3],
      'respuestas':[['2','3','1','4'],['9','15','10','14'],['5','3','1','2'],['6','3','1','4']]},
      'Español':{
      'id_preguntas':[4,5,6,7],
      'preguntas':['¿Cual es la primera vocal?','¿Cuantas vocales existen?','Seleccione una letra que no sea una vocal','¿Cual es la tercera vocal?'],
      'index':[2,1,3,2],
      'respuestas':[['e','u','a','o'],['4','5','2','7'],['e','a','i','s'],['e','o','i','a']]},
      'Artistica':{
      'id_preguntas':[8,9,10,11],
      'preguntas':['¿Cual de estos es un color primario?','¿Cual es la forma del sol?','¿Cuantos lados tiene un cuadrado?','¿Cuantos lados tiene un triangulo?'],
      'index':[1,2,0,3],
      'respuestas':[['Morado','Amarillo','Cuaderno','Blanco'],['Cubo','Cuadrado','Circulo','Triangulo'],['Cuatro','Dos','Uno','No tiene'],['Dos','Cuatro','No tiene','Tres']]},
      'Etica':{
      'id_preguntas':[12,13,14,15],
      'preguntas':['¿Cual de estos es un valor?','¿Que es respeto?','¿Cual de estos no es un valor?','¿Cual de estas es una emoción?'],
      'index':[1,0,2,1],
      'respuestas':[['Arroz','Tolerancia','Futbol','Rojo'],['Un valor','Una emoción','Un color','Una ciudad'],['Respeto','Tolerancia','Fresa','Amor'],['Azul','Amor','Futbol','Cuatro']]}}
      ,1:{'Matematicas':{
      'id_preguntas':[16,17,18,19],
      'preguntas':['¿Cuanto es 15+7?','¿Cuanto es 12-3?','¿Cuanto es 2x3?','¿Cual de estos es un numero par?'],
      'index':[3,2,1,2],
      'respuestas':[['12','13','23','22'],['5','10','9','12'],['5','6','2','14'],['3','7','4','1']]},
      'Español':{
      'id_preguntas':[20,21,22,23],
      'preguntas':['¿Cuantas letras tiene la palabra "Carro"?','¿Cual de estas no es una fruta?','¿Que letra sigiue en el abecedario despues de la A?','¿Cual es la ultima letra del abecedario?'],
      'index':[2,1,0,3],
      'respuestas':[['2','6','5','4'],['Banano','Jugo de pera','Pera','Manzana'],['B','E','W','Z'],['A','M','X','Z']]},
      'Artistica':{
      'id_preguntas':[24,25,26,27],
      'preguntas':['¿Cuantas esquinas tiene un rectangulo?','¿Cual de estos no es un color primario?','¿Cual de estos es un color secundario?','¿Que color se obtiene mezclando el color amarillo y el azul?'],
      'index':[3,1,3,2],
      'respuestas':[['2','3','5','4'],['Amarillo','Blanco','Azul','Rojo'],['Negro','Cafe','Blanco','Morado'],['Cafe claro','Amarillo oscuro','Verde','Ninguno']]},
      'Etica':{
      'id_preguntas':[28,29,30,31],
      'preguntas':['Seleccione un valor','¿Que es la tolerancia?','¿Cuando soy un buen amigo?','¿Que es la alegria?'],
      'index':[2,1,0,3],
      'respuestas':[['Arroz','Tristeza','Respeto','Amarillo'],['Un deber','Un valor','Una señora','Una marca de carros'],['Cuando respeto a mis amigos','Cuando peleo con mis amigos','Cuando tengo hambre','Nunca'],['Un derecho','Una niña','Un color','Un sentimiento']]}}

      ,2:{'Matematicas':{
      'id_preguntas':[32,33,34,35],
      'preguntas':['¿Cuanto es 3x5?','¿Cuanto es 1+4?','¿Cual de estos es un numero impar?','¿Cuanto es 2/2?'],
      'index':[2,1,0,3],
      'respuestas':[['5','3','15','30'],['2','5','12','10'],['7','12','4','8'],['4','2','8','1']]},
      'Español':{
      'id_preguntas':[36,37,38,39],
      'preguntas':['¿Cual es un antonimo de alegria?','¿Cual es un sinonimo de miedo?','¿Cuantas silabas tiene la palabra "Zapato"?','¿Cual de estos no es un verbo?'],
      'index':[1,2,0,3],
      'respuestas':[['Miedo','Tristeza','Amarillo','No tiene'],['Tristeza','Alegria','Temor','Capricho'],['3','No tiene','2','1'],['Dormir','Elegir','Ellos','Empezar']]},
      'Artistica':{
      'id_preguntas':[40,41,42,43],
      'preguntas':['¿Cual de estos es un color secundario?','¿Cual de estos no es un instrumento musical?','¿Cuantos lados tiene un cubo?','¿Cuales son los colores de la bandera de Colombia?'],
      'index':[2,1,3,2],
      'respuestas':[['Rosado','Negro','Naranja','Ninguno de los anteriores'],['Guitarra','Equipo de sonido','Flauta','Tambor'],['4','2','8','6'],['Amarillo y rojo','Morado,azul y rojo','Amarillo,azul y rojo','Amarillo,azul y verde']]},
      'Etica':{
      'id_preguntas':[44,45,46,47],
      'preguntas':['¿Que es la solidaridad?','¿Cual de estos es un valor?','¿Cual de estas es una mala decisión?','¿Que es la honestidad?'],
      'index':[1,1,2,2],
      'respuestas':[['Una ciudad','Un valor','Una montaña','Un derecho'],['Salud','Bondad','Arroz','Culpa'],['Decir la verdad','Ser agradecido','Decir mentiras','Ser amable'],['Un departamento','Un derecho de los niños','Un valor','Ninguna de las anteriores']]}}

      ,3:{'Matematicas':{
      'id_preguntas':[48,49,50,51],
      'preguntas':['¿Cuanto es 7 + 7?','¿Cuanto es 14 / 2?','¿Cuanto es 28 - 13?','¿Cuanto es 6 x 4?'],
      'index':[2,1,2,3],
      'respuestas':[['12','19','14','13'],['5','7','2','11'],['10','17','15','13'],['18','26','28','24']]},
      'Español':{
      'id_preguntas':[52,53,54,55],
      'preguntas':['¿Cual de estas es una de las partes de un cuento?','¿Cual de estas palabras está mal escrita?','¿Cual de estos es un sinonimo de hogar?','¿Cual de estas palabras está bien escrita?'],
      'index':[1,2,0,3],
      'respuestas':[['Imagenes','Introducción','Letras','Frases'],['Hoja','Huevo','Colejio','Carro'],['Casa','Hermano','Grito','Felicidad'],['Hojo','Cabayo','Rrio','Cuaderno']]},
      'Sociales':{
      'id_preguntas':[56,57,58,59],
      'preguntas':['¿Cual es la capital de Colombia?','¿Cual de estas no es una ciudad de Colombia?','¿Que es Colombia?','¿Cual de estos no es un color de la bandera de Colombia?'],
      'index':[1,2,1,2],
      'respuestas':[['Cali','Bogota','Medellin','Pasto'],['Barranquilla','Cartagena','Lima','Cali'],['Un departamento','Un pais','Una ciudad','Un continente'],['Azul','Amarillo','Verde','Rojo']]},
      'Etica':{
      'id_preguntas':[60,61,62,63],
      'preguntas':['¿Cual de estas es una mala actitud?','¿Que es lo contrario de estar feliz?','¿Cual de estos es un valor?','¿Que es lo contrario a amar?'],
      'index':[1,2,3,1],
      'respuestas':[['Compañerismo','Pereza','Alegria','Gratitud'],['Tener hambre','Tener miedo','Estar triste','Estar viejo'],['Miedo','Dinero','Camisa','Responsabilidad'],['Caminar','Odiar','Trabajar','Guardar']]}},


      
      5:{'Matematicas':{
      'id_preguntas':[48,49,50,51],
      'preguntas':['¿Cuánto es 22 - (3×5) + 12','¿Cuánto es (3+8) x100?','0,63 expresado en porcentaje es igual a:','¿Cuanto es 38 x 2?'],
      'index':[0,2,1,2],
      'respuestas':[['19','12','31','17.5'],['810','1.001','1.100','1.110'],['36%','63%','0,06%','54%'],['86','66','76','51']]},
      'Español':{
      'id_preguntas':[52,53,54,55],
      'preguntas':['¿Cual de estas palabras está mal escrita?','¿Cual de estas palabras está bien escrita?','¿Cuántas vocales tiene la palabra "Murciélago"?','¿Cuantas silabas tiene la palabra "Fresa"?'],
      'index':[1,1,2,0],
      'respuestas':[['Color','Hasiento','Fruto','Mango'],['Biento','Cabello','Cilla','Cavle'],['3','4','5','Ninguna de las anteriores'],['2','1','No tiene','3']]},
      'Artistica':{
      'id_preguntas':[56,57,58,59],
      'preguntas':['¿Que colores debemos mezclar para conseguir el color verde?','Seleccione un instrumento musical de cuerda:','Al mezclar el color amarillo y el rojo obtenemos:','Seleccione un instrumento electronico:'],
      'index':[0,2,0,0],
      'respuestas':[['Azul y amarillo','Blanco y azul','Naranja y rosado','Amarillo y rojo'],['Platillos','Bombo','Violín','Flauta'],['Naranja','Nada','Rosado','Negro'],['Guitarra eléctrica','Tambor','Saxofón','Trompeta']]},
      'Etica':{
      'id_preguntas':[60,61,62,63],
      'preguntas':['¿Quien debe aplicar la etica?','¿A que personsa debemos respetar?','Es importante siempre:','¿Cuando es bueno robar?'],
      'index':[1,3,3,1],
      'respuestas':[['La familia','Todo el mundo','Las personas malas','Las personas buenas'],['A nadie','A mis amigos','Solo a mis padres','A todas las personas'],['Robar','Correr','Jugar','Decir la verdad'],['Cuando tenemos hambre','Nunca','Cuando tenemos sueño','Siempre']]}}}
    return d2

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
