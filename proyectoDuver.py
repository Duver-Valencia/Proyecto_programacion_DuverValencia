##Autor: Duver Valencia

#Importo los modulos necesarios desde flask y las funciones de python 
from flask import Flask 
from flask import render_template
from flask import request
import forms
from validar_inicio import*
from funciones import*
from flask import session
from flask import jsonify
import json


nombre = '' #Variable para el nombre del usuario que está jugando

app = Flask(__name__)

def retornarMatriz(ruta):
  f = open(ruta,'r')
  matriz = []
  for linea in f:
    linea = linea.replace('\n','')
    fila = linea.split(',')
    matriz.append([int(i) for i in fila])
  f.close()
  return matriz

def leerMatriz(grado):
  matriz = []
  if grado in [1,2,3,4,5]:
    ruta = './static/matriz1.txt'
  #elif [6,7,8,9]

  #elif [10,11]

  return retornarMatriz(ruta)



  



@app.route('/' , methods = ['GET','POST'])
def principal():
  #Está funcion renderiza la pagina inicial
  if 'username' in session:
    print('ya esta el usuario')
    mapaGeneral = leerMatriz(int(1))
    preguntas = diccionarioPreguntas()
    return render_template('juego.html', nombre = session['username'], vida = 5, grado = 1,mapa=mapaGeneral, preguntas = preguntas)
  return render_template('pagina_inicial.html')



@app.route('/inicio_sesión', methods = ['GET','POST'])
def index():
  #Está es la ruta para la pagina de inicio de sesión
  #Está funcion renderiza la pagina del juego cuando inicia sesión
  global nombre
  comment_form = forms.CommentForm(request.form)
  if request.method == 'POST':
    if comment_form.validate(): #Valido el envio correcto del formulario con flask
      if verificarUsuario(comment_form.username.data,comment_form.comment.data):
        nombre = comment_form.username.data
        session['username'] = nombre
        vida = verVidas(nombre)
        grado = verGrado(nombre) 
        mapaGeneral = leerMatriz(int(grado))
        preguntas = diccionarioPreguntas()
        return render_template('juego.html', nombre = nombre, vida = vida, grado = grado,mapa=mapaGeneral,preguntas = preguntas)

  title = 'Juego'
  return render_template('index.html', title = title, form = comment_form)


@app.route('/logout', methods = ['GET','POST'])
def logout():
  global nombre
  session.pop('username', None)
  comment_form = forms.CommentForm(request.form)
  if request.method == 'POST':
    if comment_form.validate(): #Valido el envio correcto del formulario con flask
      if verificarUsuario(comment_form.username.data,comment_form.comment.data):
        nombre = comment_form.username.data
        session['username'] = nombre
        vida = verVidas(nombre)
        grado = verGrado(nombre) 
        mapaGeneral = leerMatriz(int(grado))
        preguntas = diccionarioPreguntas()
        return render_template('juego.html', nombre = nombre, vida = vida, grado = grado,mapa=mapaGeneral,preguntas = preguntas)

  title = 'Juego'
  return render_template('index.html',title = title, form = comment_form )

@app.route('/preguntas', methods = ['GET','POST'])
def preguntas():
  #Esta es la pagina de las preguntas en flask
  global nombre
  preguntas_form = forms.PreguntasForm(request.form)
  title = 'Preguntas'
  return render_template('preguntas.html',title = title, form = preguntas_form,nombre= nombre)


@app.route('/inicio_administrador', methods = ['GET','POST'])
def inicio_administrador():
  #Está es la ruta para la pagina de inicio de sesión del administrador
  #Está funcion renderiza la pagina del administrador cuando inicia sesión
   administrador_form = forms.AdministradorForm(request.form)
   if request.method == 'POST' and administrador_form.validate(): #Valido en envio correcto del formulario con flask
    if verificarAdministrador(administrador_form.administrador.data,administrador_form.contraseña_administrador.data):
      return render_template('pagina_administrador.html')
    else:
      #Cuando el administrador y la contraseña no coinciden
      print('No exite')
       
   title = 'Juego'
   return render_template('inicio_administrador.html', title = title, form = administrador_form)
                  
                                                                                              


l_registro=[]

@app.route('/registro', methods = ['GET','POST'])
def registro():
  #Está es la ruta para la pagina de registro
   registro_form = forms.RegistroForm(request.form)
   if request.method == 'POST' and registro_form.validate(): #Valido el envio correcto del formulario con flask
    if compararUsuario(registro_form.username_registro.data):
      #Añado la información necesaria a el bloc de notas que corresponde al registro y el inicio de sesión
       f = open('registro_cuentas.txt', 'a')
       f.write('\n')
       f.write(registro_form.username_registro.data)
       f.write(',')
       f.write(registro_form.email_registro.data)
       f.write(',')
       f.write(registro_form.comment_registro.data)
       f.write(',')
       f.write(str(registro_form.edad_registro.data))
       f.write(',')
       f.write(registro_form.curso_registro.data)
       f.close()
       f = open('perfil.txt', 'a')
       f.write('\n')
       f.write(registro_form.username_registro.data)
       f.write(',')
       f.write(registro_form.curso_registro.data)
       f.write(',')
       f.write('5')
       f.close()
       f = open('inicio_sesión.txt', 'a')
       f.write('\n')
       f.write(registro_form.username_registro.data)
       f.write(',')
       f.write(registro_form.comment_registro.data)
       f.close()
       l = []
       l_new = []
       l_new.append((registro_form.username_registro.data))
       l_new.append((registro_form.comment_registro.data))
       l.append(l_new)
       print(l)
       l_new = []
       l_new.append((registro_form.username_registro.data))
       l_new.append((registro_form.email_registro.data))
       l_new.append((registro_form.comment_registro.data))
       l_new.append(str(registro_form.edad_registro.data))
       l_new.append((registro_form.curso_registro.data))
       l_registro.append(l_new)
       print(l_registro)
       title = 'Juego'
       return render_template('registroCorrecto.html')
    else:
      print('Ya esta')


   title = 'Juego'
   return render_template('registro.html', title = title, form = registro_form)


@app.route('/saludo')
def saludo():
  #Esta funcion renderiza a una pegina que le dice cual es el usuario y la contraseña del jugador
  global nombre
  con = contraseña(nombre)
  return render_template('saludo.html', nombre = nombre, contraseña = con)


@app.route('/juego')
def juego():
    #Esta funcion renderiza la pagina del juego
  return render_template('juego.html')


@app.route('/pagina_administrador')
def pagina_administrador():
  #Está funcion renderiza la pagina del administrador
   return render_template('pagina_administrador.html')



if __name__ == '__main__':
  app.secret_key = 'cladjadodmep'
  app.run( debug = True, port = 12001)

