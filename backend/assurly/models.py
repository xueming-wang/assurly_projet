from django.db import models


class User(models.Model):
	first_name = models.CharField('first name', max_length=50)
	last_name = models.CharField('last name', max_length=50)
	brith_date = models.DateField('brithdate')
	create_date = models.DateField('create date', auto_now_add=True)
