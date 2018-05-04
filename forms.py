##Author: Duver Valencia
from wtforms import Form
from wtforms import StringField, TextField, IntegerField, PasswordField,SelectField
from wtforms.fields.html5 import EmailField
from wtforms import validators


class CommentForm(Form):
	username = StringField('',
						   [validators.Required(message= 'El usuario es requerido'),
							validators.length(min=4,max=25, message='Ingrese un usuario valido. (min:4,max:25)')] )
	comment = PasswordField('',
						[validators.required(message= 'La contraseña es requerida'),
						 validators.length(min=5,max=16,message='Ingrese una contraseña valida. (min:5,max:16)')])
class RegistroForm(Form):
	admin_registro = StringField('',
									[validators.Required(message='El admin es requerido'),
									 validators.length(min=4, max=25,
													   message='Ingrese un admin valido. (min:4,max:25)')])
	username_registro = StringField('',
						   [validators.Required(message= 'El usuario es requerido'),
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
        				choices=[('', ''),('1', 'Grado 1'), ('2', 'Grado 2'), ('3', 'Grado 3'),
						 ('4', 'Grado 4'), ('5', 'Grado 5'), ('6', 'Grado 6'),('7', 'Grado 7'), 
						 ('8', 'Grado 8')])
