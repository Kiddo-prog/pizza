from urllib import request
from django.db import models
from django.urls import reverse
from django.utils.text import slugify

sizes = (('S', 'small'), ('M', 'medium'), ('L', 'large'))

class PizzaTopping(models.Model):
    topping = models.ForeignKey('Topping', on_delete=models.CASCADE)
    pizza = models.ForeignKey('Pizza', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.CharField(max_length=200)
    slug = models.SlugField()

    def save(self):
        if self.slug is None:
            self.slug = slugify(self.pizza.name)
        return super().save()

    def get_absolute_url(self):
        return reverse('pizza:detail', kwargs={'slug': self.slug})

class Pizza(models.Model):  
    name = models.CharField(max_length=50) 
    topped_by = models.ManyToManyField('Topping', through=PizzaTopping)
    size = models.CharField(max_length=100, choices=sizes)
    def __str__(self):
        return self.name

class Topping(models.Model):   
    name=models.CharField(max_length=50)
    is_on = models.ManyToManyField('Pizza', through=PizzaTopping)
    def __str__(self):
        return self.name
