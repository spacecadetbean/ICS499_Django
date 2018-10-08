from django.db import models
from django.db.models.signals import post_init
from PIL import Image
from imagehash import whash, hex_to_hash
import os

# Create your models here.

class ImageModel(models.Model):
	randomKey = models.TextField(primary_key=True, null=False)
	hash = models.CharField(max_length=16)
	path = models.TextField()
	docfile = models.FileField(
		upload_to='documents'+os.path.sep+'%Y'+os.path.sep+'%m'+os.path.sep+'%d',
		null=True
	)
	dbName = models.TextField(null=False, default="main")

class UserDatabase(models.Model):
	dbName = models.TextField(primary_key=True, null=False)
	dbOwner = models.TextField(null=False, default='admin')


#class StoredImage(models.Model):
#	docfile = models.FileField(upload_to='documents'+os.path.sep+'%Y'+os.path.sep+'%m'+os.path.sep+'%d')


# maybe implement a custom field specifically for Hashes instead of as a string.
#
#class whashField(models.Field):
#	description = "Wavelet hash of an image"
#
#	def __init__(self, *args, **kwargs):
#		kwargs['max_length'] = 1234
#		super().__init__(*args, **kwargs)
#
#	def deconstruct(self):
#		name, path, args, kwargs = super().deconstruct()
#		del kwargs['max_length']
#		return name, path, args, kwargs
#
#	def from_db_value(self, value, expression, connection):
#		if value is None:
#			return value
#		return hex_to_hash(value)
#
#	def to_python(self, value):
#		if(isinstance(value, whash):
#			return value
#		if value is None:
#			return value
#		try:
#			return hex_to_hash(value)
#		except:
#			raise ValidationError("Problem reading has value from database.")
#
#	def get_prep_value(self, value):
#		return str(value)
#
