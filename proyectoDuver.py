##Autor: Duver Valencia
from flask import Flask
from flask import render_template
from flask import request
import forms

l=[]



app = Flask(__name__)

@app.route('/' , methods = ['GET','POST'])
def principal():
  return render_template('pagina_inicial.html')

@app.route('/inicio_sesión', methods = ['GET','POST'])
def index():
   comment_form = forms.CommentForm(request.form)
   if request.method == 'POST' and comment_form.validate():
       f = open('inicio_sesión.txt', 'a')
       f.write('\n')
       f.write(comment_form.username.data)
       f.write(',')
       f.write(comment_form.comment.data)
       f.close()
       l_new = []
       l_new.append((comment_form.username.data))
       l_new.append((comment_form.comment.data))
       l.append(l_new)
       print(l)
       return render_template('juego.html')
       
   title = 'Juego'
   return render_template('index.html', title = title, form = comment_form)

@app.route('/inicio_administrador', methods = ['GET','POST'])
def inicio_administrador():
   administrador_form = forms.AdministradorForm(request.form)
   if request.method == 'POST' and administrador_form.validate():
       f = open('inicio_sesión.txt', 'a')
       f.write('\n')
       f.write(administrador_form.administrador.data)
       f.write(',')
       f.write(administrador_form.contraseña_administrador.data)
       f.close()
       l_new = []
       l_new.append((administrador_form.administrador.data))
       l_new.append((administrador_form.contraseña_administrador.data))
       l.append(l_new)
       print(l)
       return render_template('pagina_administrador.html')
       
   title = 'Juego'
   return render_template('inicio_administrador.html', title = title, form = administrador_form)




l_registro=[]

@app.route('/registro', methods = ['GET','POST'])
def registro():
   registro_form = forms.RegistroForm(request.form)
   if request.method == 'POST' and registro_form.validate():
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
       l_new = []
       l_new.append((registro_form.username_registro.data))
       l_new.append((registro_form.email_registro.data))
       l_new.append((registro_form.comment_registro.data))
       l_new.append(str(registro_form.edad_registro.data))
       l_new.append((registro_form.curso_registro.data))
       l_registro.append(l_new)
       print(l_registro)


   title = 'Juego'
   return render_template('registro.html', title = title, form = registro_form)




@app.route('/juego')
def juego():
   return render_template('juego.html')

@app.route('/pagina_administrador')
def pagina_administrador():
   return render_template('pagina_administrador.html')

if __name__ == '__main__':
   app.run( debug = True, port = 13002)
