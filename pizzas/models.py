from django.db import models

# Create your models here.

class Pizza(models.Model):
    """A topic the user is learning about"""
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(max_length=200)



class Topping(models.Model):
    """A topic the user is learning about"""
    pizza = models.ForeignKey(Pizza)
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.name