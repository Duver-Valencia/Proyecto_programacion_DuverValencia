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
      'respuestas':[['2','3','1'],['9','15','10','14'],['5','3','1','2'],['6','3','1','4']]},
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


      
      4:{'Matematicas':{
      'id_preguntas':[48,49,50,51],
      'preguntas':['¿Cuánto es 22 - (3×5) + 12','¿Cuánto es (3+8) x100?','¿Cuánto es 11 x (2+7)','¿Cuanto es 38 x 2?'],
      'index':[0,2,1,2],
      'respuestas':[['19','12','31','17.5'],['810','1.001','1.100','1.110'],['111','99','132','79'],['86','66','76','51']]},
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
      'respuestas':[['La familia','Todo el mundo','Las personas malas','Las personas buenas'],['A nadie','A mis amigos','Solo a mis padres','A todas las personas'],['Robar','Correr','Jugar','Decir la verdad'],['Cuando tenemos hambre','Nunca','Cuando tenemos sueño','Siempre']]}},

      5:{'Matematicas':{
      'id_preguntas':[64,65,66,67],
      'preguntas':['¿Cuánto es 50 -(7×5)','Sí tenemos (40x2) - ___ = 37','¿Cuánto es 583x1000?','¿Cuánto es 1.240/2?'],
      'index':[0,2,1,3],
      'respuestas':[['15','32','21','17'],['34','10','43','57'],['58300','583000','5831000','4380009'],['386','606','760','620']]},
      'Español':{
      'id_preguntas':[68,69,70,71],
      'preguntas':['Complete la siguiente oración: Esperaré hasta que _________ de llover','¿Cuándo utilizamos una mayúscula?','¿Qué es narración?','Las palabras monosemicas son aquellas que:'],
      'index':[1,0,0,1],
      'respuestas':[['Dejará','Deje','Deja'],['Después de un punto','Después de un verbo','Después de una coma','Cuando se quiere'],['Narrar hechos en el tiempo','Describir un suceso','Escribir versos'],['Tienen un solo sonido','Tienen un solo significado','Tienen una sola silaba']]},
      'Artistica':{
      'id_preguntas':[72,73,74,75],
      'preguntas':['La primera nota musical se llama:','Cuál de estos no es un color primario ni secundario?','¿Al mezclar el color rojo y el azul obtenemos el color morado?','Sí te piden pintar un paisaje rural, debes pintar:'],
      'index':[1,2,0,3],
      'respuestas':[['Re','Do','Sol','La'],['Amarillo','Morado','Gris','Azul'],['Si','No'],['La ciudad','La naturaleza','El campo y las flores ','La zona fuera de la ciudad']]},
      'Etica':{
      'id_preguntas':[76,77,78,79],
      'preguntas':['¿La ética es buena?','Debemos respetar a los abuelos','Complete la siguiente oración: Debemos ser ___________','¿Cuándo es bueno mentir?'],
      'index':[0,1,0,2],
      'respuestas':[['Si','No'],['No','Si','Solo si nos dan dinero','No, solo a los niños'],['Solidarios','Groseros','Mentirosos','Intolerantes'],['Cuando tenemos miedo','Cuando no tenemos lo que queremos','Nunca','Siempre']]}},

      6:{'Matematicas':{
      'id_preguntas':[48,49,50,51],
      'preguntas':['¿Cuánto es 22 - (3x5) + 12?','¿Cuánto es 45 + (3+8) x 100?','Sí tenemos el decimal 7,9 al pasarlo a un número mixto tendríamos:','¿Cuánto es 13 - (9x3) + 14?'],
      'index':[1,0,1,2],
      'respuestas':[['157','19','23','16'],['1145','893','1129','932'],['9/10','7 9/10','10 3/6','9 7/2'],['12','23','15','12']]},
      'Español':{
      'id_preguntas':[52,53,54,55],
      'preguntas':['Para sacar el resumen de un texto, es necesario:','El cuento posee:','Una idea principal es:','Los verbos se pueden conjugar en:'],
      'index':[2,3,1,1],
      'respuestas':[['Leerlo muchas veces','Memorizarlo','Sacar la idea principal'],['Inicio,Nudo y desenlace','Personajes,nombres y villanos','Lugar,tiempo y espacio','Todas las anteriores'],['Un resumen del texto','Una idea general del texto','Algo que surge en el texto'],['Infinitivo y aumentativo','Presente,pasado y futuro','Depende del verbo que sea']]},
      'Artistica':{
      'id_preguntas':[56,57,58,59],
      'preguntas':['Al pintar una zona urbana necesitamos:','Es necesario usar diversos pinceles a la hora de pintar porque:','Para mezclar las pinturas usamos algo llamado:','El arte es:'],
      'index':[0,1,0,0],
      'respuestas':[['Prestar atención al paisaje de la ciudad','Pintar a la gente','Pintar el paisaje citadino','Ninguna de las anteriores'],['Permite complementar el cuadro','Todos no pintan de igual forma','Le da mejor acabado al trabajo'],['Paleta','Mezclador','Recipiente','Frasco'],['Emocional','Problematico','Malo']]},
      'Etica':{
      'id_preguntas':[60,61,62,63],
      'preguntas':['Los valores son:','El antivalor de la verdad es:','¿El antivalor de la sabiduría es la ignorancia?','¿Donde es importante ser honestos?'],
      'index':[1,0,1,0],
      'respuestas':[['Atribuciones que se le dan a las personas cuando son buenas en todo lo que hacen','Atribuciones que se le dan a las personas cuando son buenas personas','Reglas que todos deben cumplir','Todas las anteriores'],['La falsedad','La tolerancia','El respeto'],['No','Si'],['En todo lugar','Solo en la casa','En ningún lugar']]},
      'Sociales':{
      'id_preguntas':[60,61,62,63],
      'preguntas':['Algo que permite diferenciar una montaña de algo plano es:','Los mapas son útiles porque:','Anteriormente se creía que la tierra era:','Las personas que pertenecían a la nobleza eran:'],
      'index':[0,1,1,0],
      'respuestas':[['El relieve','El tamaño'],['Son cuadrados','Nos muestran los limites de un país','Nos ubican en el mundo'],['Redonda','Plana','Cuadrada'],['Aquellos que tenían poder o riquezas','Aquellos que eran pobres']]}},

      7:{'Matematicas':{
      'id_preguntas':[48,49,50,51],
      'preguntas':['Al explicar el por qué 8x12 = 12x8 debemos mencionar la propiedad:'
      ,'Jairo invita a sus 3 amigos a comer, pero ellos quedan de pagarle después porque en el momento no tienen dinero, él compra 4 helados y paga $3200, ¿Cuánto cuesta cada helado?'
      ,'Si tenemos un rectangulo cuyas medidas son 8cm de largo y 3cm de ancho, el área de esta figura es:'
      ,'Si tenemos 3X + 2 = 8 al despejar la X obtenemos:'],
      'index':[3,1,2,0],
      'respuestas':[['Distributiva','Del inverso','Asociativa','Conmutativa'],
      ['500','800','1200','3200'],
      ['32cm (al cuadrado)','38cm (al cuadrado)','24cm (al cuadrado)','83cm (al cuadrado)'],
      ['2','3','1','4']]},
      'Español':{
      'id_preguntas':[52,53,54,55],
      'preguntas':['Para hacer un resumen yo debo sacar:',
      'La palabra "Manso" significa:',
      'El error en la palabra "Afirmacion" es:',
      'La forma correcta de escribir "Haber el partido" es:'],
      'index':[2,2,0,2],
      'respuestas':[['Personajes','Preguntas','Características del texto'],
      ['Que se deja tratar','Apacible, de buen carácter','Todas las anteriores'],
      ['Que falta una tilde','Que debe ponerse en mayúsculas'],
      ['A ber el partido','Ha ver el partido','A ver el partido','Está escrita correctamente']]},
      'Artistica':{
      'id_preguntas':[56,57,58,59],
      'preguntas':['Cuando dibujamos en un papel sobre una imagen esto se llama:',
      'Para darle brillo a un trabajo con plastilina debemos usar:',
      'Cuando pintamos, la mejor opción para hacerlo es:',
      'Los dibujos son una herramienta para:'],
      'index':[0,2,0,3],
      'respuestas':[['Calcar','Dibujar','Resaltar','Todas las anteriores'],
      ['Escarcha','Agua','Ega','Esmalte'],
      ['Hacerlo sobre un lienzo','Hacerlo con miedo','Comer antes de pintar','Hacerlo sobre cartulina'],
      ['Representar algo fisico','Usar la imaginación','Plasmar los sentimientos','Todas las anteriores']]},
      'Etica':{
      'id_preguntas':[60,61,62,63],
      'preguntas':['Uno debe quererse a sí mismo, eso se llama:',
      'Algo que sería incorrecto es:',
      'El núcleo de la sociedad se llama:',
      '¿Qué vale más?'],
      'index':[1,3,1,2],
      'respuestas':[['Respeto','Buena autoestima','Miedo','Valor propio'],
      ['Robar','Romper cosas','Mentir','Todas las anteriores'],
      ['Personas','Familia','Amigos'],
      ['La plata','Las cosas materiales','Las cosas que aprendemos']]},
      'Sociales':{
      'id_preguntas':[60,61,62,63],
      'preguntas':['La pirámide social de la edad media era:',
      'Ser campesino es lo mismo que pertenecer al tercer estado o estado llano, esta afirmación es:',
      'La historia se puede dividir en:',
      'La época de la prehistoria es conocida también como la etapa de:'],
      'index':[1,0,3,1],
      'respuestas':[['Rey,clero,nobleza y campesino','Rey,nobleza,clero y llano'],
      ['Verdadera','Falsa'],
      ['Edades','Siglos','Épocas','Todas las anteriores'],
      ['Los mounstruos','Los cavernícolas','Lo mítico']]}},

      8:{'Matematicas':{
      'id_preguntas':[48,49,50,51],
      'preguntas':['El mínimo común múltiplo entre 3 y 4 es:',
      'Si 4xb = g entonces b es igual a:',
      'Si tenemos 4 5/6, el fraccionario de este número es:',
      'El perímetro de un triángulo cuyas medidas son 3cm,20cm y 2cm es:'],
      'index':[0,1,1,3],
      'respuestas':[['12','3','8','10'],
      ['14','g/4','10','4+g'],
      ['14','29/6','(2x5)/6'],
      ['23cm','17cm','24cm','25cm']]},
      'Español':{
      'id_preguntas':[52,53,54,55],
      'preguntas':['"Talvez" se escribe:',
      'Los nombres propios deben llevar:',
      'La oración simple consta de:',
      'Las oraciones compuestas constan de:'],
      'index':[1,2,0,2],
      'respuestas':[['Así como está','Separado: Tal vez','Talves'],
      ['Mayúscula','Mayúscula al final','Mayúscula al principio'],
      ['Sujeto y predicado','Sujeto,verbo y predicado','Sujeto y complemento'],
      ['Sujeto y predicado', 'Verbo,sujeto y complemento','Sujeto,verbo,predicado y complemento']]},
      'Artistica':{
      'id_preguntas':[56,57,58,59],
      'preguntas':['Las manualidades son:',
      'Las canciones se componen de:',
      'Dos instrumentos de cuerda son:',
      'Para empezar un dibujo es necesario tener:'],
      'index':[3,3,2,3],
      'respuestas':[['Obras de arte','Dibujos','Canciones','Obras de arte hechas a mano'],
      ['Notas','Música','Estrofas y coros','Todas las anteriores'],
      ['Tambor y guitarra','Bajo y batería','Violín y guitarra','Batería y piano'],
      ['Una idea','Un boceto','Un lápiz','Todas las anteriores']]},
      'Etica':{
      'id_preguntas':[60,61,62,63],
      'preguntas':['¿La ética debe aplicarse en el colegio?:',
      'Una razón correcta para decir una mentira es:',
      'La humildad es:',
      'La felicidad se ve cuando:'],
      'index':[0,1,0,2],
      'respuestas':[['Si','No'],
      ['Para ayudar a alguien','No existe esa posibilidad','Para sorprender a alguien','Para ganar algo'],
      ['Saber que no soy más que nadie y todos somos iguales','Creerme más que todos','Sentirme menos que los demás'],
      ['Lo tengo todo','Soy rico','Doy todo en cada ocasión']]},
      'Sociales':{
      'id_preguntas':[60,61,62,63],
      'preguntas':['Los censos son:',
      'La tasa de natalidad es:',
      'Una población es:',
      'Un emigrante es aquel que:'],
      'index':[1,1,1,3],
      'respuestas':[['Informes de una sociedad','El recuento de los individuos de una población determinada'],
      ['La cantidad de muertes','La cantidad de nacimientos','La cantidad de abortos'],
      ['Una persona','Un conjunto de personas','Habitantes'],
      ['Llega a un país','Llega a una ciudad','Se queda en un sólo lugar','Sale de un lugar o país a otro']]}},

      9:{'Matematicas':{
      'id_preguntas':[48,49,50,51],
      'preguntas':['Los números reales son:',
      'El numero pi equivale a:',
      'Si tenemos 5w+10 = 20, ¿Cuánto vale w?',
      'Los numeros racionales son aquellos que:'],
      'index':[2,1,0,3],
      'respuestas':[['Los naturales','Los complejos','Los numeros irracionales y racionales','Los que no tiene decimales'],
      ['3,10','3,1416...','4,2','15'],
      ['2','12','4','5'],
      ['Están compuestos por los numeros irracionales','Están compuestos por enteros','Son menores a 1','Están formados por los números enteros y fraccionarios']]},
      'Español':{
      'id_preguntas':[52,53,54,55],
      'preguntas':['Las preposiciones son:',
      'Un ejemplo de preposiciones es:',
      'La lengua castellana es llamada así por su origen en:',
      'Las lenguas romances son:'],
      'index':[1,0,2,2],
      'respuestas':[['Ayudas en las oraciones','Ayuda para generar un texto más completo','Palabras que nos ayudan a darle sentido a un texto'],
      ['Ante,según y sin','Bajo,es y estar','Yo,tú y el'],
      ['Roma','El castillo de Italia en 1944','Castilla'],
      ['Lenguas romanticas','Lenguas que surgieron en Roma','Lenguas que surgieron como evolución del latín vulgar']]},
      'Artistica':{
      'id_preguntas':[56,57,58,59],
      'preguntas':['Una herramienta útil para todo tipo de dibujo es:',
      'Los dibujos pueden hacerse con:',
      'Un elemento de expresión gráfica es:',
      'Un instrumento que no es de viento es:'],
      'index':[0,3,1,3],
      'respuestas':[['La escuadra','La regla','El martillo','El transportador'],
      ['Puntos','Líneas','Difuminación','Todas las anteriores'],
      ['El lápiz','Textura','Un cuaderno','Borrador'],
      ['La flauta','El xilofono','La trompeta']]},
      'Etica':{
      'id_preguntas':[60,61,62,63],
      'preguntas':['El respeto y la tolerancia implican:',
      'El altruismo es un valor que muestra:',
      'La ética es importante porque:',
      '¿Debemos respetar la opinión de las demas personas?'],
      'index':[1,3,0,1],
      'respuestas':[['Ayudar a los demás','Valorar lo que otra persona dice o hace aún si no estoy de acuerdo','No igualarme con mayores'],
      ['Cómo una persona es capaz de renunciar a todo por otros','Ser generoso','Dar sin esperar recibir nada a cambio','Todas las anteriores'],
      ['Nos enseña como debemos ser y actuar ante la sociedad','Nos muestra valores','Nos manda a cumplir ciertas leyes'],
      ['No','Si']]},
      'Sociales':{
      'id_preguntas':[60,61,62,63],
      'preguntas':['En la primera guerra mundial se aplicaron métodos con armas muy peligrosas también conocidas como:',
      'Una caracteristica de la guerra fría es:',
      'Cristóbal Colón es conocido por:',
      'En la primera guerra mundial, el bando de la Triple Alianza estaba conformado por:'],
      'index':[2,1,0,2],
      'respuestas':[['Armas mortales','Armas neutrales','Armas químicas'],
      ['Ocurrió en la Artántida','No hay enfrentamiento armado','Ocurrió hace muchos años'],
      ['Descubrir América','Descubrir que la tierra no era plana'],
      ['Estados Unidos,Inglaterra y Japón','Reino Unido,China y Gran Bretaña','Alemania,Imperio Austrohúngaro e Italia']]}}

      ,10:{'Matematicas':{
      'id_preguntas':[0,1,2,3],
      'preguntas':['El ángulo que se forma cuando el reloj está a las 3:00pm, es:',
      'El ángulo obtuso es aquel que:',
      'El ángulo agudo es aquel que:',
      'La cantidad de segundos que hay en una hora son:'],
      'index':[0,2,3,0],
      'respuestas':[['Recto','Obtuso','Agudo','Infinito'],
      ['Es muy grande','Es muy pequeño','Mide más de 90 (grados) ','Mide menos de 90'],
      ['Es muy grande','Es muy pequeño','Mide más de 90','Mide menos de 90'],
      ['3.600','2.100','3.200']]},
      'Artistica':{
      'id_preguntas':[0,1,2,3],
      'preguntas':['Un elemento de expresión gráfica es:',
      'Cuando pasamos de oscuro a claro, o de claro a oscuro, esto se conoce como:',
      'Se pueden hacer obras de arte con:',
      'Al libro o libreto lleno de gráficos y con poco texto, que cuenta las historias de súper héroes, se le conoce por:'],
      'index':[0,1,3,3],
      'respuestas':[['Volúmen','Dureza','Material ','Ninguna de las anteriores'],
      ['Degradé','Valor tonal','A y B son correctas ','Ninguna es correcta'],
      ['Arroz','Pintura','Cáscaras de huevo','Todas las anteriores '],
      ['Una novela','Un cómic ','Una película','Un cuento corto']]},
      'Etica':{
      'id_preguntas':[0,1,2,3],
      'preguntas':['Una persona valiente es aquella que:',
      'El amor',
      'Ser íntegro es:',
      'Uno debe cumplir lo que promete porque:'],
      'index':[0,3,2,1],
      'respuestas':[['Es capaz de enfrentar sus miedos y seguir adelante',' Nunca tiene miedo a nada','Siempre huye de las cosas','Confía mucho en sí mismo'],
      ['Es una herramienta para unir a otros','No sirve de nada si no es correspondido ','Es una pérdida de tiempo ','Es para todos, aunque a veces no funcione'],
      ['Cumplir en todo','Ser excelente en todo','Tener bien cada área de su vida','Ninguna de las anteriores'],
      ['Eso nos hace verdaderos amigos','Eso nos convierte en personas verdaderas','Eso nos hace mentirosos']]},
      'Español':{
      'id_preguntas':[0,1,2,3],
      'preguntas':['Un texto puede ser:',
      'Para una exposición, es necesario:',
      'La morfología es aquella que estudia:',
      'Para dar sentido a lo que decimos necesitamos:'],
      'index':[2,3,1,3],
      'respuestas':[['Argumentativo, largo','Corto','Expositivo'],
      ['Tener claro el tema','Tener ayudas visuales y prácticas a la hora de explicar','Estudiar el tema','Todas las anteriores'],
      ['El origen de las palabras ','La composición de las palabras '],
      ['Argumentar','Sustentar','Justificar','Todas las anteriores ']]}},

      'Sociales':{
      'id_preguntas':[0,1,2,3],
      'preguntas':['La procuraduría está encargada de:',
      'La corte Suprema de justicia ',
      'En el comercio, es importante tener en cuenta:',
      'El estado es lo mismo que el Gobierno'],
      'index':[0,2,1,1],
      'respuestas':[['Sancionar las irregularidades de los gobernantes','Ver por el bienestar del pueblo '],
      ['Se encarga de impartir miedo a los ciudadanos','Es internacional','Es el más alto organismo de poder en Colombia'],
      ['Importaciones y exportaciones','Oferta y demanda','Cantidad de materia prima'],
      ['Verdadero','Falso']]},

      'Religion':{
      'id_preguntas':[0,1,2,3],
      'preguntas':['Los diferentes tipos de religiones se aplican a:',
      'El Salvador, también es conocido como:',
      'Jesús era:',
      ' Las religiones más conocidas del mundo son:'],
      'index':[0,2,0,1],
      'respuestas':[['Diferentes tipos de cultura','Diferentes tipos de países'],
      ['El Mesías ','El enviado de Dios','Todas las anteriores'],
      ['Un carpintero ','Un profesor','Un maestro de la ley'],
      ['Cristianismo, hinduísmo','Judaísmo, cristianismo','El Islam, testigo de Jehová ']]}}

      # 11:{'Matematicas':{
      # 'id_preguntas':[0,0,2,3],
      # 'preguntas':['Log 7 de 343','¿Cuánto es 894x12?','Un conjunto se representa gráficamente con lo que se conoce como un:','Para despejar la x de la ecuación 3x - 4 = 18, es necesario hacer:'],
      # 'index':[0,1,3,0],
      # 'respuestas':[['3','12','13','6'],['10728','1232','3212'],['Gráfico de barras','Gráfico de pastel','Diagrama de Venn'],['X= 18+4/3','3x = 18+4','18-4+3= x']]},

      # 'Artistica':{
      # 'id_preguntas':[0,1,2,3],
      # 'preguntas':['','','',''],
      # 'index':[2,1,3,3],
      # 'respuestas':[[''],[''],[''],['']]},
      # 'Matematicas':{
      # 'id_preguntas':[0,1,2,3],
      # 'preguntas':['','','',''],
      # 'index':[2,1,3,3],
      # 'respuestas':[[''],[''],[''],['']]},
      # 'Matematicas':{
      # 'id_preguntas':[0,1,2,3],
      # 'preguntas':['','','',''],
      # 'index':[2,1,3,3],
      # 'respuestas':[[''],[''],[''],['']]}},
      # 'Matematicas':{
      # 'id_preguntas':[0,1,2,3],
      # 'preguntas':['','','',''],
      # 'index':[2,1,3,3],
      # 'respuestas':[[''],[''],[''],['']]},
      # 'Matematicas':{
      # 'id_preguntas':[0,1,2,3],
      # 'preguntas':['','','',''],
      # 'index':[2,1,3,3],
      # 'respuestas':[[''],[''],[''],['']]}
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
