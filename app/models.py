# from __future__ import unicode_literals
from django.db import models

from django.db.models import Model

class Person(Model):
	client_name =models.CharField(max_length=100, unique=True)
	address =models.CharField(max_length=100)


