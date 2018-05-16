##Autor: Duver Valencia
from flask import Flask
from flask import render_template
from flask import request
import forms
from validar_inicio import*
from funciones import*
l=[]

nombre = ''

app = Flask(__name__)

@app.route('/' , methods = ['GET','POST'])
def principal():
  return render_template('pagina_inicial.html')

@app.route('/inicio_sesión', methods = ['GET','POST'])
def index():
  global nombre
  comment_form = forms.CommentForm(request.form)
  if request.method == 'POST' and comment_form.validate():
    if verificarUsuario(comment_form.username.data,comment_form.comment.data):
       nombre = comment_form.username.data
       vida = 5
       grado = verGrado(nombre)
       print(nombre)
       return render_template('juego.html', nombre = nombre, vida = vida, grado = grado)
    else:
      print('no existe')
  title = 'Juego'
  return render_template('index.html', title = title, form = comment_form)


@app.route('/preguntas', methods = ['GET','POST'])
def preguntas():
  global nombre
  preguntas_form = forms.PreguntasForm(request.form)
  title = 'Preguntas'
  return render_template('preguntas.html',title = title, form = preguntas_form,nombre= nombre)


@app.route('/inicio_administrador', methods = ['GET','POST'])
def inicio_administrador():
   administrador_form = forms.AdministradorForm(request.form)
   if request.method == 'POST' and administrador_form.validate():
    if verificarAdministrador(administrador_form.administrador.data,administrador_form.contraseña_administrador.data):
      return render_template('pagina_administrador.html')
    else:
      print('No exite')
       
   title = 'Juego'
   return render_template('inicio_administrador.html', title = title, form = administrador_form)




l_registro=[]

@app.route('/registro', methods = ['GET','POST'])
def registro():
   registro_form = forms.RegistroForm(request.form)
   if request.method == 'POST' and registro_form.validate():
    if compararUsuario(registro_form.username_registro.data):
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
       f = open('grados.txt', 'a')
       f.write('\n')
       f.write(registro_form.username_registro.data)
       f.write(',')
       f.write(registro_form.curso_registro.data)
       f.close()
       f = open('inicio_sesión.txt', 'a')
       f.write('\n')
       f.write(registro_form.username_registro.data)
       f.write(',')
       f.write(registro_form.comment_registro.data)
       f.close()
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
    else:
      print('Ya esta')


   title = 'Juego'
   return render_template('registro.html', title = title, form = registro_form)

@app.route('/saludo')
def saludo():
  global nombre
  con = contraseña(nombre)
  return render_template('saludo.html', nombre = nombre, contraseña = con)


@app.route('/juego')
def juego():
   return render_template('juego.html')

@app.route('/pagina_administrador')
def pagina_administrador():
   return render_template('pagina_administrador.html')

if __name__ == '__main__':
   app.run( debug = True, port = 12004)
