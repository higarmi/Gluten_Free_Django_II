#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

class Recipe(models.Model):
	title = models.CharField(max_length=100, verbose_name='Title', unique=True)
	ingredients = models.TextField(help_text='List the Ingredients')
	directions = models.TextField(verbose_name='Directions', help_text='How do you make it ?')
	image = models.ImageField(upload_to='Recipes', verbose_name='Image')
	time_now = models.DateTimeField(auto_now=True)
	user = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.title

class Comments(models.Model):
    recipe = models.ForeignKey(Recipe)
    text = models.TextField(help_text='Your Comment', verbose_name='Comment')

    def __unicode__(self):
        return self.text
