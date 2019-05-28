from django.db import models

# Create your models here.
class Author(models.Model):
	name = models.TextField();

class Contact(models.Model):
	name = models.TextField();
