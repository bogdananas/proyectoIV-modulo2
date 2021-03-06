#from django.db import models 
from mongoengine import *
from mongoengine.context_managers import switch_collection
import datetime

"""
Para guardar un objeto 
-----------------------
bar =Bares(nombre="x",direccion="y",nrvisitas="1")
bar.switch_collection('Bares')
bar.save()
"""


class Tapas(Document):
	nombre=StringField(max_length=40,required=True)
	nrvotos=IntField()
	meta = {'collection': 'Tapas'}
	#with switch_collection(Group,'Tapas') as Group:

class Bares(Document):
	nombre=StringField(max_length=50,required=True)
	direccion=StringField(max_length=150,required=True)
	nrvisitas=IntField()
	tapas=ListField(ReferenceField(Tapas))
	meta = {'collection': 'Bares'}
	#with switch_collection(Group,'Bares') as Group:

class Usuario(Document):
	username = StringField(max_length=200,required=True)
	email=EmailField()
	password =StringField()
	meta = {'collection': 'usuarios'}
	#with switch_collection(Group,'usuarios') as Group:


	#Las tablas de la base de datos

#from mongoengine import *


#class Producto(models.Model):
#    nombre = models.CharField(max_length=50)
#    estado = models.CharField(max_length=20)

#class Usuario(models.Model):
#    nombre=models.CharField(max_length=50)
#    edad=models.IntegerField()
#    correo=models.CharField(max_length=50)
#    telefono=models.CharField(max_length=35)


#class Usuario(Document):
#	username = StringField(max_length=200,required=True)
#	email=EmailField()
#	password =StringField()

#class Post(Document):
#	author = ReferenceField(Usuario)
#	content = StringField()
#	tags = ListField(StringField(max_length=50))