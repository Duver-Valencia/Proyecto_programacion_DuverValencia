##Author: Duver Valencia
from wtforms import Form
from wtforms import StringField, TextField, IntegerField, PasswordField,SelectField, RadioField
from wtforms.fields.html5 import EmailField
from wtforms import validators
from proyectoDuver import *

class CommentForm(Form):
	username = StringField('',
						   [validators.Required(message= 'El usuario es requerido'),
							validators.length(min=4,max=25, message='Ingrese un usuario valido. (min:4,max:25)')] )
	comment = PasswordField('',
						[validators.required(message= 'La contraseña es requerida'),
						 validators.length(min=5,max=16,message='Ingrese una contraseña valida. (min:5,max:16)')])
	
class AdministradorForm(Form):
	administrador = StringField('',
						   [validators.Required(message= 'El administrador es requerido'),
							validators.length(min=4,max=25, message='Ingrese un usuario valido. (min:4,max:25)')] )
	contraseña_administrador = PasswordField('',
						[validators.required(message= 'La contraseña es requerida'),
						 validators.length(min=5,max=16,message='Ingrese una contraseña valida. (min:5,max:16)')])


class RegistroForm(Form):
	username_registro = StringField('',
						   [validators.Required(message= 'El usuario a registrar es requerido'),
							validators.length(min=4,max=25, message='Ingrese un usuario valido. (min:4,max:25)')] )
	email_registro = EmailField('',
					   [validators.Required(message= 'El email es requerido'),
						validators.Email(message='Ingrese un email valido')])
	comment_registro = PasswordField('',
						[validators.required(message= 'La contraseña es requerida'),
						 validators.length(min=5,max=16,message='Ingrese una contraseña valida. (min:5,max:16)')])
	edad_registro = IntegerField('',
						[validators.required(message= 'La edad es requerida ,(Solo numeros)'),
						 ])
	curso_registro = SelectField('',
        				choices=[('', ''),('0', 'Preescolar'), ('1', 'Primero'), ('2', 'Segundo'),
						 ('3', 'Tercero'), ('4', 'Cuarto'), ('5', 'Quinto'),('6', 'Sexto'), 
						 ('7', 'Septimo'),('8', 'Octavo'),('9', 'Noveno'),('10', 'Decimo'),('11', 'Undecimo')])

class PreguntasForm(Form):
	preguntas = RadioField( [validators.Required()], choices=[('choice1', 'Choice One'),('choice2', 'Choice Two')])
	username_p = StringField('',
						   [validators.Required(message= 'El usuario es requerido'),
							validators.length(min=4,max=25, message='Ingrese un usuario valido. (min:4,max:25)')] )
	comment_p = PasswordField('',
						[validators.required(message= 'La contraseña es requerida'),
						 validators.length(min=5,max=16,message='Ingrese una contraseña valida. (min:5,max:16)')])
	